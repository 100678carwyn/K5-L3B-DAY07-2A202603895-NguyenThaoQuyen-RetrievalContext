# Báo cáo Day 7 — Agentic RAG (2A202603895 · Nguyễn Thảo Quyên · L3B)

## Dữ liệu và benchmark

- Nguồn, quyền, trang, chunk: OpenStax *Introduction to Computer Science* (CC BY-NC-SA 4.0), chương 8 (PDF tr. 370–389) và chương 9 (tr. 440–459) = 40 trang nội dung (manifest Day 6: `data/real/day6_manifest.json`; trang đã chuẩn hóa: `data/real/pages.jsonl`). 176 chunk (chiến lược B của Day 6, trung bình 754 ký tự) xuất ra `data/real/chunks.json` bằng `src/export_day6.py`.
- Vector store / embedding: PostgreSQL 16 + pgvector 0.8.7 (container Day 6 `day6_student_starter-postgres-1`, bảng `chunks`, strategy `B`, cosine, tìm kiếm chính xác không ANN), `intfloat/multilingual-e5-small` (384 chiều, local, tiền tố `query: `/`passage: `, sentence-transformers 6.3.0). Query embedding dùng đúng model/index Day 6. Chi phí embedding 0 USD.
- Agent: **Ollama 0.23.1, `qwen2.5:3b` local** (tool calling thật, temperature 0, seed 7, num_ctx 8192). Chi phí 0 USD.
- Phân chia: **dev = 24 câu có đáp án + 3 câu thiếu evidence**; **test = 6 câu có đáp án + 2 câu thiếu evidence** (`benchmark/questions.json`, sinh bởi `src/build_benchmark.py`). 24 câu dev lấy từ Day 6 (18 dev + 6 test Day 6; 6 câu test Day 6 đã được xem ở Day 6 nên **gán lại thành dev**). 6 câu test là câu **mới**, viết từ corpus trước mọi lần chạy Day 7, gold nằm ở tr. 377, 379, 450, 455, 457; chỉ tr. 450 trùng với một gold thay thế của dev (`dev-d12`), các trang còn lại không phải gold của câu dev nào. Câu có filter: dev 5, test 2 (`test-n04` chương 9, `test-n06` chương 8). Filter là ngữ cảnh người dùng ("đang đọc chương N") do harness áp dụng, không lấy từ gold.
- Câu thiếu evidence: kiểm bằng grep từ khóa trên cả 40 trang (`absence_reason` trong từng câu; script assert không có từ khóa). Evidence của câu có đáp án được script kiểm nằm đúng trang gold sau chuẩn hóa (0 lỗi).

## Retrieval và thử nghiệm

Ba phương pháp (`rag/retrievers.py`): **dense** (pgvector Day 6), **BM25** (Okapi, tự cài, nhẹ), **hybrid RRF** (dense + BM25, k=60, pool 20). Hit = chunk đúng nguồn/trang **và** chứa nguyên evidence (chuẩn hóa).

Retrieval thuần (query gốc, top-3, không LLM; `results/retrieval_dev_summary.json`, `retrieval_test_summary.json`):

| Phương pháp | Split | Hit@1 | Evidence Hit@3 | Hit@3 khi áp filter |
|---|---|---|---|---|
| dense | dev | 15/24 | 18/24 | 19/24 |
| BM25 | dev | 11/24 | 15/24 | 16/24 |
| hybrid RRF | dev | 11/24 | 20/24 | 21/24 |
| dense / BM25 / hybrid | test | 5/6 | 6/6 | 6/6 (cả ba) |

Agent trên dev (27 câu: 24 có đáp án, 3 thiếu evidence; `results/agent/dev_*.json`). Context Evidence Rate = số câu có đủ evidence trong **context cuối** gửi model; "Hit@1 truy vấn agent" là Hit@1 của lượt tìm đầu với query do model viết lại (khác query gốc).

| Cấu hình | Phương pháp, top-k, budget, lượt | Giả thuyết | Context Evidence Rate | Hit@1 query agent | Abstain đúng | Từ chối nhầm | s/câu (tổng) | Token vào/ra |
|---|---|---|---|---|---|---|---|---|
| **Baseline** `base_dense` | dense, 3, 2500, ≤2 | Index Day 6 dùng được | 16/24 | 12/24 | 3/3 | 3/24 | 22,0 (593 s) | 35.430 / 2.737 |
| Phương pháp 2 `base_bm25` | BM25, 3, 2500, ≤2 | Từ khóa tốt cho thuật ngữ hiếm | 14/24 | 12/24 | 2/3 | 3/24 | 32,0 (864 s) | 36.364 / 3.005 |
| Phương pháp 3 `base_hybrid` | hybrid RRF, 3, 2500, ≤2 | Hợp nhất tăng recall | 17/24 | 11/24 | 3/3 | 1/24 | 22,4 (605 s) | 35.103 / 3.066 |
| **Cải thiện 1** `imp_topk5` (chọn) | hybrid, **5**, **4000**, ≤2 | Nhiều candidate + budget lớn tăng CER | **20/24** | 11/24 | 3/3 | 3/24 | **17,7** (477 s) | 44.120 / 2.834 |
| Cải thiện 2 `imp_neighbors` | hybrid, 3, 4000, ≤3, + chunk liền kề | Evidence bị cắt giữa hai chunk | 20/24 | 11/24 | 3/3 | 3/24 | 21,9 (591 s) | 44.216 / 2.904 |

Tiêu chí chọn chốt **trước** khi chạy agent (`SELECTION_CRITERIA.md`): (1) Context Evidence Rate, (2) abstention đúng / từ chối nhầm nếu chênh ≤1 câu, (3) thời gian. `imp_topk5` và `imp_neighbors` hòa (1) và (2) nên chọn theo (3): `imp_topk5`. Hybrid và dense/BM25 hòa ở Hit@1 nhưng hybrid có Hit@3 cao nhất.

Test (chạy **một lần** sau khi chốt; `results/agent/test_*.json`):

| Cấu hình | Split | Hit@1 query gốc | Evidence Hit@3 query gốc | Context Evidence Rate | s/câu (tổng) | Token vào/ra |
|---|---|---|---|---|---|---|
| Baseline `base_dense` | test | 5/6 | 6/6 | 6/6 | 26,3 (210 s) | 10.683 / 849 |
| Đã chọn `imp_topk5` | test | 5/6 (hybrid, query gốc) | 6/6 | 6/6 | 14,6 (117 s) | 13.285 / 751 |

**Hai lỗi dev (đã đọc, đối chiếu nguồn):**
1. `dev-d03` ("final say over who may access a dataset", gold tr. 375). Cả `base_dense` và `imp_topk5` từ chối (`INSUFFICIENT_EVIDENCE`). Nguyên nhân: model viết lại query thành "final say over dataset", làm mất "access/usage"; với query gốc dense xếp gold hạng **1**, nhưng với query viết lại gold nằm ngoài top-20. Dùng query "who decides access to and usage of data data owner" thì dense lại xếp hạng 1. → Lỗi do **query rewriting của model 3B**, không phải chỉ mục. Chưa sửa (ví dụ ép tool dùng thêm câu hỏi gốc); đây là hướng cải thiện.
2. `dev-d07` (Codd/1970, gold tr. 383). Câu trả lời của agent **đúng** (Codd, 1970) nhưng bị tính là không có evidence trong context: chunk `p383:B01` chứa cả "Codd" lẫn "1970" nhưng chuỗi evidence gold không khớp nguyên văn với chunk. → Lỗi **nhãn/metric khớp chuỗi**, nên Context Evidence Rate có thể thấp hơn thực tế. Tôi không sửa lại gold sau khi xem kết quả để tránh thay đổi benchmark.

Các cải thiện: tăng top-k từ 3 lên 5 và budget 2500 → 4000 nâng CER từ 17/24 (hybrid baseline) lên 20/24 với chi phí ~26% token đầu vào. Thêm chunk liền kề + tìm 3 lượt cho cùng CER 20/24 (hầu hết câu chỉ search 1 lần, 26 hoặc 27/27) nên không đáng kể.

## Agent và đánh giá

- Agent (`rag/agent.py`): một tool `search_documents(query)`; model quyết định query; harness áp filter chương (ngữ cảnh người dùng), chọn context (dedup, giữ thứ tự xếp hạng, cắt theo budget ký tự, tùy chọn chunk liền kề), kiểm ID citation. Điều kiện dừng: model trả lời không gọi tool, hoặc hết `max_searches` (khi đó tool bị gỡ để buộc trả lời). Nếu model trả lời mà chưa search, harness nhắc tối đa 2 lần ("nudge") — ghi trong event. Từ chối bằng chuỗi `INSUFFICIENT_EVIDENCE`. Lỗi provider được ghi `status: error`, không giả kết quả (0 lỗi ở mọi lần chạy). Nội dung tài liệu coi là dữ liệu.
- Tool use (dev và test): 27/27 và 8/8 cho mọi cấu hình; số lượt gọi: gần như toàn bộ 1 lượt (phân bố trong `summarize_agent.py`).

Test, **nhãn thủ công** (`results/manual/reviews_test_*.json`, tổng hợp bằng `starter/agent_metrics.py` → `results/agent/test_*_manual_summary.json`):

| Cấu hình / split | Tool use | Lượt gọi | Grounded answer 0/1/2, TB | Citation hợp lệ (hỗ trợ / tổng) | Câu có citation | Abstention đúng | Từ chối nhầm | Context 0/1/2 (6 câu) |
|---|---|---|---|---|---|---|---|---|
| `base_dense` test | 8/8 | 1 lượt × 8 | 0/5/1, **1,17/2** | 2/3 | 2/6 | 2/2 | 0/6 | 0/0/6 |
| `imp_topk5` test | 8/8 | 1 lượt × 8 | 0/4/2, **1,33/2** | 2/2 | 2/6 | 2/2 | 0/6 | 0/0/6 |

| Query | Loại | Tool call → kết quả | Trả lời / citation | Nhãn, lý do |
|---|---|---|---|---|
| test-n06 (cả hai) | có đáp án + filter ch.8 | `GIS database application example` → `p377:B02` | "Google Maps" [p377:B02] | 2: đúng, citation hỗ trợ |
| test-n02 `base_dense` | có đáp án | `DBMS component translate statements` → `p379:B01, p382:B02, p382:B00` | "DDL compiler" cite `p382:B02` | 1: đúng nhưng citation `p382:B02` **không chứa** câu DDL (nằm ở `p379:B01`) |
| test-n04 `imp_topk5` | có đáp án + filter ch.9 | `numbers at associations UML…` → `p455:B01…` | multiplicities; ví dụ BlindSpotDetection–Car không có trong nguồn | 1: lõi đúng, thêm khẳng định vô căn cứ, không citation |
| test-a1 / a2 (cả hai) | thiếu evidence | Scrum stand-up / Oracle license | `INSUFFICIENT_EVIDENCE` | abstention đúng, không bịa |

Mỗi câu trả lời, citation, lý do nằm trong `results/manual/reviews_test_*.json`; trace đầy đủ trong `results/agent/*.json`.

Phát hiện chính: mọi cấu hình đều **tìm đúng evidence** (Context Evidence Rate test 6/6) nhưng **chất lượng câu trả lời của model 3B hạn chế**: 4–5/6 câu có thêm khẳng định vô căn cứ và chỉ 2/6 câu có citation (model hay quên cite dù prompt yêu cầu). Retrieval tốt chưa đảm bảo câu trả lời đúng, đúng như BENCHMARK.md lưu ý.

- Lệnh chạy và thời gian: xem `README.md` mục "Day 7"; dev ≈ 55 phút, test ≈ 6 phút trên máy macOS CPU. Chi phí API 0 USD.

## Kết luận, đánh đổi, giới hạn

- Chọn `imp_topk5` (hybrid RRF, top-5, budget 4000): CER dev cao nhất (hòa), nhanh nhất; test không kém baseline (CER 6/6, grounded 1,33 so với 1,17).
- Đánh đổi: top-5/budget 4000 tăng ~25% token đầu vào nhưng thời gian trung bình lại thấp hơn (17,7 s so với 22,4 s); tôi chưa điều tra nguyên nhân, có thể do tải máy hoặc độ dài câu trả lời, nên không kết luận.
- **Hạn chế:** (1) test chỉ 6+2 câu và quá dễ — cả ba phương pháp retrieval hòa 6/6 Hit@3 ở test, nên **không phân biệt được** phương pháp tốt hơn; chênh lệch 1/6 không có ý nghĩa thống kê. (2) 6 câu dev lấy từ test Day 6 (đã xem ở Day 6). (3) Nhãn test do một người chấm (AI) gán, chưa kiểm chéo, có thể thiên lệch; citation hỗ trợ chấm mức chunk, chưa chấm từng điều kiện. (4) Dev chỉ có chỉ số tự động (Context Evidence Rate, abstain theo `status`); câu trả lời dev không chấm thủ công, chỉ đọc lỗi. (5) Metric khớp chuỗi nguyên văn bỏ sót evidence diễn đạt khác (d07). (6) Model agent 3B local yếu về citation/bám nguồn. (7) Thời gian đo trên một máy, một lần chạy, không lặp để đo phương sai.
- Nếu làm tiếp: buộc tool luôn thêm câu hỏi gốc vào query (sửa d03); model lớn hơn hoặc few-shot bắt buộc citation; thêm test mới có nhiều câu khó (ngoại lệ, nhiều đoạn); chấm bởi người thứ hai.
- Thử thách nâng cao (+15đ): đã dựng (tài liệu tiếng Việt 104 trang, index, benchmark 30 test + 18 dev, agent DeepSeek) nhưng **kết quả test chưa chạy/chấm, chưa có bằng chứng ≥90%**; xem [báo cáo nâng cao](2A202603895_NguyenThaoQuyen_ADVANCED.md).
