# Báo cáo thử thách nâng cao — 2A202603895 · Nguyễn Thảo Quyên · L3B

> **Trạng thái:** đã chạy đủ dev (3 cấu hình) và test (đúng một lần) với DeepSeek. Kết quả: **30/30 trên test theo nhãn thủ công** (ngưỡng ≥27/30). **Cách chấm:** nhãn do trợ lý AI (Claude) gán bằng cách đối chiếu câu trả lời, citation và nội dung chunk; sau đó **học viên tự đối chiếu với bản gốc PDF và xác nhận các nhãn/số liệu khớp** (xác nhận của học viên, 16/11/2026; chưa có người thứ hai độc lập kiểm tra). Giá trị bảng/hình xuất phát từ ghi chú chuyển ghi do cùng AI viết, nên vẫn là rủi ro đồng nhất nếu cả hai bước cùng bỏ sót. Câu `t-mh2` ở biên (xem mục 6): nếu bị chấm nghiêm thì vẫn 29/30 ≥ 27.

## 1. Tài liệu, quyền sử dụng, index

- **Tài liệu:** *Việt Nam: Báo cáo Quốc gia về Khí hậu và Phát triển* (CCDR), Ngân hàng Thế giới, 07/2022, **bản tiếng Việt, 104 trang** PDF (trang in = trang PDF − 10), có bảng (Bảng 1–6, Phụ lục), 22 hình (biểu đồ, bản đồ, sơ đồ), 9 hộp. Nguồn: `https://www.ifc.org/content/dam/ifc/doc/mgrt/ccdr-full-report-vie-1107.pdf` (cũng có trên documents.worldbank.org). Truy cập 16/11/2026, SHA-256 trong [adv/manifest.json](../../adv/manifest.json).
- **Quyền:** trang bản quyền của tài liệu cho phép sao chép toàn bộ hoặc một phần **cho mục đích phi thương mại có ghi nhận nguồn**; dùng cho bài tập học thuật, có ghi nguồn. **PDF, văn bản trích xuất và ảnh trang không được commit** (`adv/raw/`, `adv/work/` bị git bỏ qua); repo chỉ có manifest, mã, ghi chú chuyển ghi ngắn, benchmark (trích đoạn ngắn) và trace. Người chấm tái tạo bằng `adv/fetch_pdf.sh`. Nội dung tài liệu được gửi tới API DeepSeek khi chạy agent: phù hợp với điều kiện phi thương mại trên, nhưng bạn nên tự cân nhắc trước khi chạy.
- **Đã loại:** *Việt Nam 2035* (bản tổng quan): chỉ là bản tổng quan, ít hình/biểu đồ, trang quyền không nêu giấy phép mở.
- **Phạm vi index:** 355 chunk trong pgvector (`adv_chunks`, PostgreSQL 16 + pgvector, cosine, embedding `intfloat/multilingual-e5-small` 384 chiều): 324 `text`, 9 `table`, 22 `figure`; 91/104 trang có nội dung được index ([adv/index_stats.json](../../adv/index_stats.json)).
- **Không xử lý / giới hạn:** trang 1–7 (bìa, bản quyền, mục lục); các trang mở chương toàn ảnh và trang trống (14, 21, 22, 28, 47, 48, 75, 76, 82, 89, 90, 103, 104); ảnh bìa chương là **ảnh trang trí**, không dùng cho câu hỏi ảnh. Lớp văn bản của Bảng 2–5 và Phụ lục **bị lỗi glyph số** (ví dụ `4 5 5 4 , – ,` thay cho `4,5–5,4`) nên không dùng được trực tiếp; văn bản lỗi đó vẫn nằm trong index như nhiễu.

## 2. Cách xử lý text, bảng, ảnh, biểu đồ

| Loại | Cách xử lý | Kiểm chứng |
|---|---|---|
| Văn bản | PyMuPDF, bỏ đầu/chân trang, gộp dòng, đóng gói đoạn ≤1.000 ký tự; metadata `chapter`, `chunk_type`, `page`, `printed_page` | trích đoạn evidence được kiểm tự động nằm đúng trang |
| Bảng, biểu đồ, bản đồ, sơ đồ | **Chuyển ghi từ ảnh trang**: render 105 dpi, Claude (vision) đọc và ghi vào [adv/visual_notes.json](../../adv/visual_notes.json) (30 mục, giữ số in trên hình; giá trị chỉ đọc từ đường/cột ghi "xấp xỉ"). Mỗi mục thành chunk `table`/`figure` kèm số trang, tên hình/bảng | đối chiếu từng giá trị với ảnh trang gốc khi viết câu hỏi |
| Cách chạm tới hình gốc | `page` (trang PDF) + `figure_id` ("Hình 12", "Bảng 3"); người chấm mở đúng trang PDF | — |

**Hạn chế quan trọng:** bước chuyển ghi hình/bảng là **thủ công bằng một model vision (Claude), không phải bước tự động của pipeline**; do cùng một tác nhân viết ghi chú và benchmark (ghi chú được viết **trước** câu hỏi và chỉ mô tả hệ thống mọi hình, không theo câu hỏi), có nguy cơ thiên lệch/lỗi đồng nhất. Ghi chú không tự bảo đảm đúng nên người chấm phải đối chiếu bản gốc. Hướng tự động hóa: VLM chạy cục bộ hoặc API vision cho từng trang chứa hình.

## 3. Benchmark ([adv/benchmark/questions.json](../../adv/benchmark/questions.json))

Viết và chia dev/test **trước mọi lần chạy**; dev và test là các câu khác nhau (kiểm tự động không trùng câu hỏi).

| | Bảng | Ảnh/sơ đồ | Biểu đồ | Multi-hop | Text | Thiếu bằng chứng | Tổng |
|---|---|---|---|---|---|---|---|
| **Test** (yêu cầu ≥24 + ≥6) | 6 | 5 | 5 | 4 | 4 | 6 | **30** |
| **Dev** (≥15 + ≥3) | 3 | 3 | 3 | 3 | 3 | 3 | **18** |

- Mỗi câu có ID, nhóm chính, câu hỏi, đáp án, `key_facts` (dùng cho proxy tự động), `gold` = {trang PDF, loại evidence, mô tả/trích đoạn} và lý do. Bốn multi-hop test dùng 2–3 nguồn khác trang (văn bản+hình `t-mh1`, hai phần của Bảng 5 `t-mh2`, ba nguồn có **mâu thuẫn số** `t-mh3`: văn bản 3,81 / Bảng 1 3,8 / Phụ lục 1 ghi 2,7, và hai bảng `t-mh4`). Các số suy ra (22,4 lần; 68 tỷ; 29,4%; 90,6%; 1,7 lần; 3,9 lần) được tính lại bằng mã.
- Câu thiếu bằng chứng: chủ đề gần nhưng không có (thiệt hại bằng tiền của riêng Cà Mau, hydro xanh, sản lượng thép, bão Yagi 2024 sau ngày xuất bản, vốn đầu tư EVN, giá điện đồng/kWh; dev: diện tích rừng ngập mặn, tuabin Ninh Thuận, đập thủy điện mới). Mỗi câu được kiểm bằng tìm từ khóa trên toàn bộ 104 trang và ghi chú hình/bảng (script `assert`), cộng đọc ngữ cảnh khi từ khóa xuất hiện (EVN).
- Evidence dạng văn bản được kiểm tự động nằm đúng trang (0 lỗi); evidence bảng/hình được đọc từ ảnh trang. Không đưa gold vào agent/retrieval.

## 4. Retrieval (không cần LLM, query gốc, top-k, không filter)

Độ phủ evidence: một câu "hit@k" khi các chunk top-k **cùng** phủ mọi trang gold (evidence bảng/hình cần chunk `table`/`figure`; đây là chỉ số cấp trang+loại, không phải kiểm nguyên văn). `adv/results/retrieval_*_summary.json`.

| Phương pháp | Split | Hit@1 | Hit@3 | Hit@5 |
|---|---|---|---|---|
| dense (pgvector) | dev (15) | 9/15 | 13/15 | 13/15 |
| BM25 (tiếng Việt, unigram+bigram) | dev (15) | 13/15 | 15/15 | 15/15 |
| hybrid RRF | dev (15) | 12/15 | 15/15 | 15/15 |
| dense | test (24) | 16/24 | 18/24 | 24/24 |
| BM25 | test (24) | 15/24 | 23/24 | 23/24 |
| hybrid RRF | test (24) | 16/24 | 22/24 | 24/24 |

Đọc kết quả: multi-hop là nhóm khó nhất ở top-1/top-3 (test hit@3: dense 0/4, hybrid 2/4, BM25 3/4) vì cần nhiều trang; top-5 phủ đủ 24/24 với dense và hybrid, nên agent cần **nhiều lượt tìm** cho multi-hop. **Minh bạch:** các số retrieval trên **test** ở trên được chạy một lần trước khi có kết quả agent; chúng không được dùng để chọn cấu hình (việc chọn chỉ dựa trên dev theo [adv/SELECTION.md](../../adv/SELECTION.md)), nhưng người đọc nên biết tôi đã thấy chúng.

## 5. Agent

- LLM: **DeepSeek** (`deepseek-chat`, API tương thích OpenAI, tool calling, temperature 0), khóa lấy từ `.env`/biến môi trường; lỗi API được ghi `status: error`, **không fallback giả lập**. `rag/llm.py` cũng có backend Ollama (đã dùng để thử khói trên 4 câu dev, chỉ kiểm tra luồng).
- Công cụ: `search_documents(query, kind)` (dense/BM25/hybrid; `kind` chỉ là ưu tiên loại chunk, nửa số kết quả lấy không lọc) và `get_page(page)`. Tối đa 4–6 lượt, điều kiện dừng: model trả lời hoặc hết lượt (khi đó gỡ tool để buộc trả lời); nếu chưa search, harness nhắc tối đa 2 lần. Context: dedup, giữ thứ tự xếp hạng, cắt theo budget ký tự, giữ id/trang/loại để trích dẫn. Từ chối bằng `KHÔNG_ĐỦ_BẰNG_CHỨNG`.
- Cấu hình dev: `adv_dense`, `adv_hybrid`, `adv_hybrid_wide` (xem SELECTION.md). Chọn tự động bằng `adv/select_config.py` chỉ trên dev; test chạy một lần.

## 6. Kết quả agent (DeepSeek `deepseek-chat`, temperature 0, 16/11/2026)

Dev (18 câu: 15 có đáp án + 3 thiếu bằng chứng; `adv/results/dev_*.json`). "Đạt tự động" là **proxy** (đủ `key_facts` + citation hợp lệ trên trang gold; câu thiếu bằng chứng đạt khi từ chối). Chi phí tiền: **chưa tính** (chưa điền đơn giá vào `.env`), chỉ báo token.

| Cấu hình | Đạt tự động | Context phủ gold | Abstain đúng | Từ chối nhầm | s/câu | Token vào/ra | Lượt gọi LLM |
|---|---|---|---|---|---|---|---|
| adv_dense (top-5, 12k ký tự, ≤4 lượt) | 17/18 | 14/15 | 3/3 | 0/15 | 4,3 | 141.191 / 4.546 | 41 |
| adv_hybrid (top-5, 12k, ≤4) | 17/18 | 13/15 | 3/3 | 1/15 | 3,4 | 128.062 / 4.468 | 39 |
| **adv_hybrid_wide** (top-8, 16k, ≤6) — chọn | 17/18 | **15/15** | 3/3 | 1/15 | 4,2 | 184.680 / 4.455 | 39 |

Cả ba hòa tiêu chí 1 (17/18); `adv_hybrid_wide` thắng tiêu chí 2 (context phủ gold 15/15) → được chọn tự động bằng `adv/select_config.py` (`adv/results/selected.json`) **trước khi chạy test**.

**Lỗi dev đã đọc (`d-bd3`, Hình 18, cả 3 cấu hình trượt):** (1) `adv_dense`: agent viết lại truy vấn thành "Hình 18 kịch bản giảm phát thải so với BAU" (hiểu nhầm "so với BAU" là giảm phát thải), không tìm được chunk Hình 18, và câu trả lời cuối là **đoạn markup gọi hàm thô** (`<｜DSML｜ ... invoke`) do model phát ra thay vì văn bản — một lỗi định dạng của model/API. (2) `adv_hybrid` và `adv_hybrid_wide` từ chối nhầm: `adv_hybrid_wide` thậm chí đã truy xuất đúng chunk Hình 18 (có −1,1) nhưng kết luận "không phải hình về giảm phát thải". Nguyên nhân: bám theo cách hiểu sai của truy vấn đầu và quy tắc từ chối quá chặt trong prompt. Tôi **không sửa** prompt sau khi biết lỗi này (để test độc lập); đây là hướng cải thiện (nhắc đọc lại câu hỏi gốc trước khi từ chối; phát hiện và thử lại khi trả lời chứa markup công cụ). Trên test không có câu trả lời nào chứa markup (0/30).

Test (30 câu, **một lần**, `adv_hybrid_wide`; `adv/results/test_final.json`, nhãn `labels_test.json`, tính bằng `adv/score_test.py`):

| Nhóm test | Đạt / tổng | Tỷ lệ | Lỗi / nhận xét |
|---|---|---|---|
| Bảng | 6/6 | 100% | |
| Ảnh, sơ đồ | 5/5 | 100% | |
| Biểu đồ | 5/5 | 100% | |
| Multi-hop | 4/4 | 100% | `t-mh2` ở biên: ý chính đúng (68 > 44 vì than −19, khí −8), nhưng lời giải thích phụ nêu "sinh khối" không có trong Bảng 5 (phần chênh thực là lưu trữ +3). `t-mh3` nêu đúng mâu thuẫn 3,81/3,8 so với 2,7. |
| Text | 4/4 | 100% | |
| Thiếu bằng chứng | 6/6 | 100% | cả 6 từ chối đúng, không thêm khẳng định; nêu đúng số gần liên quan (ví dụ 79% diện tích Cà Mau, 17 tỷ USD cho cả ĐBSCL) |
| **Toàn bộ** | **30/30** | **100%** | cần ≥27/30 |

Chỉ số khác trên test: lỗi hệ thống/timeout 0; Context phủ gold 24/24; dùng tool 30/30 (số lượt tìm: 2 lượt ×23, 3 ×1, 4 ×5, 6 ×1); 67 lượt gọi LLM, 329.093 token vào / 8.184 token ra, 97 s tổng (3,2 s/câu); chi phí tiền chưa tính. Về citation: mọi câu có đáp án đều có ít nhất một citation hợp lệ nằm trong context; tôi đã đối chiếu các citation phụ (ví dụ p52 cho `t-bang4`, p58 cho `t-anh3`) với nội dung chunk thật. Một số citation phụ không chứa ý được gán (ví dụ `p12:t2` không chứa "khử carbon"), nhưng citation chính của mỗi số liệu đều đúng.

## 7. Giới hạn đã biết (trước khi có kết quả agent)

1. Kết quả 30/30 dựa trên nhãn do AI gán và được học viên tự đối chiếu bản gốc, chưa có người chấm độc lập; test chỉ 30 câu, một lần chạy, một model, nên không suy rộng. Dev và test cùng dùng một prompt; các câu test được viết bởi cùng tác nhân đã viết ghi chú chuyển ghi.
2. Chuyển ghi hình/bảng do cùng một AI thực hiện, chưa kiểm chéo bởi người thứ hai; giá trị đọc từ biểu đồ là xấp xỉ, các câu hỏi chỉ dùng số in trên hình hoặc so sánh rõ ràng.
3. Nhãn cuối cùng cần người chấm đối chiếu bản gốc; proxy tự động (khớp `key_facts` + citation đúng trang) chỉ dùng để chọn cấu hình trên dev.
4. `e5-small` cắt ở 512 token: các chunk bảng dài đã được cắt ≤900 ký tự để vector phủ hết nội dung.
5. Test nhỏ (30 câu), một lần chạy, một model; thời gian/chi phí đo trên một lần chạy.
6. Chi phí DeepSeek chỉ được ước tính nếu bạn điền đơn giá vào `.env`; tôi không ghi sẵn đơn giá vì có thể đã đổi.
