# Tiêu chí chọn cấu hình — thử thách nâng cao (chốt TRƯỚC khi chạy agent trên dev/test)

Chọn **chỉ dựa trên dev** (15 câu có đáp án + 3 câu thiếu bằng chứng) bằng `adv/select_config.py`, theo thứ tự:
1. **Tỷ lệ đạt tự động** cao nhất (proxy: câu có đáp án đạt khi trả lời đủ `key_facts` và có ít nhất một citation hợp lệ nằm trên trang gold; câu thiếu bằng chứng đạt khi từ chối; lỗi hệ thống tính không đạt).
2. Hòa → số câu có đáp án mà context cuối chứa đủ trang/loại evidence gold (`context_covers_gold`).
3. Hòa → thời gian trung bình mỗi câu thấp hơn.

Test chỉ chạy **một lần** với cấu hình được chọn sau khi dev xong; **không** chỉnh gì sau khi xem test. Kết quả chấm cuối cùng trên test là nhãn đạt/không đạt do người đọc đối chiếu bản gốc (xem `ADVANCED_REPORT.md`), không phải proxy tự động.

Cấu hình thử trên dev (cùng index, cùng câu hỏi, cùng LLM):
- `adv_dense`: dense (pgvector), top_k=5, budget 12.000 ký tự, tối đa 4 lượt.
- `adv_hybrid`: hybrid RRF (dense + BM25 tiếng Việt), top_k=5, budget 12.000, tối đa 4 lượt.
- `adv_hybrid_wide`: hybrid RRF, top_k=8, budget 16.000, tối đa 6 lượt.
