"""LLM backends with one interface. API keys come ONLY from environment variables (optionally loaded from a git-ignored .env);
they are never printed, logged, written to traces or included in exception messages."""
from __future__ import annotations
import json, os, time
import httpx


def load_env(path=".env"):
    """Tiny .env loader (KEY=VALUE). Does not override variables already set; values are never echoed."""
    if not os.path.exists(path): return
    for line in open(path, encoding="utf-8"):
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line: continue
        k, v = line.split("=", 1)
        k, v = k.strip(), v.strip().strip('"').strip("'")
        if k and v and k not in os.environ: os.environ[k] = v


class LLMError(RuntimeError): pass


class DeepSeek:
    """OpenAI-compatible chat/completions with tool calling (https://api.deepseek.com)."""
    name = "deepseek"

    def __init__(self, model=None, base_url=None):
        load_env()
        self.key = os.environ.get("DEEPSEEK_API_KEY", "")
        if not self.key: raise LLMError("DEEPSEEK_API_KEY chưa được đặt (đặt trong .env hoặc biến môi trường). Không có fallback giả lập.")
        self.model = model or os.environ.get("DEEPSEEK_MODEL") or "deepseek-chat"
        self.base = (base_url or os.environ.get("DEEPSEEK_BASE_URL") or "https://api.deepseek.com").rstrip("/")

    def chat(self, messages, tools=None, temperature=0.0, max_tokens=1200):
        body = {"model": self.model, "messages": messages, "temperature": temperature, "max_tokens": max_tokens, "stream": False}
        if tools: body["tools"] = tools
        last = None
        for attempt in range(4):
            try:
                r = httpx.post(f"{self.base}/chat/completions", headers={"Authorization": f"Bearer {self.key}", "Content-Type": "application/json"}, json=body, timeout=180)
                if r.status_code in (429, 500, 502, 503, 504):
                    last = f"HTTP {r.status_code}"; time.sleep(2 ** attempt * 2); continue
                if r.status_code >= 400: raise LLMError(f"DeepSeek HTTP {r.status_code}: {r.text[:300]}")
                j = r.json(); m = j["choices"][0]["message"]; u = j.get("usage", {})
                return {"content": m.get("content") or "", "tool_calls": m.get("tool_calls") or [],
                        "usage": {"prompt": u.get("prompt_tokens", 0), "completion": u.get("completion_tokens", 0), "cache_hit": u.get("prompt_cache_hit_tokens", 0)}}
            except (httpx.TimeoutException, httpx.TransportError) as e:
                last = type(e).__name__; time.sleep(2 ** attempt * 2)
        raise LLMError(f"DeepSeek không phản hồi sau 4 lần thử ({last})")


class Ollama:
    name = "ollama"

    def __init__(self, model="qwen2.5:3b", base_url="http://127.0.0.1:11434"):
        self.model, self.base = model, base_url

    def chat(self, messages, tools=None, temperature=0.0, max_tokens=1200):
        msgs = []
        for m in messages:  # OpenAI -> Ollama message shape
            m = dict(m)
            if m.get("tool_calls"):
                m["tool_calls"] = [{"function": {"name": c["function"]["name"], "arguments": json.loads(c["function"]["arguments"] or "{}")}} for c in m["tool_calls"]]
            m.pop("tool_call_id", None); msgs.append(m)
        body = {"model": self.model, "messages": msgs, "stream": False, "options": {"temperature": temperature, "seed": 7, "num_ctx": 16384, "num_predict": max_tokens}}
        if tools: body["tools"] = tools
        try:
            r = httpx.post(f"{self.base}/api/chat", json=body, timeout=900); r.raise_for_status(); j = r.json()
        except Exception as e: raise LLMError(f"Ollama lỗi: {type(e).__name__}")
        m = j["message"]
        calls = [{"id": f"call_{i}", "type": "function", "function": {"name": c["function"]["name"], "arguments": json.dumps(c["function"]["arguments"], ensure_ascii=False)}} for i, c in enumerate(m.get("tool_calls") or [])]
        return {"content": m.get("content") or "", "tool_calls": calls, "usage": {"prompt": j.get("prompt_eval_count", 0), "completion": j.get("eval_count", 0), "cache_hit": 0}}


def make_llm(name: str, model=None):
    return DeepSeek(model) if name == "deepseek" else Ollama(model or "qwen2.5:3b")
