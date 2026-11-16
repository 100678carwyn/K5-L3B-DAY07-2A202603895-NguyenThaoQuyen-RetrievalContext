# Phiếu chấm test (đối chiếu với bản gốc PDF, không chỉ dựa vào ghi chú chuyển ghi)

## t-bang1 · bang
**Câu hỏi:** Theo Bảng 1, phát thải GHG trên đầu người của Việt Nam là bao nhiêu tCO2e và thấp hơn Thái Lan bao nhiêu tCO2e trên đầu người?

**Đáp án chuẩn:** Việt Nam 3,8; Thái Lan 6,2; thấp hơn 2,4 tCO2e/người.  
**Evidence (trang PDF):** tr.19 [table] Bảng 1: hàng Việt Nam 3,8; hàng Thái Lan 6,2 (cột phát thải trên đầu người)

**Trạng thái:** answered · lượt tìm: 2 · 4.29s · auto_pass (proxy): True

**Công cụ:** search_documents({'query': 'Bảng 1 phát thải GHG trên đầu người Việt Nam Thái Lan', 'kind': 'table'}) → ['p19:fg5', 'p19:tb4', 'p91:tb29a', 'p15:fg1', 'p19:t0', 'p18:t1', 'p23:t0', 'p11:t0']; search_documents({'query': 'phát thải trên đầu người tCO2e Việt Nam so với Thái Lan', 'kind': 'any'}) → ['p19:t0', 'p19:tb4', 'p18:t1', 'p19:fg5', 'p91:tb29a', 'p49:t3', 'p98:t2', 'p11:t0']

**Câu trả lời:** Theo Bảng 1, phát thải GHG trên đầu người của Việt Nam là 3,8 tCO2e/người, còn Thái Lan là 6,2 tCO2e/người [ccdr-vn-2022:p19:tb4]. Như vậy Việt Nam thấp hơn Thái Lan 2,4 tCO2e/người (tính: 6,2 − 3,8 = 2,4) [ccdr-vn-2022:p19:tb4].

**Citation:** ['ccdr-vn-2022:p19:tb4'] (không hợp lệ: [])

**Nhãn (điền vào labels_test.json):** pass = ?, lý do = ?

## t-bang2 · bang
**Câu hỏi:** Theo Bảng 2, tổng nhu cầu tài chính tích lũy (NPV) cho các biện pháp thích ứng giai đoạn 2022–2050 nằm trong khoảng nào, tính bằng tỷ USD?

**Đáp án chuẩn:** 479,2–547,6 tỷ USD.  
**Evidence (trang PDF):** tr.32 [table] Bảng 2: hàng 'Tổng nhu cầu tài chính', cột giá trị tích lũy: 479,2–547,6

**Trạng thái:** answered · lượt tìm: 2 · 2.68s · auto_pass (proxy): True

**Công cụ:** search_documents({'query': 'Bảng 2 tổng nhu cầu tài chính tích lũy NPV biện pháp thích ứng 2022-2050', 'kind': 'table'}) → ['p32:tb9', 'p50:tb13', 'p77:fg26', 'p56:tb17', 'p32:t0', 'p31:t2', 'p32:t1', 'p50:t0']; search_documents({'query': 'nhu cầu tài chính thích ứng tích lũy tỷ USD 2022-2050', 'kind': 'any'}) → ['p32:t0', 'p32:tb9', 'p31:t2', 'p77:t3', 'p77:t0', 'p50:t0', 'p31:t0', 'p77:fg26']

**Câu trả lời:** Theo Bảng 2, tổng nhu cầu tài chính tích lũy (NPV, chiết khấu 6%) cho các biện pháp thích ứng giai đoạn 2022–2050 là 479,2–547,6 tỷ USD [ccdr-vn-2022:p32:tb9], trong đó nhu cầu tài chính tăng thêm là 342,3–410,7 tỷ USD và nguồn tài chính hiện có là 136,9 tỷ USD [ccdr-vn-2022:p32:tb9].

**Citation:** ['ccdr-vn-2022:p32:tb9'] (không hợp lệ: [])

**Nhãn (điền vào labels_test.json):** pass = ?, lý do = ?

## t-bang3 · bang
**Câu hỏi:** Theo Bảng 3, tác động kinh tế ròng giai đoạn 2022–2040 của NZP kèm những cải cách hỗ trợ là bao nhiêu tỷ USD?

**Đáp án chuẩn:** -1,3 tỷ USD (gần như không đáng kể).  
**Evidence (trang PDF):** tr.50 [table] Bảng 3: khối 'NZP với những cải cách hỗ trợ', hàng 'Tác động kinh tế ròng', cột 2022–2040: -1,3

**Trạng thái:** answered · lượt tìm: 2 · 2.96s · auto_pass (proxy): True

**Công cụ:** search_documents({'query': 'Bảng 3 tác động kinh tế ròng 2022-2040 NZP cải cách hỗ trợ', 'kind': 'table'}) → ['p50:tb13', 'p53:tb14', 'p72:fg25', 'p57:tb18', 'p50:t0', 'p50:t1', 'p52:t3', 'p53:t1']; search_documents({'query': 'tác động kinh tế ròng NZP kèm cải cách tỷ USD 2040', 'kind': 'any'}) → ['p50:tb13', 'p50:t0', 'p53:tb14', 'p53:t1', 'p72:fg25', 'p50:t1', 'p77:t0', 'p70:fg23']

**Câu trả lời:** Theo Bảng 3, tác động kinh tế ròng của NZP kèm các cải cách hỗ trợ trong giai đoạn 2022–2040 là **-1,3 tỷ USD** (tức thiệt hại nhỏ khoảng 1,3 tỷ USD, gần như không ảnh hưởng GDP) [ccdr-vn-2022:p50:tb13][ccdr-vn-2022:p50:t1]. Con số này gồm -20,5 tỷ USD (2022–2030) và +19,3 tỷ USD (2031–2040), với mức sản lượng tăng 80,1 tỷ USD trừ nhu cầu đầu tư 81,3 tỷ USD [ccdr-vn-2022:p50:tb13].

**Citation:** ['ccdr-vn-2022:p50:tb13', 'ccdr-vn-2022:p50:t1'] (không hợp lệ: [])

**Nhãn (điền vào labels_test.json):** pass = ?, lý do = ?

## t-bang4 · bang
**Câu hỏi:** Theo Bảng 4, khi áp dụng NZP cùng tất cả các biện pháp hỗ trợ, GDP năm 2040 thay đổi bao nhiêu % và phát thải khí nhà kính năm 2040 thay đổi bao nhiêu %?

**Đáp án chuẩn:** GDP +3,3%; phát thải khí nhà kính -71,9%.  
**Evidence (trang PDF):** tr.53 [table] Bảng 4: hàng 'NZP và tất cả các biện pháp hỗ trợ': phát thải 2040 -71,9; GDP 2040 3,3

**Trạng thái:** answered · lượt tìm: 2 · 3.79s · auto_pass (proxy): True

**Công cụ:** search_documents({'query': 'Bảng 4 NZP cùng tất cả các biện pháp hỗ trợ GDP 2040 phát thải', 'kind': 'table'}) → ['p53:tb14', 'p50:tb13', 'p32:tb9', 'p72:fg25', 'p52:t3', 'p53:t1', 'p53:t0', 'p74:t2']; search_documents({'query': 'NZP GDP 2040 thay đổi phần trăm phát thải khí nhà kính 2040', 'kind': 'table'}) → ['p53:tb14', 'p91:tb29a', 'p50:tb13', 'p72:fg25', 'p53:t0', 'p53:t1', 'p49:t3', 'p52:t3']

**Câu trả lời:** Theo Bảng 4, khi áp dụng NZP cùng tất cả các biện pháp hỗ trợ, GDP năm 2040 tăng 3,3% và phát thải khí nhà kính năm 2040 giảm 71,9% so với kịch bản cơ sở [ccdr-vn-2022:p53:tb14]. Văn bản cũng xác nhận GDP tăng 3,3% vào năm 2040 và phát thải giảm hơn 70% vào năm 2040 [ccdr-vn-2022:p52:t3].

**Citation:** ['ccdr-vn-2022:p53:tb14', 'ccdr-vn-2022:p52:t3'] (không hợp lệ: [])

**Nhãn (điền vào labels_test.json):** pass = ?, lý do = ?

## t-bang5 · bang
**Câu hỏi:** Theo Bảng 5, so với CPS, chi phí vốn cho điện gió ngoài khơi trong kịch bản ADS thay đổi bao nhiêu tỷ USD và bao nhiêu phần trăm?

**Đáp án chuẩn:** +39 tỷ USD, tức +402%.  
**Evidence (trang PDF):** tr.57 [table] Bảng 5 (tiếp): hàng 'Gió (ngoài khơi)': +39 | +402%

**Trạng thái:** answered · lượt tìm: 2 · 2.59s · auto_pass (proxy): True

**Công cụ:** search_documents({'query': 'Bảng 5 chi phí vốn điện gió ngoài khơi CPS ADS', 'kind': 'table'}) → ['p56:tb17', 'p57:tb18', 'p56:fg16', 'p65:fg21', 'p56:t1', 'p56:t3', 'p56:t2', 'p57:t1']; search_documents({'query': 'chi phí vốn điện gió ngoài khơi kịch bản ADS so với CPS tỷ USD', 'kind': 'any'}) → ['p56:t1', 'p56:tb17', 'p56:fg16', 'p56:t3', 'p56:t2', 'p57:tb18', 'p54:t2', 'p58:t1']

**Câu trả lời:** Theo Bảng 5, chi phí vốn cho điện gió ngoài khơi trong kịch bản ADS tăng **+39 tỷ USD**, tương đương **+402%** so với CPS [ccdr-vn-2022:p57:tb18].

**Citation:** ['ccdr-vn-2022:p57:tb18'] (không hợp lệ: [])

**Nhãn (điền vào labels_test.json):** pass = ?, lý do = ?

## t-bang6 · bang
**Câu hỏi:** Theo Phụ lục 1, lượng phát thải từ điện/nhiệt năm 2018 gấp khoảng bao nhiêu lần năm 1990?

**Đáp án chuẩn:** 109,13 / 4,88 ≈ 22,4 lần.  
**Evidence (trang PDF):** tr.91 [table] Phụ lục 1: hàng 'Điện/nhiệt': 4,88 (1990) và 109,13 (2018) triệu tấn CO2e

**Trạng thái:** answered · lượt tìm: 2 · 4.26s · auto_pass (proxy): True

**Công cụ:** search_documents({'query': 'Phụ lục 1 phát thải điện nhiệt 1990 2018', 'kind': 'table'}) → ['p91:tb29a', 'p91:tb29b', 'p18:fg3', 'p56:fg16', 'p91:t0', 'p91:t1', 'p92:t0', 'p17:t2']; search_documents({'query': 'phát thải khí nhà kính từ điện và nhiệt năm 2018 so với 1990', 'kind': 'any'}) → ['p91:t1', 'p49:t3', 'p18:fg3', 'p18:t1', 'p53:t3', 'p61:t3', 'p91:tb29a', 'p17:t2']

**Câu trả lời:** Theo Phụ lục 1, phát thải từ điện/nhiệt là 4,88 triệu tấn CO2e năm 1990 và 109,13 triệu tấn CO2e năm 2018 [ccdr-vn-2022:p91:tb29b]. Tính: 109,13 / 4,88 ≈ 22,4 lần. Vậy năm 2018 gấp khoảng 22 lần năm 1990.

**Citation:** ['ccdr-vn-2022:p91:tb29b'] (không hợp lệ: [])

**Nhãn (điền vào labels_test.json):** pass = ?, lý do = ?

## t-anh1 · anh
**Câu hỏi:** Theo sơ đồ Hình 1 (mô hình phát triển mới), hai lộ trình nối 'Việt Nam hiện nay' với 'Việt Nam năm 2045' là gì?

**Đáp án chuẩn:** Lộ trình xây dựng khả năng chống chịu và Hành trình khử carbon.  
**Evidence (trang PDF):** tr.13 [diagram] Hình 1: hai mũi tên cong 'Lộ trình xây dựng khả năng chống chịu' và 'Hành trình khử carbon'

**Trạng thái:** answered · lượt tìm: 2 · 2.87s · auto_pass (proxy): True

**Công cụ:** search_documents({'query': 'Hình 1 mô hình phát triển mới Việt Nam hiện nay Việt Nam năm 2045 lộ trình', 'kind': 'figure'}) → ['p13:fg0', 'p15:fg1', 'p70:fg23', 'p62:fg20', 'p15:t0', 'p13:t0', 'p12:t2', 'p13:t2']; search_documents({'query': 'sơ đồ mô hình phát triển mới hai lộ trình 2045', 'kind': 'any'}) → ['p13:fg0', 'p12:t2', 'p13:t0', 'p15:t0', 'p49:t1', 'p100:t0', 'p49:t0', 'p77:t0']

**Câu trả lời:** Hai lộ trình đó là: (1) **Lộ trình xây dựng khả năng chống chịu** (thích ứng với biến đổi khí hậu) và (2) **Hành trình khử carbon** (giảm thiểu biến đổi khí hậu) [ccdr-vn-2022:p13:fg0][ccdr-vn-2022:p12:t2]. Sơ đồ Hình 1 nối "Việt Nam hiện nay" với "Việt Nam năm 2045" bằng hai mũi tên cong tương ứng hai lộ trình này, với năm hành động ở giữa: xây dựng cơ sở hạ tầng có khả năng chống chịu; bảo vệ những đối tượng bị tổn thương nhất; cải cách cơ cấu để khuyến khích nông dân và doanh nghiệp; định giá carbon; huy động nguồn vốn [ccdr-vn-2022:p13:fg0][ccdr-vn-2022:p13:t2].

**Citation:** ['ccdr-vn-2022:p13:fg0', 'ccdr-vn-2022:p12:t2', 'ccdr-vn-2022:p13:t2'] (không hợp lệ: [])

**Nhãn (điền vào labels_test.json):** pass = ?, lý do = ?

## t-anh2 · anh
**Câu hỏi:** Theo sơ đồ Hình 21, nguồn nào đóng góp nhiều nhất cho nhu cầu tài chính giai đoạn 2022–2040 và là bao nhiêu tỷ USD?

**Đáp án chuẩn:** Khu vực tư nhân, 184 tỷ USD.  
**Evidence (trang PDF):** tr.77 [diagram] Hình 21: ba ô con: Khu vực tư nhân 184, Khu vực công 130, Bên ngoài 54 tỷ USD

**Trạng thái:** answered · lượt tìm: 2 · 2.77s · auto_pass (proxy): True

**Công cụ:** search_documents({'query': 'Hình 21 nhu cầu tài chính 2022-2040 nguồn đóng góp', 'kind': 'figure'}) → ['p77:fg26', 'p71:fg24', 'p25:fg6', 'p30:fg8', 'p77:t3', 'p32:tb9', 'p77:t0', 'p32:t1']; search_documents({'query': 'nhu cầu đầu tư tài chính 2022-2040 tỷ USD nguồn vốn', 'kind': 'any'}) → ['p77:t3', 'p50:tb13', 'p32:tb9', 'p50:t0', 'p77:t0', 'p77:fg26', 'p32:t1', 'p31:t2']

**Câu trả lời:** Theo Hình 21, nguồn đóng góp lớn nhất là **khu vực tư nhân với 184 tỷ USD** (khoảng 3,4% GDP mỗi năm), trong tổng nhu cầu tài chính 368 tỷ USD giai đoạn 2022–2040; tiếp theo là khu vực công 130 tỷ USD và bên ngoài 54 tỷ USD [ccdr-vn-2022:p77:fg26][ccdr-vn-2022:p77:t3].

**Citation:** ['ccdr-vn-2022:p77:fg26', 'ccdr-vn-2022:p77:t3'] (không hợp lệ: [])

**Nhãn (điền vào labels_test.json):** pass = ?, lý do = ?

## t-anh3 · anh
**Câu hỏi:** Trên bản đồ Hình 14, tỉnh nào được chú thích là tỉnh sản xuất than chính?

**Đáp án chuẩn:** Quảng Ninh.  
**Evidence (trang PDF):** tr.59 [map] Hình 14: khung chú thích 'Quảng Ninh — Tỉnh sản xuất than chính'

**Trạng thái:** answered · lượt tìm: 2 · 2.27s · auto_pass (proxy): True

**Công cụ:** search_documents({'query': 'Hình 14 bản đồ tỉnh sản xuất than chính', 'kind': 'figure'}) → ['p59:fg19', 'p54:fg15', 'p42:fg12', 'p26:fg7', 'p59:t0', 'p58:t2', 'p54:t1', 'p58:t0']; search_documents({'query': 'tỉnh sản xuất than chính Quảng Ninh', 'kind': 'any'}) → ['p59:fg19', 'p59:t0', 'p58:t2', 'p85:t3', 'p54:fg15', 'p58:t0', 'p54:t0', 'p54:t1']

**Câu trả lời:** Trên Hình 14, tỉnh được chú thích là "Tỉnh sản xuất than chính" là Quảng Ninh [ccdr-vn-2022:p59:fg19]. Bản đồ cũng đánh dấu các điểm Hòn Gai và Cẩm Phả (vòng tròn đỏ) trong tỉnh này [ccdr-vn-2022:p59:fg19], phù hợp với nội dung văn bản rằng than nội địa chủ yếu khai thác ở miền Bắc, "đặc biệt ở tỉnh Quảng Ninh" [ccdr-vn-2022:p58:t2].

**Citation:** ['ccdr-vn-2022:p59:fg19', 'ccdr-vn-2022:p58:t2'] (không hợp lệ: [])

**Nhãn (điền vào labels_test.json):** pass = ?, lý do = ?

## t-anh4 · anh
**Câu hỏi:** Trên bản đồ rủi ro ngập lụt ở Hình 11, những thành phố nào được đánh dấu?

**Đáp án chuẩn:** Hà Nội, Hải Phòng, Đà Nẵng, TP. Hồ Chí Minh và Cần Thơ.  
**Evidence (trang PDF):** tr.42 [map] Hình 11: năm điểm xanh dương gắn nhãn Hanoi, Haiphong, Da Nang, Ho Chi Minh City, Can Tho

**Trạng thái:** answered · lượt tìm: 2 · 2.54s · auto_pass (proxy): True

**Công cụ:** search_documents({'query': 'Hình 11 bản đồ rủi ro ngập lụt thành phố', 'kind': 'figure'}) → ['p42:fg12', 'p37:fg10', 'p40:fg11', 'p25:fg6', 'p37:t1', 'p42:t0', 'p41:t3', 'p39:t0']; search_documents({'query': 'rủi ro ngập lụt đô thị bản đồ thành phố được đánh dấu', 'kind': 'any'}) → ['p42:fg12', 'p42:t3', 'p37:t1', 'p39:t0', 'p41:t2', 'p46:t1', 'p42:t0', 'p41:t3']

**Câu trả lời:** Hình 11 (Rủi ro ngập lụt tại các vùng ven biển) đánh dấu 5 thành phố: Hà Nội, Hải Phòng, Đà Nẵng, TP. Hồ Chí Minh và Cần Thơ [ccdr-vn-2022:p42:fg12].

**Citation:** ['ccdr-vn-2022:p42:fg12'] (không hợp lệ: [])

**Nhãn (điền vào labels_test.json):** pass = ?, lý do = ?

## t-anh5 · anh
**Câu hỏi:** Hình 9 gồm ba bản đồ về mức độ dễ bị ảnh hưởng của các tuyến đường quốc gia. Ba bản đồ đó thể hiện những loại thiên tai nào?

**Đáp án chuẩn:** Lở đất, Lũ lụt 1.000 năm và Bão lũ.  
**Evidence (trang PDF):** tr.37 [map] Hình 9: tiêu đề ba bản đồ 'Lở đất', 'Lũ lụt 1.000 năm', 'Bão lũ'

**Trạng thái:** answered · lượt tìm: 2 · 2.39s · auto_pass (proxy): True

**Công cụ:** search_documents({'query': 'Hình 9 mức độ dễ bị ảnh hưởng của các tuyến đường quốc gia', 'kind': 'figure'}) → ['p37:fg10', 'p25:fg6', 'p30:fg8', 'p26:fg7', 'p37:t1', 'p37:t0', 'p39:t1', 'p36:t2']; search_documents({'query': 'bản đồ đường quốc gia ngập lụt sạt lở nước biển dâng', 'kind': 'figure'}) → ['p37:fg10', 'p30:fg8', 'p42:fg12', 'p40:fg11', 'p37:t1', 'p42:t3', 'p11:t0', 'p30:t2']

**Câu trả lời:** Ba bản đồ trong Hình 9 thể hiện ba loại thiên tai: **lở đất**, **lũ lụt 1.000 năm** và **bão lũ** [ccdr-vn-2022:p37:fg10].

**Citation:** ['ccdr-vn-2022:p37:fg10'] (không hợp lệ: [])

**Nhãn (điền vào labels_test.json):** pass = ?, lý do = ?

## t-bd1 · bieu_do
**Câu hỏi:** Theo Hình 3, khoản chi phí do biến đổi khí hậu năm 2020 lớn nhất là gì và là bao nhiêu triệu USD?

**Đáp án chuẩn:** Thủy sản, 4.219 triệu USD.  
**Evidence (trang PDF):** tr.17 [chart] Hình 3 (treemap): ô lớn nhất 'Thủy sản, 4219'

**Trạng thái:** answered · lượt tìm: 2 · 1.61s · auto_pass (proxy): True

**Công cụ:** search_documents({'query': 'Hình 3 chi phí biến đổi khí hậu năm 2020', 'kind': 'figure'}) → ['p17:fg2', 'p25:fg6', 'p78:fg27', 'p65:fg21', 'p17:t1', 'p17:t0', 'p93:t1', 'p16:t3']; search_documents({'query': 'chi phí do biến đổi khí hậu 2020 triệu USD', 'kind': 'any'}) → ['p17:fg2', 'p17:t1', 'p16:t3', 'p17:t0', 'p56:t1', 'p38:t0', 'p31:t0', 'p24:t3']

**Câu trả lời:** Theo Hình 3, khoản chi phí lớn nhất là **Thủy sản**, với **4.219 triệu USD** [ccdr-vn-2022:p17:fg2].

**Citation:** ['ccdr-vn-2022:p17:fg2'] (không hợp lệ: [])

**Nhãn (điền vào labels_test.json):** pass = ?, lý do = ?

## t-bd2 · bieu_do
**Câu hỏi:** Theo Hình 12, than đá chiếm bao nhiêu % điện năng sản xuất từ nhiên liệu hóa thạch năm 2020 và bao nhiêu % công suất lắp đặt?

**Đáp án chuẩn:** 59% điện năng sản xuất và 30% công suất lắp đặt.  
**Evidence (trang PDF):** tr.54 [chart] Hình 12: hai biểu đồ vành khuyên, phần Than đá 59% (200 TWh) và 30% (68 GW)

**Trạng thái:** answered · lượt tìm: 2 · 3.24s · auto_pass (proxy): True

**Công cụ:** search_documents({'query': 'Hình 12 than đá điện năng sản xuất từ nhiên liệu hóa thạch công suất lắp đặt 2020', 'kind': 'figure'}) → ['p54:fg15', 'p25:fg6', 'p56:fg16', 'p18:fg3', 'p54:t0', 'p54:t1', 'p53:t3', 'p92:t0']; search_documents({'query': 'than đá chiếm % sản lượng điện công suất lắp đặt năm 2020', 'kind': 'any'}) → ['p53:t3', 'p54:fg15', 'p54:t0', 'p54:t1', 'p53:t2', 'p55:t0', 'p92:t0', 'p59:t1']

**Câu trả lời:** Theo Hình 12 (năm 2020), than đá chiếm 59% điện năng sản xuất từ nhiên liệu hóa thạch (tổng 200 TWh) và 30% công suất lắp đặt (tổng 68 GW) [ccdr-vn-2022:p54:fg15]; số liệu này cũng được nêu trong phần văn bản: khoảng 30% công suất lắp đặt và 59% sản lượng điện [ccdr-vn-2022:p53:t3].

**Citation:** ['ccdr-vn-2022:p54:fg15', 'ccdr-vn-2022:p53:t3'] (không hợp lệ: [])

**Nhãn (điền vào labels_test.json):** pass = ?, lý do = ?

## t-bd3 · bieu_do
**Câu hỏi:** Theo Hình 20, lĩnh vực nào có % chuyển việc làm cao nhất trong kịch bản NZP đã cải cách vào năm 2040 và giá trị là bao nhiêu?

**Đáp án chuẩn:** Điện, 23,6%.  
**Evidence (trang PDF):** tr.72 [chart] Hình 20: cột cam 'NZP đã cải cách' cao nhất ở Điện: 23,6

**Trạng thái:** answered · lượt tìm: 2 · 2.85s · auto_pass (proxy): True

**Công cụ:** search_documents({'query': 'Hình 20 chuyển việc làm kịch bản NZP đã cải cách năm 2040', 'kind': 'figure'}) → ['p72:fg25', 'p70:fg23', 'p56:fg16', 'p62:fg20', 'p96:t0', 'p71:t3', 'p74:t2', 'p51:t0']; search_documents({'query': 'chuyển dịch việc làm theo lĩnh vực NZP cải cách 2040', 'kind': 'any'}) → ['p72:fg25', 'p71:t3', 'p52:t3', 'p72:t1', 'p53:tb14', 'p72:t3', 'p96:t0', 'p53:t1']

**Câu trả lời:** Theo Hình 20, trong kịch bản NZP đã cải cách năm 2040, lĩnh vực Điện có % chuyển việc làm cao nhất, đạt 23,6% (độ lệch so với BAU) [ccdr-vn-2022:p72:fg25].

**Citation:** ['ccdr-vn-2022:p72:fg25'] (không hợp lệ: [])

**Nhãn (điền vào labels_test.json):** pass = ?, lý do = ?

## t-bd4 · bieu_do
**Câu hỏi:** Theo Hình 22, dư nợ tín dụng xanh năm 2018 là bao nhiêu tỷ USD?

**Đáp án chuẩn:** 10,3 tỷ USD.  
**Evidence (trang PDF):** tr.78 [chart] Hình 22 (trái): cột năm 2018 có nhãn 10,3

**Trạng thái:** answered · lượt tìm: 2 · 3.0s · auto_pass (proxy): True

**Công cụ:** search_documents({'query': 'Hình 22 dư nợ tín dụng xanh', 'kind': 'figure'}) → ['p78:fg27', 'p62:fg20', 'p30:fg8', 'p13:fg0', 'p78:t2', 'p78:t1', 'p79:t4', 'p80:t4']; search_documents({'query': 'tín dụng xanh dư nợ 2018 tỷ USD', 'kind': 'any'}) → ['p78:fg27', 'p78:t2', 'p79:t4', 'p78:t1', 'p77:t2', 'p50:t0', 'p80:t2', 'p24:t3']

**Câu trả lời:** Theo Hình 22, dư nợ tín dụng xanh năm 2018 là 10,3 tỷ USD [ccdr-vn-2022:p78:fg27].

**Citation:** ['ccdr-vn-2022:p78:fg27'] (không hợp lệ: [])

**Nhãn (điền vào labels_test.json):** pass = ?, lý do = ?

## t-bd5 · bieu_do
**Câu hỏi:** Theo Hình 7, năm 2018 ngành nào có tỷ trọng sản lượng của DNNN thấp nhất và là bao nhiêu phần trăm?

**Đáp án chuẩn:** Kim loại, 14%.  
**Evidence (trang PDF):** tr.26 [chart] Hình 7: nhãn cuối đường 'Kim loại, 14%' (thấp nhất)

**Trạng thái:** answered · lượt tìm: 2 · 2.28s · auto_pass (proxy): True

**Công cụ:** search_documents({'query': 'Hình 7 tỷ trọng sản lượng của DNNN theo ngành', 'kind': 'figure'}) → ['p26:fg7', 'p18:fg3', 'p54:fg15', 'p25:fg6', 'p25:t2', 'p26:t2', 'p50:t0', 'p61:t4']; search_documents({'query': 'doanh nghiệp nhà nước tỷ trọng sản lượng ngành 2018', 'kind': 'any'}) → ['p26:fg7', 'p25:t1', 'p61:t3', 'p25:fg6', 'p71:t0', 'p91:tb29a', 'p50:t0', 'p25:t2']

**Câu trả lời:** Theo Hình 7, năm 2018 ngành có tỷ trọng sản lượng của DNNN thấp nhất là **Kim loại**, với **14%** [ccdr-vn-2022:p26:fg7].

**Citation:** ['ccdr-vn-2022:p26:fg7'] (không hợp lệ: [])

**Nhãn (điền vào labels_test.json):** pass = ?, lý do = ?

## t-mh1 · multi_hop
**Câu hỏi:** Văn bản nêu công suất nhiệt điện than năm 2020 là 20 GW, còn Hình 12 cho tổng công suất lắp đặt là 68 GW. Tỷ trọng than tính từ hai số này là bao nhiêu % và có khớp với phần than đá trên Hình 12 không?

**Đáp án chuẩn:** 20/68 ≈ 29,4% ≈ 30%, khớp với phần Than đá 30% trên Hình 12.  
**Evidence (trang PDF):** tr.53 [text] 'công suất lắp đặt của các nhà máy nhiệt điện than ... từ 5 GW năm 2010 lên 20 GW'; tr.54 [chart] Hình 12: tổng 68 GW; Than đá 30%

**Trạng thái:** answered · lượt tìm: 2 · 3.1s · auto_pass (proxy): True

**Công cụ:** search_documents({'query': 'nhiệt điện than công suất 2020 GW', 'kind': 'any'}) → ['p53:t3', 'p54:t1', 'p54:fg15', 'p54:t0', 'p55:t0', 'p56:fg16', 'p23:t0', 'p92:t0']; search_documents({'query': 'Hình 12 tổng công suất lắp đặt 68 GW cơ cấu nguồn điện', 'kind': 'figure'}) → ['p54:fg15', 'p56:fg16', 'p13:fg0', 'p18:fg3', 'p53:t2', 'p54:t1', 'p54:t0', 'p57:t1']

**Câu trả lời:** 20/68 ≈ 29,4% (tức khoảng 30%), khớp với phần "Than đá 30%" trong biểu đồ công suất lắp đặt 68 GW của Hình 12 [ccdr-vn-2022:p53:t3][ccdr-vn-2022:p54:fg15]; văn bản cũng nêu nhiệt điện than chiếm khoảng 30% công suất lắp đặt năm 2020 [ccdr-vn-2022:p53:t3].

**Citation:** ['ccdr-vn-2022:p53:t3', 'ccdr-vn-2022:p54:fg15'] (không hợp lệ: [])

**Nhãn (điền vào labels_test.json):** pass = ?, lý do = ?

## t-mh2 · multi_hop
**Câu hỏi:** Theo Bảng 5, cộng chi phí tăng thêm của điện mặt trời, gió trên bờ và gió ngoài khơi là bao nhiêu tỷ USD, và so với dòng 'Chi phí vốn để lưu trữ và phát điện mới' (+44 tỷ USD) ở phần đầu bảng thì thế nào, vì sao?

**Đáp án chuẩn:** 21+8+39 = 68 tỷ USD, lớn hơn +44 vì chi phí vốn cho than đá (-19) và khí đốt (-8) giảm.  
**Evidence (trang PDF):** tr.57 [table] Bảng 5 (tiếp): Mặt trời +21; Gió trên bờ +8; Gió ngoài khơi +39; tr.56 [table] Bảng 5 (đầu): Chi phí vốn +44; Than đá -19; Khí đốt -8

**Trạng thái:** answered · lượt tìm: 2 · 3.73s · auto_pass (proxy): True

**Công cụ:** search_documents({'query': 'Bảng 5 chi phí tăng thêm điện mặt trời gió trên bờ gió ngoài khơi', 'kind': 'table'}) → ['p57:tb18', 'p56:tb17', 'p56:fg16', 'p65:fg21', 'p56:t1', 'p57:t0', 'p59:t1', 'p85:t4']; search_documents({'query': 'chi phí vốn để lưu trữ và phát điện mới 44 tỷ USD', 'kind': 'table'}) → ['p56:tb17', 'p57:tb18', 'p77:fg26', 'p32:tb9', 'p56:t3', 'p56:t1', 'p50:t0', 'p92:t1']

**Câu trả lời:** Cộng ba dòng trong Bảng 5: mặt trời +21, gió trên bờ +8, gió ngoài khơi +39 = **68 tỷ USD** [ccdr-vn-2022:p57:tb18]. Con số này lớn hơn dòng "Chi phí vốn để lưu trữ và phát điện mới" (+44 tỷ USD) [ccdr-vn-2022:p56:tb17] vì +44 là số **ròng** đã trừ phần giảm than đá (-19) và khí đốt (-8): 68 − 19 − 8 = 41, chênh lệch nhỏ so với 44 có thể do các hạng mục khác (lưu trữ, thủy điện, sinh khối) và làm tròn [ccdr-vn-2022:p56:tb17][ccdr-vn-2022:p57:tb18]. Báo cáo giải thích chi phí đầu tư ứng trước phụ trội cao hơn là do nhu cầu tích hợp năng lượng tái tạo (trữ điện, nâng cấp lưới, công suất dự phòng) [ccdr-vn-2022:p56:t1].

**Citation:** ['ccdr-vn-2022:p57:tb18', 'ccdr-vn-2022:p56:tb17', 'ccdr-vn-2022:p56:t1'] (không hợp lệ: [])

**Nhãn (điền vào labels_test.json):** pass = ?, lý do = ?

## t-mh3 · multi_hop
**Câu hỏi:** Phát thải GHG bình quân đầu người của Việt Nam năm 2018 được nêu trong văn bản (trang 8), Bảng 1 và Phụ lục 1 là bao nhiêu? Các số này có thống nhất không?

**Đáp án chuẩn:** Văn bản 3,81 và Bảng 1 3,8 (thống nhất); Phụ lục 1 ghi 2,7 nên không nhất quán.  
**Evidence (trang PDF):** tr.18 [text] 'Lượng phát thải GHG bình quân đầu người năm 2018 là 3,81 tấn CO2e'; tr.19 [table] Bảng 1: Việt Nam 3,8; tr.91 [table] Phụ lục 1: Phát thải bình quân đầu người: 0,3 (1990), 1,1 (2005), 2,7 (2018)

**Trạng thái:** answered · lượt tìm: 3 · 3.24s · auto_pass (proxy): True

**Công cụ:** get_page({'page': 8}) → ['p8:t0', 'p8:t1', 'p8:t2', 'p8:t3', 'p8:t4']; search_documents({'query': 'phát thải GHG bình quân đầu người Việt Nam 2018 tấn CO2e', 'kind': 'table'}) → ['p19:fg5', 'p91:tb29a', 'p15:fg1', 'p19:tb4', 'p18:t1', 'p91:t1', 'p19:t0', 'p98:t2']; search_documents({'query': 'Phụ lục 1 phát thải bình quân đầu người', 'kind': 'table'}) → ['p91:tb29a', 'p19:fg5', 'p91:tb29b', 'p15:fg1', 'p91:t0', 'p19:t0', 'p95:t1', 'p97:t1']

**Câu trả lời:** Ba số liệu không thống nhất: văn bản trang 18 nêu 3,81 tấn CO2e/người năm 2018 [ccdr-vn-2022:p18:t1], Bảng 1 ghi 3,8 tCO2e/người (không nêu năm, nguồn Climate Watch) [ccdr-vn-2022:p19:tb4], còn Phụ lục 1 ghi 2,7 tấn CO2e/người năm 2018 [ccdr-vn-2022:p91:tb29a]. Như vậy văn bản và Bảng 1 khớp nhau (3,81 ≈ 3,8), nhưng Phụ lục 1 thấp hơn khoảng 1,1 tấn/người (chênh ~29% so với 3,81). Báo cáo không giải thích trực tiếp khác biệt này; phần "Khác biệt về dữ liệu" chỉ đề cập chênh lệch số liệu phát thải nông nghiệp giữa NDC và WRI/FAO [ccdr-vn-2022:p98:t2].

**Citation:** ['ccdr-vn-2022:p18:t1', 'ccdr-vn-2022:p19:tb4', 'ccdr-vn-2022:p91:tb29a', 'ccdr-vn-2022:p98:t2'] (không hợp lệ: [])

**Nhãn (điền vào labels_test.json):** pass = ?, lý do = ?

## t-mh4 · multi_hop
**Câu hỏi:** Tác động kinh tế ròng 2022–2040 của NZP kèm cải cách hỗ trợ theo Bảng 3 là bao nhiêu tỷ USD, và GDP năm 2040 thay đổi bao nhiêu % khi áp dụng tất cả biện pháp hỗ trợ theo Bảng 4?

**Đáp án chuẩn:** -1,3 tỷ USD (Bảng 3) và +3,3% GDP năm 2040 (Bảng 4).  
**Evidence (trang PDF):** tr.50 [table] Bảng 3: -1,3; tr.53 [table] Bảng 4: NZP và tất cả các biện pháp hỗ trợ: GDP 2040 = 3,3

**Trạng thái:** answered · lượt tìm: 2 · 2.63s · auto_pass (proxy): True

**Công cụ:** search_documents({'query': 'Bảng 3 tác động kinh tế ròng NZP cải cách hỗ trợ 2022-2040 tỷ USD', 'kind': 'table'}) → ['p50:tb13', 'p53:tb14', 'p32:tb9', 'p57:tb18', 'p50:t0', 'p52:t3', 'p50:t1', 'p53:t1']; search_documents({'query': 'Bảng 4 GDP năm 2040 thay đổi % tất cả biện pháp hỗ trợ', 'kind': 'table'}) → ['p53:tb14', 'p32:tb9', 'p72:fg25', 'p77:fg26', 'p52:t3', 'p74:t2', 'p53:t1', 'p53:t0']

**Câu trả lời:** Tác động kinh tế ròng 2022–2040 của NZP kèm cải cách hỗ trợ là **-1,3 tỷ USD** (NPV, chiết khấu 6%) [ccdr-vn-2022:p50:tb13]. Khi áp dụng tất cả các biện pháp hỗ trợ theo Bảng 4, GDP năm 2040 **tăng 3,3%** so với đường cơ sở (và tăng 1,7% vào năm 2030) [ccdr-vn-2022:p53:tb14].

**Citation:** ['ccdr-vn-2022:p50:tb13', 'ccdr-vn-2022:p53:tb14'] (không hợp lệ: [])

**Nhãn (điền vào labels_test.json):** pass = ?, lý do = ?

## t-tx1 · text
**Câu hỏi:** Theo văn bản, năm 2020 biến đổi khí hậu gây thiệt hại cho Việt Nam bao nhiêu và tương đương bao nhiêu % GDP?

**Đáp án chuẩn:** 10 tỷ USD, tương đương 3,2% GDP.  
**Evidence (trang PDF):** tr.17 [text] năm 2020 Việt Nam đã thiệt hại 10 tỷ USD, tương đương 3,2% GDP

**Trạng thái:** answered · lượt tìm: 2 · 2.7s · auto_pass (proxy): True

**Công cụ:** search_documents({'query': 'năm 2020 thiệt hại do biến đổi khí hậu % GDP', 'kind': 'any'}) → ['p17:t0', 'p30:t2', 'p30:t1', 'p24:t3', 'p30:fg8', 'p17:t1', 'p30:t3', 'p29:t1']; search_documents({'query': 'thiệt hại kinh tế thiên tai năm 2020 tỷ USD', 'kind': 'any'}) → ['p17:t0', 'p30:t2', 'p57:tb18', 'p25:fg6', 'p30:t1', 'p17:fg2', 'p17:t2', 'p43:t3']

**Câu trả lời:** Năm 2020, Việt Nam thiệt hại 10 tỷ USD, tương đương 3,2% GDP, do tác động của biến đổi khí hậu [ccdr-vn-2022:p17:t0]. Con số này là tổng chi phí ước tính theo các hạng mục trong Hình 3 (thủy sản 4.219 triệu USD lớn nhất, năng suất lao động 2.807, nước biển dâng 1.474, nông nghiệp 837, chi phí giải nhiệt 518, thiên tai 447, sức khỏe 235, nước 218, du lịch 148 triệu USD) [ccdr-vn-2022:p17:fg2].

**Citation:** ['ccdr-vn-2022:p17:t0', 'ccdr-vn-2022:p17:fg2'] (không hợp lệ: [])

**Nhãn (điền vào labels_test.json):** pass = ?, lý do = ?

## t-tx2 · text
**Câu hỏi:** Đồng bằng sông Cửu Long đóng góp bao nhiêu % sản lượng lúa và bao nhiêu % kim ngạch xuất khẩu gạo của Việt Nam?

**Đáp án chuẩn:** 50% sản lượng lúa và 95% kim ngạch xuất khẩu gạo.  
**Evidence (trang PDF):** tr.40 [text] đóng góp 50% sản lượng lúa và 95% kim ngạch xuất khẩu gạo

**Trạng thái:** answered · lượt tìm: 2 · 2.43s · auto_pass (proxy): True

**Công cụ:** search_documents({'query': 'Đồng bằng sông Cửu Long sản lượng lúa phần trăm', 'kind': 'any'}) → ['p40:t0', 'p40:t1', 'p65:fg21', 'p66:t3', 'p40:t3', 'p65:t1', 'p33:t4', 'p40:fg11']; search_documents({'query': 'xuất khẩu gạo Đồng bằng sông Cửu Long kim ngạch', 'kind': 'any'}) → ['p40:t0', 'p40:fg11', 'p65:fg21', 'p40:t1', 'p65:t1', 'p83:t1', 'p40:t3', 'p66:t3']

**Câu trả lời:** Đồng bằng sông Cửu Long đóng góp 50% sản lượng lúa và 95% kim ngạch xuất khẩu gạo của Việt Nam [ccdr-vn-2022:p40:t0].

**Citation:** ['ccdr-vn-2022:p40:t0'] (không hợp lệ: [])

**Nhãn (điền vào labels_test.json):** pass = ?, lý do = ?

## t-tx3 · text
**Câu hỏi:** Tỷ lệ tiếp cận điện của Việt Nam tăng từ bao nhiêu % năm 1993 lên bao nhiêu % năm 2020?

**Đáp án chuẩn:** Từ 14% lên 99%.  
**Evidence (trang PDF):** tr.53 [text] tỷ lệ tiếp cận điện năng từ 14% năm 1993 lên 99% vào năm 2020

**Trạng thái:** answered · lượt tìm: 2 · 2.92s · auto_pass (proxy): True

**Công cụ:** search_documents({'query': 'tỷ lệ tiếp cận điện năm 1993 2020', 'kind': 'any'}) → ['p53:t2', 'p92:t1', 'p70:t2', 'p71:t0', 'p53:t3', 'p56:fg16', 'p54:t0', 'p92:t0']; search_documents({'query': 'điện khí hóa nông thôn tiếp cận điện tăng', 'kind': 'any'}) → ['p53:t2', 'p54:t0', 'p92:t1', 'p56:fg16', 'p85:t3', 'p51:t2', 'p92:t0', 'p25:t2']

**Câu trả lời:** Tỷ lệ tiếp cận điện của Việt Nam tăng từ 14% năm 1993 lên 99% vào năm 2020 [ccdr-vn-2022:p53:t2].

**Citation:** ['ccdr-vn-2022:p53:t2'] (không hợp lệ: [])

**Nhãn (điền vào labels_test.json):** pass = ?, lý do = ?

## t-tx4 · text
**Câu hỏi:** Theo kết quả mô hình, hộ gia đình người Kinh có khả năng bị ảnh hưởng thấp hơn bao nhiêu % so với hộ gia đình dân tộc thiểu số?

**Đáp án chuẩn:** Thấp hơn 37%.  
**Evidence (trang PDF):** tr.70 [text] Hộ gia đình người Kinh có khả năng bị ảnh hưởng thấp hơn 37% so với hộ gia đình dân tộc thiểu số

**Trạng thái:** answered · lượt tìm: 2 · 2.36s · auto_pass (proxy): True

**Công cụ:** search_documents({'query': 'hộ gia đình người Kinh khả năng bị ảnh hưởng so với dân tộc thiểu số mô hình', 'kind': 'any'}) → ['p70:t1', 'p45:t3', 'p70:t0', 'p69:t2', 'p43:t2', 'p37:t0', 'p71:t0', 'p44:t4']; search_documents({'query': 'dân tộc thiểu số hộ gia đình bị ảnh hưởng bởi khí hậu xác suất', 'kind': 'any'}) → ['p45:t3', 'p70:t1', 'p43:t2', 'p30:t1', 'p70:t0', 'p43:t1', 'p37:t0', 'p69:t2']

**Câu trả lời:** Theo kết quả mô hình, hộ gia đình người Kinh có khả năng bị ảnh hưởng thấp hơn **37%** so với hộ gia đình dân tộc thiểu số [ccdr-vn-2022:p70:t1].

**Citation:** ['ccdr-vn-2022:p70:t1'] (không hợp lệ: [])

**Nhãn (điền vào labels_test.json):** pass = ?, lý do = ?

## t-a1 · thieu_bang_chung
**Câu hỏi:** Thiệt hại kinh tế cụ thể của riêng tỉnh Cà Mau do mực nước biển dâng đến năm 2050 là bao nhiêu tỷ USD?

**Mong đợi:** từ chối. Báo cáo chỉ nêu tỷ lệ diện tích Cà Mau bị ngập (79%), không nêu thiệt hại tiền. Kiểm tra: tìm từ khóa ['thiệt hại của tỉnh cà mau'] trên toàn bộ 104 trang (lớp văn bản) và ghi chú hình/bảng, không có.

**Trạng thái:** abstain · lượt tìm: 4 · 4.34s · auto_pass (proxy): True

**Công cụ:** search_documents({'query': 'Cà Mau thiệt hại kinh tế nước biển dâng 2050', 'kind': 'any'}) → ['p30:t2', 'p30:fg8', 'p40:t1', 'p17:t0', 'p94:t1', 'p30:t1', 'p29:t0', 'p94:t2']; search_documents({'query': 'thiệt hại kinh tế do nước biển dâng theo tỉnh đồng bằng sông Cửu Long', 'kind': 'any'}) → ['p17:t0', 'p40:t1', 'p45:t2', 'p40:fg11', 'p40:t3', 'p30:t2', 'p40:t0', 'p33:t4']; search_documents({'query': 'Cà Mau tổn thất tỷ USD nước biển dâng 2050', 'kind': 'table'}) → ['p30:fg8', 'p40:fg11', 'p17:fg2', 'p57:tb18', 'p40:t1', 'p30:t2', 'p17:t0', 'p30:t1']; search_documents({'query': 'bảng thiệt hại kinh tế cấp tỉnh nước biển dâng Cà Mau Kiên Giang', 'kind': 'any'}) → ['p30:t2', 'p40:t1', 'p30:fg8', 'p29:t0', 'p30:t1', 'p17:t2', 'p57:tb18', 'p17:t0']

**Câu trả lời:** KHÔNG_ĐỦ_BẰNG_CHỨNG — Báo cáo chỉ nêu Cà Mau sẽ bị ngập 79% diện tích khi nước biển dâng 1 m [ccdr-vn-2022:p40:t1] và tổn thất ~17 tỷ USD vào năm 2030 là con số cho toàn Đồng bằng sông Cửu Long [ccdr-vn-2022:p40:t1]; không có ước tính thiệt hại kinh tế riêng của tỉnh Cà Mau đến năm 2050.

**Citation:** ['ccdr-vn-2022:p40:t1'] (không hợp lệ: [])

**Nhãn (điền vào labels_test.json):** pass = ?, lý do = ?

## t-a2 · thieu_bang_chung
**Câu hỏi:** Báo cáo ước tính nhu cầu đầu tư cho hydro xanh ở Việt Nam đến năm 2040 là bao nhiêu tỷ USD?

**Mong đợi:** từ chối. Chủ đề năng lượng sạch gần nhưng không nhắc đến hydro. Kiểm tra: tìm từ khóa ['hydro', 'hydrogen'] trên toàn bộ 104 trang (lớp văn bản) và ghi chú hình/bảng, không có.

**Trạng thái:** abstain · lượt tìm: 6 · 5.57s · auto_pass (proxy): True

**Công cụ:** search_documents({'query': 'nhu cầu đầu tư hydro xanh đến năm 2040 tỷ USD', 'kind': 'any'}) → ['p77:t0', 'p50:t0', 'p50:tb13', 'p77:t3', 'p31:t2', 'p57:tb18', 'p56:t1', 'p56:t3']; search_documents({'query': 'hydro xanh đầu tư 2040', 'kind': 'any'}) → ['p50:tb13', 'p77:t0', 'p50:t0', 'p77:t2', 'p49:t2', 'p56:t1', 'p49:t1', 'p53:tb14']; search_documents({'query': 'hydro xanh sản xuất hydro điện phân', 'kind': 'any'}) → ['p56:t0', 'p66:t1', 'p92:t1', 'p92:t0', 'p54:fg15', 'p59:t0', 'p54:t0', 'p9:t0']; search_documents({'query': 'hydrogen green', 'kind': 'any'}) → ['p17:t2', 'p34:t4', 'p20:t1', 'p63:t3', 'p17:t1', 'p56:t0', 'p91:t1', 'p9:t0']; search_documents({'query': 'hydro xanh nhu cầu đầu tư ước tính', 'kind': 'text'}) → ['p50:t0', 'p31:t2', 'p96:t2', 'p77:t0', 'p32:tb9', 'p32:t1', 'p50:tb13', 'p57:tb18']; search_documents({'query': 'hydro xanh', 'kind': 'table'}) → ['p40:fg11', 'p78:fg27', 'p42:fg12', 'p19:fg5', 'p74:t3', 'p77:t2', 'p78:t2', 'p78:t1']

**Câu trả lời:** KHÔNG_ĐỦ_BẰNG_CHỨNG — Các đoạn truy xuất chỉ nêu tổng nhu cầu đầu tư cho lộ trình phát thải ròng bằng 0 (81,3 tỷ USD NPV 2022–2040) [ccdr-vn-2022:p50:tb13] và tổng nhu cầu tài chính 368 tỷ USD đến 2040 [ccdr-vn-2022:p77:t0], không có ước tính riêng cho hydro xanh.

**Citation:** ['ccdr-vn-2022:p50:tb13', 'ccdr-vn-2022:p77:t0'] (không hợp lệ: [])

**Nhãn (điền vào labels_test.json):** pass = ?, lý do = ?

## t-a3 · thieu_bang_chung
**Câu hỏi:** Sản lượng thép của Việt Nam năm 2020 là bao nhiêu triệu tấn?

**Mong đợi:** từ chối. Báo cáo nói về công nghiệp (xi măng, kim loại) nhưng không có số liệu sản lượng thép. Kiểm tra: tìm từ khóa ['thép'] trên toàn bộ 104 trang (lớp văn bản) và ghi chú hình/bảng, không có.

**Trạng thái:** abstain · lượt tìm: 4 · 3.58s · auto_pass (proxy): True

**Công cụ:** search_documents({'query': 'sản lượng thép Việt Nam năm 2020 triệu tấn', 'kind': 'any'}) → ['p53:t3', 'p91:tb29a', 'p98:t2', 'p41:t3', 'p91:t0', 'p18:t1', 'p91:t1', 'p58:t0']; search_documents({'query': 'sản xuất thép thô công suất thép', 'kind': 'any'}) → ['p54:t1', 'p54:fg15', 'p54:t0', 'p25:t1', 'p66:t1', 'p60:t1', 'p25:fg6', 'p91:t1']; search_documents({'query': 'ngành thép sản lượng thép thô Việt Nam', 'kind': 'any'}) → ['p18:t1', 'p91:t0', 'p41:t3', 'p26:fg7', 'p91:tb29a', 'p26:t2', 'p17:t2', 'p54:fg15']; search_documents({'query': 'xi măng thép vật liệu sản xuất công nghiệp nặng phát thải', 'kind': 'any'}) → ['p96:t1', 'p72:t1', 'p26:fg7', 'p18:t1', 'p18:fg3', 'p17:t2', 'p91:t1', 'p25:t1']

**Câu trả lời:** KHÔNG_ĐỦ_BẰNG_CHỨNG — Báo cáo không nêu sản lượng thép (triệu tấn) của Việt Nam năm 2020; chỉ có dữ liệu về tỷ trọng sản lượng của doanh nghiệp nhà nước trong ngành "Kim loại" (14% năm 2018) [ccdr-vn-2022:p26:fg7], không phải sản lượng thép.

**Citation:** ['ccdr-vn-2022:p26:fg7'] (không hợp lệ: [])

**Nhãn (điền vào labels_test.json):** pass = ?, lý do = ?

## t-a4 · thieu_bang_chung
**Câu hỏi:** Thiệt hại do bão Yagi năm 2024 gây ra cho Việt Nam được báo cáo là bao nhiêu?

**Mong đợi:** từ chối. Báo cáo xuất bản 07/2022, không thể có sự kiện năm 2024. Kiểm tra: tìm từ khóa ['yagi'] trên toàn bộ 104 trang (lớp văn bản) và ghi chú hình/bảng, không có.

**Trạng thái:** abstain · lượt tìm: 4 · 4.02s · auto_pass (proxy): True

**Công cụ:** search_documents({'query': 'bão Yagi thiệt hại', 'kind': 'any'}) → ['p30:t2', 'p30:t1', 'p94:t1', 'p57:tb18', 'p30:t3', 'p17:t0', 'p30:fg8', 'p29:t0']; search_documents({'query': 'thiệt hại kinh tế do bão lũ năm 2024', 'kind': 'any'}) → ['p30:t2', 'p29:t1', 'p30:fg8', 'p30:t1', 'p57:tb18', 'p37:fg10', 'p29:t0', 'p37:t1']; search_documents({'query': 'Yagi', 'kind': 'any'}) → ['p14:t0', 'p28:t0', 'p29:t2', 'p91:t1', 'p96:t1', 'p95:t0', 'p82:t0', 'p78:t3']; search_documents({'query': 'bão năm 2024 thiệt hại tỷ USD', 'kind': 'any'}) → ['p30:t2', 'p57:tb18', 'p30:fg8', 'p17:t0', 'p56:t1', 'p30:t1', 'p30:t3', 'p94:t1']

**Câu trả lời:** KHÔNG_ĐỦ_BẰNG_CHỨNG — Báo cáo (xuất bản 2022) không đề cập bão Yagi hay thiệt hại cụ thể của năm 2024; chỉ có số liệu chung về thiệt hại do hiện tượng khí hậu cực đoan (trung bình ~2,4 tỷ USD/năm, 0,8% GDP) [ccdr-vn-2022:p30:t1] và thiệt hại 10 tỷ USD năm 2020 [ccdr-vn-2022:p17:t0].

**Citation:** ['ccdr-vn-2022:p30:t1', 'ccdr-vn-2022:p17:t0'] (không hợp lệ: [])

**Nhãn (điền vào labels_test.json):** pass = ?, lý do = ?

## t-a5 · thieu_bang_chung
**Câu hỏi:** Tổng vốn đầu tư năm 2021 của Tập đoàn Điện lực Việt Nam (EVN) là bao nhiêu tỷ đồng?

**Mong đợi:** từ chối. EVN chỉ được nhắc 4 lần (viết tắt, đơn vị cung cấp điện, nguồn số liệu, đơn vị thu tiền), đã đọc từng ngữ cảnh: không có số vốn đầu tư. Kiểm tra: tìm từ khóa ['vốn đầu tư của evn', 'evn đầu tư'] trên toàn bộ 104 trang (lớp văn bản) và ghi chú hình/bảng, không có.

**Trạng thái:** abstain · lượt tìm: 4 · 4.29s · auto_pass (proxy): True

**Công cụ:** search_documents({'query': 'EVN tổng vốn đầu tư năm 2021', 'kind': 'any'}) → ['p9:t0', 'p93:t1', 'p59:t2', 'p54:t1', 'p78:t1', 'p54:fg15', 'p24:t3', 'p97:t1']; search_documents({'query': 'Tập đoàn Điện lực Việt Nam đầu tư vốn', 'kind': 'any'}) → ['p9:t0', 'p53:t2', 'p78:t0', 'p85:t1', 'p60:t1', 'p58:t0', 'p80:t2', 'p85:t4']; search_documents({'query': 'tổng vốn đầu tư EVN tỷ đồng 2021 nhu cầu vốn', 'kind': 'table'}) → ['p32:tb9', 'p50:tb13', 'p56:tb17', 'p57:tb18', 'p96:t2', 'p50:t0', 'p32:t1', 'p80:t2']; search_documents({'query': 'EVN đầu tư 2021 tỷ đồng kế hoạch vốn', 'kind': 'any'}) → ['p54:t1', 'p59:t2', 'p38:t3', 'p80:t2', 'p78:t1', 'p23:t1', 'p79:t4', 'p85:t1']

**Câu trả lời:** KHÔNG_ĐỦ_BẰNG_CHỨNG — Báo cáo không nêu tổng vốn đầu tư năm 2021 của EVN; các đoạn chỉ có dữ liệu về công suất lắp đặt ngành điện (68 GW năm 2020) và nhu cầu đầu tư chung, không có con số vốn đầu tư của EVN.

**Citation:** [] (không hợp lệ: [])

**Nhãn (điền vào labels_test.json):** pass = ?, lý do = ?

## t-a6 · thieu_bang_chung
**Câu hỏi:** Giá điện bán lẻ bình quân cụ thể (đồng/kWh) mà báo cáo đề xuất cho năm 2030 là bao nhiêu?

**Mong đợi:** từ chối. Báo cáo nói giá điện ADS cao hơn 16–26% so với CPS nhưng không nêu mức đồng/kWh. Kiểm tra: tìm từ khóa ['đồng/kwh', 'vnd/kwh'] trên toàn bộ 104 trang (lớp văn bản) và ghi chú hình/bảng, không có.

**Trạng thái:** abstain · lượt tìm: 4 · 5.37s · auto_pass (proxy): True

**Công cụ:** search_documents({'query': 'giá điện bán lẻ bình quân đề xuất năm 2030 đồng/kWh', 'kind': 'any'}) → ['p56:t2', 'p92:t0', 'p54:t1', 'p54:t0', 'p36:t3', 'p9:t0', 'p101:t0', 'p56:fg16']; search_documents({'query': 'giá điện bán lẻ bình quân', 'kind': 'table'}) → ['p91:tb29a', 'p56:fg16', 'p54:fg15', 'p71:fg24', 'p56:t2', 'p92:t0', 'p97:t1', 'p95:t1']; search_documents({'query': 'giá điện bình quân đồng/kWh năm 2030 kịch bản CPS ADS', 'kind': 'figure'}) → ['p56:fg16', 'p62:fg20', 'p30:fg8', 'p70:fg23', 'p56:t2', 'p56:t1', 'p56:t3', 'p56:tb17']; search_documents({'query': 'biểu giá điện bình quân tăng giá điện lộ trình 2020 2030 2040', 'kind': 'any'}) → ['p56:t2', 'p70:t2', 'p71:t0', 'p92:t0', 'p56:fg16', 'p9:t0', 'p91:tb29a', 'p50:tb13']

**Câu trả lời:** KHÔNG_ĐỦ_BẰNG_CHỨNG — Báo cáo chỉ nêu giá điện bình quân trong ADS cao hơn CPS 26% vào 2040 và cao hơn trung bình 16% giai đoạn 2020–2040 [ccdr-vn-2022:p56:t2], không có con số tuyệt đối (đồng/kWh) cho năm 2030.

**Citation:** ['ccdr-vn-2022:p56:t2'] (không hợp lệ: [])

**Nhãn (điền vào labels_test.json):** pass = ?, lý do = ?
