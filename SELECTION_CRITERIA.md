# Tiêu chí chọn cấu hình (chốt TRƯỚC khi chạy bất kỳ agent dev/test nào)

Chọn trên **dev** (24 câu có đáp án + 3 câu thiếu evidence), theo thứ tự ưu tiên:
1. **Context Evidence Rate** cao nhất (câu có đáp án mà context cuối chứa đủ evidence).
2. Nếu chênh ≤1 câu: **abstention đúng cao hơn và từ chối nhầm thấp hơn** (tính theo `status` của agent).
3. Nếu vẫn hòa: **thời gian trung bình/câu thấp hơn**.

Chi phí API = 0 USD ở mọi cấu hình (embedding và LLM đều chạy local), nên không dùng làm tiêu chí.
Test chỉ chạy **một lần** cho baseline và cấu hình đã chọn, sau khi tiêu chí này và kết quả dev đã được chốt.

Cấu hình thử nghiệm (định nghĩa trước khi có kết quả agent):
- `base_dense`, `base_bm25`, `base_hybrid`: ba phương pháp retrieval, top_k=3, budget=2500 ký tự, tối đa 2 lượt search. Baseline = `base_dense`.
- `imp_topk5`: hybrid_rrf, top_k=5, budget=4000 (giả thuyết: nhiều candidate hơn làm tăng Context Evidence Rate).
- `imp_neighbors`: hybrid_rrf, top_k=3, budget=4000, thêm chunk liền kề của kết quả đầu, tối đa 3 lượt search (giả thuyết: evidence bị cắt giữa hai chunk và truy vấn lại giúp lấy đủ).

## Kết quả chọn (ghi TRƯỚC khi chạy test)
Dev: `imp_topk5` và `imp_neighbors` cùng Context Evidence Rate 20/24 (cao nhất), cùng abstention 3/3 và cùng từ chối nhầm 3/24 → xét tiêu chí 3 (thời gian): `imp_topk5` 17,7 s/câu < `imp_neighbors` 21,9 s/câu.
**Cấu hình chọn: `imp_topk5`** (hybrid_rrf, top_k=5, budget 4000, tối đa 2 lượt search). Baseline: `base_dense`. Test chạy đúng một lần cho hai cấu hình này.
