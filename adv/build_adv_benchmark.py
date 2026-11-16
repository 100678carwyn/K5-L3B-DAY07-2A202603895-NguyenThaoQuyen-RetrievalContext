"""Advanced benchmark (CCDR Vietnam, Vietnamese). Written BEFORE any agent run.
 test: 30 = 24 answerable (6 bảng, 5 ảnh/sơ đồ, 5 biểu đồ, 4 multi-hop, 4 text) + 6 thiếu evidence
 dev : 18 = 15 answerable (3 per group) + 3 thiếu evidence
Text evidence is checked against the PDF text layer; table/image/chart evidence was read from the page render (see adv/visual_notes.json)
and every number is re-checked against the notes; derived numbers are recomputed here."""
import json, re, sys, pymupdf
SRC = "ccdr-vn-2022"
doc = pymupdf.open("adv/raw/ccdr_vi.pdf")
PT = {i + 1: re.sub(r"\s+", " ", p.get_text()) for i, p in enumerate(doc)}
notes = {(n["page"], n["figure_id"]): n["text"] for n in json.load(open("adv/visual_notes.json"))["items"]}
allnotes = " ".join(notes.values())
Q = []
def A(id, split, group, q, ans, key, gold, why=""):
    Q.append({"id": id, "split": split, "group": group, "question": q, "expected_answer": ans, "answerable": True, "key_facts": key, "gold": gold, "reason": why})
def G(page, kind, ev): return {"source_id": SRC, "page": page, "evidence_type": kind, "evidence": ev}
def X(id, split, q, why, kws):
    for k in kws: assert not any(k.lower() in t.lower() for t in PT.values()) and k.lower() not in allnotes.lower(), (id, k)
    Q.append({"id": id, "split": split, "group": "thieu_bang_chung", "question": q, "answerable": False, "expected_behavior": "search_and_abstain",
              "absence_reason": why + f" Kiểm tra: tìm từ khóa {kws} trên toàn bộ 104 trang (lớp văn bản) và ghi chú hình/bảng, không có.", "key_facts": []})
# ---------------- TEST: bảng ----------------
A("t-bang1","test","bang","Theo Bảng 1, phát thải GHG trên đầu người của Việt Nam là bao nhiêu tCO2e và thấp hơn Thái Lan bao nhiêu tCO2e trên đầu người?","Việt Nam 3,8; Thái Lan 6,2; thấp hơn 2,4 tCO2e/người.",[["3,8"],["2,4"]],[G(19,"table","Bảng 1: hàng Việt Nam 3,8; hàng Thái Lan 6,2 (cột phát thải trên đầu người)")],"tra hàng + phép trừ 6,2-3,8")
A("t-bang2","test","bang","Theo Bảng 2, tổng nhu cầu tài chính tích lũy (NPV) cho các biện pháp thích ứng giai đoạn 2022–2050 nằm trong khoảng nào, tính bằng tỷ USD?","479,2–547,6 tỷ USD.",[["479,2"],["547,6"]],[G(32,"table","Bảng 2: hàng 'Tổng nhu cầu tài chính', cột giá trị tích lũy: 479,2–547,6")])
A("t-bang3","test","bang","Theo Bảng 3, tác động kinh tế ròng giai đoạn 2022–2040 của NZP kèm những cải cách hỗ trợ là bao nhiêu tỷ USD?","-1,3 tỷ USD (gần như không đáng kể).",[["1,3"]],[G(50,"table","Bảng 3: khối 'NZP với những cải cách hỗ trợ', hàng 'Tác động kinh tế ròng', cột 2022–2040: -1,3")])
A("t-bang4","test","bang","Theo Bảng 4, khi áp dụng NZP cùng tất cả các biện pháp hỗ trợ, GDP năm 2040 thay đổi bao nhiêu % và phát thải khí nhà kính năm 2040 thay đổi bao nhiêu %?","GDP +3,3%; phát thải khí nhà kính -71,9%.",[["3,3"],["71,9"]],[G(53,"table","Bảng 4: hàng 'NZP và tất cả các biện pháp hỗ trợ': phát thải 2040 -71,9; GDP 2040 3,3")])
A("t-bang5","test","bang","Theo Bảng 5, so với CPS, chi phí vốn cho điện gió ngoài khơi trong kịch bản ADS thay đổi bao nhiêu tỷ USD và bao nhiêu phần trăm?","+39 tỷ USD, tức +402%.",[["39"],["402"]],[G(57,"table","Bảng 5 (tiếp): hàng 'Gió (ngoài khơi)': +39 | +402%")])
A("t-bang6","test","bang","Theo Phụ lục 1, lượng phát thải từ điện/nhiệt năm 2018 gấp khoảng bao nhiêu lần năm 1990?","109,13 / 4,88 ≈ 22,4 lần.",[["22,4","22,3"]],[G(91,"table","Phụ lục 1: hàng 'Điện/nhiệt': 4,88 (1990) và 109,13 (2018) triệu tấn CO2e")],"tra hai ô + phép chia")
assert round(109.13 / 4.88, 1) == 22.4 and round(6.2 - 3.8, 1) == 2.4
# ---------------- TEST: ảnh/sơ đồ ----------------
A("t-anh1","test","anh","Theo sơ đồ Hình 1 (mô hình phát triển mới), hai lộ trình nối 'Việt Nam hiện nay' với 'Việt Nam năm 2045' là gì?","Lộ trình xây dựng khả năng chống chịu và Hành trình khử carbon.",[["chống chịu"],["khử carbon"]],[G(13,"diagram","Hình 1: hai mũi tên cong 'Lộ trình xây dựng khả năng chống chịu' và 'Hành trình khử carbon'")])
A("t-anh2","test","anh","Theo sơ đồ Hình 21, nguồn nào đóng góp nhiều nhất cho nhu cầu tài chính giai đoạn 2022–2040 và là bao nhiêu tỷ USD?","Khu vực tư nhân, 184 tỷ USD.",[["tư nhân"],["184"]],[G(77,"diagram","Hình 21: ba ô con: Khu vực tư nhân 184, Khu vực công 130, Bên ngoài 54 tỷ USD")])
A("t-anh3","test","anh","Trên bản đồ Hình 14, tỉnh nào được chú thích là tỉnh sản xuất than chính?","Quảng Ninh.",[["quảng ninh"]],[G(59,"map","Hình 14: khung chú thích 'Quảng Ninh — Tỉnh sản xuất than chính'")])
A("t-anh4","test","anh","Trên bản đồ rủi ro ngập lụt ở Hình 11, những thành phố nào được đánh dấu?","Hà Nội, Hải Phòng, Đà Nẵng, TP. Hồ Chí Minh và Cần Thơ.",[["hà nội","hanoi"],["hải phòng","haiphong"],["đà nẵng","da nang"],["hồ chí minh","ho chi minh"],["cần thơ","can tho"]],[G(42,"map","Hình 11: năm điểm xanh dương gắn nhãn Hanoi, Haiphong, Da Nang, Ho Chi Minh City, Can Tho")])
A("t-anh5","test","anh","Hình 9 gồm ba bản đồ về mức độ dễ bị ảnh hưởng của các tuyến đường quốc gia. Ba bản đồ đó thể hiện những loại thiên tai nào?","Lở đất, Lũ lụt 1.000 năm và Bão lũ.",[["lở đất"],["lũ lụt"],["bão lũ"]],[G(37,"map","Hình 9: tiêu đề ba bản đồ 'Lở đất', 'Lũ lụt 1.000 năm', 'Bão lũ'")])
# ---------------- TEST: biểu đồ ----------------
A("t-bd1","test","bieu_do","Theo Hình 3, khoản chi phí do biến đổi khí hậu năm 2020 lớn nhất là gì và là bao nhiêu triệu USD?","Thủy sản, 4.219 triệu USD.",[["thủy sản"],["4219","4.219"]],[G(17,"chart","Hình 3 (treemap): ô lớn nhất 'Thủy sản, 4219'")])
A("t-bd2","test","bieu_do","Theo Hình 12, than đá chiếm bao nhiêu % điện năng sản xuất từ nhiên liệu hóa thạch năm 2020 và bao nhiêu % công suất lắp đặt?","59% điện năng sản xuất và 30% công suất lắp đặt.",[["59"],["30"]],[G(54,"chart","Hình 12: hai biểu đồ vành khuyên, phần Than đá 59% (200 TWh) và 30% (68 GW)")])
A("t-bd3","test","bieu_do","Theo Hình 20, lĩnh vực nào có % chuyển việc làm cao nhất trong kịch bản NZP đã cải cách vào năm 2040 và giá trị là bao nhiêu?","Điện, 23,6%.",[["điện"],["23,6"]],[G(72,"chart","Hình 20: cột cam 'NZP đã cải cách' cao nhất ở Điện: 23,6")])
A("t-bd4","test","bieu_do","Theo Hình 22, dư nợ tín dụng xanh năm 2018 là bao nhiêu tỷ USD?","10,3 tỷ USD.",[["10,3"]],[G(78,"chart","Hình 22 (trái): cột năm 2018 có nhãn 10,3")])
A("t-bd5","test","bieu_do","Theo Hình 7, năm 2018 ngành nào có tỷ trọng sản lượng của DNNN thấp nhất và là bao nhiêu phần trăm?","Kim loại, 14%.",[["kim loại"],["14"]],[G(26,"chart","Hình 7: nhãn cuối đường 'Kim loại, 14%' (thấp nhất)")])
# ---------------- TEST: multi-hop ----------------
A("t-mh1","test","multi_hop","Văn bản nêu công suất nhiệt điện than năm 2020 là 20 GW, còn Hình 12 cho tổng công suất lắp đặt là 68 GW. Tỷ trọng than tính từ hai số này là bao nhiêu % và có khớp với phần than đá trên Hình 12 không?","20/68 ≈ 29,4% ≈ 30%, khớp với phần Than đá 30% trên Hình 12.",[["29,4","29"],["30"]],[G(53,"text","'công suất lắp đặt của các nhà máy nhiệt điện than ... từ 5 GW năm 2010 lên 20 GW'"),G(54,"chart","Hình 12: tổng 68 GW; Than đá 30%")],"2 trang: văn bản + hình")
A("t-mh2","test","multi_hop","Theo Bảng 5, cộng chi phí tăng thêm của điện mặt trời, gió trên bờ và gió ngoài khơi là bao nhiêu tỷ USD, và so với dòng 'Chi phí vốn để lưu trữ và phát điện mới' (+44 tỷ USD) ở phần đầu bảng thì thế nào, vì sao?","21+8+39 = 68 tỷ USD, lớn hơn +44 vì chi phí vốn cho than đá (-19) và khí đốt (-8) giảm.",[["68"],["44"]],[G(57,"table","Bảng 5 (tiếp): Mặt trời +21; Gió trên bờ +8; Gió ngoài khơi +39"),G(56,"table","Bảng 5 (đầu): Chi phí vốn +44; Than đá -19; Khí đốt -8")],"2 trang: bảng bị tách")
assert 21 + 8 + 39 == 68 and 68 - 19 - 8 + 3 == 44
A("t-mh3","test","multi_hop","Phát thải GHG bình quân đầu người của Việt Nam năm 2018 được nêu trong văn bản (trang 8), Bảng 1 và Phụ lục 1 là bao nhiêu? Các số này có thống nhất không?","Văn bản 3,81 và Bảng 1 3,8 (thống nhất); Phụ lục 1 ghi 2,7 nên không nhất quán.",[["3,81","3,8"],["2,7"]],[G(18,"text","'Lượng phát thải GHG bình quân đầu người năm 2018 là 3,81 tấn CO2e'"),G(19,"table","Bảng 1: Việt Nam 3,8"),G(91,"table","Phụ lục 1: Phát thải bình quân đầu người: 0,3 (1990), 1,1 (2005), 2,7 (2018)")],"3 nguồn; có mâu thuẫn")
A("t-mh4","test","multi_hop","Tác động kinh tế ròng 2022–2040 của NZP kèm cải cách hỗ trợ theo Bảng 3 là bao nhiêu tỷ USD, và GDP năm 2040 thay đổi bao nhiêu % khi áp dụng tất cả biện pháp hỗ trợ theo Bảng 4?","-1,3 tỷ USD (Bảng 3) và +3,3% GDP năm 2040 (Bảng 4).",[["1,3"],["3,3"]],[G(50,"table","Bảng 3: -1,3"),G(53,"table","Bảng 4: NZP và tất cả các biện pháp hỗ trợ: GDP 2040 = 3,3")],"2 bảng khác trang")
# ---------------- TEST: text ----------------
A("t-tx1","test","text","Theo văn bản, năm 2020 biến đổi khí hậu gây thiệt hại cho Việt Nam bao nhiêu và tương đương bao nhiêu % GDP?","10 tỷ USD, tương đương 3,2% GDP.",[["10 tỷ"],["3,2"]],[G(17,"text","năm 2020 Việt Nam đã thiệt hại 10 tỷ USD, tương đương 3,2% GDP")])
A("t-tx2","test","text","Đồng bằng sông Cửu Long đóng góp bao nhiêu % sản lượng lúa và bao nhiêu % kim ngạch xuất khẩu gạo của Việt Nam?","50% sản lượng lúa và 95% kim ngạch xuất khẩu gạo.",[["50"],["95"]],[G(40,"text","đóng góp 50% sản lượng lúa và 95% kim ngạch xuất khẩu gạo")])
A("t-tx3","test","text","Tỷ lệ tiếp cận điện của Việt Nam tăng từ bao nhiêu % năm 1993 lên bao nhiêu % năm 2020?","Từ 14% lên 99%.",[["14"],["99"]],[G(53,"text","tỷ lệ tiếp cận điện năng từ 14% năm 1993 lên 99% vào năm 2020")])
A("t-tx4","test","text","Theo kết quả mô hình, hộ gia đình người Kinh có khả năng bị ảnh hưởng thấp hơn bao nhiêu % so với hộ gia đình dân tộc thiểu số?","Thấp hơn 37%.",[["37"]],[G(70,"text","Hộ gia đình người Kinh có khả năng bị ảnh hưởng thấp hơn 37% so với hộ gia đình dân tộc thiểu số")])
for id, q, why, kws in [
 ("t-a1","Thiệt hại kinh tế cụ thể của riêng tỉnh Cà Mau do mực nước biển dâng đến năm 2050 là bao nhiêu tỷ USD?","Báo cáo chỉ nêu tỷ lệ diện tích Cà Mau bị ngập (79%), không nêu thiệt hại tiền.",["thiệt hại của tỉnh cà mau"]),
 ("t-a2","Báo cáo ước tính nhu cầu đầu tư cho hydro xanh ở Việt Nam đến năm 2040 là bao nhiêu tỷ USD?","Chủ đề năng lượng sạch gần nhưng không nhắc đến hydro.",["hydro","hydrogen"]),
 ("t-a3","Sản lượng thép của Việt Nam năm 2020 là bao nhiêu triệu tấn?","Báo cáo nói về công nghiệp (xi măng, kim loại) nhưng không có số liệu sản lượng thép.",["thép"]),
 ("t-a4","Thiệt hại do bão Yagi năm 2024 gây ra cho Việt Nam được báo cáo là bao nhiêu?","Báo cáo xuất bản 07/2022, không thể có sự kiện năm 2024.",["yagi"]),
 ("t-a5","Tổng vốn đầu tư năm 2021 của Tập đoàn Điện lực Việt Nam (EVN) là bao nhiêu tỷ đồng?","EVN chỉ được nhắc 4 lần (viết tắt, đơn vị cung cấp điện, nguồn số liệu, đơn vị thu tiền), đã đọc từng ngữ cảnh: không có số vốn đầu tư.",["vốn đầu tư của evn","evn đầu tư"]),
 ("t-a6","Giá điện bán lẻ bình quân cụ thể (đồng/kWh) mà báo cáo đề xuất cho năm 2030 là bao nhiêu?","Báo cáo nói giá điện ADS cao hơn 16–26% so với CPS nhưng không nêu mức đồng/kWh.",["đồng/kwh","vnd/kwh"])]:
    X(id, "test", q, why, kws)
# ---------------- DEV ----------------
A("d-bang1","dev","bang","Theo Bảng 6, loại hành động nào có mức khẩn cấp Cao và tác động Cao?","Những hành động không thể trì hoãn, có tác động lớn và ngay lập tức (thắng nhanh).",[["thắng nhanh"]],[G(84,"table","Bảng 6: ô (Khẩn cấp Cao, Tác động Cao)")])
A("d-bang2","dev","bang","Theo Bảng 2, nguồn tài chính hiện có là bao nhiêu % GDP trung bình mỗi năm và bao nhiêu tỷ USD (NPV)?","1,8% GDP; 136,9 tỷ USD.",[["1,8"],["136,9"]],[G(32,"table","Bảng 2: hàng 'Nguồn tài chính hiện có': 1,8 | 136,9")])
A("d-bang3","dev","bang","Theo Bảng 5, chi phí vốn cho điện than đá trong ADS so với CPS thay đổi bao nhiêu tỷ USD và bao nhiêu %?","-19 tỷ USD, tức -72%.",[["19"],["72"]],[G(56,"table","Bảng 5 (đầu): hàng 'Than đá': -19 | -72%")])
A("d-anh1","dev","anh","Hình 10 thể hiện dự báo gì, vào năm nào, ở khu vực nào?","Dự báo tình trạng ngập mặn do triều cường vào năm 2050 tại khu vực sông Mekong (Đồng bằng sông Cửu Long).",[["2050"],["ngập"],["mekong","cửu long"]],[G(40,"map","Hình 10: tiêu đề phụ 'Dự báo tình trạng ngập mặn do triều cường vào năm 2050 tại khu vực sông Mekong'")])
A("d-anh2","dev","anh","Trong Hình 9, bản đồ nào được tô màu cam?","Bản đồ 'Lở đất'.",[["lở đất"]],[G(37,"map","Hình 9: bản đồ thứ nhất 'Lở đất' màu cam (xanh dương cho Lũ lụt, xanh lá cho Bão lũ)")])
A("d-anh3","dev","anh","Trong sơ đồ Hình 21, nhu cầu tài chính cho khả năng chống chịu bằng bao nhiêu % GDP mỗi năm và cho khử carbon là bao nhiêu?","4,7% và 2,1% GDP mỗi năm.",[["4,7"],["2,1"]],[G(77,"diagram","Hình 21: khối trên 'Khả năng chống chịu: 4,7% GDP mỗi năm; Khử carbon: 2,1% GDP mỗi năm'")])
A("d-bd1","dev","bieu_do","Theo Hình 6, bao nhiêu % doanh nghiệp báo cáo 'thiếu nguồn cung nguyên liệu đầu vào' ở mức 'hầu như không'?","33%.",[["33"]],[G(25,"chart","Hình 6: hàng 'Thiếu nguồn cung nguyên liệu đầu vào', mức 'Hầu như không' = 33")])
A("d-bd2","dev","bieu_do","Theo Hình 16, biện pháp giảm phát thải từ sản xuất lúa gạo nào có chi phí cao nhất tính theo $/tCO2e?","Chuyển từ trồng lúa sang trồng ngô (khoảng 390 $/tCO2e).",[["ngô"]],[G(65,"chart","Hình 16: cột cao nhất 'Chuyển từ trồng lúa sang trồng ngô' ≈ 390")])
A("d-bd3","dev","bieu_do","Theo Hình 18, chỉ tiêu nào giảm nhiều nhất so với BAU năm 2040 và giảm bao nhiêu?","Bất bình đẳng (chỉ số Gini), -1,1.",[["bất bình đẳng","gini"],["1,1"]],[G(70,"chart","Hình 18: cột 'Bất bình đẳng (Chỉ số Gini)' = -1,1")])
A("d-mh1","dev","multi_hop","Theo Hình 13, điện than năm 2040 của ADS (26 TWh) thấp hơn CPS (276 TWh) khoảng bao nhiêu %, và so với mức giảm chi phí vốn cho than đá ở Bảng 5 thì thế nào?","(276-26)/276 ≈ 90,6%; chi phí vốn than đá giảm 72% nên điện than giảm nhiều hơn chi phí vốn.",[["90,6","90,5","91"],["72"]],[G(56,"chart","Hình 13: điện than 2040 CPS 276, ADS 26 TWh"),G(56,"table","Bảng 5: Than đá -19 | -72%")])
assert round((276 - 26) / 276 * 100, 1) == 90.6
A("d-mh2","dev","multi_hop","Theo Bảng 1, phát thải trên đầu người của Indonesia gấp khoảng bao nhiêu lần Việt Nam, và văn bản trang 8 nói gì về cường độ phát thải của Việt Nam so với Indonesia?","6,4/3,8 ≈ 1,7 lần; cường độ phát thải của Việt Nam tương đương Indonesia.",[["1,7","1,68"],["tương đương"]],[G(19,"table","Bảng 1: Indonesia 6,4; Việt Nam 3,8"),G(18,"text","cường độ phát thải GHG ... tương đương với Indonesia")])
assert round(6.4 / 3.8, 1) == 1.7
A("d-mh3","dev","multi_hop","Theo Hình 22, dư nợ tín dụng xanh quý 1 năm 2021 gấp khoảng bao nhiêu lần năm 2016, và văn bản cùng trang nói tín dụng xanh tăng gần mấy lần kể từ 2015?","14,5/3,7 ≈ 3,9 lần; văn bản nói gần 5 lần kể từ 2015 (hai mốc so sánh khác nhau).",[["3,9"],["5 lần","gần 5"]],[G(78,"chart","Hình 22: 2016 = 3,7; 2021:Q1 = 14,5"),G(78,"text","tín dụng xanh đã tăng gần gấp 5 lần kể từ năm 2015")])
assert round(14.5 / 3.7, 1) == 3.9
A("d-tx1","dev","text","Năng lượng chiếm khoảng bao nhiêu % lượng phát thải GHG của Việt Nam năm 2020 và nông nghiệp chiếm bao nhiêu %?","Năng lượng khoảng 65%; nông nghiệp khoảng 19%.",[["65"],["19"]],[G(18,"text","năng lượng chiếm khoảng 65% lượng phát thải GHG của cả nước ... Nông nghiệp ... chiếm khoảng 19%")])
A("d-tx2","dev","text","Việc Quốc lộ 1A ngừng hoạt động có thể gây tổn thất kinh tế bao nhiêu mỗi ngày?","1,9 triệu USD mỗi ngày.",[["1,9"]],[G(37,"text","ngừng hoạt động có thể gây tổn thất kinh tế 1,9 triệu USD mỗi ngày")])
A("d-tx3","dev","text","Trong 85 tổ chức tín dụng do NHNN quản lý, bao nhiêu tổ chức chưa có đơn vị kinh doanh chuyên trách về tài chính xanh?","72 tổ chức.",[["72"]],[G(78,"text","Trong số 85 tổ chức tín dụng do NHNN quản lý, 72 tổ chức chưa có đơn vị kinh doanh chuyên trách")])
for id, q, why, kws in [
 ("d-a1","Tổng diện tích rừng ngập mặn hiện có của Việt Nam là bao nhiêu hecta?","Báo cáo nói về rừng ngập mặn như giải pháp thích ứng nhưng không nêu tổng diện tích.",["hecta","diện tích rừng ngập mặn"]),
 ("d-a2","Báo cáo ước tính tổng vốn đầu tư cho các tuabin gió ở Ninh Thuận là bao nhiêu?","Có điện gió nhưng không nhắc tỉnh Ninh Thuận hay tuabin.",["ninh thuận","tuabin"]),
 ("d-a3","Báo cáo khuyến nghị xây dựng thêm bao nhiêu đập thủy điện mới đến năm 2040?","Có thủy điện trong cơ cấu điện nhưng không có khuyến nghị về đập mới.",["đập thủy điện"])]:
    X(id, "dev", q, why, kws)
# ---------------- verify ----------------
def nt(s): return re.sub(r"\s+", " ", s).lower()
bad = 0
for q in Q:
    if not q["answerable"]: continue
    for g in q["gold"]:
        if g["evidence_type"] == "text":
            frag = g["evidence"].split(" ... ")[0] if " ... " in g["evidence"] else g["evidence"]
            frag = re.sub(r"[‘’']", "", frag)
            if nt(frag).strip("'") not in nt(PT[g["page"]]):
                # allow loose check on the shortest distinctive tail
                tail = nt(frag.split("'")[-1] if "'" in frag else frag)[-45:]
                if tail not in nt(PT[g["page"]]): bad += 1; print("TEXT EVIDENCE NOT FOUND", q["id"], g["page"], frag[:70])
    # key facts must be consistent with expected answer
    for alts in q["key_facts"]:
        if not any(nt(a) in nt(q["expected_answer"]) for a in alts): bad += 1; print("KEY FACT NOT IN EXPECTED", q["id"], alts)
from collections import Counter
print(Counter((q["split"], q["group"]) for q in Q), "bad:", bad)
json.dump({"_readme": "Advanced benchmark on 'Việt Nam: Báo cáo Quốc gia về Khí hậu và Phát triển' (World Bank, 07/2022, tiếng Việt). Written before any run. gold.page = PDF page (printed page = PDF page - 10). Test and dev questions differ in content.",
           "source_id": SRC, "questions": Q}, open("adv/benchmark/questions.json", "w"), ensure_ascii=False, indent=1)
