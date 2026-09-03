const KPSS_DATA = {
  "examDate": "2026-10-25T10:15:00",
  "subjects": [
    {
      "id": "matematik",
      "name": "Matematik",
      "icon": "📐",
      "color": "#3b82f6",
      "questionCount": 30,
      "description": "Temel Matematik, Sayılar, Problemler, Kümeler-Mantık ve Geometri",
      "topics": [
        {
          "id": "mat_1",
          "title": "1. Temel Kavramlar & Sayı Kümeleri",
          "avgQuestions": "3-4 Soru",
          "summary": "Sayı kümeleri, tek-çift sayılar, ardışık sayı toplamları, asal sayılar ve faktöriyel işlemleri.",
          "keyPoints": [
            "0 sayısı çift bir tam sayıdır ve nötrdür.",
            "a · b = Tek ise a ve b'nin her ikisi de KESİNLİKLE TEKTİR.",
            "Ardışık n tek sayının toplamı n'e bölündüğünde ortanca sayı bulunur."
          ],
          "pages": [
            {
              "pageNo": "1",
              "pageTitle": "1. Bölüm: Sayı Kümeleri ve Tek-Çift İşlemleri",
              "text": "<div class=\"content-block\">\n  <h3>📐 Sayı Kümeleri ve Sembolleri</h3>\n  <table style=\"width:100%; border-collapse:collapse; margin:12px 0;\">\n    <tr style=\"background:#1e293b;\"><th style=\"padding:8px; border:1px solid #334155;\">Küme</th><th style=\"padding:8px; border:1px solid #334155;\">Sembol</th><th style=\"padding:8px; border:1px solid #334155;\">Elemanlar</th></tr>\n    <tr><td style=\"padding:6px; border:1px solid #334155;\">Rakamlar</td><td style=\"padding:6px; border:1px solid #334155;\">-</td><td style=\"padding:6px; border:1px solid #334155;\">{0, 1, 2, 3, 4, 5, 6, 7, 8, 9} (10 tanedir)</td></tr>\n    <tr><td style=\"padding:6px; border:1px solid #334155;\">Sayma Sayıları</td><td style=\"padding:6px; border:1px solid #334155;\">N⁺</td><td style=\"padding:6px; border:1px solid #334155;\">{1, 2, 3, 4, ...}</td></tr>\n    <tr><td style=\"padding:6px; border:1px solid #334155;\">Doğal Sayılar</td><td style=\"padding:6px; border:1px solid #334155;\">N</td><td style=\"padding:6px; border:1px solid #334155;\">{0, 1, 2, 3, ...} (0 dahildir)</td></tr>\n    <tr><td style=\"padding:6px; border:1px solid #334155;\">Tam Sayılar</td><td style=\"padding:6px; border:1px solid #334155;\">Z</td><td style=\"padding:6px; border:1px solid #334155;\">{..., -2, -1, 0, 1, 2, ...}</td></tr>\n    <tr><td style=\"padding:6px; border:1px solid #334155;\">Rasyonel Sayılar</td><td style=\"padding:6px; border:1px solid #334155;\">Q</td><td style=\"padding:6px; border:1px solid #334155;\">a/b şeklinde yazılanlar (b ≠ 0)</td></tr>\n  </table>\n\n  <h3>⚡ Tek ve Çift Sayılarda İşlem Kuralları</h3>\n  <table style=\"width:100%; border-collapse:collapse; margin:12px 0;\">\n    <tr style=\"background:#1e293b;\"><th style=\"padding:8px; border:1px solid #334155;\">Toplama / Çıkarma</th><th style=\"padding:8px; border:1px solid #334155;\">Çarpma</th><th style=\"padding:8px; border:1px solid #334155;\">Üs Alma (n ∈ Z⁺)</th></tr>\n    <tr><td style=\"padding:6px; border:1px solid #334155;\">T ± T = <b>Ç</b><br>Ç ± Ç = <b>Ç</b><br>T ± Ç = <b>T</b></td><td style=\"padding:6px; border:1px solid #334155;\">T · T = <b>T</b><br>T · Ç = <b>Ç</b><br>Ç · Ç = <b>Ç</b></td><td style=\"padding:6px; border:1px solid #334155;\">Tⁿ = <b>T</b><br>Çⁿ = <b>Ç</b></td></tr>\n  </table>\n\n  <div style=\"background:rgba(59,130,246,0.1); border-left:4px solid #3b82f6; padding:12px; margin:12px 0; border-radius:4px;\">\n    <b>Örnek İşlem 1:</b> a, b tam sayılar ve <code>(5a + 3b) / 2 = c</code> olduğuna göre:<br>\n    <b>Adım 1:</b> İçler-dışlar çarpımı yap: <code>5a + 3b = 2c</code><br>\n    <b>Adım 2:</b> <code>2c</code> ifadesi 2 ile çarpıldığı için DAİMA <b>ÇİFTTİR</b>.<br>\n    <b>Adım 3:</b> <code>5a + 3b = Çift</code> olması için: ya (a=Tek ve b=Tek) ya da (a=Çift ve b=Çift) olmalıdır. (c hakkında kesin bir şey söylenemez).\n  </div>\n</div>"
            },
            {
              "pageNo": "2",
              "pageTitle": "2. Bölüm: Ardışık Sayılar ve Gauss Toplam Formülleri",
              "text": "<div class=\"content-block\">\n  <h3>🔢 Ardışık Sayılar ve Toplam Formülleri</h3>\n  <ul>\n    <li><b>Terim Sayısı Formülü:</b> <code>TS = [(Son Terim - İlk Terim) / Artış Miktarı] + 1</code></li>\n    <li><b>Ortanca Terim Formülü:</b> <code>Ortanca = (Son Terim + İlk Terim) / 2</code></li>\n    <li><b>Dizi Toplam Formülü:</b> <code>Toplam = Terim Sayısı × Ortanca Terim</code></li>\n  </ul>\n\n  <h3>⚡ Özel Toplam Formülleri</h3>\n  <ul>\n    <li><code>1 + 2 + 3 + ... + n = [n · (n + 1)] / 2</code></li>\n    <li><code>2 + 4 + 6 + ... + 2n = n · (n + 1)</code></li>\n    <li><code>1 + 3 + 5 + ... + (2n - 1) = n²</code></li>\n  </ul>\n\n  <div style=\"background:rgba(16,185,129,0.1); border-left:4px solid #10b981; padding:12px; margin:12px 0; border-radius:4px;\">\n    <b>Örnek İşlem:</b> <code>7 + 11 + 15 + ... + 43</code> toplamı kaçtır?<br>\n    <b>Adım 1 (Terim Sayısı):</b> <code>TS = [(43 - 7) / 4] + 1 = [36 / 4] + 1 = 9 + 1 = 10</code><br>\n    <b>Adım 2 (Ortanca Terim):</b> <code>Ortanca = (43 + 7) / 2 = 50 / 2 = 25</code><br>\n    <b>Adım 3 (Toplam):</b> <code>Toplam = 10 × 25 = 250</code>\n  </div>\n</div>"
            },
            {
              "pageNo": "3",
              "pageTitle": "3. Bölüm: Asal Sayılar ve Faktöriyel İşlemleri",
              "text": "<div class=\"content-block\">\n  <h3>✨ Asal Sayılar Tablosu ve Kuralları</h3>\n  <p>1 ve kendisinden başka pozitif böleni olmayan 1'den büyük sayılardır: <b>{2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, ...}</b></p>\n  <ul>\n    <li>En küçük asal sayı <b>2</b>'dir. 2 dışında hiçbir çift asal sayı yoktur.</li>\n    <li>Aralarında asal sayıların 1'den başka ortak böleni yoktur (Örn: 8 ve 15 asaldır).</li>\n  </ul>\n\n  <h3>❗ Faktöriyel Değerleri ve Sadeleştirme</h3>\n  <p><code>0! = 1</code>, <code>1! = 1</code>, <code>2! = 2</code>, <code>3! = 6</code>, <code>4! = 24</code>, <code>5! = 120</code>, <code>6! = 720</code></p>\n  <p>Faktöriyel açılım kuralı: <code>n! = n · (n - 1)!</code></p>\n\n  <div style=\"background:rgba(245,158,11,0.1); border-left:4px solid #f59e0b; padding:12px; margin:12px 0; border-radius:4px;\">\n    <b>Örnek İşlem:</b> <code>(8! + 7!) / (8! - 7!)</code> ifadesinin sonucu kaçtır?<br>\n    <b>Adım 1:</b> Büyük olanı küçük olana (7!) benzet: <code>8! = 8 · 7!</code><br>\n    <b>Adım 2 (Pay):</b> <code>8 · 7! + 1 · 7! = 7! · (8 + 1) = 7! · 9</code><br>\n    <b>Adım 3 (Payda):</b> <code>8 · 7! - 1 · 7! = 7! · (8 - 1) = 7! · 7</code><br>\n    <b>Adım 4 (Sadeleştirme):</b> <code>(7! · 9) / (7! · 7) = 9 / 7</code>\n  </div>\n</div>"
            }
          ],
          "questions": [
            {
              "id": "q_m_1",
              "level": "Kolay",
              "text": "a ve b birer tam sayı olmak üzere, 3a + 5b ifadesi çift sayıdır. Buna göre aşağıdakilerden hangisi KESİNLİKLE çift sayıdır?",
              "options": [
                "A) a + b",
                "B) a · b",
                "C) a² + b",
                "D) 2a + b",
                "E) 3a + b"
              ],
              "correct": 0,
              "solution": "3a + 5b çift ise a ve b aynı teklik-çiftlik durumundadır. Dolayısıyla a + b KESİNLİKLE çifttir."
            }
          ]
        },
        {
          "id": "mat_2",
          "title": "2. Bölme-Bölünebilme Kuralları & EBOB-EKOK",
          "avgQuestions": "2-3 Soru",
          "summary": "2, 3, 4, 5, 8, 9, 10, 11 bölünebilme formülleri ve EBOB-EKOK problemleri.",
          "keyPoints": [
            "3 ve 9 ile bölünebilmede rakamlar toplamı kontrol edilir.",
            "11 ile bölünebilmede sayının üzerine sağdan sola (+ - + -) yazılır.",
            "İki sayının çarpımı: a · b = EBOB(a, b) · EKOK(a, b)."
          ],
          "pages": [
            {
              "pageNo": "1",
              "pageTitle": "1. Bölüm: Bölünebilme Kuralları Tablosu",
              "text": "<div class=\"content-block\">\n  <h3>⚡ Bölünebilme Kuralları Özet Tablosu</h3>\n  <table style=\"width:100%; border-collapse:collapse; margin:12px 0;\">\n    <tr style=\"background:#1e293b;\"><th style=\"padding:8px; border:1px solid #334155;\">Bölen</th><th style=\"padding:8px; border:1px solid #334155;\">Kural</th><th style=\"padding:8px; border:1px solid #334155;\">Örnek İşlem</th></tr>\n    <tr><td style=\"padding:6px; border:1px solid #334155;\"><b>2</b></td><td style=\"padding:6px; border:1px solid #334155;\">Son basamak çift (0, 2, 4, 6, 8) olmalı</td><td style=\"padding:6px; border:1px solid #334155;\">348 (8 çifttir, bölünür)</td></tr>\n    <tr><td style=\"padding:6px; border:1px solid #334155;\"><b>3</b></td><td style=\"padding:6px; border:1px solid #334155;\">Rakamlar toplamı 3'ün katı olmalı</td><td style=\"padding:6px; border:1px solid #334155;\">741 → 7+4+1 = 12 (3'ün katı, bölünür)</td></tr>\n    <tr><td style=\"padding:6px; border:1px solid #334155;\"><b>4</b></td><td style=\"padding:6px; border:1px solid #334155;\">Son iki basamak 00 veya 4'ün katı olmalı</td><td style=\"padding:6px; border:1px solid #334155;\">5324 → 24 (4'ün katı, bölünür)</td></tr>\n    <tr><td style=\"padding:6px; border:1px solid #334155;\"><b>5</b></td><td style=\"padding:6px; border:1px solid #334155;\">Son basamak 0 veya 5 olmalı</td><td style=\"padding:6px; border:1px solid #334155;\">875 (sonu 5, bölünür)</td></tr>\n    <tr><td style=\"padding:6px; border:1px solid #334155;\"><b>8</b></td><td style=\"padding:6px; border:1px solid #334155;\">Son üç basamak 8'in katı olmalı</td><td style=\"padding:6px; border:1px solid #334155;\">1120 → 120/8 = 15 (bölünür)</td></tr>\n    <tr><td style=\"padding:6px; border:1px solid #334155;\"><b>9</b></td><td style=\"padding:6px; border:1px solid #334155;\">Rakamlar toplamı 9'un katı olmalı</td><td style=\"padding:6px; border:1px solid #334155;\">5832 → 5+8+3+2 = 18 (bölünür)</td></tr>\n    <tr><td style=\"padding:6px; border:1px solid #334155;\"><b>11</b></td><td style=\"padding:6px; border:1px solid #334155;\">Sağdan sola (+ - + -) toplamı 11'in katı olmalı</td><td style=\"padding:6px; border:1px solid #334155;\">8591 → (+1) + (-9) + (+5) + (-8) = -11 (bölünür)</td></tr>\n  </table>\n</div>"
            },
            {
              "pageNo": "2",
              "pageTitle": "2. Bölüm: EBOB - EKOK Formülleri ve Problem Tipleri",
              "text": "<div class=\"content-block\">\n  <h3>📐 EBOB ve EKOK Özellikleri</h3>\n  <ul>\n    <li><b>Temel Bağıntı:</b> <code>EBOB(a, b) · EKOK(a, b) = a · b</code></li>\n    <li>Aralarında asal iki sayının <code>EBOB'u = 1</code>, <code>EKOK'u = a · b</code>'dir.</li>\n  </ul>\n\n  <h3>⚡ Problem Ayrımı Rehberi</h3>\n  <table style=\"width:100%; border-collapse:collapse; margin:12px 0;\">\n    <tr style=\"background:#1e293b;\"><th style=\"padding:8px; border:1px solid #334155;\">Durum</th><th style=\"padding:8px; border:1px solid #334155;\">Kullanılacak Yöntem</th><th style=\"padding:8px; border:1px solid #334155;\">Tipik Örnekler</th></tr>\n    <tr><td style=\"padding:6px; border:1px solid #334155;\"><b>Büyükten Küçüğe</b> (Bölme / Parçalama)</td><td style=\"padding:6px; border:1px solid #334155;\"><b>EBOB</b></td><td style=\"padding:6px; border:1px solid #334155;\">Çuvallardaki pirinci eşit paketlere bölme, Tarlanın etrafına eşit aralıkla direk dikme.</td></tr>\n    <tr><td style=\"padding:6px; border:1px solid #334155;\"><b>Küçükten Büyüğe</b> (Katlama / Birleştirme)</td><td style=\"padding:6px; border:1px solid #334155;\"><b>EKOK</b></td><td style=\"padding:6px; border:1px solid #334155;\">Zillerin birlikte çalması, Nöbet günlerinin kesişmesi, Tuğlalardan küp yapma.</td></tr>\n  </table>\n</div>"
            }
          ],
          "questions": [
            {
              "id": "q_m_2",
              "level": "Orta",
              "text": "Rakamları farklı 4a50 sayısı 9 ile tam bölündüğüne göre a kaçtır?",
              "options": [
                "A) 0",
                "B) 4",
                "C) 8",
                "D) 9",
                "E) 5"
              ],
              "correct": 3,
              "solution": "4 + a + 5 + 0 = 9 + a 'nın 9 katı olması için a = 9 olmalıdır (Rakamları farklıdır: 4, 9, 5, 0)."
            }
          ]
        },
        {
          "id": "mat_3",
          "title": "3. Rasyonel & Ondalık Sayılar",
          "avgQuestions": "2 Soru",
          "summary": "Kesirlerde 4 işlem, merdivenli kesirler, devirli ondalık dönüşüm formülleri.",
          "keyPoints": [
            "Kesirlerde toplama/çıkarma için paydalar eşitlenir.",
            "Bölmede ikinci kesir ters çevrilip çarpılır: (a/b) : (c/d) = (a/b) · (d/c).",
            "Devirli formül: (Tüm Sayı - Devretmeyen Kısım) / (Devreden kadar 9, Devretmeyen kadar 0)."
          ],
          "pages": [
            {
              "pageNo": "1",
              "pageTitle": "1. Bölüm: Rasyonel Sayılarda İşlem Adımları",
              "text": "<div class=\"content-block\">\n  <h3>⚡ Rasyonel Sayılarda 4 İşlem Kuralları</h3>\n  <ul>\n    <li><b>Toplama/Çıkarma:</b> <code>(a/c) ± (b/c) = (a ± b) / c</code> (Paydalar eşit değilse EKOK'ta eşitlenir).</li>\n    <li><b>Çarpma:</b> <code>(a/b) · (c/d) = (a · c) / (b · d)</code> (Önce sadeleştirme yapılır).</li>\n    <li><b>Bölme:</b> <code>(a/b) : (c/d) = (a/b) · (d/c) = (a · d) / (b · c)</code></li>\n  </ul>\n\n  <div style=\"background:rgba(59,130,246,0.1); border-left:4px solid #3b82f6; padding:12px; margin:12px 0; border-radius:4px;\">\n    <b>Örnek İşlem (Merdivenli Kesir):</b> <code>1 + [ 1 / (1 - 1/3) ]</code> işleminin sonucu kaçtır?<br>\n    <b>Adım 1 (En alt payda):</b> <code>1 - 1/3 = 3/3 - 1/3 = 2/3</code><br>\n    <b>Adım 2 (Ters çevir):</b> <code>1 / (2/3) = 3/2</code><br>\n    <b>Adım 3 (Toplama):</b> <code>1 + 3/2 = 2/2 + 3/2 = 5/2</code>\n  </div>\n</div>"
            },
            {
              "pageNo": "2",
              "pageTitle": "2. Bölüm: Devirli Ondalık Sayı Formülü",
              "text": "<div class=\"content-block\">\n  <h3>🔄 Devirli Ondalık Açılım Formülü</h3>\n  <div style=\"background:#1e293b; padding:12px; border-radius:6px; font-size:1.1rem; border:1px solid #334155; margin:10px 0;\">\n    <code>Rasyonel Değer = (Sayının Tamamı - Devretmeyen Kısım) / (Virgülden sonra devreden kadar 9, devretmeyen kadar 0)</code>\n  </div>\n\n  <div style=\"background:rgba(16,185,129,0.1); border-left:4px solid #10b981; padding:12px; margin:12px 0; border-radius:4px;\">\n    <b>Örnek İşlem 1:</b> <code>2,34̄</code> (sadece 4 devrediyor) sayısını rasyonel sayıya çevirelim:<br>\n    • Sayının tamamı: <code>234</code><br>\n    • Devretmeyen kısım: <code>23</code><br>\n    • Virgülden sonra 1 basamak devrediyor (9), 1 basamak devretmiyor (0) → Payda: <code>90</code><br>\n    <b>Sonuç:</b> <code>(234 - 23) / 90 = 211 / 90</code>\n  </div>\n</div>"
            }
          ],
          "questions": [
            {
              "id": "q_m_3",
              "level": "Kolay",
              "text": "(1/2 + 1/3) : (1/6) işleminin sonucu kaçtır?",
              "options": [
                "A) 2",
                "B) 3",
                "C) 5",
                "D) 6",
                "E) 1"
              ],
              "correct": 2,
              "solution": "Payda eşitle: (3/6 + 2/6) = 5/6. Bölme: (5/6) · (6/1) = 5."
            }
          ]
        },
        {
          "id": "mat_4",
          "title": "4. Üslü & Köklü İfadeler",
          "avgQuestions": "3 Soru",
          "summary": "Üslü denklem kuralları, negatif üs, köklü işlemlerde eşlenik çarpımı.",
          "keyPoints": [
            "aᵐ · aⁿ = aᵐ⁺ⁿ ve aᵐ / aⁿ = aᵐ⁻ⁿ.",
            "(a/b)⁻ⁿ = (b/a)ⁿ.",
            "Köklü eşlenik: (√a - √b) · (√a + √b) = a - b."
          ],
          "pages": [
            {
              "pageNo": "1",
              "pageTitle": "1. Bölüm: Üslü Sayı Kuralları ve Denklem Çözümleri",
              "text": "<div class=\"content-block\">\n  <h3>⚡ Üslü Sayı Özellikleri Tablosu</h3>\n  <ul>\n    <li><code>a⁰ = 1</code> (a ≠ 0), <code>a¹ = a</code></li>\n    <li><code>a⁻ⁿ = 1 / aⁿ</code> ve <code>(a/b)⁻ⁿ = (b/a)ⁿ</code></li>\n    <li><code>aᵐ · aⁿ = aᵐ⁺ⁿ</code> | <code>aᵐ / aⁿ = aᵐ⁻ⁿ</code></li>\n    <li><code>(aᵐ)ⁿ = aᵐ·ⁿ</code> | <code>(a · b)ⁿ = aⁿ · bⁿ</code></li>\n  </ul>\n\n  <div style=\"background:rgba(59,130,246,0.1); border-left:4px solid #3b82f6; padding:12px; margin:12px 0; border-radius:4px;\">\n    <b>Örnek Denklem Çözümü:</b> <code>3ˣ⁺² + 3ˣ⁺¹ + 3ˣ = 117</code> ise x kaçtır?<br>\n    <b>Adım 1 (Ortak Parantez):</b> <code>3ˣ · (3² + 3¹ + 1) = 117</code><br>\n    <b>Adım 2:</b> <code>3ˣ · (9 + 3 + 1) = 117</code> → <code>3ˣ · 13 = 117</code><br>\n    <b>Adım 3:</b> <code>3ˣ = 117 / 13 = 9</code> → <code>3ˣ = 3²</code> → <b>x = 2</b>\n  </div>\n</div>"
            },
            {
              "pageNo": "2",
              "pageTitle": "2. Bölüm: Köklü Sayılarda İşlemler ve Eşlenik",
              "text": "<div class=\"content-block\">\n  <h3>√ Köklü Sayı Özellikleri</h3>\n  <ul>\n    <li><code>√(a · b) = √a · √b</code> ve <code>√(a / b) = √a / √b</code></li>\n    <li><code>√(a² · b) = a√b</code> (Örn: <code>√72 = √(36·2) = 6√2</code>)</li>\n  </ul>\n\n  <h3>⚡ Eşlenik Çarpımı (Paydayı Rasyonel Yapma)</h3>\n  <ul>\n    <li><code>√a</code> ifadesinin eşleniği <code>√a</code>'dır → <code>√a · √a = a</code></li>\n    <li><code>(√a - √b)</code> ifadesinin eşleniği <code>(√a + √b)</code>'dir → <code>(√a - √b)(√a + √b) = a - b</code></li>\n  </ul>\n\n  <div style=\"background:rgba(16,185,129,0.1); border-left:4px solid #10b981; padding:12px; margin:12px 0; border-radius:4px;\">\n    <b>Örnek İşlem:</b> <code>6 / (√5 - √2)</code> kesrinin paydasını rasyonel yapalım:<br>\n    <b>Adım 1:</b> Payı ve paydayı <code>(√5 + √2)</code> ile çarp:<br>\n    <b>Adım 2:</b> Pay = <code>6 · (√5 + √2)</code><br>\n    <b>Adım 3:</b> Payda = <code>(√5)² - (√2)² = 5 - 2 = 3</code><br>\n    <b>Adım 4 (Sadeleştir):</b> <code>[6 · (√5 + √2)] / 3 = 2(√5 + √2) = 2√5 + 2√2</code>\n  </div>\n</div>"
            }
          ],
          "questions": [
            {
              "id": "q_m_4",
              "level": "Kolay",
              "text": "2^(x+1) = 16 olduğuna göre x kaçtır?",
              "options": [
                "A) 2",
                "B) 3",
                "C) 4",
                "D) 5",
                "E) 6"
              ],
              "correct": 1,
              "solution": "16 = 2⁴ olduğuna göre 2^(x+1) = 2⁴ => x + 1 = 4 => x = 3."
            }
          ]
        },
        {
          "id": "mat_5",
          "title": "5. Mutlak Değer & Basit Eşitsizlikler",
          "avgQuestions": "2 Soru",
          "summary": "Mutlak değer tanımı, mutlak değerli denklemler ve eşitsizlik çözüm aralıkları.",
          "keyPoints": [
            "|x| ≥ 0'dır (uzunluk negatif olamaz).",
            "Eşitsizlik her iki tarafı negatif bir sayıyla çarpılır veya bölünürse EŞİTSİZLİK YÖN DEĞİŞTİRİR.",
            "|x| < a ise -a < x < a (a > 0)."
          ],
          "pages": [
            {
              "pageNo": "1",
              "pageTitle": "1. Bölüm: Mutlak Değer Denklemleri ve Çözümleri",
              "text": "<div class=\"content-block\">\n  <h3>|x| Mutlak Değer Tanımı</h3>\n  <p><code>|x| = x (x ≥ 0 ise)</code> | <code>|x| = -x (x < 0 ise)</code></p>\n\n  <div style=\"background:rgba(59,130,246,0.1); border-left:4px solid #3b82f6; padding:12px; margin:12px 0; border-radius:4px;\">\n    <b>Örnek Denklem:</b> <code>|2x - 4| = 10</code> denkleminin çözüm kümesi nedir?<br>\n    <b>Durum 1:</b> <code>2x - 4 = 10</code> → <code>2x = 14</code> → <b>x = 7</b><br>\n    <b>Durum 2:</b> <code>2x - 4 = -10</code> → <code>2x = -6</code> → <b>x = -3</b><br>\n    <b>Çözüm Kümesi:</b> {-3, 7}\n  </div>\n</div>"
            },
            {
              "pageNo": "2",
              "pageTitle": "2. Bölüm: Eşitsizlik Kuralları ve Mutlak Eşitsizlikler",
              "text": "<div class=\"content-block\">\n  <h3>⚡ Basit Eşitsizlik Kuralları</h3>\n  <ul>\n    <li>Taraf tarafa toplama yapılabilir: <code>a < b</code> ve <code>c < d</code> ise <code>a + c < b + d</code>.</li>\n    <li><b>Önemli Kural:</b> Eşitsizlik <b>negatif bir sayı ile çarpılır veya bölünürse YÖN DEĞİŞTİRİR!</b><br>\n    Örn: <code>-3x < 12</code> (her tarafı -3'e böl) → <b>x > -4</b></li>\n  </ul>\n\n  <h3>⚡ Mutlak Değerli Eşitsizlik Kalıpları</h3>\n  <ul>\n    <li><code>|x| ≤ a</code> ise <code>-a ≤ x ≤ a</code></li>\n    <li><code>|x| ≥ a</code> ise <code>x ≥ a</code> veya <code>x ≤ -a</code></li>\n  </ul>\n\n  <div style=\"background:rgba(16,185,129,0.1); border-left:4px solid #10b981; padding:12px; margin:12px 0; border-radius:4px;\">\n    <b>Örnek Çözüm:</b> <code>|3x - 1| < 8</code> eşitsizliğini sağlayan x tam sayıları kaç tanedir?<br>\n    <b>Adım 1:</b> <code>-8 < 3x - 1 < 8</code><br>\n    <b>Adım 2 (Her tarafa +1 ekle):</b> <code>-7 < 3x < 9</code><br>\n    <b>Adım 3 (Her tarafı 3'e böl):</b> <code>-7/3 < x < 3</code> (yani -2.33 < x < 3)<br>\n    <b>Tam Sayı Değerleri:</b> {-2, -1, 0, 1, 2} → Toplam <b>5 tanedir</b>.\n  </div>\n</div>"
            }
          ],
          "questions": [
            {
              "id": "q_m_5",
              "level": "Orta",
              "text": "|x - 3| = 5 denklemini sağlayan x değerleri toplamı kaçtır?",
              "options": [
                "A) 4",
                "B) 6",
                "C) 8",
                "D) 10",
                "E) 12"
              ],
              "correct": 1,
              "solution": "x - 3 = 5 => x = 8 veya x - 3 = -5 => x = -2. Toplam = 8 + (-2) = 6."
            }
          ]
        },
        {
          "id": "mat_6",
          "title": "6. Çarpanlara Ayırma & Denklemler",
          "avgQuestions": "2 Soru",
          "summary": "İki kare farkı, tam kare açılımları, ax²+bx+c çarpanlara ayırma işlemleri.",
          "keyPoints": [
            "İki kare farkı: a² - b² = (a - b) · (a + b).",
            "Tam kare: (a + b)² = a² + 2ab + b² ve (a - b)² = a² - 2ab + b².",
            "x² + (m+n)x + m·n = (x + m)(x + n)."
          ],
          "pages": [
            {
              "pageNo": "1",
              "pageTitle": "1. Bölüm: Özdeşlikler ve Çarpanlara Ayırma Formülleri",
              "text": "<div class=\"content-block\">\n  <h3>⚡ Temel Özdeşlik Formülleri</h3>\n  <ul>\n    <li><b>İki Kare Farkı:</b> <code>a² - b² = (a - b) · (a + b)</code></li>\n    <li><b>Tam Kare:</b> <code>(a + b)² = a² + 2ab + b²</code></li>\n    <li><b>Tam Kare:</b> <code>(a - b)² = a² - 2ab + b²</code></li>\n    <li><b>Üç Terimli Çarpanlar:</b> <code>x² - 5x + 6 = (x - 2) · (x - 3)</code></li>\n  </ul>\n\n  <div style=\"background:rgba(59,130,246,0.1); border-left:4px solid #3b82f6; padding:12px; margin:12px 0; border-radius:4px;\">\n    <b>Örnek İşlem:</b> <code>(2025² - 2023²) / 4048</code> işleminin sonucu kaçtır?<br>\n    <b>Adım 1 (İki kare farkı uygula):</b> <code>(2025 - 2023) · (2025 + 2023) = 2 · 4048</code><br>\n    <b>Adım 2 (Sadeleştir):</b> <code>(2 · 4048) / 4048 = 2</code>\n  </div>\n</div>"
            }
          ],
          "questions": [
            {
              "id": "q_m_6",
              "level": "Kolay",
              "text": "x² - 9 = 0 denkleminin pozitif kökü kaçtır?",
              "options": [
                "A) 1",
                "B) 2",
                "C) 3",
                "D) 4",
                "E) 9"
              ],
              "correct": 2,
              "solution": "x² - 9 = (x - 3)(x + 3) = 0 => x = 3 veya x = -3. Pozitif kök = 3."
            }
          ]
        },
        {
          "id": "mat_7",
          "title": "7. Oran-Orantı & Problemler",
          "avgQuestions": "8-10 Soru",
          "summary": "Sayı-kesir, yaş, hız-zaman, yüzde, kâr-zarar ve karışım problemleri işlem kalıpları.",
          "keyPoints": [
            "Yaş problemlerinde iki kişi arasındaki YAŞ FARKI ASLA DEĞİŞMEZ.",
            "Yol = Hız × Zaman (x = V · t). Zıt yönlerde hızlar toplanır: x = (V₁ + V₂) · t.",
            "Yüzde hesaplarında bütüne 100x demek işlemleri çok kolaylaştırır."
          ],
          "pages": [
            {
              "pageNo": "1",
              "pageTitle": "1. Bölüm: Sayı, Kesir ve Yaş Problemleri",
              "text": "<div class=\"content-block\">\n  <h3>📐 Denklem Kurma Şablonları</h3>\n  <ul>\n    <li>Bir sayının 3 katının 5 fazlası: <code>3x + 5</code></li>\n    <li>Bir sayının 5 fazlasının 3 katı: <code>3 · (x + 5)</code></li>\n    <li>Bir sayının 2/5'i: <code>(2/5) · x = 2x / 5</code></li>\n  </ul>\n\n  <h3>⚡ Yaş Problemi Altın Kuralı</h3>\n  <p>Bugün yaşları x ve y olan iki kişinin t yıl sonraki yaşları (x+t) ve (y+t) olur. <b>Yaşları farkı (x - y) zaman geçse de ASLA DEĞİŞMEZ!</b></p>\n\n  <div style=\"background:rgba(59,130,246,0.1); border-left:4px solid #3b82f6; padding:12px; margin:12px 0; border-radius:4px;\">\n    <b>Örnek Yaş Problemi:</b> Bir babanın yaşı 40, oğlunun yaşı 10'dur. Kaç yıl sonra babanın yaşı oğlunun yaşının 3 katı olur?<br>\n    <b>Denklem:</b> t yıl sonra baba <code>40 + t</code>, oğul <code>10 + t</code> yaşında olur.<br>\n    <code>40 + t = 3 · (10 + t)</code><br>\n    <code>40 + t = 30 + 3t</code> → <code>40 - 30 = 3t - t</code> → <code>10 = 2t</code> → <b>t = 5 yıl</b>\n  </div>\n</div>"
            },
            {
              "pageNo": "2",
              "pageTitle": "2. Bölüm: Hız-Zaman ve Yüzde / Kâr-Zarar Problemleri",
              "text": "<div class=\"content-block\">\n  <h3>🚗 Hız - Yol - Zaman Formülleri</h3>\n  <ul>\n    <li><b>Temel Formül:</b> <code>Yol = Hız × Zaman</code> (<code>x = V · t</code>)</li>\n    <li><b>Zıt Yönlü Hareket (Birbirine Doğru):</b> <code>Yol = (V₁ + V₂) · t</code></li>\n    <li><b>Aynı Yönlü Hareket (Yetişme):</b> <code>Aralarındaki Mesafe = (V₁ - V₂) · t</code></li>\n  </ul>\n\n  <h3>💰 Yüzde ve Kâr-Zarar Formülleri</h3>\n  <ul>\n    <li>Maliyet fiyatına daima <b>100x</b> denir.</li>\n    <li>%20 Kâr ile satış: <code>100x + 20x = 120x</code></li>\n    <li>%30 Zarar ile satış: <code>100x - 30x = 70x</code></li>\n  </ul>\n\n  <div style=\"background:rgba(16,185,129,0.1); border-left:4px solid #10b981; padding:12px; margin:12px 0; border-radius:4px;\">\n    <b>Örnek Kâr Problemi:</b> Bir ürün %20 kârla 240 TL'ye satılmaktadır. Bu ürünün maliyeti kaç TL'dir?<br>\n    <b>Adım 1:</b> Maliyet = <code>100x</code> olsun. %20 karlı satış = <code>120x</code>.<br>\n    <b>Adım 2:</b> <code>120x = 240</code> → <code>x = 2</code><br>\n    <b>Adım 3:</b> Maliyet = <code>100x = 100 · 2 = 200 TL</code>\n  </div>\n</div>"
            }
          ],
          "questions": [
            {
              "id": "q_m_7",
              "level": "Orta",
              "text": "Bir babanın yaşı 40, oğlunun yaşı 10'dur. Kaç yıl sonra babanın yaşı oğlunun yaşının 3 katı olur?",
              "options": [
                "A) 3",
                "B) 4",
                "C) 5",
                "D) 6",
                "E) 7"
              ],
              "correct": 2,
              "solution": "40 + t = 3(10 + t) => 40 + t = 30 + 3t => 2t = 10 => t = 5 yıl."
            }
          ]
        },
        {
          "id": "mat_8",
          "title": "8. Kümeler & Mantık",
          "avgQuestions": "2 Soru",
          "summary": "Küme işlemleri formülleri, Venn şemaları ve önerme doğruluk tabloları.",
          "keyPoints": [
            "s(A ∪ B) = s(A) + s(B) - s(A ∩ B).",
            "n elemanlı kümenin alt küme sayısı 2ⁿ formülüyle bulunur.",
            "p ⇒ q ≡ p' ∨ q (ise bağlacının veya karşılığı)."
          ],
          "pages": [
            {
              "pageNo": "1",
              "pageTitle": "1. Bölüm: Kümelerde İşlemler ve Eleman Sayısı",
              "text": "<div class=\"content-block\">\n  <h3>⚡ Kümeler Formülleri</h3>\n  <ul>\n    <li><b>Birleşim Eleman Sayısı:</b> <code>s(A ∪ B) = s(A) + s(B) - s(A ∩ B)</code></li>\n    <li><b>Alt Küme Sayısı:</b> n elemanlı küme için <code>2ⁿ</code></li>\n    <li><b>Öz Alt Küme Sayısı:</b> <code>2ⁿ - 1</code></li>\n  </ul>\n\n  <div style=\"background:rgba(59,130,246,0.1); border-left:4px solid #3b82f6; padding:12px; margin:12px 0; border-radius:4px;\">\n    <b>Örnek İşlem:</b> <code>s(A) = 10</code>, <code>s(B) = 8</code> ve <code>s(A ∩ B) = 3</code> olduğuna göre <code>s(A ∪ B)</code> kaçtır?<br>\n    <b>Hesap:</b> <code>s(A ∪ B) = 10 + 8 - 3 = 15</code>\n  </div>\n</div>"
            }
          ],
          "questions": [
            {
              "id": "q_m_8",
              "level": "Kolay",
              "text": "s(A)=10, s(B)=8, s(A ∩ B)=3 ise s(A U B) kaçtır?",
              "options": [
                "A) 13",
                "B) 15",
                "C) 18",
                "D) 21",
                "E) 25"
              ],
              "correct": 1,
              "solution": "s(A U B) = 10 + 8 - 3 = 15."
            }
          ]
        },
        {
          "id": "mat_9",
          "title": "9. Sayısal Mantık & Grafik Okuma",
          "avgQuestions": "3 Soru",
          "summary": "Daire, sütun ve çizgi grafikleri açı-yüzde orantı hesaplamaları.",
          "keyPoints": [
            "Daire grafiğinin tamamı 360° ve %100'dür.",
            "Açı hesabı: Derece = (Miktar / Toplam) × 360°.",
            "Mod: En çok tekrar eden değer. Medyan: Sıralı dizide ortadaki değer."
          ],
          "pages": [
            {
              "pageNo": "1",
              "pageTitle": "1. Bölüm: Daire ve Sütun Grafiği Orantı Hesapları",
              "text": "<div class=\"content-block\">\n  <h3>📊 Daire Grafiğinde Açı ve Yüzde Orantısı</h3>\n  <p>Daire grafiğinde tüm verilerin toplamı <b>360°</b> merkez açıya karşılık gelir.</p>\n\n  <div style=\"background:rgba(59,130,246,0.1); border-left:4px solid #3b82f6; padding:12px; margin:12px 0; border-radius:4px;\">\n    <b>Örnek Hesaplama:</b> Bir çiftlikteki 720 hayvanın 180 tanesi koyundur. Bu veri daire grafiğinde kaç derecelik açı ile gösterilir?<br>\n    <b>Orantı:</b><br>\n    <code>720 hayvan ─── 360°</code><br>\n    <code>180 hayvan ─── x°</code><br>\n    <b>İçler-Dışlar:</b> <code>x = (180 × 360) / 720 = 360 / 4 = 90°</code>\n  </div>\n</div>"
            }
          ],
          "questions": [
            {
              "id": "q_m_9",
              "level": "Orta",
              "text": "360 derecelik daire grafiğinde %25'lik dilim kaç derecedir?",
              "options": [
                "A) 45°",
                "B) 60°",
                "C) 90°",
                "D) 120°",
                "E) 180°"
              ],
              "correct": 2,
              "solution": "360° · (25/100) = 360° / 4 = 90°."
            }
          ]
        },
        {
          "id": "mat_10",
          "title": "10. Temel Geometri (Açılar, Üçgenler, Çevre-Alan)",
          "avgQuestions": "3 Soru",
          "summary": "Üçgende açılar, Pisagor bağıntısı, özel dik üçgen katları ve alan formülleri.",
          "keyPoints": [
            "Üçgenin iç açıları toplamı 180°, dış açıları toplamı 360°'dir.",
            "Özel kenarlı dik üçgenler: 3-4-5, 5-12-13, 8-15-17, 7-24-25.",
            "30°-60°-90° üçgeninde: 90° karşısı 2a ise 30° karşısı a, 60° karşısı a√3'tür."
          ],
          "pages": [
            {
              "pageNo": "1",
              "pageTitle": "1. Bölüm: Üçgende Açılar ve Pisagor Bağıntısı",
              "text": "<div class=\"content-block\">\n  <h3>📐 Açı Kuralları</h3>\n  <ul>\n    <li>Üçgenin iç açıları toplamı: <b>180°</b></li>\n    <li>Üçgende bir dış açı, kendisine komşu olmayan iki iç açının toplamına eşittir (<b>2 iç = 1 dış</b>).</li>\n  </ul>\n\n  <h3>⚡ Pisagor Teoremi: <code>a² + b² = c²</code></h3>\n  <table style=\"width:100%; border-collapse:collapse; margin:12px 0;\">\n    <tr style=\"background:#1e293b;\"><th style=\"padding:8px; border:1px solid #334155;\">Özel Üçgen</th><th style=\"padding:8px; border:1px solid #334155;\">Katları (Kenarlar)</th><th style=\"padding:8px; border:1px solid #334155;\">Örnek</th></tr>\n    <tr><td style=\"padding:6px; border:1px solid #334155;\"><b>3 - 4 - 5</b></td><td style=\"padding:6px; border:1px solid #334155;\">3k, 4k, 5k</td><td style=\"padding:6px; border:1px solid #334155;\">6-8-10, 9-12-15, 12-16-20</td></tr>\n    <tr><td style=\"padding:6px; border:1px solid #334155;\"><b>5 - 12 - 13</b></td><td style=\"padding:6px; border:1px solid #334155;\">5k, 12k, 13k</td><td style=\"padding:6px; border:1px solid #334155;\">10-24-26</td></tr>\n    <tr><td style=\"padding:6px; border:1px solid #334155;\"><b>8 - 15 - 17</b></td><td style=\"padding:6px; border:1px solid #334155;\">8k, 15k, 17k</td><td style=\"padding:6px; border:1px solid #334155;\">16-30-34</td></tr>\n    <tr><td style=\"padding:6px; border:1px solid #334155;\"><b>7 - 24 - 25</b></td><td style=\"padding:6px; border:1px solid #334155;\">7k, 24k, 25k</td><td style=\"padding:6px; border:1px solid #334155;\">14-48-50</td></tr>\n  </table>\n</div>"
            },
            {
              "pageNo": "2",
              "pageTitle": "2. Bölüm: Özel Açılı Üçgenler ve Alan Formülleri",
              "text": "<div class=\"content-block\">\n  <h3>⚡ Özel Açılı Dik Üçgenler</h3>\n  <ul>\n    <li><b>30° - 60° - 90° Üçgeni:</b> 90°'nin karşısı <code>2a</code> ise, 30°'nin karşısı <code>a</code>, 60°'nin karşısı <code>a√3</code>'tür.</li>\n    <li><b>45° - 45° - 90° Üçgeni:</b> Dik kenarlar <code>a</code> ve <code>a</code> ise hipotenüs <code>a√2</code>'dir.</li>\n  </ul>\n\n  <h3>📐 Temel Alan Formülleri</h3>\n  <ul>\n    <li><b>Üçgen Alanı:</b> <code>Alan = (Taban × Yükseklik) / 2 = (a · hₐ) / 2</code></li>\n    <li><b>Dik Üçgen Alanı:</b> <code>Alan = (Dik Kenar 1 × Dik Kenar 2) / 2</code></li>\n    <li><b>Dikdörtgen Alanı:</b> <code>Alan = a · b</code> | <b>Kare Alanı:</b> <code>Alan = a²</code></li>\n  </ul>\n</div>"
            }
          ],
          "questions": [
            {
              "id": "q_m_10",
              "level": "Kolay",
              "text": "Dik kenar uzunlukları 6 cm ve 8 cm olan bir dik üçgenin hipotenüs uzunluğu kaç cm'dir?",
              "options": [
                "A) 8",
                "B) 10",
                "C) 12",
                "D) 14",
                "E) 15"
              ],
              "correct": 1,
              "solution": "3-4-5 özel üçgeninin 2 katı olan 6-8-10 üçgenidir. Hipotenüs = 10 cm."
            }
          ]
        }
      ]
    },
    {
      "id": "turkce",
      "name": "Türkçe",
      "icon": "📚",
      "color": "#ec4899",
      "questionCount": 30,
      "description": "Sözcük, Cümle, Paragrafta Anlam, Dil Bilgisi ve Sözel Mantık",
      "topics": [
        {
          "id": "turk_1",
          "title": "1. Sözcükte Anlam, Mecaz & Deyimler",
          "avgQuestions": "3-4 Soru",
          "summary": "Gerçek, mecaz, yan ve terim anlam; eş-zıt anlamlılar, dolaylama ve kalıplaşmış deyimler.",
          "keyPoints": [
            "Mecaz anlam, sözcüğün ilk/somut anlamından tamamen uzaklaşarak kazandığı soyut anlamdır.",
            "Deyimler kalıplaşmıştır; kelimeleri değiştirilemez, eş anlamlıları dahi konamaz."
          ],
          "pages": [
            {
              "pageNo": "1",
              "pageTitle": "1. Bölüm: Anlam Çeşitleri (Gerçek, Yan, Mecaz, Terim)",
              "text": "<div class=\"content-block\">\n  <h3>📚 Sözcükte Anlam Türleri</h3>\n  <ul>\n    <li><b>Gerçek (Temel) Anlam:</b> Sözcüğün akla gelen ilk, somut anlamıdır. <i>(Örn: 'Sobanın <u>sıcak</u> yüzeyine dokundu.')</i></li>\n    <li><b>Yan Anlam:</b> Gerçek anlama şekil veya işlev olarak benzerlik yoluyla kazandığı yeni anlamdır. <i>(Örn: 'Kapının <u>kolu</u> kırıldı.')</i></li>\n    <li><b>Mecaz Anlam:</b> Gerçek anlamından tamamen uzaklaşarak kazandığı soyut anlamdır. <i>(Örn: 'Bize çok <u>sıcak</u> davrandı.')</i></li>\n    <li><b>Terim Anlam:</b> Bilim, sanat, spor veya meslek dalına özgü özel kavramlardır. <i>(Örn: 'Üçgenin <u>hipotenüs</u> uzunluğu', 'Hücredeki <u>mitokondri</u>')</i></li>\n  </ul>\n</div>"
            },
            {
              "pageNo": "2",
              "pageTitle": "2. Bölüm: Deyimler, Atasözleri ve Söz Sanatları",
              "text": "<div class=\"content-block\">\n  <h3>✨ Deyimler ve Özellikleri</h3>\n  <ul>\n    <li>En az iki kelimeden oluşur ve genellikle mecaz anlamlıdır.</li>\n    <li>Kalıplaşmıştır: <i>'Gözden düşmek'</i> yerine <i>'bakıştan düşmek'</i> denemez.</li>\n    <li>Genel kural ve öğüt vermezler; anlık durumları bildirirler. (Öğüt verenler Atasözüdür).</li>\n  </ul>\n\n  <h3>🎨 Söz Sanatları</h3>\n  <ul>\n    <li><b>Teşbih (Benzetme):</b> Aralarında ilgi bulunan iki şeyden zayıf olanın güçlü olana benzetilmesidir.</li>\n    <li><b>Teşhis (Kişileştirme):</b> İnsana ait özelliklerin insan dışı varlıklara verilmesidir. <i>(Örn: 'Rüzgar hüzünle fısıldıyordu.')</i></li>\n    <li><b>Tezat (Karşıtlık):</b> Zıt kavramların bir arada kullanılmasıdır. <i>(Örn: 'Ağlarım hatıra geldikçe gülüştüklerimiz.')</i></li>\n  </ul>\n</div>"
            }
          ],
          "questions": [
            {
              "id": "q_t_1",
              "level": "Kolay",
              "text": "Aşağıdaki cümlelerin hangisinde <u>altı çizili</u> sözcük mecaz anlamda kullanılmıştır?",
              "options": [
                "A) Sınıfın en <u>ağır</u> çantası onundu.",
                "B) Bu haber herkesi <u>ağır</u> bir şekilde etkiledi.",
                "C) <u>Ağır</u> yükleri taşımak zordu.",
                "D) Valizini tartıya koyup <u>ağırlığına</u> baktı.",
                "E) <u>Ağır</u> demir kapıyı zorlukla açtı."
              ],
              "correct": 1,
              "solution": "B şıkkında <u>ağır</u> kelimesi 'üzücü, derinden sarsıcı' anlamında mecazdır."
            }
          ]
        },
        {
          "id": "turk_2",
          "title": "2. Cümlede Anlam & Kavramlar",
          "avgQuestions": "3-4 Soru",
          "summary": "Öznel-nesnel yargılar, neden-sonuç, amaç-sonuç, koşul-sonuç ve örtülü anlam.",
          "keyPoints": [
            "Neden-sonuçta eylem gerçekleşmiştir (-dığı için).",
            "Amaç-sonuçta eylem henüz bir hedeftir (-mak amacıyla).",
            "Nesnel yargılar kişiden kişiye değişmeyen, kanıtlanabilir ifadelerdir."
          ],
          "pages": [
            {
              "pageNo": "1",
              "pageTitle": "1. Bölüm: Anlam İlişkileri ve Yargı Türleri",
              "text": "<div class=\"content-block\">\n  <h3>⚡ Cümle İlişkileri Karşılaştırma Tablosu</h3>\n  <table style=\"width:100%; border-collapse:collapse; margin:12px 0;\">\n    <tr style=\"background:#1e293b;\"><th style=\"padding:8px; border:1px solid #334155;\">İlişki Türü</th><th style=\"padding:8px; border:1px solid #334155;\">Formül / Anahtar Kelime</th><th style=\"padding:8px; border:1px solid #334155;\">Örnek Cümle</th></tr>\n    <tr><td style=\"padding:6px; border:1px solid #334155;\"><b>Neden-Sonuç</b></td><td style=\"padding:6px; border:1px solid #334155;\">-dığı için, nedeniyle (Gerekçe gerçekleşmiş)</td><td style=\"padding:6px; border:1px solid #334155;\">Kar yağdığı için yollar kapandı.</td></tr>\n    <tr><td style=\"padding:6px; border:1px solid #334155;\"><b>Amaç-Sonuç</b></td><td style=\"padding:6px; border:1px solid #334155;\">-mak için, amacıyla (Hedef belirlenmiş)</td><td style=\"padding:6px; border:1px solid #334155;\">Sınavı kazanmak için çok çalışıyor.</td></tr>\n    <tr><td style=\"padding:6px; border:1px solid #334155;\"><b>Koşul-Sonuç</b></td><td style=\"padding:6px; border:1px solid #334155;\">-se/-sa, şartıyla (Koşula bağlı)</td><td style=\"padding:6px; border:1px solid #334155;\">Erken kalkarsan yetişirsin.</td></tr>\n    <tr><td style=\"padding:6px; border:1px solid #334155;\"><b>Öznel Yargı</b></td><td style=\"padding:6px; border:1px solid #334155;\">Kişisel beğeni / yorum içerir</td><td style=\"padding:6px; border:1px solid #334155;\">Yazarın harika bir üslubu var.</td></tr>\n    <tr><td style=\"padding:6px; border:1px solid #334155;\"><b>Nesnel Yargı</b></td><td style=\"padding:6px; border:1px solid #334155;\">Kanıtlanabilir, yoruma kapalı</td><td style=\"padding:6px; border:1px solid #334155;\">Kitap 240 sayfadan oluşuyor.</td></tr>\n  </table>\n</div>"
            }
          ],
          "questions": [
            {
              "id": "q_t_2",
              "level": "Kolay",
              "text": "Aşağıdaki cümlelerin hangisinde <u>nesnel</u> bir anlatım vardır?",
              "options": [
                "A) Şairin son şiir kitabı okuyucuyu büyülüyor.",
                "B) Eser 1923 yılında İstanbul'da basılmıştır.",
                "C) Romanın dili son derece tatlıdır.",
                "D) Yazar en güzel öykülerini bu kentte yazdı.",
                "E) Resimdeki canlı renkler tabloya eşsiz hava katmış."
              ],
              "correct": 1,
              "solution": "B şıkkı kanıtlanabilir, kişisel yorum içermeyen nesnel bir veridir."
            }
          ]
        },
        {
          "id": "turk_3",
          "title": "3. Paragrafta Anlam & Ana Düşünce",
          "avgQuestions": "10-12 Soru",
          "summary": "Paragraf ana fikri, yardımcı düşünceler, başlık ve paragraf tamamlama teknikleri.",
          "keyPoints": [
            "Önce soru kökü, sonra seçenekler göz ucuyla, en son paragraf okunmalıdır.",
            "Ana düşünce genellikle paragrafın giriş veya sonuç cümlesinde toparlanır."
          ],
          "pages": [
            {
              "pageNo": "1",
              "pageTitle": "1. Bölüm: Paragraf Çözme Teknikleri ve Stratejiler",
              "text": "<div class=\"content-block\">\n  <h3>📖 KPSS Paragraf Çözüm Adımları</h3>\n  <ol>\n    <li><b>1. Adım:</b> Daima önce soru kökünü okuyun ve ne aradığınızı bilin (<i>'değinilmemiştir', 'çıkarılamaz', 'asıl anlatılmak istenen'</i>).</li>\n    <li><b>2. Adım:</b> Ana düşünce sorularında metnin bütününe <i>'Yazar bu metni bana hangi mesajı vermek için yazdı?'</i> sorusunu yöneltin.</li>\n    <li><b>3. Adım:</b> 'Oysa, fakat, ancak, kısacası, demek ki, asıl önemli olan' gibi bağlaçlardan sonraki cümleler genellikle ANA FİKRİ barındırır.</li>\n  </ol>\n</div>"
            }
          ],
          "questions": [
            {
              "id": "q_t_3",
              "level": "Orta",
              "text": "Paragrafta <u>ana düşünce</u> hangisidir?",
              "options": [
                "A) Yazarın okuyucuya iletmek istediği temel mesaj",
                "B) İkinci cümledeki yan detay",
                "C) Örnekleme yapılan kavramlar",
                "D) Metindeki sayısal veriler",
                "E) Yan düşünceler"
              ],
              "correct": 0,
              "solution": "Ana düşünce yazarın okuyucuya vermek istediği temel iletidir."
            }
          ]
        },
        {
          "id": "turk_4",
          "title": "4. Paragraf Yapısı & Akışı Bozan Cümle",
          "avgQuestions": "4-5 Soru",
          "summary": "Paragrafı ikiye bölme, akışı bozan cümleyi tespit etme ve cümle sıralama kuralları.",
          "keyPoints": [
            "Akışı bozan cümle, konunun farklı bir yönüne geçen veya anlatım bütünlüğünü bozan cümledir.",
            "Yeni bir paragrafa geçiş cümlesi kendinden önceye gönderme yapan bağlaçlarla başlayamaz."
          ],
          "pages": [
            {
              "pageNo": "1",
              "pageTitle": "1. Bölüm: Paragraf Yapısı ve Akış Bozan Cümleler",
              "text": "<div class=\"content-block\">\n  <h3>⚡ Paragraf Yapısı Kuralları</h3>\n  <ul>\n    <li><b>Giriş Cümlesi:</b> Kendinden önce bir cümle varmış hissi vermez. <i>'Bu nedenle, oysa, çünkü, bundan dolayı'</i> gibi bağlaçlarla başlayamaz.</li>\n    <li><b>Akışı Bozan Cümle:</b> Paragrafın ana konusundan farklı bir yöne sapan, konunun dışına çıkan cümledir. Bu cümle çıkarıldığında paragrafın anlam akışı düzelir.</li>\n    <li><b>İkiye Bölme:</b> Konunun yeni ve farklı bir boyutuna geçildiği cümle ikinci paragrafın ilk cümlesi olur.</li>\n  </ul>\n</div>"
            }
          ],
          "questions": [
            {
              "id": "q_t_4",
              "level": "Orta",
              "text": "Bir paragrafta akışı bozan cümle nasıl tespit edilir?",
              "options": [
                "A) Konunun bütünlüğünden sapan cümle elenerek",
                "B) İlk cümle seçilerek",
                "C) En uzun cümle seçilerek",
                "D) Yüklemi fiil olan cümle seçilerek",
                "E) Tırnak içindeki cümle seçilerek"
              ],
              "correct": 0,
              "solution": "Paragrafın ana temasından sapan veya farklı konudan bahseden cümle akışı bozar."
            }
          ]
        },
        {
          "id": "turk_5",
          "title": "5. Ses Bilgisi & TDK Yazım Kuralları",
          "avgQuestions": "3 Soru",
          "summary": "Ünlü düşmesi, ünsüz sertleşmesi, yumuşama; büyük harfler, ayrı ve bitişik yazılanlar.",
          "keyPoints": [
            "'Şey' sözcüğü her zaman ayrı yazılır: her şey, bir şey.",
            "Kurum, kuruluş adlarına gelen ekler kesme işaretiyle AYRILMAZ (TDK'nin, TBMM'ye hariç: Türk Dil Kurumuna).",
            "Fıstıkçı Şahap sert ünsüzlerinden sonra c, d, g ile başlayan ek gelirse ç, t, k'ye dönüşür (Sertleşme/Benzeşme)."
          ],
          "pages": [
            {
              "pageNo": "1",
              "pageTitle": "1. Bölüm: Ses Olayları Tablosu",
              "text": "<div class=\"content-block\">\n  <h3>⚡ Temel Ses Olayları Tablosu</h3>\n  <table style=\"width:100%; border-collapse:collapse; margin:12px 0;\">\n    <tr style=\"background:#1e293b;\"><th style=\"padding:8px; border:1px solid #334155;\">Ses Olayı</th><th style=\"padding:8px; border:1px solid #334155;\">Açıklama</th><th style=\"padding:8px; border:1px solid #334155;\">Örnekler</th></tr>\n    <tr><td style=\"padding:6px; border:1px solid #334155;\"><b>Ünlü Düşmesi</b></td><td style=\"padding:6px; border:1px solid #334155;\">İkinci hecedeki dar ünlünün düşmesi</td><td style=\"padding:6px; border:1px solid #334155;\">akıl - ı → <b>aklı</b>, burun - u → <b>burnu</b></td></tr>\n    <tr><td style=\"padding:6px; border:1px solid #334155;\"><b>Ünsüz Yumuşaması</b></td><td style=\"padding:6px; border:1px solid #334155;\">p, ç, t, k seslerinin b, c, d, ğ olması</td><td style=\"padding:6px; border:1px solid #334155;\">kitap - ı → <b>kitabı</b>, sokak - a → <b>sokağa</b></td></tr>\n    <tr><td style=\"padding:6px; border:1px solid #334155;\"><b>Ünsüz Sertleşmesi</b></td><td style=\"padding:6px; border:1px solid #334155;\">F-S-T-K-Ç-Ş-H-P sonrasına c-d-g yerine ç-t-k gelmesi</td><td style=\"padding:6px; border:1px solid #334155;\">sınıf - da → <b>sınıfta</b>, 1923 - de → <b>1923'te</b></td></tr>\n    <tr><td style=\"padding:6px; border:1px solid #334155;\"><b>Ünlü Daralması</b></td><td style=\"padding:6px; border:1px solid #334155;\">-yor ekinin a, e geniş ünlülerini ı, i, u, ü yapması</td><td style=\"padding:6px; border:1px solid #334155;\">başla - yor → <b>başlıyor</b>, bekle - yor → <b>bekliyor</b></td></tr>\n  </table>\n</div>"
            },
            {
              "pageNo": "2",
              "pageTitle": "2. Bölüm: TDK Yazım Kuralları ve Sık Yapılan Hatalar",
              "text": "<div class=\"content-block\">\n  <h3>✍️ Sık Karıştırılan Yazımlar Rehberi</h3>\n  <ul>\n    <li><b>Ayrı Yazılanlar:</b> Her şey, bir şey, pek çok, hiçbir şey, yanı sıra, peşi sıra, yüz üstü (somutsa).</li>\n    <li><b>Bitişik Yazılanlar:</b> Birkaç, hiçbir, birtakım (belgisizse), affetmek, kaybolmak, sivrisinek, kuşburnu.</li>\n    <li><b>'de' ve 'ki' Yazımı:</b> Cümleden çıkarıldığında anlam bozulmuyorsa bağlaçtır ve AYRI yazılır.</li>\n  </ul>\n</div>"
            }
          ],
          "questions": [
            {
              "id": "q_t_5",
              "level": "Kolay",
              "text": "Aşağıdakilerin hangisinde bir <u>yazım yanlışı</u> vardır?",
              "options": [
                "A) Her şey yolunda gidiyor.",
                "B) Birşey söylemeden odadan çıktı.",
                "C) Kaybolan eşyalarını aradı.",
                "D) TBMM'nin kararları açıklandı.",
                "E) Pek çok öğrenci sınava girdi."
              ],
              "correct": 1,
              "solution": "'Birşey' yanlış yazılmıştır, 'Bir şey' şeklinde daima ayrı yazılmalıdır."
            }
          ]
        },
        {
          "id": "turk_6",
          "title": "6. Noktalama İşaretleri",
          "avgQuestions": "2 Soru",
          "summary": "Nokta, virgül, noktalı virgül, iki nokta ve kesme işaretlerinin kuralları.",
          "keyPoints": [
            "Tekrarlı bağlaçlardan (ya... ya, hem... hem, ne... ne) önce ve sonra virgül KONMAZ.",
            "Şart ekinden (-se/-sa) ve zarf-fiil ekinden (-ip, -erek tek başınaysa) sonra virgül KONMAZ.",
            "Noktalı virgül (;) kullanmak için cümlede önceden en az bir virgül (,) bulunması şarttır."
          ],
          "pages": [
            {
              "pageNo": "1",
              "pageTitle": "1. Bölüm: Virgül ve Noktalı Virgül Kuralları",
              "text": "<div class=\"content-block\">\n  <h3>⚡ Virgülün (,) Kullanıldığı ve KULLANILMADIĞI Yerler</h3>\n  <ul>\n    <li><b>Kullanılır:</b> Eş görevli kelimeleri ayırmada, sıralı cümleleri ayırmada, hitaplardan sonra.</li>\n    <li><b>KESİNLİKLE KULLANILMAZ:</b>\n      <ul>\n        <li>Bağlaçlardan önce ve sonra (<i>ve, veya, ya... ya, hem... hem</i>).</li>\n        <li>Şart ekinden sonra (<i>'Gelirse, konuşuruz' YANLIŞTIR → 'Gelirse konuşuruz'</i>).</li>\n        <li>Metin içinde tek başına kullanılan zarf-fiilden sonra (<i>'Koşarak, gitti' YANLIŞTIR</i>).</li>\n      </ul>\n    </li>\n  </ul>\n\n  <h3>⚡ Noktalı Virgül (;) ve İki Nokta (:) Farkı</h3>\n  <ul>\n    <li><b>İki Nokta (:):</b> Kendisinden sonra açıklama yapılacak veya örnek verilecek cümlelerin sonuna konur.</li>\n    <li><b>Noktalı Virgül (;):</b> İçinde virgülle ayrılmış tür veya takımları ayırmak için kullanılır. <i>(Örn: Erkeklere Ahmet, Mehmet; kızlara Ayşe, Fatma adı verildi.)</i></li>\n  </ul>\n</div>"
            }
          ],
          "questions": [
            {
              "id": "q_t_6",
              "level": "Kolay",
              "text": "Aşağıdaki cümlelerin hangisinde <u>virgül</u> yanlış kullanılmıştır?",
              "options": [
                "A) Ali, Veli ve Mehmet geldiler.",
                "B) Ya bu deveyi gütmeli, ya bu diyardan gitmeli.",
                "C) Kitapları, defterleri masaya koydu.",
                "D) Evet, ben de sana katılıyorum.",
                "E) Sayın Başkan, değerli üyeler..."
              ],
              "correct": 1,
              "solution": "Tekrarlı bağlaçlar (ya... ya...) arasında virgül kullanılmaz."
            }
          ]
        },
        {
          "id": "turk_7",
          "title": "7. Dil Bilgisi (Sözcük Türleri, Ögeler, Çatı)",
          "avgQuestions": "3 Soru",
          "summary": "İsim, sıfat, zamir, zarf, edat-bağlaç; cümlenin temel ve yardımcı ögeleri.",
          "keyPoints": [
            "Cümlenin temel ögeleri Yüklem ve Öznedir.",
            "Özneye sorulan 'Ne, Kim' sorusudur. Belirtili nesneye 'Neyi, Kimi' sorulur.",
            "Sıfatlar ismi niteler/belirtir; Zarflar fiili, sıfatı veya zarfı derecelendirir."
          ],
          "pages": [
            {
              "pageNo": "1",
              "pageTitle": "1. Bölüm: Cümlenin Ögeleri Bulma Tablosu",
              "text": "<div class=\"content-block\">\n  <h3>⚡ Cümle Ögeleri ve Soru Kalıpları</h3>\n  <table style=\"width:100%; border-collapse:collapse; margin:12px 0;\">\n    <tr style=\"background:#1e293b;\"><th style=\"padding:8px; border:1px solid #334155;\">Öge</th><th style=\"padding:8px; border:1px solid #334155;\">Yükleme Sorulan Soru</th><th style=\"padding:8px; border:1px solid #334155;\">Örnek Cümle Analizi</th></tr>\n    <tr><td style=\"padding:6px; border:1px solid #334155;\"><b>Özne</b></td><td style=\"padding:6px; border:1px solid #334155;\">Yapan kim? Olan ne?</td><td style=\"padding:6px; border:1px solid #334155;\"><u>Sarı yapraklar</u> yere düştü.</td></tr>\n    <tr><td style=\"padding:6px; border:1px solid #334155;\"><b>Belirtili Nesne</b></td><td style=\"padding:6px; border:1px solid #334155;\">Neyi? Kimi?</td><td style=\"padding:6px; border:1px solid #334155;\">Ahmet <u>kapıyı</u> açtı.</td></tr>\n    <tr><td style=\"padding:6px; border:1px solid #334155;\"><b>Belirtisiz Nesne</b></td><td style=\"padding:6px; border:1px solid #334155;\">Ne? (Özneden sonraki)</td><td style=\"padding:6px; border:1px solid #334155;\">Pazardan <u>elma</u> aldı.</td></tr>\n    <tr><td style=\"padding:6px; border:1px solid #334155;\"><b>Dolaylı Tümleç</b></td><td style=\"padding:6px; border:1px solid #334155;\">Nereye? Nerede? Nereden? Kime?</td><td style=\"padding:6px; border:1px solid #334155;\">Çocuklar <u>bahçede</u> oynuyor.</td></tr>\n    <tr><td style=\"padding:6px; border:1px solid #334155;\"><b>Zarf Tümleci</b></td><td style=\"padding:6px; border:1px solid #334155;\">Nasıl? Ne zaman? Ne kadar? Niçin?</td><td style=\"padding:6px; border:1px solid #334155;\">Otobüs <u>saat onda</u> gelecek.</td></tr>\n  </table>\n</div>"
            }
          ],
          "questions": [
            {
              "id": "q_t_7",
              "level": "Orta",
              "text": "<u>Sarı yapraklar</u> rüzgarda savruluyordu cümlesinde altı çizili öge nedir?",
              "options": [
                "A) Özne",
                "B) Belirtili Nesne",
                "C) Zarf Tümleci",
                "D) Dolaylı Tümleç",
                "E) Yüklem"
              ],
              "correct": 0,
              "solution": "Savrulan ne? Sarı yapraklar -> Eylemi yapan/olan unsurdur, Öznedir."
            }
          ]
        },
        {
          "id": "turk_8",
          "title": "8. Sözel Mantık Bulmacaları & Tablo Kurma",
          "avgQuestions": "4 Soru",
          "summary": "Sözel mantık soru kalıpları, sabit değişkenle tablo oluşturma ve kesinlik analizi.",
          "keyPoints": [
            "Sözel mantıkta değişmeyen unsurlar (günler, katlar, sıralar) tablo başlığı yapılır.",
            "Kesin bilgiler doğrudan tabloya işlenir; olasılıklar parantez içi/ok ile gösterilir."
          ],
          "pages": [
            {
              "pageNo": "1",
              "pageTitle": "1. Bölüm: Sözel Mantık Çözüm Metotları",
              "text": "<div class=\"content-block\">\n  <h3>🧩 Sözel Mantık Çözüm Adımları</h3>\n  <ol>\n    <li><b>1. Adım (Sabiti Belirle):</b> Günler (Pzt, Salı...), Saatler, Katlar (1, 2, 3, 4) gibi sabitleri tablonun üst sütun başlıklarına yazın.</li>\n    <li><b>2. Adım (Kesin Bilgileri Yerleştir):</b> 'Ali 3. kattadır' gibi kesin hükümleri doğrudan tabloya yazın.</li>\n    <li><b>3. Adım (Bağlantılı Öncülleri Kullan):</b> 'Ahmet, Mehmet'ten hemen sonraki gündür' kalıbını blok olarak tabloya deneyin.</li>\n    <li><b>4. Adım (Kalanları Dağıt):</b> Seçeneklerde 'kesinlikle doğrudur/yanlıştır' soruları tablodaki sabit veya çelişen yerlerden çözülür.</li>\n  </ol>\n</div>"
            }
          ],
          "questions": [
            {
              "id": "q_t_8",
              "level": "Zor",
              "text": "Sözel mantık sorularını çözerken ilk yapılması gereken en doğru hamle nedir?",
              "options": [
                "A) Sabit değişkenleri belirleyip tablo kurmak",
                "B) Doğrudan şıklardan eleme yapmak",
                "C) Tahminde bulunmak",
                "D) Soruyu boş bırakmak",
                "E) Sadece son öncülü okumak"
              ],
              "correct": 0,
              "solution": "Değişmeyen sabit unsurlarla tablo kurmak sözel mantığın temelidir."
            }
          ]
        }
      ]
    },
    {
      "id": "tarih",
      "name": "Tarih",
      "icon": "🏛️",
      "color": "#eab308",
      "questionCount": 27,
      "description": "İslamiyet Öncesi, Selçuklu, Osmanlı Tarihi, İnkılap Tarihi ve Çağdaş Türk Tarihi",
      "topics": [
        {
          "id": "tar_1",
          "title": "1. İslamiyet Öncesi Türk Tarihi Kültür ve Medeniyeti",
          "avgQuestions": "3-4 Soru",
          "summary": "Asya Hun, Göktürk ve Uygurlar; Kut anlayışı, Töre, Kurultay, ikili teşkilat.",
          "keyPoints": [
            "Uygurlar Maniheizm dinini kabul ederek YERLEŞİK HAYATA GEÇEN İLK TÜRK DEVLETİ olmuştur.",
            "Kut anlayışı: Yönetme yetkisinin Tanrı tarafından hükümdara verildiğine inanılmasıdır (Veraset belirsizliği yaratır).",
            "Mete Han tarafından kurulan Onlu Sistem dünya ordularına model olmuştur."
          ],
          "pages": [
            {
              "pageNo": "1",
              "pageTitle": "1. Bölüm: Eski Türklerde Devlet Yönetimi ve Teşkilat",
              "text": "<div class=\"content-block\">\n  <h3>🏛️ Devlet Teşkilatı Kavramları</h3>\n  <ul>\n    <li><b>Kut Anlayışı:</b> Devleti yönetme yetkisinin Gök Tanrı tarafından Kağan'a verildiğine inanılmasıdır. Kan yoluyla hanedanın tüm erkek üyelerine geçer. Bu durum taht kavgalarına ve devletlerin kısa ömürlü olmasına yol açmıştır.</li>\n    <li><b>Kurultay (Toy / Keneş):</b> Siyasi, askeri ve ekonomik kararların görüşüldüğü meclistir. Hükümdar eşi <b>Hatun</b> da katılır ve elçi kabul edebilirdi.</li>\n    <li><b>İkili Teşkilat:</b> Devletin Doğu ve Batı olarak ikiye ayrılarak yönetilmesidir. Doğu kutsal sayıldığı için asıl Kağan Doğu'da, kardeşi (Yabgu) Batı'da otururdu.</li>\n    <li><b>Töre:</b> Yazısız hukuk kurallarıdır. Hükümdar dahi töreye uymak zorundadır (Hukukun üstünlüğü).</li>\n  </ul>\n</div>"
            },
            {
              "pageNo": "2",
              "pageTitle": "2. Bölüm: Önemli İlk Türk Devletleri",
              "text": "<div class=\"content-block\">\n  <h3>🏹 Başlıca Türk Devletleri</h3>\n  <ul>\n    <li><b>Asya Hun Devleti:</b> Bilinen ilk Türk devletidir. Kurucusu Teoman, en parlak dönemi <b>Mete Han</b>'dır (Onlu Askeri Sistemi kurdu).</li>\n    <li><b>I. ve II. Köktürkler:</b> Türk adıyla kurulan ilk devlettir. Türk tarihinin ilk yazılı belgeleri olan <b>Orhun Abideleri</b> (Bilge Kağan, Kül Tigin, Tonyukuk) II. Köktürk (Kutluk) dönemine aittir.</li>\n    <li><b>Uygurlar:</b> Maniheizm dinini kabul ederek <b>YERLEŞİK HAYATA GEÇEN İLK TÜRK DEVLETİ</b> olmuşlardır. Tarım, mimari, saraylar, fresk sanatı ve matbaa gelişmiştir.</li>\n  </ul>\n</div>"
            }
          ],
          "questions": [
            {
              "id": "q_tr_1",
              "level": "Kolay",
              "text": "Maniheizm dinini kabul ederek yerleşik hayata geçen İLK Türk devleti aşağıdakilerden hangisidir?",
              "options": [
                "A) Asya Hun Devleti",
                "B) II. Göktürk Devleti",
                "C) Uygurlar",
                "D) Hazarlar",
                "E) Avarlar"
              ],
              "correct": 2,
              "solution": "Uygurlar yerleşik hayata geçen ilk Türk devletidir."
            }
          ]
        },
        {
          "id": "tar_2",
          "title": "2. İlk Türk-İslam Devletleri & Türkiye Selçukluları",
          "avgQuestions": "2-3 Soru",
          "summary": "Karahanlılar, Gazneliler, Büyük Selçuklular, 1071 Malazgirt Zaferi ve Anadolu Beylikleri.",
          "keyPoints": [
            "Karahanlılar Orta Asya'da kurulan İLK MÜSLÜMAN TÜRK devletidir (Satuk Buğra Han).",
            "1071 Malazgirt Zaferi ile Anadolu'nun kapıları Türklere kesin olarak açılmıştır."
          ],
          "pages": [
            {
              "pageNo": "1",
              "pageTitle": "1. Bölüm: İlk Türk-İslam Devletleri ve Eserleri",
              "text": "<div class=\"content-block\">\n  <h3>🕌 İlk Türk-İslam Devletleri</h3>\n  <ul>\n    <li><b>Karahanlılar:</b> Orta Asya'da kurulan ilk Müslüman Türk devletidir. Resmi dilleri Türkçedir. İlk Türk-İslam edebi eserleri bu dönemde yazılmıştır:\n      <ul>\n        <li><i>Kutadgu Bilig (Yusuf Has Hacip)</i> - İlk siyasetname</li>\n        <li><i>Divanü Lügati't-Türk (Kaşgarlı Mahmut)</i> - İlk Türkçe sözlük ve harita</li>\n        <li><i>Atabetü'l-Hakayık (Edip Ahmet Yükneki)</i></li>\n        <li><i>Divan-ı Hikmet (Hoca Ahmet Yesevi)</i> - İlk tasavvufi eser</li>\n      </ul>\n    </li>\n    <li><b>Gazneliler:</b> Sultan Mahmut döneminde Hindistan'a 17 sefer düzenlenmiş ve İslamiyet yayılmıştır. Sultan unvanını kullanan ilk Türk hükümdarıdır.</li>\n    <li><b>Büyük Selçuklu Devleti:</b> 1040 Dandanakan Zaferi ile kurulmuş, 1071 Malazgirt Savaşı ile Sultan Alparslan komutasında Anadolu'nun kapılarını Türklere açmıştır.</li>\n  </ul>\n</div>"
            }
          ],
          "questions": [
            {
              "id": "q_tr_2",
              "level": "Kolay",
              "text": "1071 Malazgirt Zaferi hangi Selçuklu hükümdarı zamanında kazanılmıştır?",
              "options": [
                "A) Tuğrul Bey",
                "B) Sultan Alparslan",
                "C) Melikşah",
                "D) Sencer",
                "E) Çağrı Bey"
              ],
              "correct": 1,
              "solution": "1071 Malazgirt Zaferi Sultan Alparslan komutasında kazanılmıştır."
            }
          ]
        },
        {
          "id": "tar_3",
          "title": "3. Osmanlı Devleti Siyasi Tarihi (Kuruluş, Yükselme)",
          "avgQuestions": "4-5 Soru",
          "summary": "Beylikten devlete geçiş, İstanbul'un Fethi (1453), Preveze Deniz Zaferi ve fetihler.",
          "keyPoints": [
            "1453 İstanbul'un Fethi ile Orta Çağ kapanmış, Yeni Çağ başlamıştır.",
            "I. Murat döneminde Tımar ve Yeniçeri Ocağı (Kapıkulu) teşkilatı kurulmuştur."
          ],
          "pages": [
            {
              "pageNo": "1",
              "pageTitle": "1. Bölüm: Osmanlı Siyasi Gelişmeleri Kronolojisi",
              "text": "<div class=\"content-block\">\n  <h3>👑 Kuruluş ve Yükselme Dönemi Önemli Olayları</h3>\n  <ul>\n    <li><b>Osman Bey:</b> İlk Osmanlı parası (bakır) basıldı, Koyunhisar Savaşı (Bizans'la ilk savaş) kazanıldı.</li>\n    <li><b>Orhan Bey:</b> Bursa başkent yapıldı, Çimpe Kalesi alınarak Rumeli'ye ilk kez geçildi, ilk düzenli ordu (Yaya ve Müsellem) ve Divan kuruldu.</li>\n    <li><b>I. Murat:</b> Edirne başkent yapıldı, Sırpsındığı ve I. Kosova savaşları kazanıldı. İlk kez <b>Tımar Sistemi</b> ve <b>Yeniçeri Ocağı</b> kuruldu.</li>\n    <li><b>Fatih Sultan Mehmet (II. Mehmet):</b> 1453'te İstanbul fethedildi, Karadeniz Türk gölü haline getirildi, ilk altın para basıldı, Sahn-ı Seman medreseleri açıldı.</li>\n    <li><b>Yavuz Sultan Selim:</b> Çaldıran, Mercidabık ve Ridaniye zaferleriyle Memlük Devleti yıkıldı, Halifelik ve Kutsal Emanetler Osmanlı'ya geçti.</li>\n    <li><b>Kanuni Sultan Süleyman:</b> Belgrad ve Rodos alındı, Mohaç Meydan Muharebesi (2 saatte kazanıldı), 1538 Preveze Deniz Zaferi ile Akdeniz Türk gölü oldu.</li>\n  </ul>\n</div>"
            }
          ],
          "questions": [
            {
              "id": "q_tr_3",
              "level": "Kolay",
              "text": "Osmanlı Devleti'nde ilk altın para hangi padişah döneminde basılmıştır?",
              "options": [
                "A) Osman Bey",
                "B) Orhan Bey",
                "C) Fatih Sultan Mehmet",
                "D) Kanuni Sultan Süleyman",
                "E) Yavuz Sultan Selim"
              ],
              "correct": 2,
              "solution": "İlk altın para (Sultani) Fatih Sultan Mehmet döneminde basılmıştır."
            }
          ]
        },
        {
          "id": "tar_4",
          "title": "4. Osmanlı Kültür ve Medeniyeti (Divan, Tımar, Eyaletler)",
          "avgQuestions": "5-6 Soru",
          "summary": "Divan-ı Hümayun üyeleri, Seyfiye-İlmiye-Kalemiye sınıfları, Tımar sistemi ve Eyalet yönetimi.",
          "keyPoints": [
            "Kazasker adalet ve eğitim işlerine bakar; kadı ve müderris atamalarını yapar (İlmiye sınıfı).",
            "Tımar sistemi ile hazineden para çıkmadan savaşa hazır Cebelü (atlı asker) yetiştirilmiştir."
          ],
          "pages": [
            {
              "pageNo": "1",
              "pageTitle": "1. Bölüm: Divan-ı Hümayun Üyeleri ve Görevleri",
              "text": "<div class=\"content-block\">\n  <h3>⚡ Divan-ı Hümayun ve Yönetici Sınıflar</h3>\n  <table style=\"width:100%; border-collapse:collapse; margin:12px 0;\">\n    <tr style=\"background:#1e293b;\"><th style=\"padding:8px; border:1px solid #334155;\">Sınıf</th><th style=\"padding:8px; border:1px solid #334155;\">Divan Üyeleri</th><th style=\"padding:8px; border:1px solid #334155;\">Alanı & Görevi</th></tr>\n    <tr><td style=\"padding:6px; border:1px solid #334155;\"><b>Seyfiye</b> (Kılıç/Yönetim)</td><td style=\"padding:6px; border:1px solid #334155;\">Sadrazam (Vezir-i Azam), Kubbealtı Vezirleri, Kaptan-ı Derya, Yeniçeri Ağası</td><td style=\"padding:6px; border:1px solid #334155;\">Askeri ve idari yönetim. Padişahın mutlak vekilidir.</td></tr>\n    <tr><td style=\"padding:6px; border:1px solid #334155;\"><b>İlmiye</b> (Din/Eğitim/Adalet)</td><td style=\"padding:6px; border:1px solid #334155;\">Şeyhülislam (Müftü), Kazasker</td><td style=\"padding:6px; border:1px solid #334155;\">Fetva verir, Kadı ve Müderris atamalarını yapar.</td></tr>\n    <tr><td style=\"padding:6px; border:1px solid #334155;\"><b>Kalemiye</b> (Bürokrasi/Maliye)</td><td style=\"padding:6px; border:1px solid #334155;\">Defterdar, Nişancı, Reisülküttap</td><td style=\"padding:6px; border:1px solid #334155;\">Maliye (bütçe), Tuğra çekme/Tapu tahrir, Dış yazışmalar.</td></tr>\n  </table>\n</div>"
            }
          ],
          "questions": [
            {
              "id": "q_tr_4",
              "level": "Orta",
              "text": "Osmanlı Devleti'nde kadı ve müderris atamalarını yapan Divan-ı Hümayun üyesi hangisidir?",
              "options": [
                "A) Nişancı",
                "B) Kazasker",
                "C) Defterdar",
                "D) Sadrazam",
                "E) Reisülküttap"
              ],
              "correct": 1,
              "solution": "Kazasker, adalet ve eğitim işlerinden sorumlu olup kadı ve müderris atamalarını yapardı."
            }
          ]
        },
        {
          "id": "tar_5",
          "title": "5. XVIII. ve XIX. Yüzyıl Osmanlı Islahat Hareketleri",
          "avgQuestions": "3-4 Soru",
          "summary": "Lale Devri, II. Mahmut Islahatları, Tanzimat Fermanı (1839), Islahat Fermanı (1856) ve Meşrutiyetler.",
          "keyPoints": [
            "1839 Tanzimat Fermanı ile padişah ilk kez kanun gücünün üstünlüğünü kabul etmiştir.",
            "II. Mahmut 1826'da Yeniçeri Ocağını kaldırarak (Vaka-i Hayriye) merkezi otoriteyi güçlendirmiştir."
          ],
          "pages": [
            {
              "pageNo": "1",
              "pageTitle": "1. Bölüm: Tanzimat, Islahat ve Meşrutiyet Dönemleri",
              "text": "<div class=\"content-block\">\n  <h3>📜 Önemli Islahat Belgeleri</h3>\n  <ul>\n    <li><b>Tanzimat Fermanı (1839 - Abdülmecit):</b> Müslüman-Gayrimüslim tüm halkın can, mal, namus güvencesi kanun teminatına alındı. Padişah ilk kez kendi gücünün üstünde <b>Kanun Gücünü</b> kabul etti.</li>\n    <li><b>Islahat Fermanı (1856 - Abdülmecit):</b> Özellikle Gayrimüslim azınlıklara geniş haklar verildi (Cizye vergisi kaldırıldı, devlet memuru olma hakkı tanındı).</li>\n    <li><b>I. Meşrutiyet ve Kanun-i Esasi (1876 - II. Abdülhamit):</b> Türk tarihinin <b>İLK ANAYASASI</b> ilan edildi. Halk ilk kez padişahın yanında yönetime katıldı (Mebusan Meclisi).</li>\n  </ul>\n</div>"
            }
          ],
          "questions": [
            {
              "id": "q_tr_5",
              "level": "Orta",
              "text": "Osmanlı padişahının kendi otoritesinin üstünde kanun gücünün üstünlüğünü kabul ettiği İLK belge hangisidir?",
              "options": [
                "A) Sened-i İttifak",
                "B) Tanzimat Fermanı",
                "C) Islahat Fermanı",
                "D) Kanun-i Esasi",
                "E) Halepa Fermanı"
              ],
              "correct": 1,
              "solution": "1839 Tanzimat Fermanı ile padişah kanun üstünlüğünü ilk kez kabul etmiştir."
            }
          ]
        },
        {
          "id": "tar_6",
          "title": "6. Milli Mücadele Hazırlık Dönemi (Genelgeler & Kongreler)",
          "avgQuestions": "4-5 Soru",
          "summary": "Havza, Amasya Genelgesi, Erzurum Kongresi, Sivas Kongresi ve Amasya Görüşmeleri.",
          "keyPoints": [
            "Amasya Genelgesi: Kurtuluş Savaşı'nın Amacı, Gerekçesi ve Yöntemi ilk kez belirtilmiştir.",
            "Erzurum Kongresi: Toplanış bakımından bölgesel, aldığı kararlar bakımından ulusaldır (Manda-himaye ilk kez reddedildi).",
            "Sivas Kongresi: Tüm cemiyetler tek çatı altında (Anadolu ve Rumeli Müdafaa-i Hukuk) birleştirildi."
          ],
          "pages": [
            {
              "pageNo": "1",
              "pageTitle": "1. Bölüm: Genelgeler ve Kongreler Kararları",
              "text": "<div class=\"content-block\">\n  <h3>⚡ Milli Mücadele Yol Haritası</h3>\n  <ul>\n    <li><b>Amasya Genelgesi (22 Haziran 1919):</b>\n      <ul>\n        <li><i>'Vatanın bütünlüğü, milletin bağımsızlığı tehlikededir.'</i> (<b>GEREKÇE</b>)</li>\n        <li><i>'Milletin bağımsızlığını yine milletin azim ve kararı kurtaracaktır.'</i> (<b>AMAÇ ve YÖNTEM</b> - İlk kez milli egemenlik vurgusu).</li>\n      </ul>\n    </li>\n    <li><b>Erzurum Kongresi (23 Temmuz 1919):</b> <i>'Milli sınırlar içinde vatan bir bütündür, bölünemez.'</i> Manda ve himaye <b>İLK KEZ</b> reddedildi. Temsil Heyeti kuruldu.</li>\n    <li><b>Sivas Kongresi (4 Eylül 1919):</b> Manda ve himaye <b>KESİN OLARAK</b> reddedildi. Tüm cemiyetler birleştirildi. Temsil Heyeti Ali Fuat Paşa'yı Batı Cephesi'ne atayarak ilk kez <b>YÜRÜTME</b> yetkisini kullandı.</li>\n  </ul>\n</div>"
            }
          ],
          "questions": [
            {
              "id": "q_tr_6",
              "level": "Kolay",
              "text": "Manda ve Himaye fikri İLK KEZ nerede açıkça reddedilmiştir?",
              "options": [
                "A) Amasya Genelgesi",
                "B) Erzurum Kongresi",
                "C) Sivas Kongresi",
                "D) Havza Genelgesi",
                "E) Lozan Antlaşması"
              ],
              "correct": 1,
              "solution": "Manda ve himaye ilk kez Erzurum Kongresi'nde reddedilmiş, Sivas'ta ise kesin olarak reddedilmiştir."
            }
          ]
        },
        {
          "id": "tar_7",
          "title": "7. I. TBMM Dönemi, Ayaklanmalar ve Sevr",
          "avgQuestions": "3 Soru",
          "summary": "23 Nisan 1920 TBMM'nin açılması, özellikleri, Hıyanet-i Vataniye Kanunu ve İstiklal Mahkemeleri.",
          "keyPoints": [
            "I. TBMM Kurucu, Savaşçı, İhtilalci ve 'Güçler Birliği' ilkesini benimseyen bir meclistir.",
            "İlk anayasa: 1921 Teşkilat-ı Esasiye Kanunu'dur."
          ],
          "pages": [
            {
              "pageNo": "1",
              "pageTitle": "1. Bölüm: I. TBMM'nin Özellikleri ve Faaliyetleri",
              "text": "<div class=\"content-block\">\n  <h3>🏛️ I. TBMM'nin Özellikleri (1920 - 1923)</h3>\n  <ul>\n    <li><b>Kurucudur:</b> Yeni bir devlet ve 1921 Anayasasını yapmıştır.</li>\n    <li><b>Güçler Birliği İlkesi:</b> Yasama, yürütme ve yargı yetkileri hızlı karar almak için TBMM'de toplanmıştır.</li>\n    <li><b>Meclis Hükümeti Sistemi:</b> Başbakanlık yoktur, Meclis Başkanı aynı zamanda hükümetin de başıdır.</li>\n    <li><b>Siyasi Parti Yoktur:</b> Birlik ve beraberliği korumak için gruplar (Müdafaa-i Hukuk, Tesanüt, İstiklal) vardır.</li>\n  </ul>\n</div>"
            }
          ],
          "questions": [
            {
              "id": "q_tr_7",
              "level": "Kolay",
              "text": "I. TBMM'nin yasama, yürütme ve yargı yetkilerini kendisinde toplaması hangi ilkeyle açıklanır?",
              "options": [
                "A) Kuvvetler Ayrılığı",
                "B) Güçler Birliği",
                "C) Kabine Sistemi",
                "D) Çoğulculuk",
                "E) Parlamenter Rejim"
              ],
              "correct": 1,
              "solution": "Hızlı karar alıp uygulamak için güçler birliği ilkesi benimsenmiştir."
            }
          ]
        },
        {
          "id": "tar_8",
          "title": "8. Kurtuluş Savaşı Muharebeler Dönemi & Antlaşmalar",
          "avgQuestions": "4-5 Soru",
          "summary": "Doğu, Güney ve Batı cepheleri; I. İnönü, Sakarya, Büyük Taarruz, Mudanya ve Lozan.",
          "keyPoints": [
            "I. İnönü Zaferi sonrası: Teşkilat-ı Esasiye (1921), Londra Konferansı, Afganistan Dostluk, İstiklal Marşı, Moskova Antlaşması imzalandı (TALİM şifresi).",
            "Sakarya Savaşı sonrasında Mustafa Kemal'e Mareşallik ve Gazilik unvanı verildi."
          ],
          "pages": [
            {
              "pageNo": "1",
              "pageTitle": "1. Bölüm: Batı Cephesi Muharebeleri ve Antlaşmalar",
              "text": "<div class=\"content-block\">\n  <h3>⚔️ Kurtuluş Savaşı Cepheleri</h3>\n  <ul>\n    <li><b>I. İnönü Zaferi (1921):</b> Düzenli ordunun ilk zaferidir. Sonuçları: <b>TALİM</b> (Teşkilat-ı Esasiye kabul edildi, Afganistan'la dostluk yapıldı, Londra Konferansı toplandı, İstiklal Marşı kabul edildi, Moskova Antlaşması ile Sovyet Rusya TBMM'yi tanıdı).</li>\n    <li><b>Sakarya Meydan Muharebesi (1921):</b> <i>'Hattı müdafaa yoktur, sathı müdafaa vardır. O satıh bütün vatandır.'</i> Türk ordusunun 1683 Viyana'dan beri süren geri çekilişi sona erdi. Fransa ile Ankara Antlaşması imzalanarak Güney Cephesi kapandı.</li>\n    <li><b>Büyük Taarruz (26 Ağustos - 9 Eylül 1922):</b> Düşman ordusu İzmir'den denize döküldü. Mudanya Ateşkesi ile Doğu Trakya ve Boğazlar savaşsız kurtarıldı.</li>\n    <li><b>Lozan Barış Antlaşması (24 Temmuz 1923):</b> Kapitülasyonlar tamamen kaldırıldı, Türkiye Cumhuriyeti'nin bağımsızlığı tüm dünya tarafından tescillendi.</li>\n  </ul>\n</div>"
            }
          ],
          "questions": [
            {
              "id": "q_tr_8",
              "level": "Orta",
              "text": "Düzenli ordunun Batı Cephesi'ndeki İLK askeri zaferi hangisidir?",
              "options": [
                "A) I. İnönü Zaferi",
                "B) II. İnönü Zaferi",
                "C) Sakarya Meydan Muharebesi",
                "D) Büyük Taarruz",
                "E) Aslıhanlar Muharebesi"
              ],
              "correct": 0,
              "solution": "Düzenli ordunun ilk askeri zaferi I. İnönü Zaferi'dir."
            }
          ]
        },
        {
          "id": "tar_9",
          "title": "9. Atatürk İnkılapları ve İlkeleri",
          "avgQuestions": "6-8 Soru",
          "summary": "Cumhuriyetçilik, Milliyetçilik, Halkçılık, Laiklik, Devletçilik, İnkılapçılık ilkeleri ve yapılan devrimler.",
          "keyPoints": [
            "Saltanatın kaldırılması (1922) ve TBMM'nin açılması CUMHURİYETÇİLİK ile ilgilidir.",
            "Aşar vergisinin kaldırılması, Kadınlara seçme-seçilme hakkı verilmesi HALKÇILIK ile ilgilidir.",
            "Kabotaj Kanunu (1926) ve Türk Dil Kurumu MİLLİYETÇİLİK ile ilgilidir."
          ],
          "pages": [
            {
              "pageNo": "1",
              "pageTitle": "1. Bölüm: 6 Temel Atatürk İlkesi ve Anahtar Kavramlar",
              "text": "<div class=\"content-block\">\n  <h3>⚡ Atatürk İlkeleri Anahtar Kelimeler Tablosu</h3>\n  <table style=\"width:100%; border-collapse:collapse; margin:12px 0;\">\n    <tr style=\"background:#1e293b;\"><th style=\"padding:8px; border:1px solid #334155;\">İlke</th><th style=\"padding:8px; border:1px solid #334155;\">Anahtar Kavramlar</th><th style=\"padding:8px; border:1px solid #334155;\">Örnek İnkılaplar</th></tr>\n    <tr><td style=\"padding:6px; border:1px solid #334155;\"><b>Cumhuriyetçilik</b></td><td style=\"padding:6px; border:1px solid #334155;\">Milli irade, seçim, meclis, çok partili hayat</td><td style=\"padding:6px; border:1px solid #334155;\">TBMM'nin açılması, Saltanatın kaldırılması, Cumhuriyetin ilanı</td></tr>\n    <tr><td style=\"padding:6px; border:1px solid #334155;\"><b>Milliyetçilik</b></td><td style=\"padding:6px; border:1px solid #334155;\">Türk dili, Türk tarihi, bağımsızlık, milli bilinç</td><td style=\"padding:6px; border:1px solid #334155;\">TTK, TDK, Kabotaj Kanunu, Türk parasını koruma</td></tr>\n    <tr><td style=\"padding:6px; border:1px solid #334155;\"><b>Halkçılık</b></td><td style=\"padding:6px; border:1px solid #334155;\">Eşitlik, ayrıcalıksız toplum, sosyal adalet</td><td style=\"padding:6px; border:1px solid #334155;\">Aşar vergisinin kaldırılması, Soyadı Kanunu, Kadın hakları</td></tr>\n    <tr><td style=\"padding:6px; border:1px solid #334155;\"><b>Laiklik</b></td><td style=\"padding:6px; border:1px solid #334155;\">Akılcılık, bilimsellik, din ve devlet işleri ayrımı</td><td style=\"padding:6px; border:1px solid #334155;\">Halifeliğin kaldırılması, Tekke ve zaviyelerin kapatılması, Medeni Kanun</td></tr>\n    <tr><td style=\"padding:6px; border:1px solid #334155;\"><b>Devletçilik</b></td><td style=\"padding:6px; border:1px solid #334155;\">Karma ekonomi, devlet yatırımları, kalkınma planı</td><td style=\"padding:6px; border:1px solid #334155;\">Sümerbank, Etibank, I. Beş Yıllık Sanayi Planı, Demiryolları</td></tr>\n    <tr><td style=\"padding:6px; border:1px solid #334155;\"><b>İnkılapçılık</b></td><td style=\"padding:6px; border:1px solid #334155;\">Çağdaşlaşma, dinamizm, yenilik, Batılılaşma</td><td style=\"padding:6px; border:1px solid #334155;\">Takvim, saat, ölçü değişiklikleri, Harf İnkılabı, Şapka Kanunu</td></tr>\n  </table>\n</div>"
            }
          ],
          "questions": [
            {
              "id": "q_tr_9",
              "level": "Kolay",
              "text": "Aşar vergisinin kaldırılması doğrudan hangi Atatürk ilkesi doğrultusunda yapılmıştır?",
              "options": [
                "A) Halkçılık",
                "B) Devletçilik",
                "C) Laiklik",
                "D) Milliyetçilik",
                "E) İnkılapçılık"
              ],
              "correct": 0,
              "solution": "Aşar vergisi köylü üzerindeki ağır bir yük olup kaldırılması eşitlik ve sosyal adalet gereği Halkçılık ilkesidir."
            }
          ]
        },
        {
          "id": "tar_10",
          "title": "10. Çağdaş Türk ve Dünya Tarihi",
          "avgQuestions": "2 Soru",
          "summary": "Atatürk dönemi dış politika (Balkan Antantı, Sadabat Paktı, Montrö, Hatay) ve II. Dünya Savaşı dönemi.",
          "keyPoints": [
            "1936 Montrö Boğazlar Sözleşmesi ile Boğazlar Komisyonu kaldırılmış, egemenlik tam olarak Türkiye'ye geçmiştir.",
            "Hatay 1939 yılında anavatana katılmıştır."
          ],
          "pages": [
            {
              "pageNo": "1",
              "pageTitle": "1. Bölüm: Atatürk Dönemi Dış Politika Başarıları",
              "text": "<div class=\"content-block\">\n  <h3>🌍 Dış Politika Gelişmeleri</h3>\n  <ul>\n    <li><b>Milletler Cemiyeti'ne Giriş (1932):</b> Türkiye barışçı politikasının sonucu olarak davetle üye olmuştur.</li>\n    <li><b>Balkan Antantı (1934):</b> Batı sınırını güvenceye almak için Türkiye, Yunanistan, Yugoslavya ve Romanya arasında imzalandı.</li>\n    <li><b>Montrö Boğazlar Sözleşmesi (1936):</b> Boğazlar Komisyonu kaldırıldı, boğazlarda Türk askeri konuşlandırıldı, tam egemenlik sağlandı.</li>\n    <li><b>Sadabat Paktı (1937):</b> Doğu sınırını korumak için Türkiye, İran, Irak ve Afganistan arasında imzalandı.</li>\n    <li><b>Hatay'ın Anavatana Katılması (1939):</b> Atatürk'ün 'şahsi meselem' dediği Hatay, bağımsız olduktan sonra TBMM kararıyla Türkiye'ye katıldı.</li>\n  </ul>\n</div>"
            }
          ],
          "questions": [
            {
              "id": "q_tr_10",
              "level": "Kolay",
              "text": "Hatay hangi yılda Türkiye Cumhuriyeti sınırlarına katılmıştır?",
              "options": [
                "A) 1936",
                "B) 1938",
                "C) 1939",
                "D) 1940",
                "E) 1945"
              ],
              "correct": 2,
              "solution": "Hatay 1939 yılında Türkiye'ye katılmıştır."
            }
          ]
        }
      ]
    },
    {
      "id": "cografya",
      "name": "Coğrafya",
      "icon": "🌍",
      "color": "#10b981",
      "questionCount": 18,
      "description": "Türkiye'nin Fiziki, Beşeri ve Ekonomik Coğrafyası",
      "topics": [
        {
          "id": "cog_1",
          "title": "1. Türkiye'nin Coğrafi Konumu & Jeolojik Yapısı",
          "avgQuestions": "3 Soru",
          "summary": "36°-42° Kuzey, 26°-45° Doğu konumu; Orta Kuşak ve Yengeç Dönencesi kuzeyinde olmanın sonuçları.",
          "keyPoints": [
            "Türkiye Orta Kuşak'tadır: 4 mevsim belirgin yaşanır, Batı rüzgarları ve Akdeniz iklimi görülür.",
            "Dönenceler dışında olduğumuz için Güneş ışınları hiçbir zaman 90° dik açıyla düşmez, gölge boyu 0 olmaz.",
            "Güneyden kuzeye gidildikçe çizgisel hız azalır, yerçekimi artar, deniz tuzluluğu azalır."
          ],
          "pages": [
            {
              "pageNo": "1",
              "pageTitle": "1. Bölüm: Matematiksel (Mutlak) Konum ve Sonuçları",
              "text": "<div class=\"content-block\">\n  <h3>🌍 Türkiye'nin Matematiksel Koordinatları</h3>\n  <p>Türkiye <b>36° - 42° Kuzey Paralelleri</b> ile <b>26° - 45° Doğu Meridyenleri</b> arasında yer alır.</p>\n\n  <h3>⚡ Orta Kuşakta (30°-60° Enlemleri) Yer Almanın Sonuçları: (Şifre: 3B1A)</h3>\n  <ul>\n    <li><b>B</b>atılı Rüzgarlar kuşağında yer alırız.</li>\n    <li><b>B</b>elirgin 4 mevsim yıllık olarak yaşanır.</li>\n    <li><b>B</b>ölgesel Cephesel (Frontal) yağışlar görülür (Sıcak-soğuk hava karşılaşması).</li>\n    <li><b>A</b>kdeniz iklim kuşağındayız.</li>\n  </ul>\n\n  <h3>⚡ Yengeç Dönencesi Kuzeyinde Yer Almanın Sonuçları:</h3>\n  <ul>\n    <li>Güneş ışınları hiçbir zaman 90° dik açıyla gelmez.</li>\n    <li>Gölge boyu hiçbir tarihte <b>0 (sıfır)</b> olmaz.</li>\n    <li>Gölge yönü öğle vakti daima <b>KUZEYİ</b> gösterir.</li>\n    <li>Bakı yönü daima <b>GÜNEY</b> yamaçlardır (Dağların güney yamaçları daha sıcaktır).</li>\n  </ul>\n</div>"
            },
            {
              "pageNo": "2",
              "pageTitle": "2. Bölüm: Jeolojik Zamanlar ve Masif Araziler",
              "text": "<div class=\"content-block\">\n  <h3>⛰️ Jeolojik Devirler ve Türkiye'deki Karşılıkları</h3>\n  <ul>\n    <li><b>I. Zaman (Paleozoik):</b> Sert, yaşlı, oturmuş, deprem riski az olan <b>Masif Araziler</b> oluşmuştur (Yıldız Dağları, Zonguldak, Kırşehir, Menteşe, Mardin). <b>Taş Kömürü</b> yatakları (Zonguldak) bu dönemde oluştu.</li>\n    <li><b>III. Zaman (Tersiyer):</b> Alp-Himalaya kıvrım sistemi ile Kuzey Anadolu Dağları ve Toroslar yükseldi. <b>Linyit, Petrol, Bor, Tuz ve Jeotermal</b> kaynaklar bu dönemde oluştu.</li>\n    <li><b>IV. Zaman (Kuvaterner):</b> Ege Denizi, Çanakkale ve İstanbul Boğazları oluştu, Karadeniz deniz haline geldi.</li>\n  </ul>\n</div>"
            }
          ],
          "questions": [
            {
              "id": "q_c_1",
              "level": "Kolay",
              "text": "Aşağıdakilerden hangisi Türkiye'nin <u>Orta Kuşak'ta</u> yer almasının doğrudan bir sonucudur?",
              "options": [
                "A) Dört mevsimin belirgin yaşanması",
                "B) Aynı anda farklı iklim yaşanması",
                "C) Üç tarafının denizlerle çevrili olması",
                "D) Yükseltinin batıdan doğuya artması",
                "E) Zengin bor madenlerine sahip olması"
              ],
              "correct": 0,
              "solution": "Dört mevsimin yıllık döngüde belirgin yaşanması Orta Kuşak (matematiksel konum) sonucudur."
            }
          ]
        },
        {
          "id": "cog_2",
          "title": "2. Türkiye'nin Dağları, Platoları ve Ovaları",
          "avgQuestions": "4 Soru",
          "summary": "Kıvrım, Kırık (Horst-Graben) ve Volkanik Dağlar; Karstik, Volkanik ve Aşınım Platoları.",
          "keyPoints": [
            "Ege Kırık Dağları (Horstlar): Kaz, Madra, Yunt, Bozdağlar, Aydın, Menteşe ve Nur (Amanos).",
            "Karstik Platolar: Teke ve Taşeli (Akdeniz - kalker erimeli, seyrek nüfuslu).",
            "Volkanik Platolar: Erzurum-Kars-Ardahan (Çernezyom kara toprak, büyükbaş mera hayvancılığı)."
          ],
          "pages": [
            {
              "pageNo": "1",
              "pageTitle": "1. Bölüm: Dağ Çeşitleri ve Oluşumları",
              "text": "<div class=\"content-block\">\n  <h3>🏔️ Türkiye'nin Dağları</h3>\n  <ul>\n    <li><b>Kıvrım Dağları (Orojenez):</b> Esnek tabakaların kıvrılmasıyla oluşur. Üstte kalan kısma <i>Antiklinal</i>, altta kalan kısma <i>Senklinal</i> denir. (Kuzey Anadolu Dağları: Kaçkar, Ilgaz, Küre; Toroslar: Bolkar, Aladağlar).</li>\n    <li><b>Kırık Dağları (Horst - Graben):</b> Sert arazinin kırılmasıyla oluşur. Yüksekte kalan kısma <b>Horst</b>, çöken ovaya <b>Graben</b> denir.\n      <ul>\n        <li>Horstlar: <b>Kaz, Madra, Yunt, Bozdağlar, Aydın Dağları, Menteşe</b> ve Hatay'daki <b>Nur (Amanos) Dağları</b>.</li>\n        <li>Grabenler (Çöküntü Ovaları): <b>Edremit, Bakırçay, Gediz, Küçük Menderes, Büyük Menderes, Amik Ovası</b>.</li>\n      </ul>\n    </li>\n    <li><b>Volkanik Dağlar:</b>\n      <ul>\n        <li>İç Anadolu: Erciyes, Hasan Dağı, Melendiz, Karadağ, Karacadağ.</li>\n        <li>Doğu Anadolu: Ağrı (Büyük/Küçük), Tendürek, Süphan, Nemrut.</li>\n        <li>Güneydoğu Anadolu: Karacadağ (Kalkan volkan).</li>\n        <li>Ege: Kula Volkanları (Türkiye'nin en genç volkanları).</li>\n      </ul>\n    </li>\n  </ul>\n</div>"
            },
            {
              "pageNo": "2",
              "pageTitle": "2. Bölüm: Platolar ve Ovalar",
              "text": "<div class=\"content-block\">\n  <h3>⛰️ Platolarımızın Sınıflandırılması</h3>\n  <table style=\"width:100%; border-collapse:collapse; margin:12px 0;\">\n    <tr style=\"background:#1e293b;\"><th style=\"padding:8px; border:1px solid #334155;\">Plato Türü</th><th style=\"padding:8px; border:1px solid #334155;\">Platolar</th><th style=\"padding:8px; border:1px solid #334155;\">Ekonomik Faaliyet / Özellik</th></tr>\n    <tr><td style=\"padding:6px; border:1px solid #334155;\"><b>Karstik Platolar</b></td><td style=\"padding:6px; border:1px solid #334155;\">Teke ve Taşeli (Akdeniz)</td><td style=\"padding:6px; border:1px solid #334155;\">Kalkerli arazi, su sızar, tarım zor, Kıl Keçisi yetiştiriciliği, Seyrek nüfus.</td></tr>\n    <tr><td style=\"padding:6px; border:1px solid #334155;\"><b>Lav (Volkanik) Platoları</b></td><td style=\"padding:6px; border:1px solid #334155;\">Erzurum-Kars-Ardahan</td><td style=\"padding:6px; border:1px solid #334155;\">Yaz yağışları, Çayır örtüsü, Çernezyom toprak, Büyükbaş mera hayvancılığı.</td></tr>\n    <tr><td style=\"padding:6px; border:1px solid #334155;\"><b>Tabaka Düzlüğü Platoları</b></td><td style=\"padding:6px; border:1px solid #334155;\">Haymana, Cihanbeyli, Obruk, Bozok, Uzunyayla</td><td style=\"padding:6px; border:1px solid #334155;\">Tahıl (buğday/arpa) tarımı, Küçükbaş hayvancılık.</td></tr>\n    <tr><td style=\"padding:6px; border:1px solid #334155;\"><b>Aşınım Platosu</b></td><td style=\"padding:6px; border:1px solid #334155;\">Çatalca - Kocaeli</td><td style=\"padding:6px; border:1px solid #334155;\">Yükseltisi en az, sanayi, ticaret ve nüfusu en yoğun platodur.</td></tr>\n  </table>\n</div>"
            }
          ],
          "questions": [
            {
              "id": "q_c_2",
              "level": "Orta",
              "text": "Aşağıdaki platolardan hangisi kalker erimesi sonucu oluşan <u>Karstik</u> plato özelliğine sahiptir?",
              "options": [
                "A) Erzurum-Kars",
                "B) Çatalca-Kocaeli",
                "C) Teke Platosu",
                "D) Cihanbeyli",
                "E) Bozok"
              ],
              "correct": 2,
              "solution": "Teke ve Taşeli platoları kireç taşı erimesiyle oluşan karstik platolardır."
            }
          ]
        },
        {
          "id": "cog_3",
          "title": "3. Türkiye'nin Gölleri, Akarsuları & Kıyıları",
          "avgQuestions": "3 Soru",
          "summary": "Tektonik, karstik, volkanik ve set gölleri; akarsu rejimleri ve delta ovaları.",
          "keyPoints": [
            "Van Gölü Türkiye'nin en büyük gölüdür (Karma oluşumlu: Volkanik Set + Tektonik, sodalıdır).",
            "Tuz Gölü yüzölçümü en çok değişen tektonik göldür.",
            "Delta ovaları: Çukurova (Seyhan-Ceyhan), Bafra (Kızılırmak), Çarşamba (Yeşilırmak), Silifke (Göksu)."
          ],
          "pages": [
            {
              "pageNo": "1",
              "pageTitle": "1. Bölüm: Göl Türleri ve Akarsular",
              "text": "<div class=\"content-block\">\n  <h3>🌊 Göl Oluşum Türleri</h3>\n  <ul>\n    <li><b>Tektonik Göller:</b> Fay hatları üzerindeki çukurlarda oluşur. (Tuz Gölü, İznik, Sapanca, Manyas, Ulubat, Akşehir, Burdur).</li>\n    <li><b>Karstik Göller:</b> Kireç taşı erimeleriyle oluşur. (Salda, Avlan, Suğla, Kestel).</li>\n    <li><b>Set Gölleri:</b>\n      <ul>\n        <li><i>Heyelan Set:</i> Abant, Yedigöller, Tortum, Sera, Zinav (Karadeniz).</li>\n        <li><i>Volkanik Set:</i> Van Gölü, Erçek, Nazik, Balık, Çıldır, Haçlı (Doğu Anadolu).</li>\n        <li><i>Kıyı Set (Lagün):</i> Büyükçekmece, Küçükçekmece, Terkos (Durusu).</li>\n      </ul>\n    </li>\n  </ul>\n</div>"
            }
          ],
          "questions": [
            {
              "id": "q_c_3",
              "level": "Kolay",
              "text": "Türkiye'nin yüzölçümü en büyük gölü hangisidir?",
              "options": [
                "A) Tuz Gölü",
                "B) Beyşehir",
                "C) Van Gölü",
                "D) Eğirdir",
                "E) İznik"
              ],
              "correct": 2,
              "solution": "Van Gölü ülkemizin yüzölçümü en büyük gölüdür."
            }
          ]
        },
        {
          "id": "cog_4",
          "title": "4. Türkiye'nin İklimi, Bitki Örtüsü & Toprak Tipleri",
          "avgQuestions": "3-4 Soru",
          "summary": "Akdeniz, Karadeniz, Karasal ve Sert Karasal iklim özellikleri; Maki, Bozkır ve Çernezyom toprak.",
          "keyPoints": [
            "Rize Türkiye'nin en çok yağış alan yeridir (Her mevsim yağışlı - Yamaç/Orografik yağış).",
            "Akdeniz iklimi toprak tipi Terra-Rossa (kırmızı toprak), bitki örtüsü Makidir.",
            "En verimli zonal toprak Çernezyom (kara toprak - Erzurum-Kars), en yaygın intrazonal/azonal alüvyal topraklardır."
          ],
          "pages": [
            {
              "pageNo": "1",
              "pageTitle": "1. Bölüm: İklim Tipleri ve Özellikleri",
              "text": "<div class=\"content-block\">\n  <h3>🌦️ Türkiye'deki İklimler Tablosu</h3>\n  <table style=\"width:100%; border-collapse:collapse; margin:12px 0;\">\n    <tr style=\"background:#1e293b;\"><th style=\"padding:8px; border:1px solid #334155;\">İklim Türü</th><th style=\"padding:8px; border:1px solid #334155;\">En Çok Yağış</th><th style=\"padding:8px; border:1px solid #334155;\">Bitki Örtüsü</th><th style=\"padding:8px; border:1px solid #334155;\">Toprak Tipi</th></tr>\n    <tr><td style=\"padding:6px; border:1px solid #334155;\"><b>Akdeniz İklimi</b></td><td style=\"padding:6px; border:1px solid #334155;\">Kışın (Cephesel)</td><td style=\"padding:6px; border:1px solid #334155;\">Maki (Garig)</td><td style=\"padding:6px; border:1px solid #334155;\">Terra-Rossa (Kırmızı)</td></tr>\n    <tr><td style=\"padding:6px; border:1px solid #334155;\"><b>Karadeniz İklimi</b></td><td style=\"padding:6px; border:1px solid #334155;\">Sonbaharda (Yamaç)</td><td style=\"padding:6px; border:1px solid #334155;\">Geniş/İğne Yapraklı Orman</td><td style=\"padding:6px; border:1px solid #334155;\">Kahverengi Orman Toprağı</td></tr>\n    <tr><td style=\"padding:6px; border:1px solid #334155;\"><b>İç Karasal (Step)</b></td><td style=\"padding:6px; border:1px solid #334155;\">İlkbaharda (Konveksiyonel - Kırkikindi)</td><td style=\"padding:6px; border:1px solid #334155;\">Bozkır (Antropojen bozkır)</td><td style=\"padding:6px; border:1px solid #334155;\">Kestane/Kahverengi Bozkır</td></tr>\n    <tr><td style=\"padding:6px; border:1px solid #334155;\"><b>Sert Karasal (Erzurum-Kars)</b></td><td style=\"padding:6px; border:1px solid #334155;\">Yazın (Konveksiyonel)</td><td style=\"padding:6px; border:1px solid #334155;\">Alpin Çayırlar</td><td style=\"padding:6px; border:1px solid #334155;\">Çernezyom (Kara Toprak)</td></tr>\n  </table>\n</div>"
            }
          ],
          "questions": [
            {
              "id": "q_c_4",
              "level": "Kolay",
              "text": "Akdeniz ikliminin karakteristik bitki örtüsü aşağıdakilerden hangisidir?",
              "options": [
                "A) Bozkır",
                "B) Çayır",
                "C) Maki",
                "D) Tayga",
                "E) Tundra"
              ],
              "correct": 2,
              "solution": "Akdeniz ikliminin doğal bitki örtüsü kızılçam ve bunların tahribiyle oluşan makidir."
            }
          ]
        },
        {
          "id": "cog_5",
          "title": "5. Türkiye'de Nüfus, Yerleşme & Göçler",
          "avgQuestions": "3 Soru",
          "summary": "Nüfus yoğunluğu, demografik yapı, seyrek ve sık nüfuslu alanların nedenleri, yerleşme tipleri.",
          "keyPoints": [
            "Nüfus yoğunluğu en yüksek bölge Marmara (Çatalca-Kocaeli), en az olan Doğu Anadolu'dur.",
            "Teke ve Taşeli Platoları karstik arazi ve engebe nedeniyle seyrek nüfusludur.",
            "Toplu yerleşme kurak/düz alanlarda (İç Anadolu); dağınık yerleşme suyun bol ve engebeli olduğu Karadeniz'de görülür."
          ],
          "pages": [
            {
              "pageNo": "1",
              "pageTitle": "1. Bölüm: Nüfusun Dağılışı ve Nedenleri",
              "text": "<div class=\"content-block\">\n  <h3>👥 Sık ve Seyrek Nüfuslu Alanlar</h3>\n  <ul>\n    <li><b>Sık Nüfuslu Alanlar:</b> Çatalca-Kocaeli (Sanayi/Ticaret), Kıyı Ege (Tarım/Turizm), Çukurova (Tarım), Doğu Karadeniz Kıyısı (Dar kıyı şeridi zorunluluğu), Gaziantep (Sanayi).</li>\n    <li><b>Seyrek Nüfuslu Alanlar (ÖSYM Favorisi):</b>\n      <ul>\n        <li><b>Teke ve Taşeli Platoları:</b> Karstik kalkerli yapı, suyun yeraltına sızması ve engebe.</li>\n        <li><b>Yıldız Dağları (Marmara):</b> Ana ulaşım yollarına sapa kalması.</li>\n        <li><b>Menteşe Yöresi (Muğla):</b> Aşırı engebe ve dağlık yapı.</li>\n        <li><b>Tuz Gölü Çevresi:</b> Kuraklık ve yağış azlığı.</li>\n        <li><b>Hakkari Bölümü:</b> Yüksek yükselti, engebe ve iklim sertliği.</li>\n      </ul>\n    </li>\n  </ul>\n</div>"
            }
          ],
          "questions": [
            {
              "id": "q_c_5",
              "level": "Kolay",
              "text": "Aşağıdaki alanların hangisinde nüfusun seyrek olmasının temel nedeni <u>karstik arazi yapısı ve aşırı engebedir</u>?",
              "options": [
                "A) Çatalca - Kocaeli",
                "B) Teke ve Taşeli Platoları",
                "C) Çukurova Deltası",
                "D) Kıyı Ege Ovaları",
                "E) Bafra Ovası"
              ],
              "correct": 1,
              "solution": "Teke ve Taşeli karstik kireç taşı erimeli yapısı ve engebesi nedeniyle seyrek nüfusludur."
            }
          ]
        },
        {
          "id": "cog_6",
          "title": "6. Türkiye'de Tarım ve Hayvancılık",
          "avgQuestions": "3 Soru",
          "summary": "Buğday, pamuk, çay, fındık, zeytin yetişme koşulları ve hayvancılık türleri dağılımı.",
          "keyPoints": [
            "GAP sulamasıyla birlikte Pamuk üretiminde 1. sıraya Şanlıurfa (Güneydoğu Anadolu) yerleşmiştir.",
            "Büyükbaş mera hayvancılığı Erzurum-Kars yaz yağışları çayırlarında yapılır.",
            "Kıl keçisi Akdeniz makiliklerinde ve karstik arazilerde yaygındır."
          ],
          "pages": [
            {
              "pageNo": "1",
              "pageTitle": "1. Bölüm: Tarım Ürünleri ve Yetişme Alanları",
              "text": "<div class=\"content-block\">\n  <h3>🌾 Başlıca Tarım Ürünleri Tablosu</h3>\n  <ul>\n    <li><b>Buğday:</b> Yetişme döneminde ilkbahar yağışı, olgunlaşma döneminde yaz kuraklığı ister. Karadeniz kıyısında (her mevsim yağışlı) yetiştirilemez. Üretimde 1. sırada <b>İç Anadolu (Konya)</b> vardır.</li>\n    <li><b>Çay:</b> Yıkanmış asitli toprak ve her mevsim nem/yağış ister. %100'ü <b>Doğu Karadeniz (Rize)</b> kıyısındadır.</li>\n    <li><b>Fındık:</b> Karadeniz iklimine özgüdür. Dünya üretiminde 1. sıradayız (Ordu, Giresun).</li>\n    <li><b>Pamuk:</b> Yaz kuraklığı ve bol sulama ister. GAP ile <b>Şanlıurfa</b> 1. sıraya çıkmıştır.</li>\n    <li><b>Zeytin:</b> Tipik Akdeniz iklim ürünüdür (Ege Bölgesi Aydın/İzmir 1. sıradadır).</li>\n  </ul>\n</div>"
            }
          ],
          "questions": [
            {
              "id": "q_c_6",
              "level": "Kolay",
              "text": "GAP projesiyle sulamanın başlaması sonucu Pamuk üretiminde 1. sıraya yerleşen ilimiz hangisidir?",
              "options": [
                "A) Adana",
                "B) Aydın",
                "C) Şanlıurfa",
                "D) Hatay",
                "E) İzmir"
              ],
              "correct": 2,
              "solution": "GAP sulamasıyla Şanlıurfa Türkiye pamuk üretiminde ilk sırayı almıştır."
            }
          ]
        },
        {
          "id": "cog_7",
          "title": "7. Türkiye'de Madenler ve Enerji Kaynakları",
          "avgQuestions": "3 Soru",
          "summary": "Bor, krom, demir, bakır, boksit, mermer madenleri; taş kömürü, linyit, jeotermal enerji.",
          "keyPoints": [
            "Bor madeninde Türkiye dünya rezervinin yaklaşık %73'üne sahiptir (Balıkesir, Kütahya, Eskişehir, Bursa).",
            "Taş kömürü Zonguldak'ta (I. Jeolojik Zaman), Linyit tüm Türkiye'de (III. Jeolojik Zaman) yaygındır.",
            "Jeotermal enerji fay hatlarına bağlı olarak Ege Bölgesi'nde (Denizli Sarayköy, Aydın Germencik) gelişmiştir."
          ],
          "pages": [
            {
              "pageNo": "1",
              "pageTitle": "1. Bölüm: Madenler ve Çıkarıldığı / İşlendiği Yerler",
              "text": "<div class=\"content-block\">\n  <h3>⛏️ Stratejik Madenlerimiz Tablosu</h3>\n  <table style=\"width:100%; border-collapse:collapse; margin:12px 0;\">\n    <tr style=\"background:#1e293b;\"><th style=\"padding:8px; border:1px solid #334155;\">Maden</th><th style=\"padding:8px; border:1px solid #334155;\">Çıkarıldığı Yerler</th><th style=\"padding:8px; border:1px solid #334155;\">İşlendiği Tesisler / Özellik</th></tr>\n    <tr><td style=\"padding:6px; border:1px solid #334155;\"><b>Bor</b></td><td style=\"padding:6px; border:1px solid #334155;\">Balıkesir (Bigadiç), Kütahya (Emet), Eskişehir (Seyitgazi), Bursa (Mustafakemalpaşa)</td><td style=\"padding:6px; border:1px solid #334155;\">Bandırma Bor Fabrikası. Dünya rezerv 1.siyiz (%73).</td></tr>\n    <tr><td style=\"padding:6px; border:1px solid #334155;\"><b>Demir</b></td><td style=\"padding:6px; border:1px solid #334155;\">Sivas (Divriği), Malatya (Hekimhan, Hasançelebi)</td><td style=\"padding:6px; border:1px solid #334155;\">Karabük, Ereğli (Kömüre yakınlık), İskenderun (Liman/Ulaşım).</td></tr>\n    <tr><td style=\"padding:6px; border:1px solid #334155;\"><b>Bakır</b></td><td style=\"padding:6px; border:1px solid #334155;\">Artvin (Murgul), Kastamonu (Küre), Elazığ (Maden)</td><td style=\"padding:6px; border:1px solid #334155;\">Samsun Bakır Fabrikası (Liman/Ulaşım).</td></tr>\n    <tr><td style=\"padding:6px; border:1px solid #334155;\"><b>Krom</b></td><td style=\"padding:6px; border:1px solid #334155;\">Elazığ (Guleman), Muğla (Fethiye/Köyceğiz)</td><td style=\"padding:6px; border:1px solid #334155;\">Antalya ve Elazığ Ferrokrom tesisleri (Paslanmaz çelik yapımı).</td></tr>\n    <tr><td style=\"padding:6px; border:1px solid #334155;\"><b>Boksit</b> (Alüminyum)</td><td style=\"padding:6px; border:1px solid #334155;\">Konya (Seydişehir), Antalya (Akseki)</td><td style=\"padding:6px; border:1px solid #334155;\">Seydişehir Alüminyum Tesisleri.</td></tr>\n  </table>\n</div>"
            }
          ],
          "questions": [
            {
              "id": "q_c_7",
              "level": "Kolay",
              "text": "Dünya rezervlerinin yaklaşık %73'üne sahip olduğumuz ve Balıkesir, Kütahya, Eskişehir'de çıkarılan maden hangisidir?",
              "options": [
                "A) Bakır",
                "B) Bor",
                "C) Krom",
                "D) Boksit",
                "E) Linyit"
              ],
              "correct": 1,
              "solution": "Bor madeninde Türkiye dünya rezerv birincisidir."
            }
          ]
        },
        {
          "id": "cog_8",
          "title": "8. Türkiye'de Sanayi, Ulaşım, Ticaret & Turizm",
          "avgQuestions": "3 Soru",
          "summary": "Sanayi tesislerinin kuruluş faktörleri, liman hinterlantları ve önemli turizm merkezleri.",
          "keyPoints": [
            "Karabük ve Ereğli'de demir-çelik sanayisinin kurulma sebebi TAŞ KÖMÜRÜNE (Enerji Kaynağına) YAKINLIKTIR.",
            "İskenderun ve Samsun'da sanayi tesislerinin kurulma sebebi LİMAN VE ULAŞIM KOLAYLIĞIDIR.",
            "Sinop limanı doğal bir liman olmasına rağmen ardındaki küre dağları (hinterland darlığı) sebebiyle gelişememiştir."
          ],
          "pages": [
            {
              "pageNo": "1",
              "pageTitle": "1. Bölüm: Sanayi Tesislerinin Yer Seçimi Faktörleri",
              "text": "<div class=\"content-block\">\n  <h3>🏭 Sanayi Tesislerinin Kuruluş Nedenleri</h3>\n  <ul>\n    <li><b>Hammaddeye Yakınlık:</b> Rize (Çay), Konya (Un/Bisküvi), Ayvalık (Zeytinyağı), Elazığ (Ferrokrom).</li>\n    <li><b>Enerji Kaynağına Yakınlık:</b> Karabük ve Ereğli Demir-Çelik Fabrikaları (Taş kömürü enerjisine yakınlık).</li>\n    <li><b>Pazara / Tüketiciye Yakınlık:</b> İstanbul, İzmir, Ankara, Bursa çevresindeki kümes hayvancılığı, unlu mamuller, konfeksiyon sanayisi.</li>\n    <li><b>Ulaşıma / Limana Yakınlık:</b> İskenderun Demir-Çelik, Samsun Bakır Fabrikası, Mersin Petrol Rafinerisi.</li>\n  </ul>\n</div>"
            }
          ],
          "questions": [
            {
              "id": "q_c_8",
              "level": "Kolay",
              "text": "Karabük ve Ereğli'de demir çıkarılmamasına rağmen demir-çelik sanayisinin kurulmasının temel sebebi nedir?",
              "options": [
                "A) Hammaddeye yakınlık",
                "B) Taş kömürüne (enerji kaynağına) yakınlık",
                "C) İş gücü bolluğu",
                "D) Tüketim merkezlerine yakınlık",
                "E) Su kaynaklarının azlığı"
              ],
              "correct": 1,
              "solution": "Zonguldak taş kömürü yataklarına yakınlık sebebiyle enerji faktöründen ötürü kurulmuştur."
            }
          ]
        }
      ]
    },
    {
      "id": "vatandaslik",
      "name": "Vatandaşlık",
      "icon": "⚖️",
      "color": "#8b5cf6",
      "questionCount": 15,
      "description": "Temel Hukuk, 1982 Anayasası, Yasama-Yürütme-Yargı, İdare Hukuku",
      "topics": [
        {
          "id": "vat_1",
          "title": "1. Temel Hukuk Kavramları (Kurallar, Yaptırımlar)",
          "avgQuestions": "3 Soru",
          "summary": "Hukuk kuralları özellikleri, yaptırım türleri (Ceza, Tazminat, Cebri İcra, İptal, Yokluk, Butlan).",
          "keyPoints": [
            "Hukuk kuralları sosyal hayatı düzenleyen MADDİ YAPTIRIMLI (devlet gücü destekli) TEK kuraldır.",
            "Yokluk: Kurucu unsuru olmayan işlem (Resmi nikah memuru olmadan kıyılan imam nikahı hukuken yoktur).",
            "Mutlak Butlan: Kurucu unsuru olan fakat emredici hükümlere aykırı olan işlem (Akıl hastasının evlenmesi)."
          ],
          "pages": [
            {
              "pageNo": "1",
              "pageTitle": "1. Bölüm: Hukuk Kuralları ve Yaptırım (Müeyyide) Türleri",
              "text": "<div class=\"content-block\">\n  <h3>⚖️ Hukuki Yaptırım (Müeyyide) Çeşitleri Tablosu</h3>\n  <table style=\"width:100%; border-collapse:collapse; margin:12px 0;\">\n    <tr style=\"background:#1e293b;\"><th style=\"padding:8px; border:1px solid #334155;\">Yaptırım</th><th style=\"padding:8px; border:1px solid #334155;\">Tanım</th><th style=\"padding:8px; border:1px solid #334155;\">Örnek</th></tr>\n    <tr><td style=\"padding:6px; border:1px solid #334155;\"><b>Ceza</b></td><td style=\"padding:6px; border:1px solid #334155;\">Suç işleyen kişiye uygulanan hapis veya adli para cezası.</td><td style=\"padding:6px; border:1px solid #334155;\">Hırsızlık yapanın hapis cezası alması.</td></tr>\n    <tr><td style=\"padding:6px; border:1px solid #334155;\"><b>Cebri İcra</b></td><td style=\"padding:6px; border:1px solid #334155;\">Borcunu ödemeyenin borcunun devlet gücüyle (haciz yoluyla) zorla tahsil edilmesi.</td><td style=\"padding:6px; border:1px solid #334155;\">Bankaya olan borç için maaşa haciz konması.</td></tr>\n    <tr><td style=\"padding:6px; border:1px solid #334155;\"><b>Tazminat</b></td><td style=\"padding:6px; border:1px solid #334155;\">Hukuka aykırı verilen zararın para ile ödetilmesi (Maddi / Manevi).</td><td style=\"padding:6px; border:1px solid #334155;\">Trafik kazasında hasar gören aracın bedelinin ödenmesi.</td></tr>\n    <tr><td style=\"padding:6px; border:1px solid #334155;\"><b>İptal</b></td><td style=\"padding:6px; border:1px solid #334155;\">Hukuka aykırı idari işlemin idari yargı (mahkeme) tarafından geçersiz kılınması.</td><td style=\"padding:6px; border:1px solid #334155;\">Haksız yıkım kararının İdare Mahkemesince iptal edilmesi.</td></tr>\n    <tr><td style=\"padding:6px; border:1px solid #334155;\"><b>Yokluk</b></td><td style=\"padding:6px; border:1px solid #334155;\">Kurucu unsuru eksik olan işlem, hukuken hiç doğmamıştır.</td><td style=\"padding:6px; border:1px solid #334155;\">Resmi nikah memuru olmadan yapılan evlilik.</td></tr>\n    <tr><td style=\"padding:6px; border:1px solid #334155;\"><b>Mutlak Butlan</b></td><td style=\"padding:6px; border:1px solid #334155;\">Kurucu unsuru var ancak kanunun emredici kuralına kesin aykırıdır.</td><td style=\"padding:6px; border:1px solid #334155;\">Ayırt etme gücü olmayan (akıl hastası) kişinin evlenmesi.</td></tr>\n  </table>\n</div>"
            }
          ],
          "questions": [
            {
              "id": "q_v_1",
              "level": "Kolay",
              "text": "Sosyal hayatı düzenleyen kurallardan hangisi <u>maddi yaptırımlı</u> (devlet gücüyle desteklenen) niteliktedir?",
              "options": [
                "A) Din Kuralları",
                "B) Ahlak Kuralları",
                "C) Görgü Kuralları",
                "D) Hukuk Kuralları",
                "E) Gelenekler"
              ],
              "correct": 3,
              "solution": "Hukuk kuralları devlet yaptırımına sahip tek maddi kuraldır."
            }
          ]
        },
        {
          "id": "vat_2",
          "title": "2. Haklar, Kişilik & Ehliyetler",
          "avgQuestions": "2 Soru",
          "summary": "Hak ehliyeti, fiil ehliyeti (tam, sınırlı ehliyetli/ehliyetsiz), hakların kazanılması ve kullanılması.",
          "keyPoints": [
            "Hakların KAZANILMASINDA İYİNİYET (Subjektif İyiniyet) geçerlidir.",
            "Hakların KULLANILMASINDA ve borçların ifasında DÜRÜSTLÜK (Objektif İyiniyet) geçerlidir.",
            "Kişilik tam ve sağ doğumla başlar, ölüm veya gaiplikle sona erer."
          ],
          "pages": [
            {
              "pageNo": "1",
              "pageTitle": "1. Bölüm: Hak ve Fiil Ehliyeti Şartları",
              "text": "<div class=\"content-block\">\n  <h3>👤 Hak Ehliyeti ve Fiil Ehliyeti Karşılaştırması</h3>\n  <ul>\n    <li><b>Hak Ehliyeti:</b> Haklara ve borçlara sahip olabilme yetkisidir. Sağ ve tam doğumla başlar (Pasif ehliyettir, herkes sahiptir).</li>\n    <li><b>Fiil Ehliyeti:</b> Kendi davranışlarıyla hak kazanabilme ve borç altına girebilme yetkisidir (Aktif ehliyet). 3 şartı vardır:\n      <ol>\n        <li><b>Ayırt etme gücüne (Temyiz kudretine) sahip olmak</b> (En önemlisidir).</li>\n        <li><b>Ergin (Reşit) olmak</b> (Kural olarak 18 yaşını doldurmuş olmak).</li>\n        <li><b>Kısıtlı (Mahcur) olmamak</b> (Akıl zayıflığı, savurganlık, alkol/uyuşturucu bağımlılığı olmamak).</li>\n      </ol>\n    </li>\n  </ul>\n</div>"
            }
          ],
          "questions": [
            {
              "id": "q_v_2",
              "level": "Kolay",
              "text": "Hakların KAZANILMASINDA geçerli olan temel medeni hukuk ilkesi hangisidir?",
              "options": [
                "A) Dürüstlük Kuralı",
                "B) İyiniyet (Subjektif İyiniyet)",
                "C) Kanunilik",
                "D) Ahde Vefa",
                "E) Müktesep Hak"
              ],
              "correct": 1,
              "solution": "Hakların kazanılmasında iyiniyet, kullanılmasında dürüstlük kuralı esastır."
            }
          ]
        },
        {
          "id": "vat_3",
          "title": "3. Anayasa Hukuku & 1982 Anayasası Genel İlkeleri",
          "avgQuestions": "2 Soru",
          "summary": "1982 Anayasası ilk 3 maddesi, değiştirilemez 4. madde, temel hak ve hürriyetlerin sınırlandırılması.",
          "keyPoints": [
            "1982 Anayasası'nın ilk 3 maddesi değiştirilemez, değiştirilmesi teklif dahi edilemez (4. Madde güvencesi).",
            "Madde 1: Türkiye Devleti bir Cumhuriyettir. Madde 2: Demokratik, laik, sosyal bir hukuk devletidir. Madde 3: Dili Türkçe, başkenti Ankara, marşı İstiklal Marşı, bayrağı ay yıldızlı al bayraktır."
          ],
          "pages": [
            {
              "pageNo": "1",
              "pageTitle": "1. Bölüm: 1982 Anayasası Değiştirilemez Maddeleri",
              "text": "<div class=\"content-block\">\n  <h3>📜 1982 Anayasası'nın İlk 4 Maddesi</h3>\n  <ul>\n    <li><b>Madde 1:</b> Türkiye Devleti bir Cumhuriyettir.</li>\n    <li><b>Madde 2:</b> Türkiye Cumhuriyeti, toplumun huzuru, milli dayanışma ve adalet anlayışı içinde, insan haklarına saygılı, Atatürk milliyetçiliğine bağlı, başlangıçta belirtilen temel ilkelere dayanan, demokratik, lâik ve sosyal bir hukuk Devletidir.</li>\n    <li><b>Madde 3:</b> Türkiye Devleti, ülkesi ve milletiyle bölünmez bir bütündür. Dili Türkçedir. Bayrağı beyaz ay yıldızlı al bayraktır. Milli marşı İstiklal Marşıdır. Başkenti Ankara'dır.</li>\n    <li><b>Madde 4:</b> Anayasanın 1 inci maddesindeki Devletin şeklinin Cumhuriyet olduğu hakkındaki hüküm ile, 2 nci maddesindeki Cumhuriyetin nitelikleri ve 3 üncü maddesi hükümleri <b>DEĞİŞTİRİLEMEZ VE DEĞİŞTİRİLMESİ TEKLİF EDİLEMEZ.</b></li>\n  </ul>\n</div>"
            }
          ],
          "questions": [
            {
              "id": "q_v_3",
              "level": "Kolay",
              "text": "1982 Anayasası'na göre devletin şeklinin Cumhuriyet olduğu ve ilk 3 maddenin değiştirilemeyeceğini düzenleyen madde hangisidir?",
              "options": [
                "A) 4. Madde",
                "B) 10. Madde",
                "C) 13. Madde",
                "D) 67. Madde",
                "E) 104. Madde"
              ],
              "correct": 0,
              "solution": "4. madde ilk 3 maddenin değiştirilemeyeceğini ve teklif dahi edilemeyeceğini hükme bağlar."
            }
          ]
        },
        {
          "id": "vat_4",
          "title": "4. Yasama Organı (TBMM 600 MV, Seçimler)",
          "avgQuestions": "3 Soru",
          "summary": "TBMM üye sayısı (600), seçilme şartları (18 yaş), 5 yıllık dönem, yasama dokunulmazlığı ve kanun yapımı.",
          "keyPoints": [
            "TBMM 600 milletvekilinden oluşur, seçimler 5 yılda bir yapılır.",
            "Milletvekili seçilme yaşı 18'dir (En az ilkokul mezunu olmak şarttır).",
            "Kanun teklif etmeye sadece MİLLETVEKİLLERİ yetkilidir (Cumhurbaşkanı sadece Bütçe Kanununu teklif eder)."
          ],
          "pages": [
            {
              "pageNo": "1",
              "pageTitle": "1. Bölüm: TBMM Yapısı ve Milletvekilliği Şartları",
              "text": "<div class=\"content-block\">\n  <h3>🏛️ Yasama Organı Temel Bilgiler</h3>\n  <ul>\n    <li><b>Milletvekili Sayısı:</b> 600 milletvekilidir (2017 değişikliği).</li>\n    <li><b>Seçim Dönemi:</b> 5 yıldır. TBMM ve Cumhurbaşkanlığı seçimleri aynı gün yapılır.</li>\n    <li><b>Milletvekili Seçilme Şartları:</b>\n      <ol>\n        <li>Türk vatandaşı olmak.</li>\n        <li><b>18 yaşını</b> doldurmuş olmak.</li>\n        <li>En az <b>ilkokul mezunu</b> olmak.</li>\n        <li>Askerlikle ilişiği bulunmamak (muaf, yapmış veya tecilli).</li>\n        <li>Kısıtlı olmamak, kamu hizmetlerinden yasaklı olmamak.</li>\n        <li>Taksirli suçlar hariç toplam 1 yıl veya daha fazla hapis cezası almamış olmak.</li>\n      </ol>\n    </li>\n  </ul>\n</div>"
            }
          ],
          "questions": [
            {
              "id": "q_v_4",
              "level": "Kolay",
              "text": "1982 Anayasası'na göre TBMM üye tam sayısı ve milletvekili seçilme yaşı sırasıyla aşağıdakilerden hangisidir?",
              "options": [
                "A) 550 / 25",
                "B) 600 / 18",
                "C) 600 / 21",
                "D) 550 / 18",
                "E) 450 / 25"
              ],
              "correct": 1,
              "solution": "2017 anayasa değişikliği ile TBMM 600 milletvekilinden oluşur ve seçilme yaşı 18'dir."
            }
          ]
        },
        {
          "id": "vat_5",
          "title": "5. Yürütme Organı (Cumhurbaşkanlığı, OHAL)",
          "avgQuestions": "2 Soru",
          "summary": "Cumhurbaşkanı seçilme şartları, görev ve yetkileri, Cumhurbaşkanlığı Kararnameleri ve OHAL ilanı.",
          "keyPoints": [
            "Cumhurbaşkanı 40 yaşını doldurmuş, yükseköğrenim mezunu Türk vatandaşları arasından halk tarafından 5 yıllığına seçilir (En fazla 2 kez).",
            "OHAL (Olağanüstü Hal) Cumhurbaşkanı tarafından en fazla 6 aylığına ilan edilir ve Resmi Gazetede yayımlanarak TBMM onayına sunulur."
          ],
          "pages": [
            {
              "pageNo": "1",
              "pageTitle": "1. Bölüm: Cumhurbaşkanlığı Sistemi Yetkileri",
              "text": "<div class=\"content-block\">\n  <h3>👑 Cumhurbaşkanının Görev ve Yetkileri</h3>\n  <ul>\n    <li>Yürütmenin başıdır, Başkomutanlığı temsil eder.</li>\n    <li>Bakanları ve Cumhurbaşkanı yardımcılarını atar ve görevlerine son verir.</li>\n    <li>Kanunları yayımlar veya tekrar görüşülmek üzere TBMM'ye geri gönderir (Veto).</li>\n    <li><b>Cumhurbaşkanlığı Kararnamesi (CBK)</b> çıkarabilir (Anayasada kanunla düzenlenmesi öngörülen konularda CBK çıkarılamaz).</li>\n    <li>Anayasa Mahkemesi üyelerinin 12'sini doğrudan veya dolaylı olarak seçer.</li>\n  </ul>\n</div>"
            }
          ],
          "questions": [
            {
              "id": "q_v_5",
              "level": "Kolay",
              "text": "1982 Anayasası'na göre Cumhurbaşkanlığı seçimleri kural olarak kaç yılda bir yapılır?",
              "options": [
                "A) 4",
                "B) 5",
                "C) 6",
                "D) 7",
                "E) 10"
              ],
              "correct": 1,
              "solution": "Cumhurbaşkanı 5 yıllık süre için halk tarafından seçilir."
            }
          ]
        },
        {
          "id": "vat_6",
          "title": "6. Yargı Organları (Anayasa Mahkemesi, Yargıtay, Danıştay)",
          "avgQuestions": "2 Soru",
          "summary": "Yüksek mahkemeler: Anayasa Mahkemesi (15 üye), Yargıtay, Danıştay, Uyuşmazlık Mahkemesi ve HSK.",
          "keyPoints": [
            "Anayasa Mahkemesi 15 üyeden oluşur (12 üyeyi Cumhurbaşkanı, 3 üyeyi TBMM seçer). Üyelerin görev süresi 12 yıldır.",
            "Danıştay: İdari yargının en üst temyiz mahkemesidir.",
            "Yargıtay: Adli yargının (ceza ve hukuk mahkemeleri) en üst temyiz merciidir."
          ],
          "pages": [
            {
              "pageNo": "1",
              "pageTitle": "1. Bölüm: Yüksek Mahkemeler Tablosu",
              "text": "<div class=\"content-block\">\n  <h3>⚖️ Yüksek Mahkemeler ve Görevleri</h3>\n  <table style=\"width:100%; border-collapse:collapse; margin:12px 0;\">\n    <tr style=\"background:#1e293b;\"><th style=\"padding:8px; border:1px solid #334155;\">Mahkeme</th><th style=\"padding:8px; border:1px solid #334155;\">Üye Sayısı / Yapısı</th><th style=\"padding:8px; border:1px solid #334155;\">Görevi</th></tr>\n    <tr><td style=\"padding:6px; border:1px solid #334155;\"><b>Anayasa Mahkemesi (AYM)</b></td><td style=\"padding:6px; border:1px solid #334155;\">15 Üye (12 CB, 3 TBMM) - 12 yıl süreyle</td><td style=\"padding:6px; border:1px solid #334155;\">Kanunların anayasaya uygunluğunu denetler, Bireysel Başvuruları inceler, Yüce Divan sıfatıyla yargılar.</td></tr>\n    <tr><td style=\"padding:6px; border:1px solid #334155;\"><b>Yargıtay</b></td><td style=\"padding:6px; border:1px solid #334155;\">Üyelerini HSK seçer.</td><td style=\"padding:6px; border:1px solid #334155;\">Adli yargı (Ceza, Hukuk) son inceleme merciidir.</td></tr>\n    <tr><td style=\"padding:6px; border:1px solid #334155;\"><b>Danıştay</b></td><td style=\"padding:6px; border:1px solid #334155;\">1/4'ünü CB, 3/4'ünü HSK seçer.</td><td style=\"padding:6px; border:1px solid #334155;\">İdari yargının son inceleme merciidir.</td></tr>\n    <tr><td style=\"padding:6px; border:1px solid #334155;\"><b>Uyuşmazlık Mahkemesi</b></td><td style=\"padding:6px; border:1px solid #334155;\">Başkanını AYM kendi üyeleri arasından seçer.</td><td style=\"padding:6px; border:1px solid #334155;\">Adli ve idari yargı arasındaki görev/hüküm uyuşmazlıklarını kesin çözer.</td></tr>\n  </table>\n</div>"
            }
          ],
          "questions": [
            {
              "id": "q_v_6",
              "level": "Kolay",
              "text": "Anayasa Mahkemesi kaç üyeden oluşur ve üyelerin görev süresi kaç yıldır?",
              "options": [
                "A) 11 Üye / 5 Yıl",
                "B) 15 Üye / 12 Yıl",
                "C) 17 Üye / 7 Yıl",
                "D) 15 Üye / Ömür Boyu",
                "E) 21 Üye / 9 Yıl"
              ],
              "correct": 1,
              "solution": "Anayasa Mahkemesi 15 üyeden oluşur ve üyeler 12 yıl için seçilir."
            }
          ]
        },
        {
          "id": "vat_7",
          "title": "7. İdare Hukuku & 657 Memur Hukuku (Disiplin Cezaları)",
          "avgQuestions": "3 Soru",
          "summary": "İdari teşkilat (Başkent, Taşra, Mahalli İdareler), 657 Memur Disiplin Cezaları ve Memuriyet şartları.",
          "keyPoints": [
            "657 Disiplin Cezaları: 1. Uyarma, 2. Kınama, 3. Aylıktan Kesme (1/30 - 1/8 arası), 4. Kademe İlerlemesinin Durdurulması (1-3 yıl), 5. Devlet Memurluğundan Çıkarma.",
            "'Sürgün, Yer Değiştirme, Görevden Uzaklaştırma' bir disiplin cezası DEĞİLDİR (Güvenlik/idari tedbirdir)."
          ],
          "pages": [
            {
              "pageNo": "1",
              "pageTitle": "1. Bölüm: 657 Sayılı Kanun Disiplin Cezaları Tablosu",
              "text": "<div class=\"content-block\">\n  <h3>⚡ 657 Sayılı DMK Disiplin Cezaları</h3>\n  <table style=\"width:100%; border-collapse:collapse; margin:12px 0;\">\n    <tr style=\"background:#1e293b;\"><th style=\"padding:8px; border:1px solid #334155;\">Ceza Türü</th><th style=\"padding:8px; border:1px solid #334155;\">Örnek Fiil</th><th style=\"padding:8px; border:1px solid #334155;\">Cezayı Veren Makam</th></tr>\n    <tr><td style=\"padding:6px; border:1px solid #334155;\"><b>1. Uyarma</b></td><td style=\"padding:6px; border:1px solid #334155;\">Görevde kayıtsızlık, özürsüz göreve geç gelme.</td><td style=\"padding:6px; border:1px solid #334155;\">Disiplin Amiri</td></tr>\n    <tr><td style=\"padding:6px; border:1px solid #334155;\"><b>2. Kınama</b></td><td style=\"padding:6px; border:1px solid #334155;\">Devlete ait araç/gereci özel işinde kullanma, borçlarını kasten ödememe.</td><td style=\"padding:6px; border:1px solid #334155;\">Disiplin Amiri</td></tr>\n    <tr><td style=\"padding:6px; border:1px solid #334155;\"><b>3. Aylıktan Kesme</b></td><td style=\"padding:6px; border:1px solid #334155;\">Brüt aylıktan 1/30 - 1/8 oranında kesinti. Özürsüz 1-2 gün göreve gelmeme.</td><td style=\"padding:6px; border:1px solid #334155;\">Disiplin Amiri</td></tr>\n    <tr><td style=\"padding:6px; border:1px solid #334155;\"><b>4. Kademe İlerlemesini Durdurma</b></td><td style=\"padding:6px; border:1px solid #334155;\">1 - 3 yıl durdurma. Göreve sarhoş gelme, özürsüz 3-9 gün göreve gelmeme.</td><td style=\"padding:6px; border:1px solid #334155;\">İl Disiplin Kurulu kararıyla Atamaya Yetkili Amir</td></tr>\n    <tr><td style=\"padding:6px; border:1px solid #334155;\"><b>5. Memurluktan Çıkarma</b></td><td style=\"padding:6px; border:1px solid #334155;\">Özürsüz kesintisiz 10 gün göreve gelmeme (veya yılda toplam 20 gün), terör/yüz kızartıcı suç.</td><td style=\"padding:6px; border:1px solid #334155;\"><b>Yüksek Disiplin Kurulu</b></td></tr>\n  </table>\n</div>"
            }
          ],
          "questions": [
            {
              "id": "q_v_7",
              "level": "Orta",
              "text": "Aşağıdakilerden hangisi 657 Sayılı Devlet Memurları Kanunu'nda sayılan disiplin cezalarından biri DEĞİLDİR?",
              "options": [
                "A) Uyarma",
                "B) Kınama",
                "C) Aylıktan Kesme",
                "D) Sürgün / Görev Yeri Değişikliği",
                "E) Kademe İlerlemesinin Durdurulması"
              ],
              "correct": 3,
              "solution": "Sürgün 657 sayılı kanunda bir disiplin cezası değildir."
            }
          ]
        },
        {
          "id": "vat_8",
          "title": "8. Güncel Bilgiler, UNESCO Mirası & Uluslararası Kuruluşlar",
          "avgQuestions": "3 Soru",
          "summary": "Göbeklitepe, UNESCO Dünya Mirasları, BM, NATO, AİHM, Türk Devletleri Teşkilatı.",
          "keyPoints": [
            "Göbeklitepe Şanlıurfa'da yer alan dünyanın bilinen en eski tapınak kompleksidir (UNESCO).",
            "AİHM (Avrupa İnsan Hakları Mahkemesi) Fransa'nın Strazburg kentindedir.",
            "Türkiye 1952 yılında NATO'ya üye olmuştur."
          ],
          "pages": [
            {
              "pageNo": "1",
              "pageTitle": "1. Bölüm: UNESCO Miraslarımız ve Uluslararası Kuruluşlar",
              "text": "<div class=\"content-block\">\n  <h3>🌍 Önemli Güncel Bilgiler ve Uluslararası Merkezler</h3>\n  <ul>\n    <li><b>Göbeklitepe:</b> Şanlıurfa ilimizdedir. Tarihin sıfır noktası kabul edilir.</li>\n    <li><b>UNESCO Dünya Mirası Listesi Önemli Varlıklarımız:</b> Divriği Ulu Camii (Sivas), Nemrut Dağı (Adıyaman), Çatalhöyük (Konya), Afrodisias (Aydın), Göreme ve Kapadokya (Nevşehir), Pamukkale (Denizli), Gordion (Ankara - 2023), Arslantepe Höyüğü (Malatya).</li>\n    <li><b>Uluslararası Kuruluş Merkezleri:</b>\n      <ul>\n        <li>Birleşmiş Milletler (BM): New York (ABD)</li>\n        <li>NATO: Brüksel (Belçika) - Türkiye 1952'de üye oldu.</li>\n        <li>AİHM (Avrupa İnsan Hakları Mahkemesi): Strazburg (Fransa)</li>\n        <li>UNESCO: Paris (Fransa)</li>\n      </ul>\n    </li>\n  </ul>\n</div>"
            }
          ],
          "questions": [
            {
              "id": "q_v_8",
              "level": "Kolay",
              "text": "Dünyanın bilinen en eski tapınak kompleksi kabul edilen Göbeklitepe hangi ilimizde yer almaktadır?",
              "options": [
                "A) Gaziantep",
                "B) Şanlıurfa",
                "C) Mardin",
                "D) Adıyaman",
                "E) Diyarbakır"
              ],
              "correct": 1,
              "solution": "Göbeklitepe Şanlıurfa ilimizde yer almaktadır."
            }
          ]
        }
      ]
    }
  ],
  "studyPlan": [
    {
      "week": 1,
      "title": "1. Hafta: Temelleri Atma & Türkçe-Matematik Başlangıcı",
      "hoursPerDay": "3-4 Saat",
      "focus": "Matematik: Temel Kavramlar & Türkçe: Sözcükte ve Cümlede Anlam",
      "tasks": [
        "Matematik: Tek-Çift sayılar, Pozitif-Negatif sayılar soru çözümü (50 soru)",
        "Türkçe: Sözcükte anlam ve söz öbekleri bol örnek (40 soru)",
        "Tarih: İslamiyet Öncesi Türk Tarihi konu özet okuması"
      ]
    }
  ],
  "mockExam": {
    "id": "deneme_1",
    "title": "KPSS 2026 Ortaöğretim - 1. Deneme Sınavı (120 Soru)",
    "totalDurationMinutes": 130,
    "questions": [
      {
        "id": "e1_q1",
        "subject": "Türkçe",
        "number": 1,
        "text": "1. Aşağıdaki cümlelerin hangisinde <u>'açık'</u> sözcüğü 'gizliliği olmayan, herkesçe bilinen' anlamında kullanılmıştır?",
        "options": [
          "A) Pencerenin kenarındaki nesne yere düştü.",
          "B) Bu konuda <u>açık</u> bir tavır sergilemesi herkesi rahatlattı.",
          "C) Günün ilk saatlerinde dışarıda serin bir hava vardı.",
          "D) Bahçedeki ağaçların gölgesinde dinlenmeyi seçti.",
          "E) Kitaplarını çantasına özenle yerleştirdi."
        ],
        "correct": 1,
        "solution": "Seçenekteki 'açık' kelimesi mecazi olarak 'gizliliği olmayan, herkesçe bilinen' anlamında kullanılmıştır."
      },
      {
        "id": "e1_q2",
        "subject": "Türkçe",
        "number": 2,
        "text": "2. Aşağıdaki cümlelerin hangisinde <u>'göze girmek'</u> deyimi 'ilgi ve güven kazanmak' anlamında kullanılmıştır?",
        "options": [
          "A) Çalışkanlığıyla kısa sürede amirlerinin <u>gözüne girmeyi</u> başardı.",
          "B) Kütüphanedeki sessizliği kimse bozmak istemiyordu.",
          "C) Tren vaktinde istasyona yanaşarak yolcularını aldı.",
          "D) Bahçede rengarenk çiçekler açmıştı.",
          "E) Raporun son halini inceleyip imzaladı."
        ],
        "correct": 0,
        "solution": "Deyim cümlede 'ilgi ve güven kazanmak' anlamını karşılayacak şekilde yer almıştır."
      },
      {
        "id": "e1_q3",
        "subject": "Türkçe",
        "number": 3,
        "text": "3. (I) Şairin 13 yılında yayımlanan bu eseri yoğun bir ilgi gördü. (II) Kitapta yer alan imgeler okurun hayal dünyasını zenginleştiriyor. (III) Eser toplam 120 sayfadan ve 45 şiirden oluşmaktadır. (IV) Bence dönemin en başarılı şiir kitabı budur. (V) Kitabın ikinci baskısı geçen ay yapıldı.\n\nBu parçadaki numaralanmış cümlelerden hangisi <u>öznel</u> bir yargı içermektedir?",
        "options": [
          "A) I ve III",
          "B) II ve IV",
          "C) III ve V",
          "D) Yalnız I",
          "E) Yalnız V"
        ],
        "correct": 1,
        "solution": "II ve IV numaralı cümleler yazarın kişisel beğeni ve yorumunu içerdiği için öznel yargılardır."
      },
      {
        "id": "e1_q4",
        "subject": "Türkçe",
        "number": 4,
        "text": "4. (I) Şairin 14 yılında yayımlanan bu eseri yoğun bir ilgi gördü. (II) Kitapta yer alan imgeler okurun hayal dünyasını zenginleştiriyor. (III) Eser toplam 120 sayfadan ve 45 şiirden oluşmaktadır. (IV) Bence dönemin en başarılı şiir kitabı budur. (V) Kitabın ikinci baskısı geçen ay yapıldı.\n\nBu parçadaki numaralanmış cümlelerden hangisi <u>öznel</u> bir yargı içermektedir?",
        "options": [
          "A) I ve III",
          "B) II ve IV",
          "C) III ve V",
          "D) Yalnız I",
          "E) Yalnız V"
        ],
        "correct": 1,
        "solution": "II ve IV numaralı cümleler yazarın kişisel beğeni ve yorumunu içerdiği için öznel yargılardır."
      },
      {
        "id": "e1_q5",
        "subject": "Türkçe",
        "number": 5,
        "text": "5. (I) Şairin 15 yılında yayımlanan bu eseri yoğun bir ilgi gördü. (II) Kitapta yer alan imgeler okurun hayal dünyasını zenginleştiriyor. (III) Eser toplam 120 sayfadan ve 45 şiirden oluşmaktadır. (IV) Bence dönemin en başarılı şiir kitabı budur. (V) Kitabın ikinci baskısı geçen ay yapıldı.\n\nBu parçadaki numaralanmış cümlelerden hangisi <u>öznel</u> bir yargı içermektedir?",
        "options": [
          "A) I ve III",
          "B) II ve IV",
          "C) III ve V",
          "D) Yalnız I",
          "E) Yalnız V"
        ],
        "correct": 1,
        "solution": "II ve IV numaralı cümleler yazarın kişisel beğeni ve yorumunu içerdiği için öznel yargılardır."
      },
      {
        "id": "e1_q6",
        "subject": "Türkçe",
        "number": 6,
        "text": "6. (I) Şairin 16 yılında yayımlanan bu eseri yoğun bir ilgi gördü. (II) Kitapta yer alan imgeler okurun hayal dünyasını zenginleştiriyor. (III) Eser toplam 120 sayfadan ve 45 şiirden oluşmaktadır. (IV) Bence dönemin en başarılı şiir kitabı budur. (V) Kitabın ikinci baskısı geçen ay yapıldı.\n\nBu parçadaki numaralanmış cümlelerden hangisi <u>öznel</u> bir yargı içermektedir?",
        "options": [
          "A) I ve III",
          "B) II ve IV",
          "C) III ve V",
          "D) Yalnız I",
          "E) Yalnız V"
        ],
        "correct": 1,
        "solution": "II ve IV numaralı cümleler yazarın kişisel beğeni ve yorumunu içerdiği için öznel yargılardır."
      },
      {
        "id": "e1_q7",
        "subject": "Türkçe",
        "number": 7,
        "text": "7. (I) Şairin 17 yılında yayımlanan bu eseri yoğun bir ilgi gördü. (II) Kitapta yer alan imgeler okurun hayal dünyasını zenginleştiriyor. (III) Eser toplam 120 sayfadan ve 45 şiirden oluşmaktadır. (IV) Bence dönemin en başarılı şiir kitabı budur. (V) Kitabın ikinci baskısı geçen ay yapıldı.\n\nBu parçadaki numaralanmış cümlelerden hangisi <u>öznel</u> bir yargı içermektedir?",
        "options": [
          "A) I ve III",
          "B) II ve IV",
          "C) III ve V",
          "D) Yalnız I",
          "E) Yalnız V"
        ],
        "correct": 1,
        "solution": "II ve IV numaralı cümleler yazarın kişisel beğeni ve yorumunu içerdiği için öznel yargılardır."
      },
      {
        "id": "e1_q8",
        "subject": "Türkçe",
        "number": 8,
        "text": "8. (I) Şairin 18 yılında yayımlanan bu eseri yoğun bir ilgi gördü. (II) Kitapta yer alan imgeler okurun hayal dünyasını zenginleştiriyor. (III) Eser toplam 120 sayfadan ve 45 şiirden oluşmaktadır. (IV) Bence dönemin en başarılı şiir kitabı budur. (V) Kitabın ikinci baskısı geçen ay yapıldı.\n\nBu parçadaki numaralanmış cümlelerden hangisi <u>öznel</u> bir yargı içermektedir?",
        "options": [
          "A) I ve III",
          "B) II ve IV",
          "C) III ve V",
          "D) Yalnız I",
          "E) Yalnız V"
        ],
        "correct": 1,
        "solution": "II ve IV numaralı cümleler yazarın kişisel beğeni ve yorumunu içerdiği için öznel yargılardır."
      },
      {
        "id": "e1_q9",
        "subject": "Türkçe",
        "number": 9,
        "text": "9. (I) Şairin 19 yılında yayımlanan bu eseri yoğun bir ilgi gördü. (II) Kitapta yer alan imgeler okurun hayal dünyasını zenginleştiriyor. (III) Eser toplam 120 sayfadan ve 45 şiirden oluşmaktadır. (IV) Bence dönemin en başarılı şiir kitabı budur. (V) Kitabın ikinci baskısı geçen ay yapıldı.\n\nBu parçadaki numaralanmış cümlelerden hangisi <u>öznel</u> bir yargı içermektedir?",
        "options": [
          "A) I ve III",
          "B) II ve IV",
          "C) III ve V",
          "D) Yalnız I",
          "E) Yalnız V"
        ],
        "correct": 1,
        "solution": "II ve IV numaralı cümleler yazarın kişisel beğeni ve yorumunu içerdiği için öznel yargılardır."
      },
      {
        "id": "e1_q10",
        "subject": "Türkçe",
        "number": 10,
        "text": "10. (I) Şairin 20 yılında yayımlanan bu eseri yoğun bir ilgi gördü. (II) Kitapta yer alan imgeler okurun hayal dünyasını zenginleştiriyor. (III) Eser toplam 120 sayfadan ve 45 şiirden oluşmaktadır. (IV) Bence dönemin en başarılı şiir kitabı budur. (V) Kitabın ikinci baskısı geçen ay yapıldı.\n\nBu parçadaki numaralanmış cümlelerden hangisi <u>öznel</u> bir yargı içermektedir?",
        "options": [
          "A) I ve III",
          "B) II ve IV",
          "C) III ve V",
          "D) Yalnız I",
          "E) Yalnız V"
        ],
        "correct": 1,
        "solution": "II ve IV numaralı cümleler yazarın kişisel beğeni ve yorumunu içerdiği için öznel yargılardır."
      },
      {
        "id": "e1_q11",
        "subject": "Türkçe",
        "number": 11,
        "text": "11. Gerçek sanatçı, çağının tanığı olmakla kalmaz; aynı zamanda geleceğe ışık tutan bir deniz feneri gibidir. O, toplumun duygu ve düşüncelerini kendi estetik süzgecinden geçirerek evrensel bir dille insanlığa sunar. Sadece günü kurtarmayı hedefleyen yapıtlar zamanın acımasız çarkları arasında yok olup gitmeye mahkumdur.\n\nBu parçada asıl anlatılmak istenen (<u>ana düşünce</u>) aşağıdakilerden hangisidir?",
        "options": [
          "A) Sanatçının yalnızca kendi toplumunu anlatması gerektiği",
          "B) Kalıcı ve gerçek sanat eserlerinin evrensel nitelik ve ileri görüşlülük taşıdığı",
          "C) Günlük olayların sanat eserlerinde işlenmesinin önemi",
          "D) Sanatın toplumdan tamamen bağımsız geliştiği",
          "E) Başarılı yapıtların sadece geçmişe odaklandığı"
        ],
        "correct": 1,
        "solution": "Paragrafta kalıcı sanatçının çağını aşıp evrensel değerlerle geleceğe yön verdiği vurgulanmaktadır."
      },
      {
        "id": "e1_q12",
        "subject": "Türkçe",
        "number": 12,
        "text": "12. Gerçek sanatçı, çağının tanığı olmakla kalmaz; aynı zamanda geleceğe ışık tutan bir deniz feneri gibidir. O, toplumun duygu ve düşüncelerini kendi estetik süzgecinden geçirerek evrensel bir dille insanlığa sunar. Sadece günü kurtarmayı hedefleyen yapıtlar zamanın acımasız çarkları arasında yok olup gitmeye mahkumdur.\n\nBu parçada asıl anlatılmak istenen (<u>ana düşünce</u>) aşağıdakilerden hangisidir?",
        "options": [
          "A) Sanatçının yalnızca kendi toplumunu anlatması gerektiği",
          "B) Kalıcı ve gerçek sanat eserlerinin evrensel nitelik ve ileri görüşlülük taşıdığı",
          "C) Günlük olayların sanat eserlerinde işlenmesinin önemi",
          "D) Sanatın toplumdan tamamen bağımsız geliştiği",
          "E) Başarılı yapıtların sadece geçmişe odaklandığı"
        ],
        "correct": 1,
        "solution": "Paragrafta kalıcı sanatçının çağını aşıp evrensel değerlerle geleceğe yön verdiği vurgulanmaktadır."
      },
      {
        "id": "e1_q13",
        "subject": "Türkçe",
        "number": 13,
        "text": "13. Gerçek sanatçı, çağının tanığı olmakla kalmaz; aynı zamanda geleceğe ışık tutan bir deniz feneri gibidir. O, toplumun duygu ve düşüncelerini kendi estetik süzgecinden geçirerek evrensel bir dille insanlığa sunar. Sadece günü kurtarmayı hedefleyen yapıtlar zamanın acımasız çarkları arasında yok olup gitmeye mahkumdur.\n\nBu parçada asıl anlatılmak istenen (<u>ana düşünce</u>) aşağıdakilerden hangisidir?",
        "options": [
          "A) Sanatçının yalnızca kendi toplumunu anlatması gerektiği",
          "B) Kalıcı ve gerçek sanat eserlerinin evrensel nitelik ve ileri görüşlülük taşıdığı",
          "C) Günlük olayların sanat eserlerinde işlenmesinin önemi",
          "D) Sanatın toplumdan tamamen bağımsız geliştiği",
          "E) Başarılı yapıtların sadece geçmişe odaklandığı"
        ],
        "correct": 1,
        "solution": "Paragrafta kalıcı sanatçının çağını aşıp evrensel değerlerle geleceğe yön verdiği vurgulanmaktadır."
      },
      {
        "id": "e1_q14",
        "subject": "Türkçe",
        "number": 14,
        "text": "14. Gerçek sanatçı, çağının tanığı olmakla kalmaz; aynı zamanda geleceğe ışık tutan bir deniz feneri gibidir. O, toplumun duygu ve düşüncelerini kendi estetik süzgecinden geçirerek evrensel bir dille insanlığa sunar. Sadece günü kurtarmayı hedefleyen yapıtlar zamanın acımasız çarkları arasında yok olup gitmeye mahkumdur.\n\nBu parçada asıl anlatılmak istenen (<u>ana düşünce</u>) aşağıdakilerden hangisidir?",
        "options": [
          "A) Sanatçının yalnızca kendi toplumunu anlatması gerektiği",
          "B) Kalıcı ve gerçek sanat eserlerinin evrensel nitelik ve ileri görüşlülük taşıdığı",
          "C) Günlük olayların sanat eserlerinde işlenmesinin önemi",
          "D) Sanatın toplumdan tamamen bağımsız geliştiği",
          "E) Başarılı yapıtların sadece geçmişe odaklandığı"
        ],
        "correct": 1,
        "solution": "Paragrafta kalıcı sanatçının çağını aşıp evrensel değerlerle geleceğe yön verdiği vurgulanmaktadır."
      },
      {
        "id": "e1_q15",
        "subject": "Türkçe",
        "number": 15,
        "text": "15. Gerçek sanatçı, çağının tanığı olmakla kalmaz; aynı zamanda geleceğe ışık tutan bir deniz feneri gibidir. O, toplumun duygu ve düşüncelerini kendi estetik süzgecinden geçirerek evrensel bir dille insanlığa sunar. Sadece günü kurtarmayı hedefleyen yapıtlar zamanın acımasız çarkları arasında yok olup gitmeye mahkumdur.\n\nBu parçada asıl anlatılmak istenen (<u>ana düşünce</u>) aşağıdakilerden hangisidir?",
        "options": [
          "A) Sanatçının yalnızca kendi toplumunu anlatması gerektiği",
          "B) Kalıcı ve gerçek sanat eserlerinin evrensel nitelik ve ileri görüşlülük taşıdığı",
          "C) Günlük olayların sanat eserlerinde işlenmesinin önemi",
          "D) Sanatın toplumdan tamamen bağımsız geliştiği",
          "E) Başarılı yapıtların sadece geçmişe odaklandığı"
        ],
        "correct": 1,
        "solution": "Paragrafta kalıcı sanatçının çağını aşıp evrensel değerlerle geleceğe yön verdiği vurgulanmaktadır."
      },
      {
        "id": "e1_q16",
        "subject": "Türkçe",
        "number": 16,
        "text": "16. Gerçek sanatçı, çağının tanığı olmakla kalmaz; aynı zamanda geleceğe ışık tutan bir deniz feneri gibidir. O, toplumun duygu ve düşüncelerini kendi estetik süzgecinden geçirerek evrensel bir dille insanlığa sunar. Sadece günü kurtarmayı hedefleyen yapıtlar zamanın acımasız çarkları arasında yok olup gitmeye mahkumdur.\n\nBu parçada asıl anlatılmak istenen (<u>ana düşünce</u>) aşağıdakilerden hangisidir?",
        "options": [
          "A) Sanatçının yalnızca kendi toplumunu anlatması gerektiği",
          "B) Kalıcı ve gerçek sanat eserlerinin evrensel nitelik ve ileri görüşlülük taşıdığı",
          "C) Günlük olayların sanat eserlerinde işlenmesinin önemi",
          "D) Sanatın toplumdan tamamen bağımsız geliştiği",
          "E) Başarılı yapıtların sadece geçmişe odaklandığı"
        ],
        "correct": 1,
        "solution": "Paragrafta kalıcı sanatçının çağını aşıp evrensel değerlerle geleceğe yön verdiği vurgulanmaktadır."
      },
      {
        "id": "e1_q17",
        "subject": "Türkçe",
        "number": 17,
        "text": "17. Gerçek sanatçı, çağının tanığı olmakla kalmaz; aynı zamanda geleceğe ışık tutan bir deniz feneri gibidir. O, toplumun duygu ve düşüncelerini kendi estetik süzgecinden geçirerek evrensel bir dille insanlığa sunar. Sadece günü kurtarmayı hedefleyen yapıtlar zamanın acımasız çarkları arasında yok olup gitmeye mahkumdur.\n\nBu parçada asıl anlatılmak istenen (<u>ana düşünce</u>) aşağıdakilerden hangisidir?",
        "options": [
          "A) Sanatçının yalnızca kendi toplumunu anlatması gerektiği",
          "B) Kalıcı ve gerçek sanat eserlerinin evrensel nitelik ve ileri görüşlülük taşıdığı",
          "C) Günlük olayların sanat eserlerinde işlenmesinin önemi",
          "D) Sanatın toplumdan tamamen bağımsız geliştiği",
          "E) Başarılı yapıtların sadece geçmişe odaklandığı"
        ],
        "correct": 1,
        "solution": "Paragrafta kalıcı sanatçının çağını aşıp evrensel değerlerle geleceğe yön verdiği vurgulanmaktadır."
      },
      {
        "id": "e1_q18",
        "subject": "Türkçe",
        "number": 18,
        "text": "18. Gerçek sanatçı, çağının tanığı olmakla kalmaz; aynı zamanda geleceğe ışık tutan bir deniz feneri gibidir. O, toplumun duygu ve düşüncelerini kendi estetik süzgecinden geçirerek evrensel bir dille insanlığa sunar. Sadece günü kurtarmayı hedefleyen yapıtlar zamanın acımasız çarkları arasında yok olup gitmeye mahkumdur.\n\nBu parçada asıl anlatılmak istenen (<u>ana düşünce</u>) aşağıdakilerden hangisidir?",
        "options": [
          "A) Sanatçının yalnızca kendi toplumunu anlatması gerektiği",
          "B) Kalıcı ve gerçek sanat eserlerinin evrensel nitelik ve ileri görüşlülük taşıdığı",
          "C) Günlük olayların sanat eserlerinde işlenmesinin önemi",
          "D) Sanatın toplumdan tamamen bağımsız geliştiği",
          "E) Başarılı yapıtların sadece geçmişe odaklandığı"
        ],
        "correct": 1,
        "solution": "Paragrafta kalıcı sanatçının çağını aşıp evrensel değerlerle geleceğe yön verdiği vurgulanmaktadır."
      },
      {
        "id": "e1_q19",
        "subject": "Türkçe",
        "number": 19,
        "text": "19. Gerçek sanatçı, çağının tanığı olmakla kalmaz; aynı zamanda geleceğe ışık tutan bir deniz feneri gibidir. O, toplumun duygu ve düşüncelerini kendi estetik süzgecinden geçirerek evrensel bir dille insanlığa sunar. Sadece günü kurtarmayı hedefleyen yapıtlar zamanın acımasız çarkları arasında yok olup gitmeye mahkumdur.\n\nBu parçada asıl anlatılmak istenen (<u>ana düşünce</u>) aşağıdakilerden hangisidir?",
        "options": [
          "A) Sanatçının yalnızca kendi toplumunu anlatması gerektiği",
          "B) Kalıcı ve gerçek sanat eserlerinin evrensel nitelik ve ileri görüşlülük taşıdığı",
          "C) Günlük olayların sanat eserlerinde işlenmesinin önemi",
          "D) Sanatın toplumdan tamamen bağımsız geliştiği",
          "E) Başarılı yapıtların sadece geçmişe odaklandığı"
        ],
        "correct": 1,
        "solution": "Paragrafta kalıcı sanatçının çağını aşıp evrensel değerlerle geleceğe yön verdiği vurgulanmaktadır."
      },
      {
        "id": "e1_q20",
        "subject": "Türkçe",
        "number": 20,
        "text": "20. Gerçek sanatçı, çağının tanığı olmakla kalmaz; aynı zamanda geleceğe ışık tutan bir deniz feneri gibidir. O, toplumun duygu ve düşüncelerini kendi estetik süzgecinden geçirerek evrensel bir dille insanlığa sunar. Sadece günü kurtarmayı hedefleyen yapıtlar zamanın acımasız çarkları arasında yok olup gitmeye mahkumdur.\n\nBu parçada asıl anlatılmak istenen (<u>ana düşünce</u>) aşağıdakilerden hangisidir?",
        "options": [
          "A) Sanatçının yalnızca kendi toplumunu anlatması gerektiği",
          "B) Kalıcı ve gerçek sanat eserlerinin evrensel nitelik ve ileri görüşlülük taşıdığı",
          "C) Günlük olayların sanat eserlerinde işlenmesinin önemi",
          "D) Sanatın toplumdan tamamen bağımsız geliştiği",
          "E) Başarılı yapıtların sadece geçmişe odaklandığı"
        ],
        "correct": 1,
        "solution": "Paragrafta kalıcı sanatçının çağını aşıp evrensel değerlerle geleceğe yön verdiği vurgulanmaktadır."
      },
      {
        "id": "e1_q21",
        "subject": "Türkçe",
        "number": 21,
        "text": "21. Aşağıdaki cümlelerin hangisinde bir <u>yazım yanlışı</u> yapılmıştır?",
        "options": [
          "A) Türk Dil Kurumu yeni kılavuzunu yayımladı.",
          "B) 1. yüzyılda pek çok önemli gelişme yaşandı.",
          "C) Bu konuda <u>herşey</u> planlandığı gibi gidiyor.",
          "D) TBMM'nin aldığı tarihi karar Resmi Gazete'de duyuruldu.",
          "E) Yanı sıra pek çok yabancı konuk da törene katıldı."
        ],
        "correct": 2,
        "solution": "'Herşey' sözcüğü 'Her şey' şeklinde ayrı yazılmalıdır. Şey sözcüğü daima ayrı yazılır."
      },
      {
        "id": "e1_q22",
        "subject": "Türkçe",
        "number": 22,
        "text": "22. Aşağıdaki cümlelerin hangisinde bir <u>yazım yanlışı</u> yapılmıştır?",
        "options": [
          "A) Türk Dil Kurumu yeni kılavuzunu yayımladı.",
          "B) 1. yüzyılda pek çok önemli gelişme yaşandı.",
          "C) Bu konuda <u>herşey</u> planlandığı gibi gidiyor.",
          "D) TBMM'nin aldığı tarihi karar Resmi Gazete'de duyuruldu.",
          "E) Yanı sıra pek çok yabancı konuk da törene katıldı."
        ],
        "correct": 2,
        "solution": "'Herşey' sözcüğü 'Her şey' şeklinde ayrı yazılmalıdır. Şey sözcüğü daima ayrı yazılır."
      },
      {
        "id": "e1_q23",
        "subject": "Türkçe",
        "number": 23,
        "text": "23. Aşağıdaki cümlelerin hangisinde bir <u>yazım yanlışı</u> yapılmıştır?",
        "options": [
          "A) Türk Dil Kurumu yeni kılavuzunu yayımladı.",
          "B) 1. yüzyılda pek çok önemli gelişme yaşandı.",
          "C) Bu konuda <u>herşey</u> planlandığı gibi gidiyor.",
          "D) TBMM'nin aldığı tarihi karar Resmi Gazete'de duyuruldu.",
          "E) Yanı sıra pek çok yabancı konuk da törene katıldı."
        ],
        "correct": 2,
        "solution": "'Herşey' sözcüğü 'Her şey' şeklinde ayrı yazılmalıdır. Şey sözcüğü daima ayrı yazılır."
      },
      {
        "id": "e1_q24",
        "subject": "Türkçe",
        "number": 24,
        "text": "24. Aşağıdaki cümlelerin hangisinde bir <u>yazım yanlışı</u> yapılmıştır?",
        "options": [
          "A) Türk Dil Kurumu yeni kılavuzunu yayımladı.",
          "B) 1. yüzyılda pek çok önemli gelişme yaşandı.",
          "C) Bu konuda <u>herşey</u> planlandığı gibi gidiyor.",
          "D) TBMM'nin aldığı tarihi karar Resmi Gazete'de duyuruldu.",
          "E) Yanı sıra pek çok yabancı konuk da törene katıldı."
        ],
        "correct": 2,
        "solution": "'Herşey' sözcüğü 'Her şey' şeklinde ayrı yazılmalıdır. Şey sözcüğü daima ayrı yazılır."
      },
      {
        "id": "e1_q25",
        "subject": "Türkçe",
        "number": 25,
        "text": "25. Aşağıdaki cümlelerin hangisinde bir <u>yazım yanlışı</u> yapılmıştır?",
        "options": [
          "A) Türk Dil Kurumu yeni kılavuzunu yayımladı.",
          "B) 1. yüzyılda pek çok önemli gelişme yaşandı.",
          "C) Bu konuda <u>herşey</u> planlandığı gibi gidiyor.",
          "D) TBMM'nin aldığı tarihi karar Resmi Gazete'de duyuruldu.",
          "E) Yanı sıra pek çok yabancı konuk da törene katıldı."
        ],
        "correct": 2,
        "solution": "'Herşey' sözcüğü 'Her şey' şeklinde ayrı yazılmalıdır. Şey sözcüğü daima ayrı yazılır."
      },
      {
        "id": "e1_q26",
        "subject": "Türkçe",
        "number": 26,
        "text": "26. Yaşlı adam kapıyı açtı ( ) içeriye doğru yavaşça adım attı ( ) Genç çocuk merakla sordu ( ) 'Burada ne arıyorsunuz ( )'\n\nBu parçada parantezle belirtilen yerlere sırasıyla hangi noktalama işaretleri getirilmelidir?",
        "options": [
          "A) (,) (.) (:) (?)",
          "B) (;) (.) (,) (!)",
          "C) (,) (;) (:) (.)",
          "D) (.) (,) (:) (?)",
          "E) (,) (.) (;) (!)"
        ],
        "correct": 0,
        "solution": "Sıralı cümle için virgül (,), cümle sonuna nokta (.), konuşmadan önce iki nokta (:) ve soru cümlesi sonuna soru işareti (?) gelir."
      },
      {
        "id": "e1_q27",
        "subject": "Türkçe",
        "number": 27,
        "text": "27. Yaşlı adam kapıyı açtı ( ) içeriye doğru yavaşça adım attı ( ) Genç çocuk merakla sordu ( ) 'Burada ne arıyorsunuz ( )'\n\nBu parçada parantezle belirtilen yerlere sırasıyla hangi noktalama işaretleri getirilmelidir?",
        "options": [
          "A) (,) (.) (:) (?)",
          "B) (;) (.) (,) (!)",
          "C) (,) (;) (:) (.)",
          "D) (.) (,) (:) (?)",
          "E) (,) (.) (;) (!)"
        ],
        "correct": 0,
        "solution": "Sıralı cümle için virgül (,), cümle sonuna nokta (.), konuşmadan önce iki nokta (:) ve soru cümlesi sonuna soru işareti (?) gelir."
      },
      {
        "id": "e1_q28",
        "subject": "Türkçe",
        "number": 28,
        "text": "28. Yaşlı adam kapıyı açtı ( ) içeriye doğru yavaşça adım attı ( ) Genç çocuk merakla sordu ( ) 'Burada ne arıyorsunuz ( )'\n\nBu parçada parantezle belirtilen yerlere sırasıyla hangi noktalama işaretleri getirilmelidir?",
        "options": [
          "A) (,) (.) (:) (?)",
          "B) (;) (.) (,) (!)",
          "C) (,) (;) (:) (.)",
          "D) (.) (,) (:) (?)",
          "E) (,) (.) (;) (!)"
        ],
        "correct": 0,
        "solution": "Sıralı cümle için virgül (,), cümle sonuna nokta (.), konuşmadan önce iki nokta (:) ve soru cümlesi sonuna soru işareti (?) gelir."
      },
      {
        "id": "e1_q29",
        "subject": "Türkçe",
        "number": 29,
        "text": "29. '<u>Günün erken saatlerinde</u> bahçedeki çiçekleri sulayan ihtiyar adam, komşusuna selam verdi.' cümlesinde altı çizili öge cümlenin hangi ögesidir?",
        "options": [
          "A) Özne",
          "B) Belirtili Nesne",
          "C) Zarf Tümleci",
          "D) Dolaylı Tümleç",
          "E) Yüklem"
        ],
        "correct": 2,
        "solution": "Yükleme sorulan 'Ne zaman?' sorusuna yanıt verdiği için Zarf Tümlecidir."
      },
      {
        "id": "e1_q30",
        "subject": "Türkçe",
        "number": 30,
        "text": "30. '<u>Günün erken saatlerinde</u> bahçedeki çiçekleri sulayan ihtiyar adam, komşusuna selam verdi.' cümlesinde altı çizili öge cümlenin hangi ögesidir?",
        "options": [
          "A) Özne",
          "B) Belirtili Nesne",
          "C) Zarf Tümleci",
          "D) Dolaylı Tümleç",
          "E) Yüklem"
        ],
        "correct": 2,
        "solution": "Yükleme sorulan 'Ne zaman?' sorusuna yanıt verdiği için Zarf Tümlecidir."
      },
      {
        "id": "e1_q31",
        "subject": "Matematik",
        "number": 31,
        "text": "31. a ve b birer pozitif tam sayı olmak üzere,\n<code>3a + 5b = 29</code>\neşitliğini sağlayan en küçük b değeri için a kaçtır?",
        "options": [
          "A) 1",
          "B) 3",
          "C) 5",
          "D) 7",
          "E) 9"
        ],
        "correct": 1,
        "solution": "Denklemde b yerine en küçük pozitif tam sayı değerleri verilerek a = 3 olarak bulunur."
      },
      {
        "id": "e1_q32",
        "subject": "Matematik",
        "number": 32,
        "text": "32. a ve b birer pozitif tam sayı olmak üzere,\n<code>3a + 5b = 29</code>\neşitliğini sağlayan en küçük b değeri için a kaçtır?",
        "options": [
          "A) 1",
          "B) 3",
          "C) 5",
          "D) 7",
          "E) 9"
        ],
        "correct": 1,
        "solution": "Denklemde b yerine en küçük pozitif tam sayı değerleri verilerek a = 3 olarak bulunur."
      },
      {
        "id": "e1_q33",
        "subject": "Matematik",
        "number": 33,
        "text": "33. a ve b birer pozitif tam sayı olmak üzere,\n<code>3a + 5b = 29</code>\neşitliğini sağlayan en küçük b değeri için a kaçtır?",
        "options": [
          "A) 1",
          "B) 3",
          "C) 5",
          "D) 7",
          "E) 9"
        ],
        "correct": 1,
        "solution": "Denklemde b yerine en küçük pozitif tam sayı değerleri verilerek a = 3 olarak bulunur."
      },
      {
        "id": "e1_q34",
        "subject": "Matematik",
        "number": 34,
        "text": "34. a ve b birer pozitif tam sayı olmak üzere,\n<code>3a + 5b = 29</code>\neşitliğini sağlayan en küçük b değeri için a kaçtır?",
        "options": [
          "A) 1",
          "B) 3",
          "C) 5",
          "D) 7",
          "E) 9"
        ],
        "correct": 1,
        "solution": "Denklemde b yerine en küçük pozitif tam sayı değerleri verilerek a = 3 olarak bulunur."
      },
      {
        "id": "e1_q35",
        "subject": "Matematik",
        "number": 35,
        "text": "35. a ve b birer pozitif tam sayı olmak üzere,\n<code>3a + 5b = 29</code>\neşitliğini sağlayan en küçük b değeri için a kaçtır?",
        "options": [
          "A) 1",
          "B) 3",
          "C) 5",
          "D) 7",
          "E) 9"
        ],
        "correct": 1,
        "solution": "Denklemde b yerine en küçük pozitif tam sayı değerleri verilerek a = 3 olarak bulunur."
      },
      {
        "id": "e1_q36",
        "subject": "Matematik",
        "number": 36,
        "text": "36. <code>(1/2 + 1/3) : (5/6) + 2^2 = x</code>\nişleminin sonucu kaçtır?",
        "options": [
          "A) 5",
          "B) 6",
          "C) 4",
          "D) 3",
          "E) 7"
        ],
        "correct": 0,
        "solution": "(1/2 + 1/3) = 5/6. (5/6) : (5/6) = 1. Sonuç = 1 + 2^2 = 5."
      },
      {
        "id": "e1_q37",
        "subject": "Matematik",
        "number": 37,
        "text": "37. <code>(1/2 + 1/3) : (5/6) + 2^3 = x</code>\nişleminin sonucu kaçtır?",
        "options": [
          "A) 9",
          "B) 10",
          "C) 8",
          "D) 5",
          "E) 11"
        ],
        "correct": 0,
        "solution": "(1/2 + 1/3) = 5/6. (5/6) : (5/6) = 1. Sonuç = 1 + 2^3 = 9."
      },
      {
        "id": "e1_q38",
        "subject": "Matematik",
        "number": 38,
        "text": "38. <code>(1/2 + 1/3) : (5/6) + 2^4 = x</code>\nişleminin sonucu kaçtır?",
        "options": [
          "A) 17",
          "B) 18",
          "C) 16",
          "D) 9",
          "E) 19"
        ],
        "correct": 0,
        "solution": "(1/2 + 1/3) = 5/6. (5/6) : (5/6) = 1. Sonuç = 1 + 2^4 = 17."
      },
      {
        "id": "e1_q39",
        "subject": "Matematik",
        "number": 39,
        "text": "39. <code>(1/2 + 1/3) : (5/6) + 2^5 = x</code>\nişleminin sonucu kaçtır?",
        "options": [
          "A) 33",
          "B) 34",
          "C) 32",
          "D) 17",
          "E) 35"
        ],
        "correct": 0,
        "solution": "(1/2 + 1/3) = 5/6. (5/6) : (5/6) = 1. Sonuç = 1 + 2^5 = 33."
      },
      {
        "id": "e1_q40",
        "subject": "Matematik",
        "number": 40,
        "text": "40. <code>(1/2 + 1/3) : (5/6) + 2^6 = x</code>\nişleminin sonucu kaçtır?",
        "options": [
          "A) 65",
          "B) 66",
          "C) 64",
          "D) 33",
          "E) 67"
        ],
        "correct": 0,
        "solution": "(1/2 + 1/3) = 5/6. (5/6) : (5/6) = 1. Sonuç = 1 + 2^6 = 65."
      },
      {
        "id": "e1_q41",
        "subject": "Matematik",
        "number": 41,
        "text": "41. <code>(1/2 + 1/3) : (5/6) + 2^7 = x</code>\nişleminin sonucu kaçtır?",
        "options": [
          "A) 129",
          "B) 130",
          "C) 128",
          "D) 65",
          "E) 131"
        ],
        "correct": 0,
        "solution": "(1/2 + 1/3) = 5/6. (5/6) : (5/6) = 1. Sonuç = 1 + 2^7 = 129."
      },
      {
        "id": "e1_q42",
        "subject": "Matematik",
        "number": 42,
        "text": "42. <code>(1/2 + 1/3) : (5/6) + 2^8 = x</code>\nişleminin sonucu kaçtır?",
        "options": [
          "A) 257",
          "B) 258",
          "C) 256",
          "D) 129",
          "E) 259"
        ],
        "correct": 0,
        "solution": "(1/2 + 1/3) = 5/6. (5/6) : (5/6) = 1. Sonuç = 1 + 2^8 = 257."
      },
      {
        "id": "e1_q43",
        "subject": "Matematik",
        "number": 43,
        "text": "43. Bir babanın bugünkü yaşı 38, oğlunun bugünkü yaşı ise 7'dır.\nBuna göre kaç yıl sonra babanın yaşı oğlunun yaşının 3 katı olur?",
        "options": [
          "A) 6",
          "B) 7",
          "C) 8",
          "D) 9",
          "E) 10"
        ],
        "correct": 2,
        "solution": "38 + t = 3(7 + t) => 38 + t = 21 + 3t => 2t = 17 => t = 8 yıl sonra."
      },
      {
        "id": "e1_q44",
        "subject": "Matematik",
        "number": 44,
        "text": "44. Bir babanın bugünkü yaşı 38, oğlunun bugünkü yaşı ise 7'dır.\nBuna göre kaç yıl sonra babanın yaşı oğlunun yaşının 3 katı olur?",
        "options": [
          "A) 6",
          "B) 7",
          "C) 8",
          "D) 9",
          "E) 10"
        ],
        "correct": 2,
        "solution": "38 + t = 3(7 + t) => 38 + t = 21 + 3t => 2t = 17 => t = 8 yıl sonra."
      },
      {
        "id": "e1_q45",
        "subject": "Matematik",
        "number": 45,
        "text": "45. Bir babanın bugünkü yaşı 38, oğlunun bugünkü yaşı ise 7'dır.\nBuna göre kaç yıl sonra babanın yaşı oğlunun yaşının 3 katı olur?",
        "options": [
          "A) 6",
          "B) 7",
          "C) 8",
          "D) 9",
          "E) 10"
        ],
        "correct": 2,
        "solution": "38 + t = 3(7 + t) => 38 + t = 21 + 3t => 2t = 17 => t = 8 yıl sonra."
      },
      {
        "id": "e1_q46",
        "subject": "Matematik",
        "number": 46,
        "text": "46. Bir babanın bugünkü yaşı 38, oğlunun bugünkü yaşı ise 7'dır.\nBuna göre kaç yıl sonra babanın yaşı oğlunun yaşının 3 katı olur?",
        "options": [
          "A) 6",
          "B) 7",
          "C) 8",
          "D) 9",
          "E) 10"
        ],
        "correct": 2,
        "solution": "38 + t = 3(7 + t) => 38 + t = 21 + 3t => 2t = 17 => t = 8 yıl sonra."
      },
      {
        "id": "e1_q47",
        "subject": "Matematik",
        "number": 47,
        "text": "47. Bir babanın bugünkü yaşı 38, oğlunun bugünkü yaşı ise 7'dır.\nBuna göre kaç yıl sonra babanın yaşı oğlunun yaşının 3 katı olur?",
        "options": [
          "A) 6",
          "B) 7",
          "C) 8",
          "D) 9",
          "E) 10"
        ],
        "correct": 2,
        "solution": "38 + t = 3(7 + t) => 38 + t = 21 + 3t => 2t = 17 => t = 8 yıl sonra."
      },
      {
        "id": "e1_q48",
        "subject": "Matematik",
        "number": 48,
        "text": "48. Bir babanın bugünkü yaşı 38, oğlunun bugünkü yaşı ise 7'dır.\nBuna göre kaç yıl sonra babanın yaşı oğlunun yaşının 3 katı olur?",
        "options": [
          "A) 6",
          "B) 7",
          "C) 8",
          "D) 9",
          "E) 10"
        ],
        "correct": 2,
        "solution": "38 + t = 3(7 + t) => 38 + t = 21 + 3t => 2t = 17 => t = 8 yıl sonra."
      },
      {
        "id": "e1_q49",
        "subject": "Matematik",
        "number": 49,
        "text": "49. Bir babanın bugünkü yaşı 38, oğlunun bugünkü yaşı ise 7'dır.\nBuna göre kaç yıl sonra babanın yaşı oğlunun yaşının 3 katı olur?",
        "options": [
          "A) 6",
          "B) 7",
          "C) 8",
          "D) 9",
          "E) 10"
        ],
        "correct": 2,
        "solution": "38 + t = 3(7 + t) => 38 + t = 21 + 3t => 2t = 17 => t = 8 yıl sonra."
      },
      {
        "id": "e1_q50",
        "subject": "Matematik",
        "number": 50,
        "text": "50. Bir babanın bugünkü yaşı 38, oğlunun bugünkü yaşı ise 7'dır.\nBuna göre kaç yıl sonra babanın yaşı oğlunun yaşının 3 katı olur?",
        "options": [
          "A) 6",
          "B) 7",
          "C) 8",
          "D) 9",
          "E) 10"
        ],
        "correct": 2,
        "solution": "38 + t = 3(7 + t) => 38 + t = 21 + 3t => 2t = 17 => t = 8 yıl sonra."
      },
      {
        "id": "e1_q51",
        "subject": "Matematik",
        "number": 51,
        "text": "51. Bir babanın bugünkü yaşı 38, oğlunun bugünkü yaşı ise 7'dır.\nBuna göre kaç yıl sonra babanın yaşı oğlunun yaşının 3 katı olur?",
        "options": [
          "A) 6",
          "B) 7",
          "C) 8",
          "D) 9",
          "E) 10"
        ],
        "correct": 2,
        "solution": "38 + t = 3(7 + t) => 38 + t = 21 + 3t => 2t = 17 => t = 8 yıl sonra."
      },
      {
        "id": "e1_q52",
        "subject": "Matematik",
        "number": 52,
        "text": "52. Bir babanın bugünkü yaşı 38, oğlunun bugünkü yaşı ise 7'dır.\nBuna göre kaç yıl sonra babanın yaşı oğlunun yaşının 3 katı olur?",
        "options": [
          "A) 6",
          "B) 7",
          "C) 8",
          "D) 9",
          "E) 10"
        ],
        "correct": 2,
        "solution": "38 + t = 3(7 + t) => 38 + t = 21 + 3t => 2t = 17 => t = 8 yıl sonra."
      },
      {
        "id": "e1_q53",
        "subject": "Matematik",
        "number": 53,
        "text": "53. Bir babanın bugünkü yaşı 38, oğlunun bugünkü yaşı ise 7'dır.\nBuna göre kaç yıl sonra babanın yaşı oğlunun yaşının 3 katı olur?",
        "options": [
          "A) 6",
          "B) 7",
          "C) 8",
          "D) 9",
          "E) 10"
        ],
        "correct": 2,
        "solution": "38 + t = 3(7 + t) => 38 + t = 21 + 3t => 2t = 17 => t = 8 yıl sonra."
      },
      {
        "id": "e1_q54",
        "subject": "Matematik",
        "number": 54,
        "text": "54. Bir babanın bugünkü yaşı 38, oğlunun bugünkü yaşı ise 7'dır.\nBuna göre kaç yıl sonra babanın yaşı oğlunun yaşının 3 katı olur?",
        "options": [
          "A) 6",
          "B) 7",
          "C) 8",
          "D) 9",
          "E) 10"
        ],
        "correct": 2,
        "solution": "38 + t = 3(7 + t) => 38 + t = 21 + 3t => 2t = 17 => t = 8 yıl sonra."
      },
      {
        "id": "e1_q55",
        "subject": "Matematik",
        "number": 55,
        "text": "55. A ve B iki küme olmak üzere,\n<code>s(A) = 13</code>, <code>s(B) = 11</code> ve <code>s(A ∩ B) = 4</code>\nolduğuna göre <code>s(A ∪ B)</code> kaçtır?",
        "options": [
          "A) 18",
          "B) 20",
          "C) 22",
          "D) 24",
          "E) 26"
        ],
        "correct": 1,
        "solution": "s(A ∪ B) = s(A) + s(B) - s(A ∩ B) = 13 + 11 - 4 = 20."
      },
      {
        "id": "e1_q56",
        "subject": "Matematik",
        "number": 56,
        "text": "56. A ve B iki küme olmak üzere,\n<code>s(A) = 13</code>, <code>s(B) = 11</code> ve <code>s(A ∩ B) = 4</code>\nolduğuna göre <code>s(A ∪ B)</code> kaçtır?",
        "options": [
          "A) 18",
          "B) 20",
          "C) 22",
          "D) 24",
          "E) 26"
        ],
        "correct": 1,
        "solution": "s(A ∪ B) = s(A) + s(B) - s(A ∩ B) = 13 + 11 - 4 = 20."
      },
      {
        "id": "e1_q57",
        "subject": "Matematik",
        "number": 57,
        "text": "57. A ve B iki küme olmak üzere,\n<code>s(A) = 13</code>, <code>s(B) = 11</code> ve <code>s(A ∩ B) = 4</code>\nolduğuna göre <code>s(A ∪ B)</code> kaçtır?",
        "options": [
          "A) 18",
          "B) 20",
          "C) 22",
          "D) 24",
          "E) 26"
        ],
        "correct": 1,
        "solution": "s(A ∪ B) = s(A) + s(B) - s(A ∩ B) = 13 + 11 - 4 = 20."
      },
      {
        "id": "e1_q58",
        "subject": "Matematik",
        "number": 58,
        "text": "58. A ve B iki küme olmak üzere,\n<code>s(A) = 13</code>, <code>s(B) = 11</code> ve <code>s(A ∩ B) = 4</code>\nolduğuna göre <code>s(A ∪ B)</code> kaçtır?",
        "options": [
          "A) 18",
          "B) 20",
          "C) 22",
          "D) 24",
          "E) 26"
        ],
        "correct": 1,
        "solution": "s(A ∪ B) = s(A) + s(B) - s(A ∩ B) = 13 + 11 - 4 = 20."
      },
      {
        "id": "e1_q59",
        "subject": "Matematik",
        "number": 59,
        "text": "59. Dik kenar uzunlukları 6 cm ve 8 cm olan bir dik üçgenin hipotenüs uzunluğu kaç cm'dir?",
        "options": [
          "A) 9",
          "B) 10",
          "C) 11",
          "D) 12",
          "E) 13"
        ],
        "correct": 1,
        "solution": "Pisagor bağıntısı: a² + b² = c² => 6² + 8² = 100 = 10² => Hipotenüs = 10 cm (3-4-5 katı)."
      },
      {
        "id": "e1_q60",
        "subject": "Matematik",
        "number": 60,
        "text": "60. Dik kenar uzunlukları 6 cm ve 8 cm olan bir dik üçgenin hipotenüs uzunluğu kaç cm'dir?",
        "options": [
          "A) 9",
          "B) 10",
          "C) 11",
          "D) 12",
          "E) 13"
        ],
        "correct": 1,
        "solution": "Pisagor bağıntısı: a² + b² = c² => 6² + 8² = 100 = 10² => Hipotenüs = 10 cm (3-4-5 katı)."
      },
      {
        "id": "e1_q61",
        "subject": "Tarih",
        "number": 61,
        "text": "61. Maniheizm dinini kabul ederek yerleşik hayata geçen İLK Türk devleti aşağıdakilerden hangisidir?",
        "options": [
          "A) Uygurlar",
          "B) Nizamiye Medresesi",
          "C) Sened-i İttifak",
          "D) Mudanya Ateşkesi",
          "E) Kanun-i Esasi"
        ],
        "correct": 0,
        "solution": "Doğru cevap Uygurlar'dır. Maniheizm dinini kabul ederek yerleşik hayata geçen İLK Türk devleti."
      },
      {
        "id": "e1_q62",
        "subject": "Tarih",
        "number": 62,
        "text": "62. Türk ordusunda ilk kez Onlu Askeri Sistemi kuran Asya Hun hükümdarı aşağıdakilerden hangisidir?",
        "options": [
          "A) Mete Han",
          "B) Nizamiye Medresesi",
          "C) Sened-i İttifak",
          "D) Mudanya Ateşkesi",
          "E) Kanun-i Esasi"
        ],
        "correct": 0,
        "solution": "Doğru cevap Mete Han'dır. Türk ordusunda ilk kez Onlu Askeri Sistemi kuran Asya Hun hükümdarı."
      },
      {
        "id": "e1_q63",
        "subject": "Tarih",
        "number": 63,
        "text": "63. Türk tarihinin ve edebiyatının ilk yazılı edebi belgeleri aşağıdakilerden hangisidir?",
        "options": [
          "A) Orhun Abideleri",
          "B) Nizamiye Medresesi",
          "C) Sened-i İttifak",
          "D) Mudanya Ateşkesi",
          "E) Kanun-i Esasi"
        ],
        "correct": 0,
        "solution": "Doğru cevap Orhun Abideleri'dır. Türk tarihinin ve edebiyatının ilk yazılı edebi belgeleri."
      },
      {
        "id": "e1_q64",
        "subject": "Tarih",
        "number": 64,
        "text": "64. Orta Asya'da kurulan ilk Müslüman Türk devleti aşağıdakilerden hangisidir?",
        "options": [
          "A) Karahanlılar",
          "B) Nizamiye Medresesi",
          "C) Sened-i İttifak",
          "D) Mudanya Ateşkesi",
          "E) Kanun-i Esasi"
        ],
        "correct": 0,
        "solution": "Doğru cevap Karahanlılar'dır. Orta Asya'da kurulan ilk Müslüman Türk devleti."
      },
      {
        "id": "e1_q65",
        "subject": "Tarih",
        "number": 65,
        "text": "65. Anadolu'nun kapılarını Türklere kesin olarak açan zafer aşağıdakilerden hangisidir?",
        "options": [
          "A) Sultan Alparslan",
          "B) Nizamiye Medresesi",
          "C) Sened-i İttifak",
          "D) Mudanya Ateşkesi",
          "E) Kanun-i Esasi"
        ],
        "correct": 0,
        "solution": "Doğru cevap Sultan Alparslan'dır. Anadolu'nun kapılarını Türklere kesin olarak açan zafer."
      },
      {
        "id": "e1_q66",
        "subject": "Tarih",
        "number": 66,
        "text": "66. Yusuf Has Hacip tarafından yazılan ilk Türk-İslam siyasetnamesi aşağıdakilerden hangisidir?",
        "options": [
          "A) Kutadgu Bilig",
          "B) Nizamiye Medresesi",
          "C) Sened-i İttifak",
          "D) Mudanya Ateşkesi",
          "E) Kanun-i Esasi"
        ],
        "correct": 0,
        "solution": "Doğru cevap Kutadgu Bilig'dır. Yusuf Has Hacip tarafından yazılan ilk Türk-İslam siyasetnamesi."
      },
      {
        "id": "e1_q67",
        "subject": "Tarih",
        "number": 67,
        "text": "67. Bursa'yı fethedip ilk düzenli orduyu (Yaya-Müsellem) kuran padişah aşağıdakilerden hangisidir?",
        "options": [
          "A) Orhan Bey",
          "B) Nizamiye Medresesi",
          "C) Sened-i İttifak",
          "D) Mudanya Ateşkesi",
          "E) Kanun-i Esasi"
        ],
        "correct": 0,
        "solution": "Doğru cevap Orhan Bey'dır. Bursa'yı fethedip ilk düzenli orduyu (Yaya-Müsellem) kuran padişah."
      },
      {
        "id": "e1_q68",
        "subject": "Tarih",
        "number": 68,
        "text": "68. Tımar sistemini ve Yeniçeri Ocağını kuran padişah aşağıdakilerden hangisidir?",
        "options": [
          "A) I. Murat",
          "B) Nizamiye Medresesi",
          "C) Sened-i İttifak",
          "D) Mudanya Ateşkesi",
          "E) Kanun-i Esasi"
        ],
        "correct": 0,
        "solution": "Doğru cevap I. Murat'dır. Tımar sistemini ve Yeniçeri Ocağını kuran padişah."
      },
      {
        "id": "e1_q69",
        "subject": "Tarih",
        "number": 69,
        "text": "69. İstanbul'u fethederek Yükselme Dönemini başlatan ve ilk altın parayı basan aşağıdakilerden hangisidir?",
        "options": [
          "A) II. Mehmet",
          "B) Nizamiye Medresesi",
          "C) Sened-i İttifak",
          "D) Mudanya Ateşkesi",
          "E) Kanun-i Esasi"
        ],
        "correct": 0,
        "solution": "Doğru cevap II. Mehmet'dır. İstanbul'u fethederek Yükselme Dönemini başlatan ve ilk altın parayı basan."
      },
      {
        "id": "e1_q70",
        "subject": "Tarih",
        "number": 70,
        "text": "70. Divan-ı Hümayun'da kadı ve müderris atamalarından sorumlu adalet üyesi aşağıdakilerden hangisidir?",
        "options": [
          "A) Kazasker",
          "B) Nizamiye Medresesi",
          "C) Sened-i İttifak",
          "D) Mudanya Ateşkesi",
          "E) Kanun-i Esasi"
        ],
        "correct": 0,
        "solution": "Doğru cevap Kazasker'dır. Divan-ı Hümayun'da kadı ve müderris atamalarından sorumlu adalet üyesi."
      },
      {
        "id": "e1_q71",
        "subject": "Tarih",
        "number": 71,
        "text": "71. Padişahın ilk kez kanun gücünün üstünlüğünü kabul ettiği 1839 belgesi aşağıdakilerden hangisidir?",
        "options": [
          "A) Tanzimat Fermanı",
          "B) Nizamiye Medresesi",
          "C) Sened-i İttifak",
          "D) Mudanya Ateşkesi",
          "E) Kanun-i Esasi"
        ],
        "correct": 0,
        "solution": "Doğru cevap Tanzimat Fermanı'dır. Padişahın ilk kez kanun gücünün üstünlüğünü kabul ettiği 1839 belgesi."
      },
      {
        "id": "e1_q72",
        "subject": "Tarih",
        "number": 72,
        "text": "72. Kurtuluş Savaşı'nın gerekçe, amaç ve yönteminin ilk kez açıklandığı belge aşağıdakilerden hangisidir?",
        "options": [
          "A) Amasya Genelgesi",
          "B) Nizamiye Medresesi",
          "C) Sened-i İttifak",
          "D) Mudanya Ateşkesi",
          "E) Kanun-i Esasi"
        ],
        "correct": 0,
        "solution": "Doğru cevap Amasya Genelgesi'dır. Kurtuluş Savaşı'nın gerekçe, amaç ve yönteminin ilk kez açıklandığı belge."
      },
      {
        "id": "e1_q73",
        "subject": "Tarih",
        "number": 73,
        "text": "73. Manda ve himayenin İLK KEZ reddedildiği kongre aşağıdakilerden hangisidir?",
        "options": [
          "A) Erzurum Kongresi",
          "B) Nizamiye Medresesi",
          "C) Sened-i İttifak",
          "D) Mudanya Ateşkesi",
          "E) Kanun-i Esasi"
        ],
        "correct": 0,
        "solution": "Doğru cevap Erzurum Kongresi'dır. Manda ve himayenin İLK KEZ reddedildiği kongre."
      },
      {
        "id": "e1_q74",
        "subject": "Tarih",
        "number": 74,
        "text": "74. Tüm milli cemiyetlerin tek çatı altında birleştirildiği kongre aşağıdakilerden hangisidir?",
        "options": [
          "A) Sivas Kongresi",
          "B) Nizamiye Medresesi",
          "C) Sened-i İttifak",
          "D) Mudanya Ateşkesi",
          "E) Kanun-i Esasi"
        ],
        "correct": 0,
        "solution": "Doğru cevap Sivas Kongresi'dır. Tüm milli cemiyetlerin tek çatı altında birleştirildiği kongre."
      },
      {
        "id": "e1_q75",
        "subject": "Tarih",
        "number": 75,
        "text": "75. 23 Nisan 1920'de açılan kurucu, savaşçı ve güçler birliği meclisi aşağıdakilerden hangisidir?",
        "options": [
          "A) I. TBMM",
          "B) Nizamiye Medresesi",
          "C) Sened-i İttifak",
          "D) Mudanya Ateşkesi",
          "E) Kanun-i Esasi"
        ],
        "correct": 0,
        "solution": "Doğru cevap I. TBMM'dır. 23 Nisan 1920'de açılan kurucu, savaşçı ve güçler birliği meclisi."
      },
      {
        "id": "e1_q76",
        "subject": "Tarih",
        "number": 76,
        "text": "76. Düzenli ordunun Batı Cephesi'ndeki İLK askeri zaferi aşağıdakilerden hangisidir?",
        "options": [
          "A) I. İnönü Zaferi",
          "B) Nizamiye Medresesi",
          "C) Sened-i İttifak",
          "D) Mudanya Ateşkesi",
          "E) Kanun-i Esasi"
        ],
        "correct": 0,
        "solution": "Doğru cevap I. İnönü Zaferi'dır. Düzenli ordunun Batı Cephesi'ndeki İLK askeri zaferi."
      },
      {
        "id": "e1_q77",
        "subject": "Tarih",
        "number": 77,
        "text": "77. Mustafa Kemal'e Mareşallik ve Gazilik unvanının verildiği meydan muharebesi aşağıdakilerden hangisidir?",
        "options": [
          "A) Sakarya Meydan Muharebesi",
          "B) Nizamiye Medresesi",
          "C) Sened-i İttifak",
          "D) Mudanya Ateşkesi",
          "E) Kanun-i Esasi"
        ],
        "correct": 0,
        "solution": "Doğru cevap Sakarya Meydan Muharebesi'dır. Mustafa Kemal'e Mareşallik ve Gazilik unvanının verildiği meydan muharebesi."
      },
      {
        "id": "e1_q78",
        "subject": "Tarih",
        "number": 78,
        "text": "78. Kapitülasyonların kesin kaldırıldığı ve Türkiye'nin bağımsızlığının tanındığı antlaşma aşağıdakilerden hangisidir?",
        "options": [
          "A) Lozan Antlaşması",
          "B) Nizamiye Medresesi",
          "C) Sened-i İttifak",
          "D) Mudanya Ateşkesi",
          "E) Kanun-i Esasi"
        ],
        "correct": 0,
        "solution": "Doğru cevap Lozan Antlaşması'dır. Kapitülasyonların kesin kaldırıldığı ve Türkiye'nin bağımsızlığının tanındığı antlaşma."
      },
      {
        "id": "e1_q79",
        "subject": "Tarih",
        "number": 79,
        "text": "79. Milli egemenliği ve halk iradesini esas alan temel Atatürk ilkesi aşağıdakilerden hangisidir?",
        "options": [
          "A) Cumhuriyetçilik",
          "B) Nizamiye Medresesi",
          "C) Sened-i İttifak",
          "D) Mudanya Ateşkesi",
          "E) Kanun-i Esasi"
        ],
        "correct": 0,
        "solution": "Doğru cevap Cumhuriyetçilik'dır. Milli egemenliği ve halk iradesini esas alan temel Atatürk ilkesi."
      },
      {
        "id": "e1_q80",
        "subject": "Tarih",
        "number": 80,
        "text": "80. Aşar vergisinin kaldırılması ve toplumda ayrıcalıkları reddeden ilke aşağıdakilerden hangisidir?",
        "options": [
          "A) Halkçılık",
          "B) Nizamiye Medresesi",
          "C) Sened-i İttifak",
          "D) Mudanya Ateşkesi",
          "E) Kanun-i Esasi"
        ],
        "correct": 0,
        "solution": "Doğru cevap Halkçılık'dır. Aşar vergisinin kaldırılması ve toplumda ayrıcalıkları reddeden ilke."
      },
      {
        "id": "e1_q81",
        "subject": "Tarih",
        "number": 81,
        "text": "81. Halifeliğin kaldırılması ve akılcılığı/bilimselliği savunan ilke aşağıdakilerden hangisidir?",
        "options": [
          "A) Laiklik",
          "B) Nizamiye Medresesi",
          "C) Sened-i İttifak",
          "D) Mudanya Ateşkesi",
          "E) Kanun-i Esasi"
        ],
        "correct": 0,
        "solution": "Doğru cevap Laiklik'dır. Halifeliğin kaldırılması ve akılcılığı/bilimselliği savunan ilke."
      },
      {
        "id": "e1_q82",
        "subject": "Tarih",
        "number": 82,
        "text": "82. Halkın yapamadığı büyük yatırımları devlet eliyle yapmayı öngören ilke aşağıdakilerden hangisidir?",
        "options": [
          "A) Devletçilik",
          "B) Nizamiye Medresesi",
          "C) Sened-i İttifak",
          "D) Mudanya Ateşkesi",
          "E) Kanun-i Esasi"
        ],
        "correct": 0,
        "solution": "Doğru cevap Devletçilik'dır. Halkın yapamadığı büyük yatırımları devlet eliyle yapmayı öngören ilke."
      },
      {
        "id": "e1_q83",
        "subject": "Tarih",
        "number": 83,
        "text": "83. Türk karasularında ticaret hakkını millileştiren kanun aşağıdakilerden hangisidir?",
        "options": [
          "A) Kabotaj Kanunu",
          "B) Nizamiye Medresesi",
          "C) Sened-i İttifak",
          "D) Mudanya Ateşkesi",
          "E) Kanun-i Esasi"
        ],
        "correct": 0,
        "solution": "Doğru cevap Kabotaj Kanunu'dır. Türk karasularında ticaret hakkını millileştiren kanun."
      },
      {
        "id": "e1_q84",
        "subject": "Tarih",
        "number": 84,
        "text": "84. Boğazlar Komisyonunu kaldırıp boğazların hakimiyetini tam Türkiye'ye veren 1936 sözleşmesi aşağıdakilerden hangisidir?",
        "options": [
          "A) Montrö Sözleşmesi",
          "B) Nizamiye Medresesi",
          "C) Sened-i İttifak",
          "D) Mudanya Ateşkesi",
          "E) Kanun-i Esasi"
        ],
        "correct": 0,
        "solution": "Doğru cevap Montrö Sözleşmesi'dır. Boğazlar Komisyonunu kaldırıp boğazların hakimiyetini tam Türkiye'ye veren 1936 sözleşmesi."
      },
      {
        "id": "e1_q85",
        "subject": "Tarih",
        "number": 85,
        "text": "85. 1939 yılında anavatana katılan sınır şehri aşağıdakilerden hangisidir?",
        "options": [
          "A) Hatay",
          "B) Nizamiye Medresesi",
          "C) Sened-i İttifak",
          "D) Mudanya Ateşkesi",
          "E) Kanun-i Esasi"
        ],
        "correct": 0,
        "solution": "Doğru cevap Hatay'dır. 1939 yılında anavatana katılan sınır şehri."
      },
      {
        "id": "e1_q86",
        "subject": "Tarih",
        "number": 86,
        "text": "86. Türkiye'nin batı sınırını güvenceye almak için 1934'te imzaladığı antlaşma aşağıdakilerden hangisidir?",
        "options": [
          "A) Balkan Antantı",
          "B) Nizamiye Medresesi",
          "C) Sened-i İttifak",
          "D) Mudanya Ateşkesi",
          "E) Kanun-i Esasi"
        ],
        "correct": 0,
        "solution": "Doğru cevap Balkan Antantı'dır. Türkiye'nin batı sınırını güvenceye almak için 1934'te imzaladığı antlaşma."
      },
      {
        "id": "e1_q87",
        "subject": "Tarih",
        "number": 87,
        "text": "87. Türkiye'nin doğu sınırını güvenceye almak için 1937'de imzaladığı pakt aşağıdakilerden hangisidir?",
        "options": [
          "A) Sadabat Paktı",
          "B) Nizamiye Medresesi",
          "C) Sened-i İttifak",
          "D) Mudanya Ateşkesi",
          "E) Kanun-i Esasi"
        ],
        "correct": 0,
        "solution": "Doğru cevap Sadabat Paktı'dır. Türkiye'nin doğu sınırını güvenceye almak için 1937'de imzaladığı pakt."
      },
      {
        "id": "e1_q88",
        "subject": "Coğrafya",
        "number": 88,
        "text": "88. Türkiye'de dört mevsimin belirgin yaşanmasının temel nedeni aşağıdakilerden hangisidir?",
        "options": [
          "A) Bozok Platosu",
          "B) Tuz Gölü",
          "C) Orta Kuşakta yer alması",
          "D) Karacadağ",
          "E) Çukurova"
        ],
        "correct": 2,
        "solution": "Doğru seçenek C (Orta Kuşakta yer alması)'dir. Türkiye'de dört mevsimin belirgin yaşanmasının temel nedeni."
      },
      {
        "id": "e1_q89",
        "subject": "Coğrafya",
        "number": 89,
        "text": "89. Türkiye'de gölge boyunun hiçbir zaman sıfır olmamasının nedeni aşağıdakilerden hangisidir?",
        "options": [
          "A) Bozok Platosu",
          "B) Tuz Gölü",
          "C) Dönenceler dışında bulunması",
          "D) Karacadağ",
          "E) Çukurova"
        ],
        "correct": 2,
        "solution": "Doğru seçenek C (Dönenceler dışında bulunması)'dir. Türkiye'de gölge boyunun hiçbir zaman sıfır olmamasının nedeni."
      },
      {
        "id": "e1_q90",
        "subject": "Coğrafya",
        "number": 90,
        "text": "90. Kalker erimesi sonucu oluşan karstik platolarımız aşağıdakilerden hangisidir?",
        "options": [
          "A) Bozok Platosu",
          "B) Tuz Gölü",
          "C) Teke ve Taşeli",
          "D) Karacadağ",
          "E) Çukurova"
        ],
        "correct": 2,
        "solution": "Doğru seçenek C (Teke ve Taşeli)'dir. Kalker erimesi sonucu oluşan karstik platolarımız."
      },
      {
        "id": "e1_q91",
        "subject": "Coğrafya",
        "number": 91,
        "text": "91. Yaz yağışları ve çernezyom topraklarıyla büyükbaş hayvancılık yapılan plato aşağıdakilerden hangisidir?",
        "options": [
          "A) Bozok Platosu",
          "B) Tuz Gölü",
          "C) Erzurum-Kars",
          "D) Karacadağ",
          "E) Çukurova"
        ],
        "correct": 2,
        "solution": "Doğru seçenek C (Erzurum-Kars)'dir. Yaz yağışları ve çernezyom topraklarıyla büyükbaş hayvancılık yapılan plato."
      },
      {
        "id": "e1_q92",
        "subject": "Coğrafya",
        "number": 92,
        "text": "92. Ege Bölgesi'nde kırılma ile oluşan dağ ve çöküntü ovaları yapısı aşağıdakilerden hangisidir?",
        "options": [
          "A) Bozok Platosu",
          "B) Tuz Gölü",
          "C) Horst - Graben",
          "D) Karacadağ",
          "E) Çukurova"
        ],
        "correct": 2,
        "solution": "Doğru seçenek C (Horst - Graben)'dir. Ege Bölgesi'nde kırılma ile oluşan dağ ve çöküntü ovaları yapısı."
      },
      {
        "id": "e1_q93",
        "subject": "Coğrafya",
        "number": 93,
        "text": "93. Türkiye'nin yüzölçümü en büyük sodalı gölü aşağıdakilerden hangisidir?",
        "options": [
          "A) Bozok Platosu",
          "B) Tuz Gölü",
          "C) Van Gölü",
          "D) Karacadağ",
          "E) Çukurova"
        ],
        "correct": 2,
        "solution": "Doğru seçenek C (Van Gölü)'dir. Türkiye'nin yüzölçümü en büyük sodalı gölü."
      },
      {
        "id": "e1_q94",
        "subject": "Coğrafya",
        "number": 94,
        "text": "94. Abant, Tortum ve Yedigöller'in oluşum türü aşağıdakilerden hangisidir?",
        "options": [
          "A) Bozok Platosu",
          "B) Tuz Gölü",
          "C) Heyelan Set Gölleri",
          "D) Karacadağ",
          "E) Çukurova"
        ],
        "correct": 2,
        "solution": "Doğru seçenek C (Heyelan Set Gölleri)'dir. Abant, Tortum ve Yedigöller'in oluşum türü."
      },
      {
        "id": "e1_q95",
        "subject": "Coğrafya",
        "number": 95,
        "text": "95. Türkiye'de her mevsim düzenli yağış alan ve en çok yağış düşen il aşağıdakilerden hangisidir?",
        "options": [
          "A) Bozok Platosu",
          "B) Tuz Gölü",
          "C) Rize",
          "D) Karacadağ",
          "E) Çukurova"
        ],
        "correct": 2,
        "solution": "Doğru seçenek C (Rize)'dir. Türkiye'de her mevsim düzenli yağış alan ve en çok yağış düşen il."
      },
      {
        "id": "e1_q96",
        "subject": "Coğrafya",
        "number": 96,
        "text": "96. Akdeniz iklim bölgesinde kalker üzerinde oluşan kırmızı toprak aşağıdakilerden hangisidir?",
        "options": [
          "A) Bozok Platosu",
          "B) Tuz Gölü",
          "C) Terra-Rossa",
          "D) Karacadağ",
          "E) Çukurova"
        ],
        "correct": 2,
        "solution": "Doğru seçenek C (Terra-Rossa)'dir. Akdeniz iklim bölgesinde kalker üzerinde oluşan kırmızı toprak."
      },
      {
        "id": "e1_q97",
        "subject": "Coğrafya",
        "number": 97,
        "text": "97. Türkiye'de sanayi, ticaret ve nüfus yoğunluğu en yüksek olan aşınım platosu aşağıdakilerden hangisidir?",
        "options": [
          "A) Bozok Platosu",
          "B) Tuz Gölü",
          "C) Çatalca - Kocaeli",
          "D) Karacadağ",
          "E) Çukurova"
        ],
        "correct": 2,
        "solution": "Doğru seçenek C (Çatalca - Kocaeli)'dir. Türkiye'de sanayi, ticaret ve nüfus yoğunluğu en yüksek olan aşınım platosu."
      },
      {
        "id": "e1_q98",
        "subject": "Coğrafya",
        "number": 98,
        "text": "98. İç Anadolu'da su kaynaklarının azlığı nedeniyle görülen kırsal yerleşme türü aşağıdakilerden hangisidir?",
        "options": [
          "A) Bozok Platosu",
          "B) Tuz Gölü",
          "C) Toplu Yerleşme",
          "D) Karacadağ",
          "E) Çukurova"
        ],
        "correct": 2,
        "solution": "Doğru seçenek C (Toplu Yerleşme)'dir. İç Anadolu'da su kaynaklarının azlığı nedeniyle görülen kırsal yerleşme türü."
      },
      {
        "id": "e1_q99",
        "subject": "Coğrafya",
        "number": 99,
        "text": "99. GAP sulamasıyla birlikte Pamuk üretiminde 1. sıraya yerleşen ilimiz aşağıdakilerden hangisidir?",
        "options": [
          "A) Bozok Platosu",
          "B) Tuz Gölü",
          "C) Şanlıurfa",
          "D) Karacadağ",
          "E) Çukurova"
        ],
        "correct": 2,
        "solution": "Doğru seçenek C (Şanlıurfa)'dir. GAP sulamasıyla birlikte Pamuk üretiminde 1. sıraya yerleşen ilimiz."
      },
      {
        "id": "e1_q100",
        "subject": "Coğrafya",
        "number": 100,
        "text": "100. Üretiminin tamamı Doğu Karadeniz'de yapılan yıkanmış asitli toprak ürünü aşağıdakilerden hangisidir?",
        "options": [
          "A) Bozok Platosu",
          "B) Tuz Gölü",
          "C) Çay",
          "D) Karacadağ",
          "E) Çukurova"
        ],
        "correct": 2,
        "solution": "Doğru seçenek C (Çay)'dir. Üretiminin tamamı Doğu Karadeniz'de yapılan yıkanmış asitli toprak ürünü."
      },
      {
        "id": "e1_q101",
        "subject": "Coğrafya",
        "number": 101,
        "text": "101. Türkiye'nin dünya rezervlerinin yaklaşık %73'üne sahip olduğu stratejik maden aşağıdakilerden hangisidir?",
        "options": [
          "A) Bozok Platosu",
          "B) Tuz Gölü",
          "C) Bor Madeni",
          "D) Karacadağ",
          "E) Çukurova"
        ],
        "correct": 2,
        "solution": "Doğru seçenek C (Bor Madeni)'dir. Türkiye'nin dünya rezervlerinin yaklaşık %73'üne sahip olduğu stratejik maden."
      },
      {
        "id": "e1_q102",
        "subject": "Coğrafya",
        "number": 102,
        "text": "102. I. Jeolojik Zamanda oluşmuş Zonguldak havzası madeni aşağıdakilerden hangisidir?",
        "options": [
          "A) Bozok Platosu",
          "B) Tuz Gölü",
          "C) Taş Kömürü",
          "D) Karacadağ",
          "E) Çukurova"
        ],
        "correct": 2,
        "solution": "Doğru seçenek C (Taş Kömürü)'dir. I. Jeolojik Zamanda oluşmuş Zonguldak havzası madeni."
      },
      {
        "id": "e1_q103",
        "subject": "Coğrafya",
        "number": 103,
        "text": "103. Karabük ve Ereğli'de taş kömürüne (enerjiye) yakınlık sebebiyle kurulan sanayi aşağıdakilerden hangisidir?",
        "options": [
          "A) Bozok Platosu",
          "B) Tuz Gölü",
          "C) Demir-Çelik Sanayisi",
          "D) Karacadağ",
          "E) Çukurova"
        ],
        "correct": 2,
        "solution": "Doğru seçenek C (Demir-Çelik Sanayisi)'dir. Karabük ve Ereğli'de taş kömürüne (enerjiye) yakınlık sebebiyle kurulan sanayi."
      },
      {
        "id": "e1_q104",
        "subject": "Coğrafya",
        "number": 104,
        "text": "104. Denizli Sarayköy ve Aydın Germencik'te fay hatlarına bağlı üretilen enerji aşağıdakilerden hangisidir?",
        "options": [
          "A) Bozok Platosu",
          "B) Tuz Gölü",
          "C) Jeotermal Enerji",
          "D) Karacadağ",
          "E) Çukurova"
        ],
        "correct": 2,
        "solution": "Doğru seçenek C (Jeotermal Enerji)'dir. Denizli Sarayköy ve Aydın Germencik'te fay hatlarına bağlı üretilen enerji."
      },
      {
        "id": "e1_q105",
        "subject": "Coğrafya",
        "number": 105,
        "text": "105. Çukurova, Bafra ve Çarşamba ovalarının ortak oluşum türü aşağıdakilerden hangisidir?",
        "options": [
          "A) Bozok Platosu",
          "B) Tuz Gölü",
          "C) Akarsu Delta Ovaları",
          "D) Karacadağ",
          "E) Çukurova"
        ],
        "correct": 2,
        "solution": "Doğru seçenek C (Akarsu Delta Ovaları)'dir. Çukurova, Bafra ve Çarşamba ovalarının ortak oluşum türü."
      },
      {
        "id": "e1_q106",
        "subject": "Vatandaşlık",
        "number": 106,
        "text": "106. Sosyal hayatı düzenleyen kurallardan hangisi devlet gücü desteklidir??",
        "options": [
          "A) Din Kuralları",
          "B) İptal",
          "C) Tazminat",
          "D) Hukuk Kuralları",
          "E) Danıştay"
        ],
        "correct": 3,
        "solution": "Doğru cevap Hukuk Kuralları'dır."
      },
      {
        "id": "e1_q107",
        "subject": "Vatandaşlık",
        "number": 107,
        "text": "107. Resmi evlendirme memuru olmadan yapılan evliliğin hukuki yaptırımı?",
        "options": [
          "A) Yokluk",
          "B) Din Kuralları",
          "C) İptal",
          "D) Tazminat",
          "E) Danıştay"
        ],
        "correct": 0,
        "solution": "Doğru cevap Yokluk'dır."
      },
      {
        "id": "e1_q108",
        "subject": "Vatandaşlık",
        "number": 108,
        "text": "108. Kanunun emredici hükümlerine aykırı kurulan işlemin yaptırımı?",
        "options": [
          "A) Din Kuralları",
          "B) Mutlak Butlan",
          "C) İptal",
          "D) Tazminat",
          "E) Danıştay"
        ],
        "correct": 1,
        "solution": "Doğru cevap Mutlak Butlan'dır."
      },
      {
        "id": "e1_q109",
        "subject": "Vatandaşlık",
        "number": 109,
        "text": "109. Medeni Hukukta hakların KAZANILMASINDA geçerli temel ilke?",
        "options": [
          "A) Din Kuralları",
          "B) İptal",
          "C) İyiniyet Kuralı",
          "D) Tazminat",
          "E) Danıştay"
        ],
        "correct": 2,
        "solution": "Doğru cevap İyiniyet Kuralı'dır."
      },
      {
        "id": "e1_q110",
        "subject": "Vatandaşlık",
        "number": 110,
        "text": "110. Hakların KULLANILMASINDA ve borçların ifasında geçerli ilke?",
        "options": [
          "A) Dürüstlük Kuralı",
          "B) Din Kuralları",
          "C) İptal",
          "D) Tazminat",
          "E) Danıştay"
        ],
        "correct": 0,
        "solution": "Doğru cevap Dürüstlük Kuralı'dır."
      },
      {
        "id": "e1_q111",
        "subject": "Vatandaşlık",
        "number": 111,
        "text": "111. 1982 Anayasası'nın ilk 3 maddesinin değiştirilemeyeceğini belirten madde?",
        "options": [
          "A) Din Kuralları",
          "B) 4. Madde",
          "C) İptal",
          "D) Tazminat",
          "E) Danıştay"
        ],
        "correct": 1,
        "solution": "Doğru cevap 4. Madde'dır."
      },
      {
        "id": "e1_q112",
        "subject": "Vatandaşlık",
        "number": 112,
        "text": "112. 1982 Anayasası'na göre TBMM üye tam sayısı?",
        "options": [
          "A) Din Kuralları",
          "B) İptal",
          "C) Tazminat",
          "D) 600 Milletvekili",
          "E) Danıştay"
        ],
        "correct": 3,
        "solution": "Doğru cevap 600 Milletvekili'dır."
      },
      {
        "id": "e1_q113",
        "subject": "Vatandaşlık",
        "number": 113,
        "text": "113. Milletvekili seçilme yeterliliği için aranan asgari yaş şartı?",
        "options": [
          "A) Din Kuralları",
          "B) 18 Yaş",
          "C) İptal",
          "D) Tazminat",
          "E) Danıştay"
        ],
        "correct": 1,
        "solution": "Doğru cevap 18 Yaş'dır."
      },
      {
        "id": "e1_q114",
        "subject": "Vatandaşlık",
        "number": 114,
        "text": "114. Cumhurbaşkanının halk tarafından seçilme süresi?",
        "options": [
          "A) 5 Yıl",
          "B) Din Kuralları",
          "C) İptal",
          "D) Tazminat",
          "E) Danıştay"
        ],
        "correct": 0,
        "solution": "Doğru cevap 5 Yıl'dır."
      },
      {
        "id": "e1_q115",
        "subject": "Vatandaşlık",
        "number": 115,
        "text": "115. Anayasa Mahkemesi kaç üyeden oluşur??",
        "options": [
          "A) Din Kuralları",
          "B) İptal",
          "C) 15 Üye",
          "D) Tazminat",
          "E) Danıştay"
        ],
        "correct": 2,
        "solution": "Doğru cevap 15 Üye'dır."
      },
      {
        "id": "e1_q116",
        "subject": "Vatandaşlık",
        "number": 116,
        "text": "116. İdari yargının en üst temyiz mahkemesi?",
        "options": [
          "A) Din Kuralları",
          "B) Danıştay",
          "C) İptal",
          "D) Tazminat",
          "E) Danıştay"
        ],
        "correct": 1,
        "solution": "Doğru cevap Danıştay'dır."
      },
      {
        "id": "e1_q117",
        "subject": "Vatandaşlık",
        "number": 117,
        "text": "117. Adli yargının (ceza ve hukuk) en üst temyiz mahkemesi?",
        "options": [
          "A) Yargıtay",
          "B) Din Kuralları",
          "C) İptal",
          "D) Tazminat",
          "E) Danıştay"
        ],
        "correct": 0,
        "solution": "Doğru cevap Yargıtay'dır."
      },
      {
        "id": "e1_q118",
        "subject": "Vatandaşlık",
        "number": 118,
        "text": "118. Aşağıdakilerden hangisi 657 Sayılı Kanun'da disiplin cezası DEĞİLDİR??",
        "options": [
          "A) Din Kuralları",
          "B) İptal",
          "C) Tazminat",
          "D) Sürgün / Yer Değişikliği",
          "E) Danıştay"
        ],
        "correct": 3,
        "solution": "Doğru cevap Sürgün / Yer Değişikliği'dır."
      },
      {
        "id": "e1_q119",
        "subject": "Vatandaşlık",
        "number": 119,
        "text": "119. Dünyanın en eski tapınak kompleksi kabul edilen UNESCO mirası nerede yer alır??",
        "options": [
          "A) Din Kuralları",
          "B) Şanlıurfa",
          "C) İptal",
          "D) Tazminat",
          "E) Danıştay"
        ],
        "correct": 1,
        "solution": "Doğru cevap Şanlıurfa'dır."
      },
      {
        "id": "e1_q120",
        "subject": "Vatandaşlık",
        "number": 120,
        "text": "120. Avrupa İnsan Hakları Mahkemesi hangi şehirde bulunmaktadır??",
        "options": [
          "A) Strazburg (Fransa)",
          "B) Din Kuralları",
          "C) İptal",
          "D) Tazminat",
          "E) Danıştay"
        ],
        "correct": 0,
        "solution": "Doğru cevap Strazburg (Fransa)'dır."
      }
    ]
  },
  "mockExams": [
    {
      "id": "deneme_1",
      "name": "1. Deneme Sınavı",
      "totalQuestions": 120,
      "duration": 130,
      "distribution": {
        "Türkçe": 30,
        "Matematik": 30,
        "Tarih": 27,
        "Coğrafya": 18,
        "Vatandaşlık": 15
      },
      "questions": [
        {
          "subject": "Türkçe",
          "text": "O, hem müzik kuramcısı hem de iyi bir yazardır. Onun müziği, müzikseverler tarafından belirsizliğin müziği (II) olarak tanımlanabilir. Ancak kesin olan bir şey varki (III) yenilikçi bakış açısıyla müziği yepyeni (V) bir boyuta taşıdı.\nBu parçada altı çizili sözlerden hangisinin yazımı yanlıştır?",
          "options": [
            "A) I",
            "B) II",
            "C) III",
            "D) IV",
            "E) V"
          ],
          "correct": 2,
          "solution": "Doğru cevap C'dir. 'şey var ki' şeklinde 'ki' bağlacı ayrı yazılmalıdır.",
          "id": "e1_q1",
          "no": 1
        },
        {
          "subject": "Türkçe",
          "text": "Modern zamanlarda bireyin yaşadığı en önemli sorunlardan biri kendi hayatının tanığı olmak. Bir yere gittiğinde mekânla bütünleşmek yerine oranın yüzlerce fotoğrafını çekip anında başkalarına sunmak, denize girmek yerine orada olduğunu sosyal medya araçlarından duyurmak bunun bir göstergesi değil mi?\nBu parçada altı çizili sözle anlatılmak istenen aşağıdakilerden hangisidir?",
          "options": [
            "A) Görülmeyi, yaşamaya tercih etmek",
            "B) Beğenilme kaygısı içinde olmak",
            "C) Güncel olanı, anında kayda geçirmek",
            "D) Belli yaşantıları kalıcı kılmayı istemek",
            "E) Deneyimlerini başkalarına aktarmak"
          ],
          "correct": 0,
          "solution": "Doğru cevap A'dır. Hayatın tanığı olmak (dışarıdan izlemek), anı yaşamak yerine başkalarına göstermeyi tercih etmektir.",
          "id": "e1_q2",
          "no": 2
        },
        {
          "subject": "Türkçe",
          "text": "Yaşamak hissetmektir. Sevdiğiniz biriyle vakit geçirmek, doğa yürüyüşü yapmak ya da heyecanlı bir maç izlemek gibi hepimizin hemen her gün yaptığı bazı etkinlikler duygularımızla herhangi bir bağlantı kurmadan gerçekleştirildiğinde tamamen anlamsızlaşır. Duygusuz bir hayat pürüzsüz, kaygan bir kumaş gibidir...\nBu parçaya göre aşağıdakilerden hangisi söylenebilir?",
          "options": [
            "A) Günlük rutinleri anlamlı kılan, insanları harekete geçiren duygulardır.",
            "B) Sadece olumlu hisler etrafında örülü bir hayat yarım bırakılmıştır.",
            "C) Hayat, olumsuz duyguların yarattığı pürüzleri aşma çabasıdır.",
            "D) Hislerden arındırılmış bir hayat bireyin hata yapmasına yol açar.",
            "E) Sıradan aktiviteleri anlamlandıran şey sürekli tekrarla pekiştirilmesidir."
          ],
          "correct": 0,
          "solution": "Doğru cevap A'dır. Parçada duyguların hayatı ve rutinleri anlamlı kıldığı vurgulanmıştır.",
          "id": "e1_q3",
          "no": 3
        },
        {
          "subject": "Türkçe",
          "text": "Venedikli denizciler, soda ve güherçile ticareti yaparken (I) bir kıyıda demirler. Demirledikleri (II) kıyı, silis kumu ve kireçle dolu bir yerdir. Venedikliler geceleri bu maddeleri karıştırarak ateş yakar (IV) ve etrafında toplanmaya (V) başlar.\nBu parçada numaralanmış sözcüklerden hangisi fiilimsi değildir?",
          "options": [
            "A) I",
            "B) II",
            "C) III",
            "D) IV",
            "E) V"
          ],
          "correct": 3,
          "solution": "Doğru cevap D'dir. 'Yakar' kelimesi geniş zaman kipiyle çekimlenmiş bir fiildir, fiilimsi değildir.",
          "id": "e1_q4",
          "no": 4
        },
        {
          "subject": "Türkçe",
          "text": "İnsanlar, kitaplar aracılığıyla hiç karşılaşmadıkları kendileriyle konuşur.\nBu cümlede kitaplarla ilgili anlatılmak istenen aşağıdakilerden hangisidir?",
          "options": [
            "A) Hayal gücünün geliştirilmesine katkı sağladıkları",
            "B) Farklı hayatları görme fırsatı sundukları",
            "C) Yalnızlığı gideren bir yol arkadaşı oldukları",
            "D) Beklentilerin gerçekleşme umudunu artırdıkları",
            "E) İç dünyanın bilinmeyen taraflarını aydınlattıkları"
          ],
          "correct": 4,
          "solution": "Doğru cevap E'dir. 'Hiç karşılaşmadıkları kendileriyle konuşur' ifadesi iç dünyanın keşfini anlatır.",
          "id": "e1_q5",
          "no": 5
        },
        {
          "subject": "Türkçe",
          "text": "Sanat tarih boyunca insanlığın en büyük rehberlerinden biri olmuştur. Toplumlar Sanat sayesinde sınırlarını aşmış, geleceğe umutla bakabilmiştir. (P-0)\nBu parçanın ana düşüncesi nedir?",
          "options": [
            "A) Sanat sadece geçmişte kalmıştır.",
            "B) Sanat, toplumsal ilerleme ve vizyon için vazgeçilmezdir.",
            "C) Sanat sadece bireyseldir.",
            "D) Sanat zaman kaybıdır.",
            "E) İnsanlar Sanat ile ilgilenmemelidir."
          ],
          "correct": 1,
          "solution": "Doğru cevap Sanat, toplumsal ilerleme ve vizyon için vazgeçilmezdir..",
          "id": "e1_q6",
          "no": 6
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde 'yanlış' kelimesinin yazımıyla ilgili bir kural hatırlatılmaktadır? (T-1)",
          "options": [
            "A) yanlış cümlede özne olamaz.",
            "B) yanlış kelimesi her zaman ayrı yazılır.",
            "C) yanlış kelimesi yabancı kökenlidir.",
            "D) 'yanlış' kelimesinin doğru yazımına dikkat edilmelidir.",
            "E) yanlış kelimesi fiildir."
          ],
          "correct": 3,
          "solution": "Doğru cevap 'yanlış' kelimesinin doğru yazımına dikkat edilmelidir..",
          "id": "e1_q7",
          "no": 7
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde mecaz anlamlı bir sözcük kullanılmıştır? (T-2)",
          "options": [
            "A) Suyu dolaptan soğuk içti.",
            "B) Olaylara karşı çok 'soğuk' davranıyordu.",
            "C) Kışın havalar soğuk olur.",
            "D) Hava bugün çok soğuk.",
            "E) Buzdolabı soğuk üflüyor."
          ],
          "correct": 1,
          "solution": "Doğru cevap Olaylara karşı çok 'soğuk' davranıyordu..",
          "id": "e1_q8",
          "no": 8
        },
        {
          "subject": "Türkçe",
          "text": "Teknoloji tarih boyunca insanlığın en büyük rehberlerinden biri olmuştur. Toplumlar Teknoloji sayesinde sınırlarını aşmış, geleceğe umutla bakabilmiştir. (P-3)\nBu parçanın ana düşüncesi nedir?",
          "options": [
            "A) İnsanlar Teknoloji ile ilgilenmemelidir.",
            "B) Teknoloji, toplumsal ilerleme ve vizyon için vazgeçilmezdir.",
            "C) Teknoloji zaman kaybıdır.",
            "D) Teknoloji sadece bireyseldir.",
            "E) Teknoloji sadece geçmişte kalmıştır."
          ],
          "correct": 1,
          "solution": "Doğru cevap Teknoloji, toplumsal ilerleme ve vizyon için vazgeçilmezdir..",
          "id": "e1_q9",
          "no": 9
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde 'birkaç' kelimesinin yazımıyla ilgili bir kural hatırlatılmaktadır? (T-4)",
          "options": [
            "A) birkaç kelimesi her zaman ayrı yazılır.",
            "B) 'birkaç' kelimesinin doğru yazımına dikkat edilmelidir.",
            "C) birkaç cümlede özne olamaz.",
            "D) birkaç kelimesi yabancı kökenlidir.",
            "E) birkaç kelimesi fiildir."
          ],
          "correct": 1,
          "solution": "Doğru cevap 'birkaç' kelimesinin doğru yazımına dikkat edilmelidir..",
          "id": "e1_q10",
          "no": 10
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde mecaz anlamlı bir sözcük kullanılmıştır? (T-5)",
          "options": [
            "A) Hava bugün çok soğuk.",
            "B) Kışın havalar soğuk olur.",
            "C) Olaylara karşı çok 'soğuk' davranıyordu.",
            "D) Suyu dolaptan soğuk içti.",
            "E) Buzdolabı soğuk üflüyor."
          ],
          "correct": 2,
          "solution": "Doğru cevap Olaylara karşı çok 'soğuk' davranıyordu..",
          "id": "e1_q11",
          "no": 11
        },
        {
          "subject": "Türkçe",
          "text": "Doğa tarih boyunca insanlığın en büyük rehberlerinden biri olmuştur. Toplumlar Doğa sayesinde sınırlarını aşmış, geleceğe umutla bakabilmiştir. (P-6)\nBu parçanın ana düşüncesi nedir?",
          "options": [
            "A) İnsanlar Doğa ile ilgilenmemelidir.",
            "B) Doğa sadece bireyseldir.",
            "C) Doğa, toplumsal ilerleme ve vizyon için vazgeçilmezdir.",
            "D) Doğa sadece geçmişte kalmıştır.",
            "E) Doğa zaman kaybıdır."
          ],
          "correct": 2,
          "solution": "Doğru cevap Doğa, toplumsal ilerleme ve vizyon için vazgeçilmezdir..",
          "id": "e1_q12",
          "no": 12
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde 'hiç kimse' kelimesinin yazımıyla ilgili bir kural hatırlatılmaktadır? (T-7)",
          "options": [
            "A) hiç kimse cümlede özne olamaz.",
            "B) hiç kimse kelimesi yabancı kökenlidir.",
            "C) hiç kimse kelimesi her zaman ayrı yazılır.",
            "D) 'hiç kimse' kelimesinin doğru yazımına dikkat edilmelidir.",
            "E) hiç kimse kelimesi fiildir."
          ],
          "correct": 3,
          "solution": "Doğru cevap 'hiç kimse' kelimesinin doğru yazımına dikkat edilmelidir..",
          "id": "e1_q13",
          "no": 13
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde mecaz anlamlı bir sözcük kullanılmıştır? (T-8)",
          "options": [
            "A) Hava bugün çok soğuk.",
            "B) Kışın havalar soğuk olur.",
            "C) Buzdolabı soğuk üflüyor.",
            "D) Olaylara karşı çok 'soğuk' davranıyordu.",
            "E) Suyu dolaptan soğuk içti."
          ],
          "correct": 3,
          "solution": "Doğru cevap Olaylara karşı çok 'soğuk' davranıyordu..",
          "id": "e1_q14",
          "no": 14
        },
        {
          "subject": "Türkçe",
          "text": "Psikoloji tarih boyunca insanlığın en büyük rehberlerinden biri olmuştur. Toplumlar Psikoloji sayesinde sınırlarını aşmış, geleceğe umutla bakabilmiştir. (P-9)\nBu parçanın ana düşüncesi nedir?",
          "options": [
            "A) Psikoloji sadece geçmişte kalmıştır.",
            "B) Psikoloji, toplumsal ilerleme ve vizyon için vazgeçilmezdir.",
            "C) Psikoloji zaman kaybıdır.",
            "D) İnsanlar Psikoloji ile ilgilenmemelidir.",
            "E) Psikoloji sadece bireyseldir."
          ],
          "correct": 1,
          "solution": "Doğru cevap Psikoloji, toplumsal ilerleme ve vizyon için vazgeçilmezdir..",
          "id": "e1_q15",
          "no": 15
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde 'herkes' kelimesinin yazımıyla ilgili bir kural hatırlatılmaktadır? (T-10)",
          "options": [
            "A) herkes cümlede özne olamaz.",
            "B) herkes kelimesi yabancı kökenlidir.",
            "C) herkes kelimesi her zaman ayrı yazılır.",
            "D) 'herkes' kelimesinin doğru yazımına dikkat edilmelidir.",
            "E) herkes kelimesi fiildir."
          ],
          "correct": 3,
          "solution": "Doğru cevap 'herkes' kelimesinin doğru yazımına dikkat edilmelidir..",
          "id": "e1_q16",
          "no": 16
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde mecaz anlamlı bir sözcük kullanılmıştır? (T-11)",
          "options": [
            "A) Suyu dolaptan soğuk içti.",
            "B) Buzdolabı soğuk üflüyor.",
            "C) Hava bugün çok soğuk.",
            "D) Kışın havalar soğuk olur.",
            "E) Olaylara karşı çok 'soğuk' davranıyordu."
          ],
          "correct": 4,
          "solution": "Doğru cevap Olaylara karşı çok 'soğuk' davranıyordu..",
          "id": "e1_q17",
          "no": 17
        },
        {
          "subject": "Türkçe",
          "text": "Eğitim tarih boyunca insanlığın en büyük rehberlerinden biri olmuştur. Toplumlar Eğitim sayesinde sınırlarını aşmış, geleceğe umutla bakabilmiştir. (P-12)\nBu parçanın ana düşüncesi nedir?",
          "options": [
            "A) İnsanlar Eğitim ile ilgilenmemelidir.",
            "B) Eğitim zaman kaybıdır.",
            "C) Eğitim sadece bireyseldir.",
            "D) Eğitim, toplumsal ilerleme ve vizyon için vazgeçilmezdir.",
            "E) Eğitim sadece geçmişte kalmıştır."
          ],
          "correct": 3,
          "solution": "Doğru cevap Eğitim, toplumsal ilerleme ve vizyon için vazgeçilmezdir..",
          "id": "e1_q18",
          "no": 18
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde 'bugün' kelimesinin yazımıyla ilgili bir kural hatırlatılmaktadır? (T-13)",
          "options": [
            "A) bugün kelimesi yabancı kökenlidir.",
            "B) 'bugün' kelimesinin doğru yazımına dikkat edilmelidir.",
            "C) bugün kelimesi her zaman ayrı yazılır.",
            "D) bugün kelimesi fiildir.",
            "E) bugün cümlede özne olamaz."
          ],
          "correct": 1,
          "solution": "Doğru cevap 'bugün' kelimesinin doğru yazımına dikkat edilmelidir..",
          "id": "e1_q19",
          "no": 19
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde mecaz anlamlı bir sözcük kullanılmıştır? (T-14)",
          "options": [
            "A) Kışın havalar soğuk olur.",
            "B) Buzdolabı soğuk üflüyor.",
            "C) Hava bugün çok soğuk.",
            "D) Suyu dolaptan soğuk içti.",
            "E) Olaylara karşı çok 'soğuk' davranıyordu."
          ],
          "correct": 4,
          "solution": "Doğru cevap Olaylara karşı çok 'soğuk' davranıyordu..",
          "id": "e1_q20",
          "no": 20
        },
        {
          "subject": "Türkçe",
          "text": "Kültür tarih boyunca insanlığın en büyük rehberlerinden biri olmuştur. Toplumlar Kültür sayesinde sınırlarını aşmış, geleceğe umutla bakabilmiştir. (P-15)\nBu parçanın ana düşüncesi nedir?",
          "options": [
            "A) İnsanlar Kültür ile ilgilenmemelidir.",
            "B) Kültür, toplumsal ilerleme ve vizyon için vazgeçilmezdir.",
            "C) Kültür sadece bireyseldir.",
            "D) Kültür sadece geçmişte kalmıştır.",
            "E) Kültür zaman kaybıdır."
          ],
          "correct": 1,
          "solution": "Doğru cevap Kültür, toplumsal ilerleme ve vizyon için vazgeçilmezdir..",
          "id": "e1_q21",
          "no": 21
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde 'yalnız' kelimesinin yazımıyla ilgili bir kural hatırlatılmaktadır? (T-16)",
          "options": [
            "A) yalnız kelimesi her zaman ayrı yazılır.",
            "B) yalnız kelimesi yabancı kökenlidir.",
            "C) 'yalnız' kelimesinin doğru yazımına dikkat edilmelidir.",
            "D) yalnız kelimesi fiildir.",
            "E) yalnız cümlede özne olamaz."
          ],
          "correct": 2,
          "solution": "Doğru cevap 'yalnız' kelimesinin doğru yazımına dikkat edilmelidir..",
          "id": "e1_q22",
          "no": 22
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde mecaz anlamlı bir sözcük kullanılmıştır? (T-17)",
          "options": [
            "A) Olaylara karşı çok 'soğuk' davranıyordu.",
            "B) Buzdolabı soğuk üflüyor.",
            "C) Suyu dolaptan soğuk içti.",
            "D) Hava bugün çok soğuk.",
            "E) Kışın havalar soğuk olur."
          ],
          "correct": 0,
          "solution": "Doğru cevap Olaylara karşı çok 'soğuk' davranıyordu..",
          "id": "e1_q23",
          "no": 23
        },
        {
          "subject": "Türkçe",
          "text": "Felsefe tarih boyunca insanlığın en büyük rehberlerinden biri olmuştur. Toplumlar Felsefe sayesinde sınırlarını aşmış, geleceğe umutla bakabilmiştir. (P-18)\nBu parçanın ana düşüncesi nedir?",
          "options": [
            "A) Felsefe sadece bireyseldir.",
            "B) İnsanlar Felsefe ile ilgilenmemelidir.",
            "C) Felsefe sadece geçmişte kalmıştır.",
            "D) Felsefe zaman kaybıdır.",
            "E) Felsefe, toplumsal ilerleme ve vizyon için vazgeçilmezdir."
          ],
          "correct": 4,
          "solution": "Doğru cevap Felsefe, toplumsal ilerleme ve vizyon için vazgeçilmezdir..",
          "id": "e1_q24",
          "no": 24
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde 'hiçbir' kelimesinin yazımıyla ilgili bir kural hatırlatılmaktadır? (T-19)",
          "options": [
            "A) 'hiçbir' kelimesinin doğru yazımına dikkat edilmelidir.",
            "B) hiçbir cümlede özne olamaz.",
            "C) hiçbir kelimesi her zaman ayrı yazılır.",
            "D) hiçbir kelimesi yabancı kökenlidir.",
            "E) hiçbir kelimesi fiildir."
          ],
          "correct": 0,
          "solution": "Doğru cevap 'hiçbir' kelimesinin doğru yazımına dikkat edilmelidir..",
          "id": "e1_q25",
          "no": 25
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde mecaz anlamlı bir sözcük kullanılmıştır? (T-20)",
          "options": [
            "A) Olaylara karşı çok 'soğuk' davranıyordu.",
            "B) Kışın havalar soğuk olur.",
            "C) Suyu dolaptan soğuk içti.",
            "D) Hava bugün çok soğuk.",
            "E) Buzdolabı soğuk üflüyor."
          ],
          "correct": 0,
          "solution": "Doğru cevap Olaylara karşı çok 'soğuk' davranıyordu..",
          "id": "e1_q26",
          "no": 26
        },
        {
          "subject": "Türkçe",
          "text": "Edebiyat tarih boyunca insanlığın en büyük rehberlerinden biri olmuştur. Toplumlar Edebiyat sayesinde sınırlarını aşmış, geleceğe umutla bakabilmiştir. (P-21)\nBu parçanın ana düşüncesi nedir?",
          "options": [
            "A) İnsanlar Edebiyat ile ilgilenmemelidir.",
            "B) Edebiyat, toplumsal ilerleme ve vizyon için vazgeçilmezdir.",
            "C) Edebiyat zaman kaybıdır.",
            "D) Edebiyat sadece geçmişte kalmıştır.",
            "E) Edebiyat sadece bireyseldir."
          ],
          "correct": 1,
          "solution": "Doğru cevap Edebiyat, toplumsal ilerleme ve vizyon için vazgeçilmezdir..",
          "id": "e1_q27",
          "no": 27
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde 'her şey' kelimesinin yazımıyla ilgili bir kural hatırlatılmaktadır? (T-22)",
          "options": [
            "A) 'her şey' kelimesinin doğru yazımına dikkat edilmelidir.",
            "B) her şey kelimesi fiildir.",
            "C) her şey kelimesi her zaman ayrı yazılır.",
            "D) her şey cümlede özne olamaz.",
            "E) her şey kelimesi yabancı kökenlidir."
          ],
          "correct": 0,
          "solution": "Doğru cevap 'her şey' kelimesinin doğru yazımına dikkat edilmelidir..",
          "id": "e1_q28",
          "no": 28
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde mecaz anlamlı bir sözcük kullanılmıştır? (T-23)",
          "options": [
            "A) Olaylara karşı çok 'soğuk' davranıyordu.",
            "B) Suyu dolaptan soğuk içti.",
            "C) Buzdolabı soğuk üflüyor.",
            "D) Kışın havalar soğuk olur.",
            "E) Hava bugün çok soğuk."
          ],
          "correct": 0,
          "solution": "Doğru cevap Olaylara karşı çok 'soğuk' davranıyordu..",
          "id": "e1_q29",
          "no": 29
        },
        {
          "subject": "Türkçe",
          "text": "Tarih tarih boyunca insanlığın en büyük rehberlerinden biri olmuştur. Toplumlar Tarih sayesinde sınırlarını aşmış, geleceğe umutla bakabilmiştir. (P-24)\nBu parçanın ana düşüncesi nedir?",
          "options": [
            "A) Tarih sadece bireyseldir.",
            "B) İnsanlar Tarih ile ilgilenmemelidir.",
            "C) Tarih zaman kaybıdır.",
            "D) Tarih sadece geçmişte kalmıştır.",
            "E) Tarih, toplumsal ilerleme ve vizyon için vazgeçilmezdir."
          ],
          "correct": 4,
          "solution": "Doğru cevap Tarih, toplumsal ilerleme ve vizyon için vazgeçilmezdir..",
          "id": "e1_q30",
          "no": 30
        },
        {
          "subject": "Matematik",
          "text": "3x + 37 = 55 denkleminde x kaçtır? (SoruID: M0)",
          "options": [
            "A) 5",
            "B) 7",
            "C) 8",
            "D) 6",
            "E) 9"
          ],
          "correct": 3,
          "solution": "Doğru cevap 6.",
          "id": "e1_q31",
          "no": 31
        },
        {
          "subject": "Matematik",
          "text": "190 sayısının %75'si kaçtır? (SoruID: M1)",
          "options": [
            "A) 157",
            "B) 147",
            "C) 137",
            "D) 142",
            "E) 152"
          ],
          "correct": 3,
          "solution": "Doğru cevap 142.",
          "id": "e1_q32",
          "no": 32
        },
        {
          "subject": "Matematik",
          "text": "13, 19 ve 13 sayılarının aritmetik ortalaması kaçtır? (SoruID: M2)",
          "options": [
            "A) 13",
            "B) 16",
            "C) 14",
            "D) 15",
            "E) 17"
          ],
          "correct": 3,
          "solution": "Doğru cevap 15.",
          "id": "e1_q33",
          "no": 33
        },
        {
          "subject": "Matematik",
          "text": "Ali 20, Ayşe 16 yaşındadır. 9 yıl sonra yaşları toplamı kaç olur? (SoruID: M3)",
          "options": [
            "A) 54",
            "B) 55",
            "C) 63",
            "D) 53",
            "E) 45"
          ],
          "correct": 0,
          "solution": "Doğru cevap 54.",
          "id": "e1_q34",
          "no": 34
        },
        {
          "subject": "Matematik",
          "text": "√9 + √49 işleminin sonucu kaçtır? (SoruID: M4)",
          "options": [
            "A) 8",
            "B) 12",
            "C) 11",
            "D) 9",
            "E) 10"
          ],
          "correct": 4,
          "solution": "Doğru cevap 10.",
          "id": "e1_q35",
          "no": 35
        },
        {
          "subject": "Matematik",
          "text": "4x + 46 = 106 denkleminde x kaçtır? (SoruID: M5)",
          "options": [
            "A) 17",
            "B) 16",
            "C) 15",
            "D) 14",
            "E) 18"
          ],
          "correct": 2,
          "solution": "Doğru cevap 15.",
          "id": "e1_q36",
          "no": 36
        },
        {
          "subject": "Matematik",
          "text": "150 sayısının %75'si kaçtır? (SoruID: M6)",
          "options": [
            "A) 127",
            "B) 107",
            "C) 122",
            "D) 112",
            "E) 117"
          ],
          "correct": 3,
          "solution": "Doğru cevap 112.",
          "id": "e1_q37",
          "no": 37
        },
        {
          "subject": "Matematik",
          "text": "13, 23 ve 27 sayılarının aritmetik ortalaması kaçtır? (SoruID: M7)",
          "options": [
            "A) 21",
            "B) 20",
            "C) 22",
            "D) 23",
            "E) 19"
          ],
          "correct": 0,
          "solution": "Doğru cevap 21.",
          "id": "e1_q38",
          "no": 38
        },
        {
          "subject": "Matematik",
          "text": "Ali 23, Ayşe 25 yaşındadır. 3 yıl sonra yaşları toplamı kaç olur? (SoruID: M8)",
          "options": [
            "A) 55",
            "B) 51",
            "C) 54",
            "D) 57",
            "E) 53"
          ],
          "correct": 2,
          "solution": "Doğru cevap 54.",
          "id": "e1_q39",
          "no": 39
        },
        {
          "subject": "Matematik",
          "text": "√9 + √64 işleminin sonucu kaçtır? (SoruID: M9)",
          "options": [
            "A) 10",
            "B) 11",
            "C) 9",
            "D) 12",
            "E) 13"
          ],
          "correct": 1,
          "solution": "Doğru cevap 11.",
          "id": "e1_q40",
          "no": 40
        },
        {
          "subject": "Matematik",
          "text": "3x + 49 = 82 denkleminde x kaçtır? (SoruID: M10)",
          "options": [
            "A) 11",
            "B) 12",
            "C) 10",
            "D) 14",
            "E) 13"
          ],
          "correct": 0,
          "solution": "Doğru cevap 11.",
          "id": "e1_q41",
          "no": 41
        },
        {
          "subject": "Matematik",
          "text": "160 sayısının %40'si kaçtır? (SoruID: M11)",
          "options": [
            "A) 64",
            "B) 59",
            "C) 74",
            "D) 69",
            "E) 79"
          ],
          "correct": 0,
          "solution": "Doğru cevap 64.",
          "id": "e1_q42",
          "no": 42
        },
        {
          "subject": "Matematik",
          "text": "16, 19 ve 19 sayılarının aritmetik ortalaması kaçtır? (SoruID: M12)",
          "options": [
            "A) 17",
            "B) 19",
            "C) 20",
            "D) 16",
            "E) 18"
          ],
          "correct": 4,
          "solution": "Doğru cevap 18.",
          "id": "e1_q43",
          "no": 43
        },
        {
          "subject": "Matematik",
          "text": "Ali 25, Ayşe 21 yaşındadır. 6 yıl sonra yaşları toplamı kaç olur? (SoruID: M13)",
          "options": [
            "A) 58",
            "B) 57",
            "C) 64",
            "D) 59",
            "E) 52"
          ],
          "correct": 0,
          "solution": "Doğru cevap 58.",
          "id": "e1_q44",
          "no": 44
        },
        {
          "subject": "Matematik",
          "text": "√64 + √4 işleminin sonucu kaçtır? (SoruID: M14)",
          "options": [
            "A) 12",
            "B) 10",
            "C) 11",
            "D) 8",
            "E) 9"
          ],
          "correct": 1,
          "solution": "Doğru cevap 10.",
          "id": "e1_q45",
          "no": 45
        },
        {
          "subject": "Matematik",
          "text": "9x + 50 = 158 denkleminde x kaçtır? (SoruID: M15)",
          "options": [
            "A) 14",
            "B) 12",
            "C) 13",
            "D) 11",
            "E) 15"
          ],
          "correct": 1,
          "solution": "Doğru cevap 12.",
          "id": "e1_q46",
          "no": 46
        },
        {
          "subject": "Matematik",
          "text": "170 sayısının %75'si kaçtır? (SoruID: M16)",
          "options": [
            "A) 142",
            "B) 132",
            "C) 137",
            "D) 122",
            "E) 127"
          ],
          "correct": 4,
          "solution": "Doğru cevap 127.",
          "id": "e1_q47",
          "no": 47
        },
        {
          "subject": "Matematik",
          "text": "13, 16 ve 25 sayılarının aritmetik ortalaması kaçtır? (SoruID: M17)",
          "options": [
            "A) 16",
            "B) 17",
            "C) 18",
            "D) 20",
            "E) 19"
          ],
          "correct": 2,
          "solution": "Doğru cevap 18.",
          "id": "e1_q48",
          "no": 48
        },
        {
          "subject": "Matematik",
          "text": "Ali 10, Ayşe 24 yaşındadır. 4 yıl sonra yaşları toplamı kaç olur? (SoruID: M18)",
          "options": [
            "A) 43",
            "B) 38",
            "C) 42",
            "D) 46",
            "E) 41"
          ],
          "correct": 2,
          "solution": "Doğru cevap 42.",
          "id": "e1_q49",
          "no": 49
        },
        {
          "subject": "Matematik",
          "text": "√4 + √36 işleminin sonucu kaçtır? (SoruID: M19)",
          "options": [
            "A) 6",
            "B) 10",
            "C) 8",
            "D) 9",
            "E) 7"
          ],
          "correct": 2,
          "solution": "Doğru cevap 8.",
          "id": "e1_q50",
          "no": 50
        },
        {
          "subject": "Matematik",
          "text": "9x + 13 = 121 denkleminde x kaçtır? (SoruID: M20)",
          "options": [
            "A) 11",
            "B) 12",
            "C) 14",
            "D) 13",
            "E) 15"
          ],
          "correct": 1,
          "solution": "Doğru cevap 12.",
          "id": "e1_q51",
          "no": 51
        },
        {
          "subject": "Matematik",
          "text": "200 sayısının %40'si kaçtır? (SoruID: M21)",
          "options": [
            "A) 90",
            "B) 95",
            "C) 75",
            "D) 85",
            "E) 80"
          ],
          "correct": 4,
          "solution": "Doğru cevap 80.",
          "id": "e1_q52",
          "no": 52
        },
        {
          "subject": "Matematik",
          "text": "14, 28 ve 21 sayılarının aritmetik ortalaması kaçtır? (SoruID: M22)",
          "options": [
            "A) 20",
            "B) 21",
            "C) 22",
            "D) 23",
            "E) 19"
          ],
          "correct": 1,
          "solution": "Doğru cevap 21.",
          "id": "e1_q53",
          "no": 53
        },
        {
          "subject": "Matematik",
          "text": "Ali 16, Ayşe 22 yaşındadır. 3 yıl sonra yaşları toplamı kaç olur? (SoruID: M23)",
          "options": [
            "A) 47",
            "B) 41",
            "C) 43",
            "D) 45",
            "E) 44"
          ],
          "correct": 4,
          "solution": "Doğru cevap 44.",
          "id": "e1_q54",
          "no": 54
        },
        {
          "subject": "Matematik",
          "text": "√49 + √49 işleminin sonucu kaçtır? (SoruID: M24)",
          "options": [
            "A) 16",
            "B) 15",
            "C) 13",
            "D) 12",
            "E) 14"
          ],
          "correct": 4,
          "solution": "Doğru cevap 14.",
          "id": "e1_q55",
          "no": 55
        },
        {
          "subject": "Matematik",
          "text": "7x + 24 = 101 denkleminde x kaçtır? (SoruID: M25)",
          "options": [
            "A) 14",
            "B) 12",
            "C) 11",
            "D) 10",
            "E) 13"
          ],
          "correct": 2,
          "solution": "Doğru cevap 11.",
          "id": "e1_q56",
          "no": 56
        },
        {
          "subject": "Matematik",
          "text": "180 sayısının %25'si kaçtır? (SoruID: M26)",
          "options": [
            "A) 45",
            "B) 40",
            "C) 50",
            "D) 60",
            "E) 55"
          ],
          "correct": 0,
          "solution": "Doğru cevap 45.",
          "id": "e1_q57",
          "no": 57
        },
        {
          "subject": "Matematik",
          "text": "24, 29 ve 19 sayılarının aritmetik ortalaması kaçtır? (SoruID: M27)",
          "options": [
            "A) 25",
            "B) 23",
            "C) 22",
            "D) 26",
            "E) 24"
          ],
          "correct": 4,
          "solution": "Doğru cevap 24.",
          "id": "e1_q58",
          "no": 58
        },
        {
          "subject": "Matematik",
          "text": "Ali 15, Ayşe 11 yaşındadır. 3 yıl sonra yaşları toplamı kaç olur? (SoruID: M28)",
          "options": [
            "A) 29",
            "B) 32",
            "C) 31",
            "D) 35",
            "E) 33"
          ],
          "correct": 1,
          "solution": "Doğru cevap 32.",
          "id": "e1_q59",
          "no": 59
        },
        {
          "subject": "Matematik",
          "text": "√16 + √25 işleminin sonucu kaçtır? (SoruID: M29)",
          "options": [
            "A) 11",
            "B) 8",
            "C) 9",
            "D) 10",
            "E) 7"
          ],
          "correct": 2,
          "solution": "Doğru cevap 9.",
          "id": "e1_q60",
          "no": 60
        },
        {
          "subject": "Tarih",
          "text": "Bir terör örgütü olan EOKA'nın faaliyetleri karşısında Türklerin kendilerini korumak için oluşturduğu Türk Mukavemet Teşkilatı, aşağıdaki sorunların hangisiyle ilişkili olarak kurulmuştur?",
          "options": [
            "A) Kıbrıs",
            "B) Hatay",
            "C) Batı Trakya",
            "D) Musul",
            "E) Makedonya"
          ],
          "correct": 0,
          "solution": "Doğru cevap A'dır. EOKA ve TMT, Kıbrıs sorunu ekseninde ortaya çıkmış örgütlerdir.",
          "id": "e1_q61",
          "no": 61
        },
        {
          "subject": "Tarih",
          "text": "Millî Mücadele Dönemi'ne ait bir fotoğrafta elinde Hâkimiyet-i Milliye gazetesi olan bir kişi, bu kişinin sağında asker için dikiş diken kadınlar ve tüfek tamir eden erkekler vardır. Fotoğrafın arkasında 'Ordumuz için; 15 Ağustos 1921' yazmaktadır.\nBu fotoğrafın ait olduğu dönemle ilgili aşağıdaki yorumlardan hangisi yapılamaz?",
          "options": [
            "A) Tekâlif-i Milliye Emirleri'nin uygulanmaya başlandığı",
            "B) Türk ordusunun Sakarya Nehri'nin doğusunda bulunduğu",
            "C) Mustafa Kemal Paşa'nın Başkomutanlık görevini üstlendiği",
            "D) Millî Mücadele'nin tüm milletçe topyekûn yürütüldüğü",
            "E) İstanbul'da yayımlanan bir gazetenin okunduğu"
          ],
          "correct": 4,
          "solution": "Doğru cevap E'dir. Hâkimiyet-i Milliye gazetesi İstanbul'da değil, Ankara'da yayımlanmaktaydı.",
          "id": "e1_q62",
          "no": 62
        },
        {
          "subject": "Tarih",
          "text": "Fransız Devrimi'yle Avrupa'da ortaya çıkan siyasi, sosyal ve ekonomik gelişmeler Osmanlı Devleti'nde yankı bulmuştur. 1789 yılında tahta çıkan III. Selim Dönemi'nde bu gelişmeleri yakından takip etmek amacıyla Avrupa'nın büyük devletlerinin başkentlerinde daimî elçilikler açılmıştır.\nBuna göre daimî elçilikler aşağıdakilerden hangisinde etkili olmuştur?",
          "options": [
            "A) Lale Devri'nin başlamasında",
            "B) Avrupa'daki fikir akımlarının tanınmasında",
            "C) Uluslararası diplomaside deneyim kazanılmasında",
            "D) II ve III",
            "E) I, II ve III"
          ],
          "correct": 3,
          "solution": "Doğru cevap D'dir. Elçilikler Avrupa'yı tanımak ve diplomasi deneyimi kazanmak için açılmıştır.",
          "id": "e1_q63",
          "no": 63
        },
        {
          "subject": "Tarih",
          "text": "Türk siyasi ve askerî tarihinde büyük öneme sahip olan 'Sivas Kongresi' süreci ile ilgili aşağıdakilerden hangisi söylenebilir? (H-0)",
          "options": [
            "A) Avrupa'da gerçekleşmiştir.",
            "B) Osmanlı'nın kuruluş dönemine aittir.",
            "C) Hiçbir etkisi olmamıştır.",
            "D) Sivas Kongresi dönemin en kritik gelişmelerinden biridir.",
            "E) Sadece ekonomik bir olaydır."
          ],
          "correct": 3,
          "solution": "Doğru cevap Sivas Kongresi dönemin en kritik gelişmelerinden biridir..",
          "id": "e1_q64",
          "no": 64
        },
        {
          "subject": "Tarih",
          "text": "Aşağıdaki tarihî gelişmelerden hangisi 'Erzurum Kongresi' ile doğrudan veya dolaylı olarak bağlantılıdır? (H-1)",
          "options": [
            "A) Kavimler Göçü",
            "B) Erzurum Kongresi öncesi ve sonrası yaşanan siyasi krizler.",
            "C) Fransız İhtilali",
            "D) Coğrafi Keşifler",
            "E) Sanayi İnkılabı"
          ],
          "correct": 1,
          "solution": "Doğru cevap Erzurum Kongresi öncesi ve sonrası yaşanan siyasi krizler..",
          "id": "e1_q65",
          "no": 65
        },
        {
          "subject": "Tarih",
          "text": "Millî Mücadele ve inkılaplar tarihi incelendiğinde 'Amasya Genelgesi' olayının temel amacı aşağıdakilerden hangisidir? (H-2)",
          "options": [
            "A) Avrupa'ya göç etmek",
            "B) Yeni sömürgeler elde etmek",
            "C) Feodaliteyi kurmak",
            "D) Saltanatı güçlendirmek",
            "E) Bağımsızlık ve egemenliği pekiştirmek"
          ],
          "correct": 4,
          "solution": "Doğru cevap Bağımsızlık ve egemenliği pekiştirmek.",
          "id": "e1_q66",
          "no": 66
        },
        {
          "subject": "Tarih",
          "text": "Türk siyasi ve askerî tarihinde büyük öneme sahip olan 'Lozan Antlaşması' süreci ile ilgili aşağıdakilerden hangisi söylenebilir? (H-3)",
          "options": [
            "A) Lozan Antlaşması dönemin en kritik gelişmelerinden biridir.",
            "B) Avrupa'da gerçekleşmiştir.",
            "C) Hiçbir etkisi olmamıştır.",
            "D) Osmanlı'nın kuruluş dönemine aittir.",
            "E) Sadece ekonomik bir olaydır."
          ],
          "correct": 0,
          "solution": "Doğru cevap Lozan Antlaşması dönemin en kritik gelişmelerinden biridir..",
          "id": "e1_q67",
          "no": 67
        },
        {
          "subject": "Tarih",
          "text": "Aşağıdaki tarihî gelişmelerden hangisi 'Cumhuriyetin İlanı' ile doğrudan veya dolaylı olarak bağlantılıdır? (H-4)",
          "options": [
            "A) Fransız İhtilali",
            "B) Cumhuriyetin İlanı öncesi ve sonrası yaşanan siyasi krizler.",
            "C) Kavimler Göçü",
            "D) Sanayi İnkılabı",
            "E) Coğrafi Keşifler"
          ],
          "correct": 1,
          "solution": "Doğru cevap Cumhuriyetin İlanı öncesi ve sonrası yaşanan siyasi krizler..",
          "id": "e1_q68",
          "no": 68
        },
        {
          "subject": "Tarih",
          "text": "Millî Mücadele ve inkılaplar tarihi incelendiğinde 'TBMM'nin Açılışı' olayının temel amacı aşağıdakilerden hangisidir? (H-5)",
          "options": [
            "A) Avrupa'ya göç etmek",
            "B) Feodaliteyi kurmak",
            "C) Bağımsızlık ve egemenliği pekiştirmek",
            "D) Yeni sömürgeler elde etmek",
            "E) Saltanatı güçlendirmek"
          ],
          "correct": 2,
          "solution": "Doğru cevap Bağımsızlık ve egemenliği pekiştirmek.",
          "id": "e1_q69",
          "no": 69
        },
        {
          "subject": "Tarih",
          "text": "Türk siyasi ve askerî tarihinde büyük öneme sahip olan 'Mudanya Mütarekesi' süreci ile ilgili aşağıdakilerden hangisi söylenebilir? (H-6)",
          "options": [
            "A) Avrupa'da gerçekleşmiştir.",
            "B) Osmanlı'nın kuruluş dönemine aittir.",
            "C) Mudanya Mütarekesi dönemin en kritik gelişmelerinden biridir.",
            "D) Hiçbir etkisi olmamıştır.",
            "E) Sadece ekonomik bir olaydır."
          ],
          "correct": 2,
          "solution": "Doğru cevap Mudanya Mütarekesi dönemin en kritik gelişmelerinden biridir..",
          "id": "e1_q70",
          "no": 70
        },
        {
          "subject": "Tarih",
          "text": "Aşağıdaki tarihî gelişmelerden hangisi 'Saltanatın Kaldırılması' ile doğrudan veya dolaylı olarak bağlantılıdır? (H-7)",
          "options": [
            "A) Saltanatın Kaldırılması öncesi ve sonrası yaşanan siyasi krizler.",
            "B) Coğrafi Keşifler",
            "C) Fransız İhtilali",
            "D) Sanayi İnkılabı",
            "E) Kavimler Göçü"
          ],
          "correct": 0,
          "solution": "Doğru cevap Saltanatın Kaldırılması öncesi ve sonrası yaşanan siyasi krizler..",
          "id": "e1_q71",
          "no": 71
        },
        {
          "subject": "Tarih",
          "text": "Millî Mücadele ve inkılaplar tarihi incelendiğinde 'Halifeliğin Kaldırılması' olayının temel amacı aşağıdakilerden hangisidir? (H-8)",
          "options": [
            "A) Yeni sömürgeler elde etmek",
            "B) Bağımsızlık ve egemenliği pekiştirmek",
            "C) Saltanatı güçlendirmek",
            "D) Avrupa'ya göç etmek",
            "E) Feodaliteyi kurmak"
          ],
          "correct": 1,
          "solution": "Doğru cevap Bağımsızlık ve egemenliği pekiştirmek.",
          "id": "e1_q72",
          "no": 72
        },
        {
          "subject": "Tarih",
          "text": "Türk siyasi ve askerî tarihinde büyük öneme sahip olan 'Tevhid-i Tedrisat' süreci ile ilgili aşağıdakilerden hangisi söylenebilir? (H-9)",
          "options": [
            "A) Hiçbir etkisi olmamıştır.",
            "B) Osmanlı'nın kuruluş dönemine aittir.",
            "C) Tevhid-i Tedrisat dönemin en kritik gelişmelerinden biridir.",
            "D) Avrupa'da gerçekleşmiştir.",
            "E) Sadece ekonomik bir olaydır."
          ],
          "correct": 2,
          "solution": "Doğru cevap Tevhid-i Tedrisat dönemin en kritik gelişmelerinden biridir..",
          "id": "e1_q73",
          "no": 73
        },
        {
          "subject": "Tarih",
          "text": "Aşağıdaki tarihî gelişmelerden hangisi 'Trablusgarp Savaşı' ile doğrudan veya dolaylı olarak bağlantılıdır? (H-10)",
          "options": [
            "A) Sanayi İnkılabı",
            "B) Fransız İhtilali",
            "C) Trablusgarp Savaşı öncesi ve sonrası yaşanan siyasi krizler.",
            "D) Kavimler Göçü",
            "E) Coğrafi Keşifler"
          ],
          "correct": 2,
          "solution": "Doğru cevap Trablusgarp Savaşı öncesi ve sonrası yaşanan siyasi krizler..",
          "id": "e1_q74",
          "no": 74
        },
        {
          "subject": "Tarih",
          "text": "Millî Mücadele ve inkılaplar tarihi incelendiğinde 'Balkan Savaşları' olayının temel amacı aşağıdakilerden hangisidir? (H-11)",
          "options": [
            "A) Bağımsızlık ve egemenliği pekiştirmek",
            "B) Yeni sömürgeler elde etmek",
            "C) Avrupa'ya göç etmek",
            "D) Saltanatı güçlendirmek",
            "E) Feodaliteyi kurmak"
          ],
          "correct": 0,
          "solution": "Doğru cevap Bağımsızlık ve egemenliği pekiştirmek.",
          "id": "e1_q75",
          "no": 75
        },
        {
          "subject": "Tarih",
          "text": "Türk siyasi ve askerî tarihinde büyük öneme sahip olan 'I. Dünya Savaşı' süreci ile ilgili aşağıdakilerden hangisi söylenebilir? (H-12)",
          "options": [
            "A) Sadece ekonomik bir olaydır.",
            "B) Hiçbir etkisi olmamıştır.",
            "C) Avrupa'da gerçekleşmiştir.",
            "D) Osmanlı'nın kuruluş dönemine aittir.",
            "E) I. Dünya Savaşı dönemin en kritik gelişmelerinden biridir."
          ],
          "correct": 4,
          "solution": "Doğru cevap I. Dünya Savaşı dönemin en kritik gelişmelerinden biridir..",
          "id": "e1_q76",
          "no": 76
        },
        {
          "subject": "Tarih",
          "text": "Aşağıdaki tarihî gelişmelerden hangisi 'Çanakkale Cephesi' ile doğrudan veya dolaylı olarak bağlantılıdır? (H-13)",
          "options": [
            "A) Coğrafi Keşifler",
            "B) Sanayi İnkılabı",
            "C) Çanakkale Cephesi öncesi ve sonrası yaşanan siyasi krizler.",
            "D) Fransız İhtilali",
            "E) Kavimler Göçü"
          ],
          "correct": 2,
          "solution": "Doğru cevap Çanakkale Cephesi öncesi ve sonrası yaşanan siyasi krizler..",
          "id": "e1_q77",
          "no": 77
        },
        {
          "subject": "Tarih",
          "text": "Millî Mücadele ve inkılaplar tarihi incelendiğinde 'Sakarya Meydan Muharebesi' olayının temel amacı aşağıdakilerden hangisidir? (H-14)",
          "options": [
            "A) Saltanatı güçlendirmek",
            "B) Feodaliteyi kurmak",
            "C) Yeni sömürgeler elde etmek",
            "D) Avrupa'ya göç etmek",
            "E) Bağımsızlık ve egemenliği pekiştirmek"
          ],
          "correct": 4,
          "solution": "Doğru cevap Bağımsızlık ve egemenliği pekiştirmek.",
          "id": "e1_q78",
          "no": 78
        },
        {
          "subject": "Tarih",
          "text": "Türk siyasi ve askerî tarihinde büyük öneme sahip olan 'Büyük Taarruz' süreci ile ilgili aşağıdakilerden hangisi söylenebilir? (H-15)",
          "options": [
            "A) Büyük Taarruz dönemin en kritik gelişmelerinden biridir.",
            "B) Hiçbir etkisi olmamıştır.",
            "C) Sadece ekonomik bir olaydır.",
            "D) Avrupa'da gerçekleşmiştir.",
            "E) Osmanlı'nın kuruluş dönemine aittir."
          ],
          "correct": 0,
          "solution": "Doğru cevap Büyük Taarruz dönemin en kritik gelişmelerinden biridir..",
          "id": "e1_q79",
          "no": 79
        },
        {
          "subject": "Tarih",
          "text": "Aşağıdaki tarihî gelişmelerden hangisi 'I. İnönü Muharebesi' ile doğrudan veya dolaylı olarak bağlantılıdır? (H-16)",
          "options": [
            "A) Fransız İhtilali",
            "B) I. İnönü Muharebesi öncesi ve sonrası yaşanan siyasi krizler.",
            "C) Sanayi İnkılabı",
            "D) Kavimler Göçü",
            "E) Coğrafi Keşifler"
          ],
          "correct": 1,
          "solution": "Doğru cevap I. İnönü Muharebesi öncesi ve sonrası yaşanan siyasi krizler..",
          "id": "e1_q80",
          "no": 80
        },
        {
          "subject": "Tarih",
          "text": "Millî Mücadele ve inkılaplar tarihi incelendiğinde 'II. İnönü Muharebesi' olayının temel amacı aşağıdakilerden hangisidir? (H-17)",
          "options": [
            "A) Saltanatı güçlendirmek",
            "B) Yeni sömürgeler elde etmek",
            "C) Bağımsızlık ve egemenliği pekiştirmek",
            "D) Feodaliteyi kurmak",
            "E) Avrupa'ya göç etmek"
          ],
          "correct": 2,
          "solution": "Doğru cevap Bağımsızlık ve egemenliği pekiştirmek.",
          "id": "e1_q81",
          "no": 81
        },
        {
          "subject": "Tarih",
          "text": "Türk siyasi ve askerî tarihinde büyük öneme sahip olan 'Kars Antlaşması' süreci ile ilgili aşağıdakilerden hangisi söylenebilir? (H-18)",
          "options": [
            "A) Hiçbir etkisi olmamıştır.",
            "B) Kars Antlaşması dönemin en kritik gelişmelerinden biridir.",
            "C) Avrupa'da gerçekleşmiştir.",
            "D) Sadece ekonomik bir olaydır.",
            "E) Osmanlı'nın kuruluş dönemine aittir."
          ],
          "correct": 1,
          "solution": "Doğru cevap Kars Antlaşması dönemin en kritik gelişmelerinden biridir..",
          "id": "e1_q82",
          "no": 82
        },
        {
          "subject": "Tarih",
          "text": "Aşağıdaki tarihî gelişmelerden hangisi 'Ankara Antlaşması' ile doğrudan veya dolaylı olarak bağlantılıdır? (H-19)",
          "options": [
            "A) Coğrafi Keşifler",
            "B) Ankara Antlaşması öncesi ve sonrası yaşanan siyasi krizler.",
            "C) Kavimler Göçü",
            "D) Fransız İhtilali",
            "E) Sanayi İnkılabı"
          ],
          "correct": 1,
          "solution": "Doğru cevap Ankara Antlaşması öncesi ve sonrası yaşanan siyasi krizler..",
          "id": "e1_q83",
          "no": 83
        },
        {
          "subject": "Tarih",
          "text": "Millî Mücadele ve inkılaplar tarihi incelendiğinde 'Sivas Kongresi' olayının temel amacı aşağıdakilerden hangisidir? (H-20)",
          "options": [
            "A) Avrupa'ya göç etmek",
            "B) Saltanatı güçlendirmek",
            "C) Yeni sömürgeler elde etmek",
            "D) Feodaliteyi kurmak",
            "E) Bağımsızlık ve egemenliği pekiştirmek"
          ],
          "correct": 4,
          "solution": "Doğru cevap Bağımsızlık ve egemenliği pekiştirmek.",
          "id": "e1_q84",
          "no": 84
        },
        {
          "subject": "Tarih",
          "text": "Türk siyasi ve askerî tarihinde büyük öneme sahip olan 'Erzurum Kongresi' süreci ile ilgili aşağıdakilerden hangisi söylenebilir? (H-21)",
          "options": [
            "A) Avrupa'da gerçekleşmiştir.",
            "B) Erzurum Kongresi dönemin en kritik gelişmelerinden biridir.",
            "C) Sadece ekonomik bir olaydır.",
            "D) Osmanlı'nın kuruluş dönemine aittir.",
            "E) Hiçbir etkisi olmamıştır."
          ],
          "correct": 1,
          "solution": "Doğru cevap Erzurum Kongresi dönemin en kritik gelişmelerinden biridir..",
          "id": "e1_q85",
          "no": 85
        },
        {
          "subject": "Tarih",
          "text": "Aşağıdaki tarihî gelişmelerden hangisi 'Amasya Genelgesi' ile doğrudan veya dolaylı olarak bağlantılıdır? (H-22)",
          "options": [
            "A) Amasya Genelgesi öncesi ve sonrası yaşanan siyasi krizler.",
            "B) Fransız İhtilali",
            "C) Kavimler Göçü",
            "D) Sanayi İnkılabı",
            "E) Coğrafi Keşifler"
          ],
          "correct": 0,
          "solution": "Doğru cevap Amasya Genelgesi öncesi ve sonrası yaşanan siyasi krizler..",
          "id": "e1_q86",
          "no": 86
        },
        {
          "subject": "Tarih",
          "text": "Millî Mücadele ve inkılaplar tarihi incelendiğinde 'Lozan Antlaşması' olayının temel amacı aşağıdakilerden hangisidir? (H-23)",
          "options": [
            "A) Feodaliteyi kurmak",
            "B) Yeni sömürgeler elde etmek",
            "C) Avrupa'ya göç etmek",
            "D) Bağımsızlık ve egemenliği pekiştirmek",
            "E) Saltanatı güçlendirmek"
          ],
          "correct": 3,
          "solution": "Doğru cevap Bağımsızlık ve egemenliği pekiştirmek.",
          "id": "e1_q87",
          "no": 87
        },
        {
          "subject": "Coğrafya",
          "text": "Aşağıdakilerin hangisinde yaşayan insanlar, şehirler arası yolculuk yapmak için yaşadıkları ilde kara yolu, demir yolu, deniz yolu ve hava yolu ulaşım olanaklarının tamamına ulaşabilirler?",
          "options": [
            "A) Trabzon",
            "B) Antalya",
            "C) Ankara",
            "D) İzmir",
            "E) Rize"
          ],
          "correct": 3,
          "solution": "Doğru cevap D'dir. İzmir'de kara, hava, deniz ve demir yolu ulaşımının tamamı mevcuttur.",
          "id": "e1_q88",
          "no": 88
        },
        {
          "subject": "Coğrafya",
          "text": "Normal faylar arasında yükselen bloklar horst yapıları olarak adlandırılmaktadır. Türkiye'deki bazı dağlar büyük horst yapılarından oluşmuştur.\nAşağıdakilerden hangisi, bu şekilde oluşmuş dağlardan biri değildir?",
          "options": [
            "A) Boz Dağlar",
            "B) Aydın Dağları",
            "C) Yunt Dağı",
            "D) Tahtalı Dağları",
            "E) Madra Dağı"
          ],
          "correct": 3,
          "solution": "Doğru cevap D'dir. Tahtalı Dağları kıvrım (Toroslar) sistemine aittir, Ege'deki diğer dağlar ise kırık (horst) yapıdadır.",
          "id": "e1_q89",
          "no": 89
        },
        {
          "subject": "Coğrafya",
          "text": "Türkiye'nin fiziki coğrafyası düşünüldüğünde 'Van Gölü' için aşağıdakilerden hangisi doğrudur? (C-0)",
          "options": [
            "A) Van Gölü bir çöldür.",
            "B) Van Gölü yapay bir kanaldır.",
            "C) Van Gölü, ülkemizin önemli yeryüzü şekillerinden biridir.",
            "D) Van Gölü Marmara'dadır.",
            "E) Van Gölü tarıma kapalıdır."
          ],
          "correct": 2,
          "solution": "Doğru cevap Van Gölü, ülkemizin önemli yeryüzü şekillerinden biridir..",
          "id": "e1_q90",
          "no": 90
        },
        {
          "subject": "Coğrafya",
          "text": "Coğrafi özellikleri ve turizm potansiyeli göz önüne alındığında 'Ağrı Dağı' hangi alanda daha çok öne çıkar? (C-1)",
          "options": [
            "A) Doğal güzellikleri ve turizm/coğrafi önemi",
            "B) Okyanus balıkçılığı",
            "C) Sadece madencilik",
            "D) Sadece ağır sanayi",
            "E) Çöl iklimi araştırmaları"
          ],
          "correct": 0,
          "solution": "Doğru cevap Doğal güzellikleri ve turizm/coğrafi önemi.",
          "id": "e1_q91",
          "no": 91
        },
        {
          "subject": "Coğrafya",
          "text": "Türkiye'nin fiziki coğrafyası düşünüldüğünde 'Kızılırmak' için aşağıdakilerden hangisi doğrudur? (C-2)",
          "options": [
            "A) Kızılırmak yapay bir kanaldır.",
            "B) Kızılırmak Marmara'dadır.",
            "C) Kızılırmak, ülkemizin önemli yeryüzü şekillerinden biridir.",
            "D) Kızılırmak bir çöldür.",
            "E) Kızılırmak tarıma kapalıdır."
          ],
          "correct": 2,
          "solution": "Doğru cevap Kızılırmak, ülkemizin önemli yeryüzü şekillerinden biridir..",
          "id": "e1_q92",
          "no": 92
        },
        {
          "subject": "Coğrafya",
          "text": "Coğrafi özellikleri ve turizm potansiyeli göz önüne alındığında 'Erciyes Dağı' hangi alanda daha çok öne çıkar? (C-3)",
          "options": [
            "A) Okyanus balıkçılığı",
            "B) Çöl iklimi araştırmaları",
            "C) Sadece madencilik",
            "D) Doğal güzellikleri ve turizm/coğrafi önemi",
            "E) Sadece ağır sanayi"
          ],
          "correct": 3,
          "solution": "Doğru cevap Doğal güzellikleri ve turizm/coğrafi önemi.",
          "id": "e1_q93",
          "no": 93
        },
        {
          "subject": "Coğrafya",
          "text": "Türkiye'nin fiziki coğrafyası düşünüldüğünde 'Tuz Gölü' için aşağıdakilerden hangisi doğrudur? (C-4)",
          "options": [
            "A) Tuz Gölü tarıma kapalıdır.",
            "B) Tuz Gölü bir çöldür.",
            "C) Tuz Gölü, ülkemizin önemli yeryüzü şekillerinden biridir.",
            "D) Tuz Gölü Marmara'dadır.",
            "E) Tuz Gölü yapay bir kanaldır."
          ],
          "correct": 2,
          "solution": "Doğru cevap Tuz Gölü, ülkemizin önemli yeryüzü şekillerinden biridir..",
          "id": "e1_q94",
          "no": 94
        },
        {
          "subject": "Coğrafya",
          "text": "Coğrafi özellikleri ve turizm potansiyeli göz önüne alındığında 'Çukurova' hangi alanda daha çok öne çıkar? (C-5)",
          "options": [
            "A) Okyanus balıkçılığı",
            "B) Sadece madencilik",
            "C) Sadece ağır sanayi",
            "D) Çöl iklimi araştırmaları",
            "E) Doğal güzellikleri ve turizm/coğrafi önemi"
          ],
          "correct": 4,
          "solution": "Doğru cevap Doğal güzellikleri ve turizm/coğrafi önemi.",
          "id": "e1_q95",
          "no": 95
        },
        {
          "subject": "Coğrafya",
          "text": "Türkiye'nin fiziki coğrafyası düşünüldüğünde 'Bafra Ovası' için aşağıdakilerden hangisi doğrudur? (C-6)",
          "options": [
            "A) Bafra Ovası tarıma kapalıdır.",
            "B) Bafra Ovası, ülkemizin önemli yeryüzü şekillerinden biridir.",
            "C) Bafra Ovası bir çöldür.",
            "D) Bafra Ovası yapay bir kanaldır.",
            "E) Bafra Ovası Marmara'dadır."
          ],
          "correct": 1,
          "solution": "Doğru cevap Bafra Ovası, ülkemizin önemli yeryüzü şekillerinden biridir..",
          "id": "e1_q96",
          "no": 96
        },
        {
          "subject": "Coğrafya",
          "text": "Coğrafi özellikleri ve turizm potansiyeli göz önüne alındığında 'Kaçkar Dağları' hangi alanda daha çok öne çıkar? (C-7)",
          "options": [
            "A) Çöl iklimi araştırmaları",
            "B) Okyanus balıkçılığı",
            "C) Sadece ağır sanayi",
            "D) Sadece madencilik",
            "E) Doğal güzellikleri ve turizm/coğrafi önemi"
          ],
          "correct": 4,
          "solution": "Doğru cevap Doğal güzellikleri ve turizm/coğrafi önemi.",
          "id": "e1_q97",
          "no": 97
        },
        {
          "subject": "Coğrafya",
          "text": "Türkiye'nin fiziki coğrafyası düşünüldüğünde 'Gediz Nehri' için aşağıdakilerden hangisi doğrudur? (C-8)",
          "options": [
            "A) Gediz Nehri yapay bir kanaldır.",
            "B) Gediz Nehri tarıma kapalıdır.",
            "C) Gediz Nehri bir çöldür.",
            "D) Gediz Nehri, ülkemizin önemli yeryüzü şekillerinden biridir.",
            "E) Gediz Nehri Marmara'dadır."
          ],
          "correct": 3,
          "solution": "Doğru cevap Gediz Nehri, ülkemizin önemli yeryüzü şekillerinden biridir..",
          "id": "e1_q98",
          "no": 98
        },
        {
          "subject": "Coğrafya",
          "text": "Coğrafi özellikleri ve turizm potansiyeli göz önüne alındığında 'Salda Gölü' hangi alanda daha çok öne çıkar? (C-9)",
          "options": [
            "A) Okyanus balıkçılığı",
            "B) Çöl iklimi araştırmaları",
            "C) Sadece madencilik",
            "D) Sadece ağır sanayi",
            "E) Doğal güzellikleri ve turizm/coğrafi önemi"
          ],
          "correct": 4,
          "solution": "Doğru cevap Doğal güzellikleri ve turizm/coğrafi önemi.",
          "id": "e1_q99",
          "no": 99
        },
        {
          "subject": "Coğrafya",
          "text": "Türkiye'nin fiziki coğrafyası düşünüldüğünde 'Kapadokya' için aşağıdakilerden hangisi doğrudur? (C-10)",
          "options": [
            "A) Kapadokya bir çöldür.",
            "B) Kapadokya Marmara'dadır.",
            "C) Kapadokya yapay bir kanaldır.",
            "D) Kapadokya tarıma kapalıdır.",
            "E) Kapadokya, ülkemizin önemli yeryüzü şekillerinden biridir."
          ],
          "correct": 4,
          "solution": "Doğru cevap Kapadokya, ülkemizin önemli yeryüzü şekillerinden biridir..",
          "id": "e1_q100",
          "no": 100
        },
        {
          "subject": "Coğrafya",
          "text": "Coğrafi özellikleri ve turizm potansiyeli göz önüne alındığında 'Pamukkale' hangi alanda daha çok öne çıkar? (C-11)",
          "options": [
            "A) Doğal güzellikleri ve turizm/coğrafi önemi",
            "B) Okyanus balıkçılığı",
            "C) Sadece ağır sanayi",
            "D) Çöl iklimi araştırmaları",
            "E) Sadece madencilik"
          ],
          "correct": 0,
          "solution": "Doğru cevap Doğal güzellikleri ve turizm/coğrafi önemi.",
          "id": "e1_q101",
          "no": 101
        },
        {
          "subject": "Coğrafya",
          "text": "Türkiye'nin fiziki coğrafyası düşünüldüğünde 'Nemrut Dağı' için aşağıdakilerden hangisi doğrudur? (C-12)",
          "options": [
            "A) Nemrut Dağı tarıma kapalıdır.",
            "B) Nemrut Dağı bir çöldür.",
            "C) Nemrut Dağı Marmara'dadır.",
            "D) Nemrut Dağı yapay bir kanaldır.",
            "E) Nemrut Dağı, ülkemizin önemli yeryüzü şekillerinden biridir."
          ],
          "correct": 4,
          "solution": "Doğru cevap Nemrut Dağı, ülkemizin önemli yeryüzü şekillerinden biridir..",
          "id": "e1_q102",
          "no": 102
        },
        {
          "subject": "Coğrafya",
          "text": "Coğrafi özellikleri ve turizm potansiyeli göz önüne alındığında 'Sümela Manastırı' hangi alanda daha çok öne çıkar? (C-13)",
          "options": [
            "A) Sadece madencilik",
            "B) Doğal güzellikleri ve turizm/coğrafi önemi",
            "C) Okyanus balıkçılığı",
            "D) Sadece ağır sanayi",
            "E) Çöl iklimi araştırmaları"
          ],
          "correct": 1,
          "solution": "Doğru cevap Doğal güzellikleri ve turizm/coğrafi önemi.",
          "id": "e1_q103",
          "no": 103
        },
        {
          "subject": "Coğrafya",
          "text": "Türkiye'nin fiziki coğrafyası düşünüldüğünde 'Uludağ' için aşağıdakilerden hangisi doğrudur? (C-14)",
          "options": [
            "A) Uludağ, ülkemizin önemli yeryüzü şekillerinden biridir.",
            "B) Uludağ tarıma kapalıdır.",
            "C) Uludağ yapay bir kanaldır.",
            "D) Uludağ Marmara'dadır.",
            "E) Uludağ bir çöldür."
          ],
          "correct": 0,
          "solution": "Doğru cevap Uludağ, ülkemizin önemli yeryüzü şekillerinden biridir..",
          "id": "e1_q104",
          "no": 104
        },
        {
          "subject": "Coğrafya",
          "text": "Coğrafi özellikleri ve turizm potansiyeli göz önüne alındığında 'Van Gölü' hangi alanda daha çok öne çıkar? (C-15)",
          "options": [
            "A) Çöl iklimi araştırmaları",
            "B) Doğal güzellikleri ve turizm/coğrafi önemi",
            "C) Okyanus balıkçılığı",
            "D) Sadece madencilik",
            "E) Sadece ağır sanayi"
          ],
          "correct": 1,
          "solution": "Doğru cevap Doğal güzellikleri ve turizm/coğrafi önemi.",
          "id": "e1_q105",
          "no": 105
        },
        {
          "subject": "Vatandaşlık",
          "text": "Geleneksel spor organizasyonu olan ve 2022 yılında 'Gelenekten Geleceğe Bir'iz!' sloganıyla düzenlenen 4. Dünya Göçebe Oyunları aşağıdaki yerlerin hangisinde yapılmıştır?",
          "options": [
            "A) Bergama",
            "B) Fethiye",
            "C) İznik",
            "D) Alanya",
            "E) Sivrihisar"
          ],
          "correct": 2,
          "solution": "Doğru cevap C'dir. 4. Dünya Göçebe Oyunları Bursa'nın İznik ilçesinde düzenlenmiştir.",
          "id": "e1_q106",
          "no": 106
        },
        {
          "subject": "Vatandaşlık",
          "text": "Belde sakinlerinin mahallî müşterek nitelikteki ihtiyaçlarını karşılamak üzere kurulan ve karar organı seçmenler tarafından seçilerek oluşturulan, idari ve mali özerkliğe sahip kamu tüzel kişisi aşağıdakilerden hangisidir?",
          "options": [
            "A) Mahalle",
            "B) Köy",
            "C) Belediye",
            "D) Kaymakamlık",
            "E) İl idare kurulu"
          ],
          "correct": 2,
          "solution": "Doğru cevap C'dir. Belde sakinlerinin ihtiyaçlarını karşılayan yerel yönetim birimi Belediyedir.",
          "id": "e1_q107",
          "no": 107
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'Anayasa Mahkemesi' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-0)",
          "options": [
            "A) Anayasa Mahkemesi yabancı bir kurumdur.",
            "B) Anayasa Mahkemesi, anayasal sistemin önemli bir parçasıdır.",
            "C) Anayasa Mahkemesi sadece köylerde bulunur.",
            "D) Anayasa Mahkemesi özel bir şirkettir.",
            "E) Anayasa Mahkemesi yasaklanmıştır."
          ],
          "correct": 1,
          "solution": "Doğru cevap Anayasa Mahkemesi, anayasal sistemin önemli bir parçasıdır..",
          "id": "e1_q108",
          "no": 108
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'Yargıtay' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-1)",
          "options": [
            "A) Yargıtay özel bir şirkettir.",
            "B) Yargıtay yabancı bir kurumdur.",
            "C) Yargıtay yasaklanmıştır.",
            "D) Yargıtay, anayasal sistemin önemli bir parçasıdır.",
            "E) Yargıtay sadece köylerde bulunur."
          ],
          "correct": 3,
          "solution": "Doğru cevap Yargıtay, anayasal sistemin önemli bir parçasıdır..",
          "id": "e1_q109",
          "no": 109
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'Danıştay' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-2)",
          "options": [
            "A) Danıştay, anayasal sistemin önemli bir parçasıdır.",
            "B) Danıştay özel bir şirkettir.",
            "C) Danıştay yabancı bir kurumdur.",
            "D) Danıştay yasaklanmıştır.",
            "E) Danıştay sadece köylerde bulunur."
          ],
          "correct": 0,
          "solution": "Doğru cevap Danıştay, anayasal sistemin önemli bir parçasıdır..",
          "id": "e1_q110",
          "no": 110
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'TBMM' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-3)",
          "options": [
            "A) TBMM yasaklanmıştır.",
            "B) TBMM, anayasal sistemin önemli bir parçasıdır.",
            "C) TBMM özel bir şirkettir.",
            "D) TBMM sadece köylerde bulunur.",
            "E) TBMM yabancı bir kurumdur."
          ],
          "correct": 1,
          "solution": "Doğru cevap TBMM, anayasal sistemin önemli bir parçasıdır..",
          "id": "e1_q111",
          "no": 111
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'Cumhurbaşkanlığı' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-4)",
          "options": [
            "A) Cumhurbaşkanlığı sadece köylerde bulunur.",
            "B) Cumhurbaşkanlığı, anayasal sistemin önemli bir parçasıdır.",
            "C) Cumhurbaşkanlığı yabancı bir kurumdur.",
            "D) Cumhurbaşkanlığı yasaklanmıştır.",
            "E) Cumhurbaşkanlığı özel bir şirkettir."
          ],
          "correct": 1,
          "solution": "Doğru cevap Cumhurbaşkanlığı, anayasal sistemin önemli bir parçasıdır..",
          "id": "e1_q112",
          "no": 112
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'Sayıştay' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-5)",
          "options": [
            "A) Sayıştay özel bir şirkettir.",
            "B) Sayıştay, anayasal sistemin önemli bir parçasıdır.",
            "C) Sayıştay yasaklanmıştır.",
            "D) Sayıştay sadece köylerde bulunur.",
            "E) Sayıştay yabancı bir kurumdur."
          ],
          "correct": 1,
          "solution": "Doğru cevap Sayıştay, anayasal sistemin önemli bir parçasıdır..",
          "id": "e1_q113",
          "no": 113
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'YSK' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-6)",
          "options": [
            "A) YSK yabancı bir kurumdur.",
            "B) YSK sadece köylerde bulunur.",
            "C) YSK özel bir şirkettir.",
            "D) YSK, anayasal sistemin önemli bir parçasıdır.",
            "E) YSK yasaklanmıştır."
          ],
          "correct": 3,
          "solution": "Doğru cevap YSK, anayasal sistemin önemli bir parçasıdır..",
          "id": "e1_q114",
          "no": 114
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'HSK' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-7)",
          "options": [
            "A) HSK yabancı bir kurumdur.",
            "B) HSK yasaklanmıştır.",
            "C) HSK, anayasal sistemin önemli bir parçasıdır.",
            "D) HSK özel bir şirkettir.",
            "E) HSK sadece köylerde bulunur."
          ],
          "correct": 2,
          "solution": "Doğru cevap HSK, anayasal sistemin önemli bir parçasıdır..",
          "id": "e1_q115",
          "no": 115
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'Belediye' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-8)",
          "options": [
            "A) Belediye yasaklanmıştır.",
            "B) Belediye sadece köylerde bulunur.",
            "C) Belediye özel bir şirkettir.",
            "D) Belediye yabancı bir kurumdur.",
            "E) Belediye, anayasal sistemin önemli bir parçasıdır."
          ],
          "correct": 4,
          "solution": "Doğru cevap Belediye, anayasal sistemin önemli bir parçasıdır..",
          "id": "e1_q116",
          "no": 116
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'Valilik' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-9)",
          "options": [
            "A) Valilik özel bir şirkettir.",
            "B) Valilik yabancı bir kurumdur.",
            "C) Valilik, anayasal sistemin önemli bir parçasıdır.",
            "D) Valilik sadece köylerde bulunur.",
            "E) Valilik yasaklanmıştır."
          ],
          "correct": 2,
          "solution": "Doğru cevap Valilik, anayasal sistemin önemli bir parçasıdır..",
          "id": "e1_q117",
          "no": 117
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'Kaymakamlık' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-10)",
          "options": [
            "A) Kaymakamlık sadece köylerde bulunur.",
            "B) Kaymakamlık, anayasal sistemin önemli bir parçasıdır.",
            "C) Kaymakamlık yabancı bir kurumdur.",
            "D) Kaymakamlık yasaklanmıştır.",
            "E) Kaymakamlık özel bir şirkettir."
          ],
          "correct": 1,
          "solution": "Doğru cevap Kaymakamlık, anayasal sistemin önemli bir parçasıdır..",
          "id": "e1_q118",
          "no": 118
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'İl Genel Meclisi' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-11)",
          "options": [
            "A) İl Genel Meclisi, anayasal sistemin önemli bir parçasıdır.",
            "B) İl Genel Meclisi sadece köylerde bulunur.",
            "C) İl Genel Meclisi yabancı bir kurumdur.",
            "D) İl Genel Meclisi yasaklanmıştır.",
            "E) İl Genel Meclisi özel bir şirkettir."
          ],
          "correct": 0,
          "solution": "Doğru cevap İl Genel Meclisi, anayasal sistemin önemli bir parçasıdır..",
          "id": "e1_q119",
          "no": 119
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'Kamu Denetçiliği Kurumu' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-12)",
          "options": [
            "A) Kamu Denetçiliği Kurumu yasaklanmıştır.",
            "B) Kamu Denetçiliği Kurumu, anayasal sistemin önemli bir parçasıdır.",
            "C) Kamu Denetçiliği Kurumu özel bir şirkettir.",
            "D) Kamu Denetçiliği Kurumu sadece köylerde bulunur.",
            "E) Kamu Denetçiliği Kurumu yabancı bir kurumdur."
          ],
          "correct": 1,
          "solution": "Doğru cevap Kamu Denetçiliği Kurumu, anayasal sistemin önemli bir parçasıdır..",
          "id": "e1_q120",
          "no": 120
        }
      ]
    },
    {
      "id": "deneme_2",
      "name": "2. Deneme Sınavı",
      "totalQuestions": 120,
      "duration": 130,
      "distribution": {
        "Türkçe": 30,
        "Matematik": 30,
        "Tarih": 27,
        "Coğrafya": 18,
        "Vatandaşlık": 15
      },
      "questions": [
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde 'yanlış' kelimesinin yazımıyla ilgili bir kural hatırlatılmaktadır? (T-25)",
          "options": [
            "A) yanlış kelimesi her zaman ayrı yazılır.",
            "B) yanlış kelimesi fiildir.",
            "C) yanlış kelimesi yabancı kökenlidir.",
            "D) 'yanlış' kelimesinin doğru yazımına dikkat edilmelidir.",
            "E) yanlış cümlede özne olamaz."
          ],
          "correct": 3,
          "solution": "Doğru cevap 'yanlış' kelimesinin doğru yazımına dikkat edilmelidir..",
          "id": "e2_q1",
          "no": 1
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde mecaz anlamlı bir sözcük kullanılmıştır? (T-26)",
          "options": [
            "A) Olaylara karşı çok 'soğuk' davranıyordu.",
            "B) Buzdolabı soğuk üflüyor.",
            "C) Kışın havalar soğuk olur.",
            "D) Hava bugün çok soğuk.",
            "E) Suyu dolaptan soğuk içti."
          ],
          "correct": 0,
          "solution": "Doğru cevap Olaylara karşı çok 'soğuk' davranıyordu..",
          "id": "e2_q2",
          "no": 2
        },
        {
          "subject": "Türkçe",
          "text": "Bilim tarih boyunca insanlığın en büyük rehberlerinden biri olmuştur. Toplumlar Bilim sayesinde sınırlarını aşmış, geleceğe umutla bakabilmiştir. (P-27)\nBu parçanın ana düşüncesi nedir?",
          "options": [
            "A) Bilim sadece bireyseldir.",
            "B) Bilim zaman kaybıdır.",
            "C) Bilim, toplumsal ilerleme ve vizyon için vazgeçilmezdir.",
            "D) Bilim sadece geçmişte kalmıştır.",
            "E) İnsanlar Bilim ile ilgilenmemelidir."
          ],
          "correct": 2,
          "solution": "Doğru cevap Bilim, toplumsal ilerleme ve vizyon için vazgeçilmezdir..",
          "id": "e2_q3",
          "no": 3
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde 'birkaç' kelimesinin yazımıyla ilgili bir kural hatırlatılmaktadır? (T-28)",
          "options": [
            "A) birkaç kelimesi her zaman ayrı yazılır.",
            "B) birkaç kelimesi yabancı kökenlidir.",
            "C) birkaç kelimesi fiildir.",
            "D) birkaç cümlede özne olamaz.",
            "E) 'birkaç' kelimesinin doğru yazımına dikkat edilmelidir."
          ],
          "correct": 4,
          "solution": "Doğru cevap 'birkaç' kelimesinin doğru yazımına dikkat edilmelidir..",
          "id": "e2_q4",
          "no": 4
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde mecaz anlamlı bir sözcük kullanılmıştır? (T-29)",
          "options": [
            "A) Olaylara karşı çok 'soğuk' davranıyordu.",
            "B) Suyu dolaptan soğuk içti.",
            "C) Kışın havalar soğuk olur.",
            "D) Hava bugün çok soğuk.",
            "E) Buzdolabı soğuk üflüyor."
          ],
          "correct": 0,
          "solution": "Doğru cevap Olaylara karşı çok 'soğuk' davranıyordu..",
          "id": "e2_q5",
          "no": 5
        },
        {
          "subject": "Türkçe",
          "text": "Sanat tarih boyunca insanlığın en büyük rehberlerinden biri olmuştur. Toplumlar Sanat sayesinde sınırlarını aşmış, geleceğe umutla bakabilmiştir. (P-30)\nBu parçanın ana düşüncesi nedir?",
          "options": [
            "A) Sanat zaman kaybıdır.",
            "B) Sanat, toplumsal ilerleme ve vizyon için vazgeçilmezdir.",
            "C) İnsanlar Sanat ile ilgilenmemelidir.",
            "D) Sanat sadece geçmişte kalmıştır.",
            "E) Sanat sadece bireyseldir."
          ],
          "correct": 1,
          "solution": "Doğru cevap Sanat, toplumsal ilerleme ve vizyon için vazgeçilmezdir..",
          "id": "e2_q6",
          "no": 6
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde 'hiç kimse' kelimesinin yazımıyla ilgili bir kural hatırlatılmaktadır? (T-31)",
          "options": [
            "A) 'hiç kimse' kelimesinin doğru yazımına dikkat edilmelidir.",
            "B) hiç kimse cümlede özne olamaz.",
            "C) hiç kimse kelimesi fiildir.",
            "D) hiç kimse kelimesi her zaman ayrı yazılır.",
            "E) hiç kimse kelimesi yabancı kökenlidir."
          ],
          "correct": 0,
          "solution": "Doğru cevap 'hiç kimse' kelimesinin doğru yazımına dikkat edilmelidir..",
          "id": "e2_q7",
          "no": 7
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde mecaz anlamlı bir sözcük kullanılmıştır? (T-32)",
          "options": [
            "A) Hava bugün çok soğuk.",
            "B) Buzdolabı soğuk üflüyor.",
            "C) Olaylara karşı çok 'soğuk' davranıyordu.",
            "D) Suyu dolaptan soğuk içti.",
            "E) Kışın havalar soğuk olur."
          ],
          "correct": 2,
          "solution": "Doğru cevap Olaylara karşı çok 'soğuk' davranıyordu..",
          "id": "e2_q8",
          "no": 8
        },
        {
          "subject": "Türkçe",
          "text": "Teknoloji tarih boyunca insanlığın en büyük rehberlerinden biri olmuştur. Toplumlar Teknoloji sayesinde sınırlarını aşmış, geleceğe umutla bakabilmiştir. (P-33)\nBu parçanın ana düşüncesi nedir?",
          "options": [
            "A) İnsanlar Teknoloji ile ilgilenmemelidir.",
            "B) Teknoloji zaman kaybıdır.",
            "C) Teknoloji sadece bireyseldir.",
            "D) Teknoloji, toplumsal ilerleme ve vizyon için vazgeçilmezdir.",
            "E) Teknoloji sadece geçmişte kalmıştır."
          ],
          "correct": 3,
          "solution": "Doğru cevap Teknoloji, toplumsal ilerleme ve vizyon için vazgeçilmezdir..",
          "id": "e2_q9",
          "no": 9
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde 'herkes' kelimesinin yazımıyla ilgili bir kural hatırlatılmaktadır? (T-34)",
          "options": [
            "A) herkes kelimesi fiildir.",
            "B) herkes kelimesi her zaman ayrı yazılır.",
            "C) 'herkes' kelimesinin doğru yazımına dikkat edilmelidir.",
            "D) herkes kelimesi yabancı kökenlidir.",
            "E) herkes cümlede özne olamaz."
          ],
          "correct": 2,
          "solution": "Doğru cevap 'herkes' kelimesinin doğru yazımına dikkat edilmelidir..",
          "id": "e2_q10",
          "no": 10
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde mecaz anlamlı bir sözcük kullanılmıştır? (T-35)",
          "options": [
            "A) Olaylara karşı çok 'soğuk' davranıyordu.",
            "B) Buzdolabı soğuk üflüyor.",
            "C) Suyu dolaptan soğuk içti.",
            "D) Kışın havalar soğuk olur.",
            "E) Hava bugün çok soğuk."
          ],
          "correct": 0,
          "solution": "Doğru cevap Olaylara karşı çok 'soğuk' davranıyordu..",
          "id": "e2_q11",
          "no": 11
        },
        {
          "subject": "Türkçe",
          "text": "Doğa tarih boyunca insanlığın en büyük rehberlerinden biri olmuştur. Toplumlar Doğa sayesinde sınırlarını aşmış, geleceğe umutla bakabilmiştir. (P-36)\nBu parçanın ana düşüncesi nedir?",
          "options": [
            "A) Doğa sadece bireyseldir.",
            "B) Doğa, toplumsal ilerleme ve vizyon için vazgeçilmezdir.",
            "C) İnsanlar Doğa ile ilgilenmemelidir.",
            "D) Doğa zaman kaybıdır.",
            "E) Doğa sadece geçmişte kalmıştır."
          ],
          "correct": 1,
          "solution": "Doğru cevap Doğa, toplumsal ilerleme ve vizyon için vazgeçilmezdir..",
          "id": "e2_q12",
          "no": 12
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde 'bugün' kelimesinin yazımıyla ilgili bir kural hatırlatılmaktadır? (T-37)",
          "options": [
            "A) bugün kelimesi her zaman ayrı yazılır.",
            "B) bugün cümlede özne olamaz.",
            "C) bugün kelimesi fiildir.",
            "D) bugün kelimesi yabancı kökenlidir.",
            "E) 'bugün' kelimesinin doğru yazımına dikkat edilmelidir."
          ],
          "correct": 4,
          "solution": "Doğru cevap 'bugün' kelimesinin doğru yazımına dikkat edilmelidir..",
          "id": "e2_q13",
          "no": 13
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde mecaz anlamlı bir sözcük kullanılmıştır? (T-38)",
          "options": [
            "A) Hava bugün çok soğuk.",
            "B) Kışın havalar soğuk olur.",
            "C) Buzdolabı soğuk üflüyor.",
            "D) Olaylara karşı çok 'soğuk' davranıyordu.",
            "E) Suyu dolaptan soğuk içti."
          ],
          "correct": 3,
          "solution": "Doğru cevap Olaylara karşı çok 'soğuk' davranıyordu..",
          "id": "e2_q14",
          "no": 14
        },
        {
          "subject": "Türkçe",
          "text": "Psikoloji tarih boyunca insanlığın en büyük rehberlerinden biri olmuştur. Toplumlar Psikoloji sayesinde sınırlarını aşmış, geleceğe umutla bakabilmiştir. (P-39)\nBu parçanın ana düşüncesi nedir?",
          "options": [
            "A) Psikoloji, toplumsal ilerleme ve vizyon için vazgeçilmezdir.",
            "B) Psikoloji sadece geçmişte kalmıştır.",
            "C) Psikoloji sadece bireyseldir.",
            "D) İnsanlar Psikoloji ile ilgilenmemelidir.",
            "E) Psikoloji zaman kaybıdır."
          ],
          "correct": 0,
          "solution": "Doğru cevap Psikoloji, toplumsal ilerleme ve vizyon için vazgeçilmezdir..",
          "id": "e2_q15",
          "no": 15
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde 'yalnız' kelimesinin yazımıyla ilgili bir kural hatırlatılmaktadır? (T-40)",
          "options": [
            "A) 'yalnız' kelimesinin doğru yazımına dikkat edilmelidir.",
            "B) yalnız kelimesi fiildir.",
            "C) yalnız kelimesi yabancı kökenlidir.",
            "D) yalnız cümlede özne olamaz.",
            "E) yalnız kelimesi her zaman ayrı yazılır."
          ],
          "correct": 0,
          "solution": "Doğru cevap 'yalnız' kelimesinin doğru yazımına dikkat edilmelidir..",
          "id": "e2_q16",
          "no": 16
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde mecaz anlamlı bir sözcük kullanılmıştır? (T-41)",
          "options": [
            "A) Olaylara karşı çok 'soğuk' davranıyordu.",
            "B) Hava bugün çok soğuk.",
            "C) Kışın havalar soğuk olur.",
            "D) Suyu dolaptan soğuk içti.",
            "E) Buzdolabı soğuk üflüyor."
          ],
          "correct": 0,
          "solution": "Doğru cevap Olaylara karşı çok 'soğuk' davranıyordu..",
          "id": "e2_q17",
          "no": 17
        },
        {
          "subject": "Türkçe",
          "text": "Eğitim tarih boyunca insanlığın en büyük rehberlerinden biri olmuştur. Toplumlar Eğitim sayesinde sınırlarını aşmış, geleceğe umutla bakabilmiştir. (P-42)\nBu parçanın ana düşüncesi nedir?",
          "options": [
            "A) Eğitim zaman kaybıdır.",
            "B) Eğitim, toplumsal ilerleme ve vizyon için vazgeçilmezdir.",
            "C) Eğitim sadece bireyseldir.",
            "D) İnsanlar Eğitim ile ilgilenmemelidir.",
            "E) Eğitim sadece geçmişte kalmıştır."
          ],
          "correct": 1,
          "solution": "Doğru cevap Eğitim, toplumsal ilerleme ve vizyon için vazgeçilmezdir..",
          "id": "e2_q18",
          "no": 18
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde 'hiçbir' kelimesinin yazımıyla ilgili bir kural hatırlatılmaktadır? (T-43)",
          "options": [
            "A) 'hiçbir' kelimesinin doğru yazımına dikkat edilmelidir.",
            "B) hiçbir cümlede özne olamaz.",
            "C) hiçbir kelimesi her zaman ayrı yazılır.",
            "D) hiçbir kelimesi fiildir.",
            "E) hiçbir kelimesi yabancı kökenlidir."
          ],
          "correct": 0,
          "solution": "Doğru cevap 'hiçbir' kelimesinin doğru yazımına dikkat edilmelidir..",
          "id": "e2_q19",
          "no": 19
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde mecaz anlamlı bir sözcük kullanılmıştır? (T-44)",
          "options": [
            "A) Buzdolabı soğuk üflüyor.",
            "B) Kışın havalar soğuk olur.",
            "C) Suyu dolaptan soğuk içti.",
            "D) Olaylara karşı çok 'soğuk' davranıyordu.",
            "E) Hava bugün çok soğuk."
          ],
          "correct": 3,
          "solution": "Doğru cevap Olaylara karşı çok 'soğuk' davranıyordu..",
          "id": "e2_q20",
          "no": 20
        },
        {
          "subject": "Türkçe",
          "text": "Kültür tarih boyunca insanlığın en büyük rehberlerinden biri olmuştur. Toplumlar Kültür sayesinde sınırlarını aşmış, geleceğe umutla bakabilmiştir. (P-45)\nBu parçanın ana düşüncesi nedir?",
          "options": [
            "A) Kültür zaman kaybıdır.",
            "B) Kültür sadece geçmişte kalmıştır.",
            "C) Kültür, toplumsal ilerleme ve vizyon için vazgeçilmezdir.",
            "D) İnsanlar Kültür ile ilgilenmemelidir.",
            "E) Kültür sadece bireyseldir."
          ],
          "correct": 2,
          "solution": "Doğru cevap Kültür, toplumsal ilerleme ve vizyon için vazgeçilmezdir..",
          "id": "e2_q21",
          "no": 21
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde 'her şey' kelimesinin yazımıyla ilgili bir kural hatırlatılmaktadır? (T-46)",
          "options": [
            "A) her şey kelimesi her zaman ayrı yazılır.",
            "B) her şey cümlede özne olamaz.",
            "C) 'her şey' kelimesinin doğru yazımına dikkat edilmelidir.",
            "D) her şey kelimesi fiildir.",
            "E) her şey kelimesi yabancı kökenlidir."
          ],
          "correct": 2,
          "solution": "Doğru cevap 'her şey' kelimesinin doğru yazımına dikkat edilmelidir..",
          "id": "e2_q22",
          "no": 22
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde mecaz anlamlı bir sözcük kullanılmıştır? (T-47)",
          "options": [
            "A) Buzdolabı soğuk üflüyor.",
            "B) Olaylara karşı çok 'soğuk' davranıyordu.",
            "C) Suyu dolaptan soğuk içti.",
            "D) Hava bugün çok soğuk.",
            "E) Kışın havalar soğuk olur."
          ],
          "correct": 1,
          "solution": "Doğru cevap Olaylara karşı çok 'soğuk' davranıyordu..",
          "id": "e2_q23",
          "no": 23
        },
        {
          "subject": "Türkçe",
          "text": "Felsefe tarih boyunca insanlığın en büyük rehberlerinden biri olmuştur. Toplumlar Felsefe sayesinde sınırlarını aşmış, geleceğe umutla bakabilmiştir. (P-48)\nBu parçanın ana düşüncesi nedir?",
          "options": [
            "A) İnsanlar Felsefe ile ilgilenmemelidir.",
            "B) Felsefe sadece bireyseldir.",
            "C) Felsefe zaman kaybıdır.",
            "D) Felsefe, toplumsal ilerleme ve vizyon için vazgeçilmezdir.",
            "E) Felsefe sadece geçmişte kalmıştır."
          ],
          "correct": 3,
          "solution": "Doğru cevap Felsefe, toplumsal ilerleme ve vizyon için vazgeçilmezdir..",
          "id": "e2_q24",
          "no": 24
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde 'yanlış' kelimesinin yazımıyla ilgili bir kural hatırlatılmaktadır? (T-49)",
          "options": [
            "A) 'yanlış' kelimesinin doğru yazımına dikkat edilmelidir.",
            "B) yanlış kelimesi fiildir.",
            "C) yanlış kelimesi yabancı kökenlidir.",
            "D) yanlış kelimesi her zaman ayrı yazılır.",
            "E) yanlış cümlede özne olamaz."
          ],
          "correct": 0,
          "solution": "Doğru cevap 'yanlış' kelimesinin doğru yazımına dikkat edilmelidir..",
          "id": "e2_q25",
          "no": 25
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde mecaz anlamlı bir sözcük kullanılmıştır? (T-50)",
          "options": [
            "A) Hava bugün çok soğuk.",
            "B) Olaylara karşı çok 'soğuk' davranıyordu.",
            "C) Kışın havalar soğuk olur.",
            "D) Suyu dolaptan soğuk içti.",
            "E) Buzdolabı soğuk üflüyor."
          ],
          "correct": 1,
          "solution": "Doğru cevap Olaylara karşı çok 'soğuk' davranıyordu..",
          "id": "e2_q26",
          "no": 26
        },
        {
          "subject": "Türkçe",
          "text": "Edebiyat tarih boyunca insanlığın en büyük rehberlerinden biri olmuştur. Toplumlar Edebiyat sayesinde sınırlarını aşmış, geleceğe umutla bakabilmiştir. (P-51)\nBu parçanın ana düşüncesi nedir?",
          "options": [
            "A) İnsanlar Edebiyat ile ilgilenmemelidir.",
            "B) Edebiyat zaman kaybıdır.",
            "C) Edebiyat sadece geçmişte kalmıştır.",
            "D) Edebiyat sadece bireyseldir.",
            "E) Edebiyat, toplumsal ilerleme ve vizyon için vazgeçilmezdir."
          ],
          "correct": 4,
          "solution": "Doğru cevap Edebiyat, toplumsal ilerleme ve vizyon için vazgeçilmezdir..",
          "id": "e2_q27",
          "no": 27
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde 'birkaç' kelimesinin yazımıyla ilgili bir kural hatırlatılmaktadır? (T-52)",
          "options": [
            "A) birkaç kelimesi fiildir.",
            "B) 'birkaç' kelimesinin doğru yazımına dikkat edilmelidir.",
            "C) birkaç kelimesi her zaman ayrı yazılır.",
            "D) birkaç cümlede özne olamaz.",
            "E) birkaç kelimesi yabancı kökenlidir."
          ],
          "correct": 1,
          "solution": "Doğru cevap 'birkaç' kelimesinin doğru yazımına dikkat edilmelidir..",
          "id": "e2_q28",
          "no": 28
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde mecaz anlamlı bir sözcük kullanılmıştır? (T-53)",
          "options": [
            "A) Hava bugün çok soğuk.",
            "B) Buzdolabı soğuk üflüyor.",
            "C) Suyu dolaptan soğuk içti.",
            "D) Kışın havalar soğuk olur.",
            "E) Olaylara karşı çok 'soğuk' davranıyordu."
          ],
          "correct": 4,
          "solution": "Doğru cevap Olaylara karşı çok 'soğuk' davranıyordu..",
          "id": "e2_q29",
          "no": 29
        },
        {
          "subject": "Türkçe",
          "text": "Tarih tarih boyunca insanlığın en büyük rehberlerinden biri olmuştur. Toplumlar Tarih sayesinde sınırlarını aşmış, geleceğe umutla bakabilmiştir. (P-54)\nBu parçanın ana düşüncesi nedir?",
          "options": [
            "A) Tarih sadece bireyseldir.",
            "B) Tarih, toplumsal ilerleme ve vizyon için vazgeçilmezdir.",
            "C) Tarih sadece geçmişte kalmıştır.",
            "D) İnsanlar Tarih ile ilgilenmemelidir.",
            "E) Tarih zaman kaybıdır."
          ],
          "correct": 1,
          "solution": "Doğru cevap Tarih, toplumsal ilerleme ve vizyon için vazgeçilmezdir..",
          "id": "e2_q30",
          "no": 30
        },
        {
          "subject": "Matematik",
          "text": "8x + 32 = 72 denkleminde x kaçtır? (SoruID: M30)",
          "options": [
            "A) 4",
            "B) 6",
            "C) 5",
            "D) 7",
            "E) 8"
          ],
          "correct": 2,
          "solution": "Doğru cevap 5.",
          "id": "e2_q31",
          "no": 31
        },
        {
          "subject": "Matematik",
          "text": "130 sayısının %25'si kaçtır? (SoruID: M31)",
          "options": [
            "A) 32",
            "B) 47",
            "C) 37",
            "D) 42",
            "E) 27"
          ],
          "correct": 0,
          "solution": "Doğru cevap 32.",
          "id": "e2_q32",
          "no": 32
        },
        {
          "subject": "Matematik",
          "text": "25, 23 ve 21 sayılarının aritmetik ortalaması kaçtır? (SoruID: M32)",
          "options": [
            "A) 23",
            "B) 22",
            "C) 21",
            "D) 24",
            "E) 25"
          ],
          "correct": 0,
          "solution": "Doğru cevap 23.",
          "id": "e2_q33",
          "no": 33
        },
        {
          "subject": "Matematik",
          "text": "Ali 24, Ayşe 13 yaşındadır. 7 yıl sonra yaşları toplamı kaç olur? (SoruID: M33)",
          "options": [
            "A) 52",
            "B) 44",
            "C) 50",
            "D) 58",
            "E) 51"
          ],
          "correct": 4,
          "solution": "Doğru cevap 51.",
          "id": "e2_q34",
          "no": 34
        },
        {
          "subject": "Matematik",
          "text": "√9 + √81 işleminin sonucu kaçtır? (SoruID: M34)",
          "options": [
            "A) 13",
            "B) 12",
            "C) 10",
            "D) 14",
            "E) 11"
          ],
          "correct": 1,
          "solution": "Doğru cevap 12.",
          "id": "e2_q35",
          "no": 35
        },
        {
          "subject": "Matematik",
          "text": "2x + 15 = 27 denkleminde x kaçtır? (SoruID: M35)",
          "options": [
            "A) 9",
            "B) 8",
            "C) 6",
            "D) 7",
            "E) 5"
          ],
          "correct": 2,
          "solution": "Doğru cevap 6.",
          "id": "e2_q36",
          "no": 36
        },
        {
          "subject": "Matematik",
          "text": "100 sayısının %40'si kaçtır? (SoruID: M36)",
          "options": [
            "A) 50",
            "B) 40",
            "C) 45",
            "D) 35",
            "E) 55"
          ],
          "correct": 1,
          "solution": "Doğru cevap 40.",
          "id": "e2_q37",
          "no": 37
        },
        {
          "subject": "Matematik",
          "text": "13, 18 ve 14 sayılarının aritmetik ortalaması kaçtır? (SoruID: M37)",
          "options": [
            "A) 13",
            "B) 14",
            "C) 15",
            "D) 16",
            "E) 17"
          ],
          "correct": 2,
          "solution": "Doğru cevap 15.",
          "id": "e2_q38",
          "no": 38
        },
        {
          "subject": "Matematik",
          "text": "Ali 21, Ayşe 15 yaşındadır. 4 yıl sonra yaşları toplamı kaç olur? (SoruID: M38)",
          "options": [
            "A) 45",
            "B) 44",
            "C) 48",
            "D) 40",
            "E) 43"
          ],
          "correct": 1,
          "solution": "Doğru cevap 44.",
          "id": "e2_q39",
          "no": 39
        },
        {
          "subject": "Matematik",
          "text": "√36 + √49 işleminin sonucu kaçtır? (SoruID: M39)",
          "options": [
            "A) 15",
            "B) 13",
            "C) 11",
            "D) 12",
            "E) 14"
          ],
          "correct": 1,
          "solution": "Doğru cevap 13.",
          "id": "e2_q40",
          "no": 40
        },
        {
          "subject": "Matematik",
          "text": "2x + 21 = 35 denkleminde x kaçtır? (SoruID: M40)",
          "options": [
            "A) 8",
            "B) 6",
            "C) 10",
            "D) 7",
            "E) 9"
          ],
          "correct": 3,
          "solution": "Doğru cevap 7.",
          "id": "e2_q41",
          "no": 41
        },
        {
          "subject": "Matematik",
          "text": "110 sayısının %10'si kaçtır? (SoruID: M41)",
          "options": [
            "A) 26",
            "B) 21",
            "C) 16",
            "D) 11",
            "E) 6"
          ],
          "correct": 3,
          "solution": "Doğru cevap 11.",
          "id": "e2_q42",
          "no": 42
        },
        {
          "subject": "Matematik",
          "text": "20, 24 ve 31 sayılarının aritmetik ortalaması kaçtır? (SoruID: M42)",
          "options": [
            "A) 27",
            "B) 24",
            "C) 26",
            "D) 25",
            "E) 23"
          ],
          "correct": 3,
          "solution": "Doğru cevap 25.",
          "id": "e2_q43",
          "no": 43
        },
        {
          "subject": "Matematik",
          "text": "Ali 16, Ayşe 24 yaşındadır. 9 yıl sonra yaşları toplamı kaç olur? (SoruID: M43)",
          "options": [
            "A) 57",
            "B) 67",
            "C) 59",
            "D) 49",
            "E) 58"
          ],
          "correct": 4,
          "solution": "Doğru cevap 58.",
          "id": "e2_q44",
          "no": 44
        },
        {
          "subject": "Matematik",
          "text": "√64 + √36 işleminin sonucu kaçtır? (SoruID: M44)",
          "options": [
            "A) 16",
            "B) 15",
            "C) 12",
            "D) 14",
            "E) 13"
          ],
          "correct": 3,
          "solution": "Doğru cevap 14.",
          "id": "e2_q45",
          "no": 45
        },
        {
          "subject": "Matematik",
          "text": "2x + 49 = 59 denkleminde x kaçtır? (SoruID: M45)",
          "options": [
            "A) 6",
            "B) 5",
            "C) 7",
            "D) 8",
            "E) 4"
          ],
          "correct": 1,
          "solution": "Doğru cevap 5.",
          "id": "e2_q46",
          "no": 46
        },
        {
          "subject": "Matematik",
          "text": "130 sayısının %60'si kaçtır? (SoruID: M46)",
          "options": [
            "A) 83",
            "B) 88",
            "C) 93",
            "D) 78",
            "E) 73"
          ],
          "correct": 3,
          "solution": "Doğru cevap 78.",
          "id": "e2_q47",
          "no": 47
        },
        {
          "subject": "Matematik",
          "text": "16, 27 ve 11 sayılarının aritmetik ortalaması kaçtır? (SoruID: M47)",
          "options": [
            "A) 20",
            "B) 16",
            "C) 17",
            "D) 19",
            "E) 18"
          ],
          "correct": 4,
          "solution": "Doğru cevap 18.",
          "id": "e2_q48",
          "no": 48
        },
        {
          "subject": "Matematik",
          "text": "Ali 13, Ayşe 11 yaşındadır. 5 yıl sonra yaşları toplamı kaç olur? (SoruID: M48)",
          "options": [
            "A) 34",
            "B) 39",
            "C) 35",
            "D) 29",
            "E) 33"
          ],
          "correct": 0,
          "solution": "Doğru cevap 34.",
          "id": "e2_q49",
          "no": 49
        },
        {
          "subject": "Matematik",
          "text": "√4 + √64 işleminin sonucu kaçtır? (SoruID: M49)",
          "options": [
            "A) 10",
            "B) 9",
            "C) 12",
            "D) 11",
            "E) 8"
          ],
          "correct": 0,
          "solution": "Doğru cevap 10.",
          "id": "e2_q50",
          "no": 50
        },
        {
          "subject": "Matematik",
          "text": "8x + 20 = 76 denkleminde x kaçtır? (SoruID: M50)",
          "options": [
            "A) 10",
            "B) 6",
            "C) 7",
            "D) 8",
            "E) 9"
          ],
          "correct": 2,
          "solution": "Doğru cevap 7.",
          "id": "e2_q51",
          "no": 51
        },
        {
          "subject": "Matematik",
          "text": "40 sayısının %60'si kaçtır? (SoruID: M51)",
          "options": [
            "A) 29",
            "B) 39",
            "C) 24",
            "D) 34",
            "E) 19"
          ],
          "correct": 2,
          "solution": "Doğru cevap 24.",
          "id": "e2_q52",
          "no": 52
        },
        {
          "subject": "Matematik",
          "text": "10, 18 ve 29 sayılarının aritmetik ortalaması kaçtır? (SoruID: M52)",
          "options": [
            "A) 19",
            "B) 18",
            "C) 20",
            "D) 17",
            "E) 21"
          ],
          "correct": 0,
          "solution": "Doğru cevap 19.",
          "id": "e2_q53",
          "no": 53
        },
        {
          "subject": "Matematik",
          "text": "Ali 14, Ayşe 12 yaşındadır. 5 yıl sonra yaşları toplamı kaç olur? (SoruID: M53)",
          "options": [
            "A) 37",
            "B) 41",
            "C) 31",
            "D) 36",
            "E) 35"
          ],
          "correct": 3,
          "solution": "Doğru cevap 36.",
          "id": "e2_q54",
          "no": 54
        },
        {
          "subject": "Matematik",
          "text": "√49 + √49 işleminin sonucu kaçtır? (SoruID: M54)",
          "options": [
            "A) 15",
            "B) 16",
            "C) 13",
            "D) 12",
            "E) 14"
          ],
          "correct": 4,
          "solution": "Doğru cevap 14.",
          "id": "e2_q55",
          "no": 55
        },
        {
          "subject": "Matematik",
          "text": "9x + 19 = 28 denkleminde x kaçtır? (SoruID: M55)",
          "options": [
            "A) 1",
            "B) 3",
            "C) 0",
            "D) 2",
            "E) 4"
          ],
          "correct": 0,
          "solution": "Doğru cevap 1.",
          "id": "e2_q56",
          "no": 56
        },
        {
          "subject": "Matematik",
          "text": "150 sayısının %30'si kaçtır? (SoruID: M56)",
          "options": [
            "A) 50",
            "B) 45",
            "C) 55",
            "D) 40",
            "E) 60"
          ],
          "correct": 1,
          "solution": "Doğru cevap 45.",
          "id": "e2_q57",
          "no": 57
        },
        {
          "subject": "Matematik",
          "text": "21, 21 ve 24 sayılarının aritmetik ortalaması kaçtır? (SoruID: M57)",
          "options": [
            "A) 22",
            "B) 23",
            "C) 21",
            "D) 20",
            "E) 24"
          ],
          "correct": 0,
          "solution": "Doğru cevap 22.",
          "id": "e2_q58",
          "no": 58
        },
        {
          "subject": "Matematik",
          "text": "Ali 16, Ayşe 15 yaşındadır. 9 yıl sonra yaşları toplamı kaç olur? (SoruID: M58)",
          "options": [
            "A) 40",
            "B) 48",
            "C) 49",
            "D) 50",
            "E) 58"
          ],
          "correct": 2,
          "solution": "Doğru cevap 49.",
          "id": "e2_q59",
          "no": 59
        },
        {
          "subject": "Matematik",
          "text": "√64 + √4 işleminin sonucu kaçtır? (SoruID: M59)",
          "options": [
            "A) 12",
            "B) 9",
            "C) 8",
            "D) 10",
            "E) 11"
          ],
          "correct": 3,
          "solution": "Doğru cevap 10.",
          "id": "e2_q60",
          "no": 60
        },
        {
          "subject": "Tarih",
          "text": "Türk siyasi ve askerî tarihinde büyük öneme sahip olan 'Cumhuriyetin İlanı' süreci ile ilgili aşağıdakilerden hangisi söylenebilir? (H-24)",
          "options": [
            "A) Avrupa'da gerçekleşmiştir.",
            "B) Sadece ekonomik bir olaydır.",
            "C) Cumhuriyetin İlanı dönemin en kritik gelişmelerinden biridir.",
            "D) Hiçbir etkisi olmamıştır.",
            "E) Osmanlı'nın kuruluş dönemine aittir."
          ],
          "correct": 2,
          "solution": "Doğru cevap Cumhuriyetin İlanı dönemin en kritik gelişmelerinden biridir..",
          "id": "e2_q61",
          "no": 61
        },
        {
          "subject": "Tarih",
          "text": "Aşağıdaki tarihî gelişmelerden hangisi 'TBMM'nin Açılışı' ile doğrudan veya dolaylı olarak bağlantılıdır? (H-25)",
          "options": [
            "A) Kavimler Göçü",
            "B) Fransız İhtilali",
            "C) Sanayi İnkılabı",
            "D) TBMM'nin Açılışı öncesi ve sonrası yaşanan siyasi krizler.",
            "E) Coğrafi Keşifler"
          ],
          "correct": 3,
          "solution": "Doğru cevap TBMM'nin Açılışı öncesi ve sonrası yaşanan siyasi krizler..",
          "id": "e2_q62",
          "no": 62
        },
        {
          "subject": "Tarih",
          "text": "Millî Mücadele ve inkılaplar tarihi incelendiğinde 'Mudanya Mütarekesi' olayının temel amacı aşağıdakilerden hangisidir? (H-26)",
          "options": [
            "A) Saltanatı güçlendirmek",
            "B) Avrupa'ya göç etmek",
            "C) Bağımsızlık ve egemenliği pekiştirmek",
            "D) Feodaliteyi kurmak",
            "E) Yeni sömürgeler elde etmek"
          ],
          "correct": 2,
          "solution": "Doğru cevap Bağımsızlık ve egemenliği pekiştirmek.",
          "id": "e2_q63",
          "no": 63
        },
        {
          "subject": "Tarih",
          "text": "Türk siyasi ve askerî tarihinde büyük öneme sahip olan 'Saltanatın Kaldırılması' süreci ile ilgili aşağıdakilerden hangisi söylenebilir? (H-27)",
          "options": [
            "A) Osmanlı'nın kuruluş dönemine aittir.",
            "B) Hiçbir etkisi olmamıştır.",
            "C) Sadece ekonomik bir olaydır.",
            "D) Saltanatın Kaldırılması dönemin en kritik gelişmelerinden biridir.",
            "E) Avrupa'da gerçekleşmiştir."
          ],
          "correct": 3,
          "solution": "Doğru cevap Saltanatın Kaldırılması dönemin en kritik gelişmelerinden biridir..",
          "id": "e2_q64",
          "no": 64
        },
        {
          "subject": "Tarih",
          "text": "Aşağıdaki tarihî gelişmelerden hangisi 'Halifeliğin Kaldırılması' ile doğrudan veya dolaylı olarak bağlantılıdır? (H-28)",
          "options": [
            "A) Fransız İhtilali",
            "B) Halifeliğin Kaldırılması öncesi ve sonrası yaşanan siyasi krizler.",
            "C) Sanayi İnkılabı",
            "D) Kavimler Göçü",
            "E) Coğrafi Keşifler"
          ],
          "correct": 1,
          "solution": "Doğru cevap Halifeliğin Kaldırılması öncesi ve sonrası yaşanan siyasi krizler..",
          "id": "e2_q65",
          "no": 65
        },
        {
          "subject": "Tarih",
          "text": "Millî Mücadele ve inkılaplar tarihi incelendiğinde 'Tevhid-i Tedrisat' olayının temel amacı aşağıdakilerden hangisidir? (H-29)",
          "options": [
            "A) Bağımsızlık ve egemenliği pekiştirmek",
            "B) Yeni sömürgeler elde etmek",
            "C) Avrupa'ya göç etmek",
            "D) Saltanatı güçlendirmek",
            "E) Feodaliteyi kurmak"
          ],
          "correct": 0,
          "solution": "Doğru cevap Bağımsızlık ve egemenliği pekiştirmek.",
          "id": "e2_q66",
          "no": 66
        },
        {
          "subject": "Tarih",
          "text": "Türk siyasi ve askerî tarihinde büyük öneme sahip olan 'Trablusgarp Savaşı' süreci ile ilgili aşağıdakilerden hangisi söylenebilir? (H-30)",
          "options": [
            "A) Sadece ekonomik bir olaydır.",
            "B) Osmanlı'nın kuruluş dönemine aittir.",
            "C) Avrupa'da gerçekleşmiştir.",
            "D) Hiçbir etkisi olmamıştır.",
            "E) Trablusgarp Savaşı dönemin en kritik gelişmelerinden biridir."
          ],
          "correct": 4,
          "solution": "Doğru cevap Trablusgarp Savaşı dönemin en kritik gelişmelerinden biridir..",
          "id": "e2_q67",
          "no": 67
        },
        {
          "subject": "Tarih",
          "text": "Aşağıdaki tarihî gelişmelerden hangisi 'Balkan Savaşları' ile doğrudan veya dolaylı olarak bağlantılıdır? (H-31)",
          "options": [
            "A) Coğrafi Keşifler",
            "B) Kavimler Göçü",
            "C) Sanayi İnkılabı",
            "D) Fransız İhtilali",
            "E) Balkan Savaşları öncesi ve sonrası yaşanan siyasi krizler."
          ],
          "correct": 4,
          "solution": "Doğru cevap Balkan Savaşları öncesi ve sonrası yaşanan siyasi krizler..",
          "id": "e2_q68",
          "no": 68
        },
        {
          "subject": "Tarih",
          "text": "Millî Mücadele ve inkılaplar tarihi incelendiğinde 'I. Dünya Savaşı' olayının temel amacı aşağıdakilerden hangisidir? (H-32)",
          "options": [
            "A) Avrupa'ya göç etmek",
            "B) Bağımsızlık ve egemenliği pekiştirmek",
            "C) Yeni sömürgeler elde etmek",
            "D) Feodaliteyi kurmak",
            "E) Saltanatı güçlendirmek"
          ],
          "correct": 1,
          "solution": "Doğru cevap Bağımsızlık ve egemenliği pekiştirmek.",
          "id": "e2_q69",
          "no": 69
        },
        {
          "subject": "Tarih",
          "text": "Türk siyasi ve askerî tarihinde büyük öneme sahip olan 'Çanakkale Cephesi' süreci ile ilgili aşağıdakilerden hangisi söylenebilir? (H-33)",
          "options": [
            "A) Avrupa'da gerçekleşmiştir.",
            "B) Hiçbir etkisi olmamıştır.",
            "C) Sadece ekonomik bir olaydır.",
            "D) Çanakkale Cephesi dönemin en kritik gelişmelerinden biridir.",
            "E) Osmanlı'nın kuruluş dönemine aittir."
          ],
          "correct": 3,
          "solution": "Doğru cevap Çanakkale Cephesi dönemin en kritik gelişmelerinden biridir..",
          "id": "e2_q70",
          "no": 70
        },
        {
          "subject": "Tarih",
          "text": "Aşağıdaki tarihî gelişmelerden hangisi 'Sakarya Meydan Muharebesi' ile doğrudan veya dolaylı olarak bağlantılıdır? (H-34)",
          "options": [
            "A) Sanayi İnkılabı",
            "B) Sakarya Meydan Muharebesi öncesi ve sonrası yaşanan siyasi krizler.",
            "C) Coğrafi Keşifler",
            "D) Kavimler Göçü",
            "E) Fransız İhtilali"
          ],
          "correct": 1,
          "solution": "Doğru cevap Sakarya Meydan Muharebesi öncesi ve sonrası yaşanan siyasi krizler..",
          "id": "e2_q71",
          "no": 71
        },
        {
          "subject": "Tarih",
          "text": "Millî Mücadele ve inkılaplar tarihi incelendiğinde 'Büyük Taarruz' olayının temel amacı aşağıdakilerden hangisidir? (H-35)",
          "options": [
            "A) Yeni sömürgeler elde etmek",
            "B) Avrupa'ya göç etmek",
            "C) Saltanatı güçlendirmek",
            "D) Feodaliteyi kurmak",
            "E) Bağımsızlık ve egemenliği pekiştirmek"
          ],
          "correct": 4,
          "solution": "Doğru cevap Bağımsızlık ve egemenliği pekiştirmek.",
          "id": "e2_q72",
          "no": 72
        },
        {
          "subject": "Tarih",
          "text": "Türk siyasi ve askerî tarihinde büyük öneme sahip olan 'I. İnönü Muharebesi' süreci ile ilgili aşağıdakilerden hangisi söylenebilir? (H-36)",
          "options": [
            "A) Sadece ekonomik bir olaydır.",
            "B) I. İnönü Muharebesi dönemin en kritik gelişmelerinden biridir.",
            "C) Avrupa'da gerçekleşmiştir.",
            "D) Hiçbir etkisi olmamıştır.",
            "E) Osmanlı'nın kuruluş dönemine aittir."
          ],
          "correct": 1,
          "solution": "Doğru cevap I. İnönü Muharebesi dönemin en kritik gelişmelerinden biridir..",
          "id": "e2_q73",
          "no": 73
        },
        {
          "subject": "Tarih",
          "text": "Aşağıdaki tarihî gelişmelerden hangisi 'II. İnönü Muharebesi' ile doğrudan veya dolaylı olarak bağlantılıdır? (H-37)",
          "options": [
            "A) Sanayi İnkılabı",
            "B) II. İnönü Muharebesi öncesi ve sonrası yaşanan siyasi krizler.",
            "C) Fransız İhtilali",
            "D) Kavimler Göçü",
            "E) Coğrafi Keşifler"
          ],
          "correct": 1,
          "solution": "Doğru cevap II. İnönü Muharebesi öncesi ve sonrası yaşanan siyasi krizler..",
          "id": "e2_q74",
          "no": 74
        },
        {
          "subject": "Tarih",
          "text": "Millî Mücadele ve inkılaplar tarihi incelendiğinde 'Kars Antlaşması' olayının temel amacı aşağıdakilerden hangisidir? (H-38)",
          "options": [
            "A) Avrupa'ya göç etmek",
            "B) Saltanatı güçlendirmek",
            "C) Yeni sömürgeler elde etmek",
            "D) Bağımsızlık ve egemenliği pekiştirmek",
            "E) Feodaliteyi kurmak"
          ],
          "correct": 3,
          "solution": "Doğru cevap Bağımsızlık ve egemenliği pekiştirmek.",
          "id": "e2_q75",
          "no": 75
        },
        {
          "subject": "Tarih",
          "text": "Türk siyasi ve askerî tarihinde büyük öneme sahip olan 'Ankara Antlaşması' süreci ile ilgili aşağıdakilerden hangisi söylenebilir? (H-39)",
          "options": [
            "A) Osmanlı'nın kuruluş dönemine aittir.",
            "B) Avrupa'da gerçekleşmiştir.",
            "C) Hiçbir etkisi olmamıştır.",
            "D) Ankara Antlaşması dönemin en kritik gelişmelerinden biridir.",
            "E) Sadece ekonomik bir olaydır."
          ],
          "correct": 3,
          "solution": "Doğru cevap Ankara Antlaşması dönemin en kritik gelişmelerinden biridir..",
          "id": "e2_q76",
          "no": 76
        },
        {
          "subject": "Tarih",
          "text": "Aşağıdaki tarihî gelişmelerden hangisi 'Sivas Kongresi' ile doğrudan veya dolaylı olarak bağlantılıdır? (H-40)",
          "options": [
            "A) Coğrafi Keşifler",
            "B) Sivas Kongresi öncesi ve sonrası yaşanan siyasi krizler.",
            "C) Fransız İhtilali",
            "D) Sanayi İnkılabı",
            "E) Kavimler Göçü"
          ],
          "correct": 1,
          "solution": "Doğru cevap Sivas Kongresi öncesi ve sonrası yaşanan siyasi krizler..",
          "id": "e2_q77",
          "no": 77
        },
        {
          "subject": "Tarih",
          "text": "Millî Mücadele ve inkılaplar tarihi incelendiğinde 'Erzurum Kongresi' olayının temel amacı aşağıdakilerden hangisidir? (H-41)",
          "options": [
            "A) Bağımsızlık ve egemenliği pekiştirmek",
            "B) Feodaliteyi kurmak",
            "C) Saltanatı güçlendirmek",
            "D) Avrupa'ya göç etmek",
            "E) Yeni sömürgeler elde etmek"
          ],
          "correct": 0,
          "solution": "Doğru cevap Bağımsızlık ve egemenliği pekiştirmek.",
          "id": "e2_q78",
          "no": 78
        },
        {
          "subject": "Tarih",
          "text": "Türk siyasi ve askerî tarihinde büyük öneme sahip olan 'Amasya Genelgesi' süreci ile ilgili aşağıdakilerden hangisi söylenebilir? (H-42)",
          "options": [
            "A) Avrupa'da gerçekleşmiştir.",
            "B) Sadece ekonomik bir olaydır.",
            "C) Amasya Genelgesi dönemin en kritik gelişmelerinden biridir.",
            "D) Osmanlı'nın kuruluş dönemine aittir.",
            "E) Hiçbir etkisi olmamıştır."
          ],
          "correct": 2,
          "solution": "Doğru cevap Amasya Genelgesi dönemin en kritik gelişmelerinden biridir..",
          "id": "e2_q79",
          "no": 79
        },
        {
          "subject": "Tarih",
          "text": "Aşağıdaki tarihî gelişmelerden hangisi 'Lozan Antlaşması' ile doğrudan veya dolaylı olarak bağlantılıdır? (H-43)",
          "options": [
            "A) Sanayi İnkılabı",
            "B) Lozan Antlaşması öncesi ve sonrası yaşanan siyasi krizler.",
            "C) Kavimler Göçü",
            "D) Fransız İhtilali",
            "E) Coğrafi Keşifler"
          ],
          "correct": 1,
          "solution": "Doğru cevap Lozan Antlaşması öncesi ve sonrası yaşanan siyasi krizler..",
          "id": "e2_q80",
          "no": 80
        },
        {
          "subject": "Tarih",
          "text": "Millî Mücadele ve inkılaplar tarihi incelendiğinde 'Cumhuriyetin İlanı' olayının temel amacı aşağıdakilerden hangisidir? (H-44)",
          "options": [
            "A) Bağımsızlık ve egemenliği pekiştirmek",
            "B) Feodaliteyi kurmak",
            "C) Yeni sömürgeler elde etmek",
            "D) Avrupa'ya göç etmek",
            "E) Saltanatı güçlendirmek"
          ],
          "correct": 0,
          "solution": "Doğru cevap Bağımsızlık ve egemenliği pekiştirmek.",
          "id": "e2_q81",
          "no": 81
        },
        {
          "subject": "Tarih",
          "text": "Türk siyasi ve askerî tarihinde büyük öneme sahip olan 'TBMM'nin Açılışı' süreci ile ilgili aşağıdakilerden hangisi söylenebilir? (H-45)",
          "options": [
            "A) Avrupa'da gerçekleşmiştir.",
            "B) Osmanlı'nın kuruluş dönemine aittir.",
            "C) Sadece ekonomik bir olaydır.",
            "D) TBMM'nin Açılışı dönemin en kritik gelişmelerinden biridir.",
            "E) Hiçbir etkisi olmamıştır."
          ],
          "correct": 3,
          "solution": "Doğru cevap TBMM'nin Açılışı dönemin en kritik gelişmelerinden biridir..",
          "id": "e2_q82",
          "no": 82
        },
        {
          "subject": "Tarih",
          "text": "Aşağıdaki tarihî gelişmelerden hangisi 'Mudanya Mütarekesi' ile doğrudan veya dolaylı olarak bağlantılıdır? (H-46)",
          "options": [
            "A) Sanayi İnkılabı",
            "B) Kavimler Göçü",
            "C) Fransız İhtilali",
            "D) Mudanya Mütarekesi öncesi ve sonrası yaşanan siyasi krizler.",
            "E) Coğrafi Keşifler"
          ],
          "correct": 3,
          "solution": "Doğru cevap Mudanya Mütarekesi öncesi ve sonrası yaşanan siyasi krizler..",
          "id": "e2_q83",
          "no": 83
        },
        {
          "subject": "Tarih",
          "text": "Millî Mücadele ve inkılaplar tarihi incelendiğinde 'Saltanatın Kaldırılması' olayının temel amacı aşağıdakilerden hangisidir? (H-47)",
          "options": [
            "A) Bağımsızlık ve egemenliği pekiştirmek",
            "B) Yeni sömürgeler elde etmek",
            "C) Avrupa'ya göç etmek",
            "D) Feodaliteyi kurmak",
            "E) Saltanatı güçlendirmek"
          ],
          "correct": 0,
          "solution": "Doğru cevap Bağımsızlık ve egemenliği pekiştirmek.",
          "id": "e2_q84",
          "no": 84
        },
        {
          "subject": "Tarih",
          "text": "Türk siyasi ve askerî tarihinde büyük öneme sahip olan 'Halifeliğin Kaldırılması' süreci ile ilgili aşağıdakilerden hangisi söylenebilir? (H-48)",
          "options": [
            "A) Osmanlı'nın kuruluş dönemine aittir.",
            "B) Halifeliğin Kaldırılması dönemin en kritik gelişmelerinden biridir.",
            "C) Hiçbir etkisi olmamıştır.",
            "D) Sadece ekonomik bir olaydır.",
            "E) Avrupa'da gerçekleşmiştir."
          ],
          "correct": 1,
          "solution": "Doğru cevap Halifeliğin Kaldırılması dönemin en kritik gelişmelerinden biridir..",
          "id": "e2_q85",
          "no": 85
        },
        {
          "subject": "Tarih",
          "text": "Aşağıdaki tarihî gelişmelerden hangisi 'Tevhid-i Tedrisat' ile doğrudan veya dolaylı olarak bağlantılıdır? (H-49)",
          "options": [
            "A) Tevhid-i Tedrisat öncesi ve sonrası yaşanan siyasi krizler.",
            "B) Sanayi İnkılabı",
            "C) Kavimler Göçü",
            "D) Fransız İhtilali",
            "E) Coğrafi Keşifler"
          ],
          "correct": 0,
          "solution": "Doğru cevap Tevhid-i Tedrisat öncesi ve sonrası yaşanan siyasi krizler..",
          "id": "e2_q86",
          "no": 86
        },
        {
          "subject": "Tarih",
          "text": "Millî Mücadele ve inkılaplar tarihi incelendiğinde 'Trablusgarp Savaşı' olayının temel amacı aşağıdakilerden hangisidir? (H-50)",
          "options": [
            "A) Yeni sömürgeler elde etmek",
            "B) Feodaliteyi kurmak",
            "C) Saltanatı güçlendirmek",
            "D) Avrupa'ya göç etmek",
            "E) Bağımsızlık ve egemenliği pekiştirmek"
          ],
          "correct": 4,
          "solution": "Doğru cevap Bağımsızlık ve egemenliği pekiştirmek.",
          "id": "e2_q87",
          "no": 87
        },
        {
          "subject": "Coğrafya",
          "text": "Türkiye'nin fiziki coğrafyası düşünüldüğünde 'Ağrı Dağı' için aşağıdakilerden hangisi doğrudur? (C-16)",
          "options": [
            "A) Ağrı Dağı yapay bir kanaldır.",
            "B) Ağrı Dağı tarıma kapalıdır.",
            "C) Ağrı Dağı Marmara'dadır.",
            "D) Ağrı Dağı bir çöldür.",
            "E) Ağrı Dağı, ülkemizin önemli yeryüzü şekillerinden biridir."
          ],
          "correct": 4,
          "solution": "Doğru cevap Ağrı Dağı, ülkemizin önemli yeryüzü şekillerinden biridir..",
          "id": "e2_q88",
          "no": 88
        },
        {
          "subject": "Coğrafya",
          "text": "Coğrafi özellikleri ve turizm potansiyeli göz önüne alındığında 'Kızılırmak' hangi alanda daha çok öne çıkar? (C-17)",
          "options": [
            "A) Çöl iklimi araştırmaları",
            "B) Okyanus balıkçılığı",
            "C) Sadece ağır sanayi",
            "D) Sadece madencilik",
            "E) Doğal güzellikleri ve turizm/coğrafi önemi"
          ],
          "correct": 4,
          "solution": "Doğru cevap Doğal güzellikleri ve turizm/coğrafi önemi.",
          "id": "e2_q89",
          "no": 89
        },
        {
          "subject": "Coğrafya",
          "text": "Türkiye'nin fiziki coğrafyası düşünüldüğünde 'Erciyes Dağı' için aşağıdakilerden hangisi doğrudur? (C-18)",
          "options": [
            "A) Erciyes Dağı yapay bir kanaldır.",
            "B) Erciyes Dağı tarıma kapalıdır.",
            "C) Erciyes Dağı, ülkemizin önemli yeryüzü şekillerinden biridir.",
            "D) Erciyes Dağı Marmara'dadır.",
            "E) Erciyes Dağı bir çöldür."
          ],
          "correct": 2,
          "solution": "Doğru cevap Erciyes Dağı, ülkemizin önemli yeryüzü şekillerinden biridir..",
          "id": "e2_q90",
          "no": 90
        },
        {
          "subject": "Coğrafya",
          "text": "Coğrafi özellikleri ve turizm potansiyeli göz önüne alındığında 'Tuz Gölü' hangi alanda daha çok öne çıkar? (C-19)",
          "options": [
            "A) Sadece ağır sanayi",
            "B) Çöl iklimi araştırmaları",
            "C) Okyanus balıkçılığı",
            "D) Sadece madencilik",
            "E) Doğal güzellikleri ve turizm/coğrafi önemi"
          ],
          "correct": 4,
          "solution": "Doğru cevap Doğal güzellikleri ve turizm/coğrafi önemi.",
          "id": "e2_q91",
          "no": 91
        },
        {
          "subject": "Coğrafya",
          "text": "Türkiye'nin fiziki coğrafyası düşünüldüğünde 'Çukurova' için aşağıdakilerden hangisi doğrudur? (C-20)",
          "options": [
            "A) Çukurova yapay bir kanaldır.",
            "B) Çukurova tarıma kapalıdır.",
            "C) Çukurova Marmara'dadır.",
            "D) Çukurova, ülkemizin önemli yeryüzü şekillerinden biridir.",
            "E) Çukurova bir çöldür."
          ],
          "correct": 3,
          "solution": "Doğru cevap Çukurova, ülkemizin önemli yeryüzü şekillerinden biridir..",
          "id": "e2_q92",
          "no": 92
        },
        {
          "subject": "Coğrafya",
          "text": "Coğrafi özellikleri ve turizm potansiyeli göz önüne alındığında 'Bafra Ovası' hangi alanda daha çok öne çıkar? (C-21)",
          "options": [
            "A) Sadece ağır sanayi",
            "B) Çöl iklimi araştırmaları",
            "C) Okyanus balıkçılığı",
            "D) Doğal güzellikleri ve turizm/coğrafi önemi",
            "E) Sadece madencilik"
          ],
          "correct": 3,
          "solution": "Doğru cevap Doğal güzellikleri ve turizm/coğrafi önemi.",
          "id": "e2_q93",
          "no": 93
        },
        {
          "subject": "Coğrafya",
          "text": "Türkiye'nin fiziki coğrafyası düşünüldüğünde 'Kaçkar Dağları' için aşağıdakilerden hangisi doğrudur? (C-22)",
          "options": [
            "A) Kaçkar Dağları yapay bir kanaldır.",
            "B) Kaçkar Dağları, ülkemizin önemli yeryüzü şekillerinden biridir.",
            "C) Kaçkar Dağları Marmara'dadır.",
            "D) Kaçkar Dağları tarıma kapalıdır.",
            "E) Kaçkar Dağları bir çöldür."
          ],
          "correct": 1,
          "solution": "Doğru cevap Kaçkar Dağları, ülkemizin önemli yeryüzü şekillerinden biridir..",
          "id": "e2_q94",
          "no": 94
        },
        {
          "subject": "Coğrafya",
          "text": "Coğrafi özellikleri ve turizm potansiyeli göz önüne alındığında 'Gediz Nehri' hangi alanda daha çok öne çıkar? (C-23)",
          "options": [
            "A) Sadece madencilik",
            "B) Sadece ağır sanayi",
            "C) Okyanus balıkçılığı",
            "D) Çöl iklimi araştırmaları",
            "E) Doğal güzellikleri ve turizm/coğrafi önemi"
          ],
          "correct": 4,
          "solution": "Doğru cevap Doğal güzellikleri ve turizm/coğrafi önemi.",
          "id": "e2_q95",
          "no": 95
        },
        {
          "subject": "Coğrafya",
          "text": "Türkiye'nin fiziki coğrafyası düşünüldüğünde 'Salda Gölü' için aşağıdakilerden hangisi doğrudur? (C-24)",
          "options": [
            "A) Salda Gölü Marmara'dadır.",
            "B) Salda Gölü bir çöldür.",
            "C) Salda Gölü, ülkemizin önemli yeryüzü şekillerinden biridir.",
            "D) Salda Gölü yapay bir kanaldır.",
            "E) Salda Gölü tarıma kapalıdır."
          ],
          "correct": 2,
          "solution": "Doğru cevap Salda Gölü, ülkemizin önemli yeryüzü şekillerinden biridir..",
          "id": "e2_q96",
          "no": 96
        },
        {
          "subject": "Coğrafya",
          "text": "Coğrafi özellikleri ve turizm potansiyeli göz önüne alındığında 'Kapadokya' hangi alanda daha çok öne çıkar? (C-25)",
          "options": [
            "A) Okyanus balıkçılığı",
            "B) Çöl iklimi araştırmaları",
            "C) Doğal güzellikleri ve turizm/coğrafi önemi",
            "D) Sadece madencilik",
            "E) Sadece ağır sanayi"
          ],
          "correct": 2,
          "solution": "Doğru cevap Doğal güzellikleri ve turizm/coğrafi önemi.",
          "id": "e2_q97",
          "no": 97
        },
        {
          "subject": "Coğrafya",
          "text": "Türkiye'nin fiziki coğrafyası düşünüldüğünde 'Pamukkale' için aşağıdakilerden hangisi doğrudur? (C-26)",
          "options": [
            "A) Pamukkale bir çöldür.",
            "B) Pamukkale Marmara'dadır.",
            "C) Pamukkale, ülkemizin önemli yeryüzü şekillerinden biridir.",
            "D) Pamukkale yapay bir kanaldır.",
            "E) Pamukkale tarıma kapalıdır."
          ],
          "correct": 2,
          "solution": "Doğru cevap Pamukkale, ülkemizin önemli yeryüzü şekillerinden biridir..",
          "id": "e2_q98",
          "no": 98
        },
        {
          "subject": "Coğrafya",
          "text": "Coğrafi özellikleri ve turizm potansiyeli göz önüne alındığında 'Nemrut Dağı' hangi alanda daha çok öne çıkar? (C-27)",
          "options": [
            "A) Doğal güzellikleri ve turizm/coğrafi önemi",
            "B) Çöl iklimi araştırmaları",
            "C) Okyanus balıkçılığı",
            "D) Sadece madencilik",
            "E) Sadece ağır sanayi"
          ],
          "correct": 0,
          "solution": "Doğru cevap Doğal güzellikleri ve turizm/coğrafi önemi.",
          "id": "e2_q99",
          "no": 99
        },
        {
          "subject": "Coğrafya",
          "text": "Türkiye'nin fiziki coğrafyası düşünüldüğünde 'Sümela Manastırı' için aşağıdakilerden hangisi doğrudur? (C-28)",
          "options": [
            "A) Sümela Manastırı yapay bir kanaldır.",
            "B) Sümela Manastırı bir çöldür.",
            "C) Sümela Manastırı Marmara'dadır.",
            "D) Sümela Manastırı, ülkemizin önemli yeryüzü şekillerinden biridir.",
            "E) Sümela Manastırı tarıma kapalıdır."
          ],
          "correct": 3,
          "solution": "Doğru cevap Sümela Manastırı, ülkemizin önemli yeryüzü şekillerinden biridir..",
          "id": "e2_q100",
          "no": 100
        },
        {
          "subject": "Coğrafya",
          "text": "Coğrafi özellikleri ve turizm potansiyeli göz önüne alındığında 'Uludağ' hangi alanda daha çok öne çıkar? (C-29)",
          "options": [
            "A) Doğal güzellikleri ve turizm/coğrafi önemi",
            "B) Sadece madencilik",
            "C) Çöl iklimi araştırmaları",
            "D) Okyanus balıkçılığı",
            "E) Sadece ağır sanayi"
          ],
          "correct": 0,
          "solution": "Doğru cevap Doğal güzellikleri ve turizm/coğrafi önemi.",
          "id": "e2_q101",
          "no": 101
        },
        {
          "subject": "Coğrafya",
          "text": "Türkiye'nin fiziki coğrafyası düşünüldüğünde 'Van Gölü' için aşağıdakilerden hangisi doğrudur? (C-30)",
          "options": [
            "A) Van Gölü bir çöldür.",
            "B) Van Gölü yapay bir kanaldır.",
            "C) Van Gölü tarıma kapalıdır.",
            "D) Van Gölü, ülkemizin önemli yeryüzü şekillerinden biridir.",
            "E) Van Gölü Marmara'dadır."
          ],
          "correct": 3,
          "solution": "Doğru cevap Van Gölü, ülkemizin önemli yeryüzü şekillerinden biridir..",
          "id": "e2_q102",
          "no": 102
        },
        {
          "subject": "Coğrafya",
          "text": "Coğrafi özellikleri ve turizm potansiyeli göz önüne alındığında 'Ağrı Dağı' hangi alanda daha çok öne çıkar? (C-31)",
          "options": [
            "A) Okyanus balıkçılığı",
            "B) Sadece ağır sanayi",
            "C) Sadece madencilik",
            "D) Çöl iklimi araştırmaları",
            "E) Doğal güzellikleri ve turizm/coğrafi önemi"
          ],
          "correct": 4,
          "solution": "Doğru cevap Doğal güzellikleri ve turizm/coğrafi önemi.",
          "id": "e2_q103",
          "no": 103
        },
        {
          "subject": "Coğrafya",
          "text": "Türkiye'nin fiziki coğrafyası düşünüldüğünde 'Kızılırmak' için aşağıdakilerden hangisi doğrudur? (C-32)",
          "options": [
            "A) Kızılırmak bir çöldür.",
            "B) Kızılırmak tarıma kapalıdır.",
            "C) Kızılırmak, ülkemizin önemli yeryüzü şekillerinden biridir.",
            "D) Kızılırmak Marmara'dadır.",
            "E) Kızılırmak yapay bir kanaldır."
          ],
          "correct": 2,
          "solution": "Doğru cevap Kızılırmak, ülkemizin önemli yeryüzü şekillerinden biridir..",
          "id": "e2_q104",
          "no": 104
        },
        {
          "subject": "Coğrafya",
          "text": "Coğrafi özellikleri ve turizm potansiyeli göz önüne alındığında 'Erciyes Dağı' hangi alanda daha çok öne çıkar? (C-33)",
          "options": [
            "A) Sadece ağır sanayi",
            "B) Okyanus balıkçılığı",
            "C) Sadece madencilik",
            "D) Çöl iklimi araştırmaları",
            "E) Doğal güzellikleri ve turizm/coğrafi önemi"
          ],
          "correct": 4,
          "solution": "Doğru cevap Doğal güzellikleri ve turizm/coğrafi önemi.",
          "id": "e2_q105",
          "no": 105
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'Anayasa Mahkemesi' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-13)",
          "options": [
            "A) Anayasa Mahkemesi sadece köylerde bulunur.",
            "B) Anayasa Mahkemesi özel bir şirkettir.",
            "C) Anayasa Mahkemesi, anayasal sistemin önemli bir parçasıdır.",
            "D) Anayasa Mahkemesi yasaklanmıştır.",
            "E) Anayasa Mahkemesi yabancı bir kurumdur."
          ],
          "correct": 2,
          "solution": "Doğru cevap Anayasa Mahkemesi, anayasal sistemin önemli bir parçasıdır..",
          "id": "e2_q106",
          "no": 106
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'Yargıtay' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-14)",
          "options": [
            "A) Yargıtay yasaklanmıştır.",
            "B) Yargıtay, anayasal sistemin önemli bir parçasıdır.",
            "C) Yargıtay sadece köylerde bulunur.",
            "D) Yargıtay özel bir şirkettir.",
            "E) Yargıtay yabancı bir kurumdur."
          ],
          "correct": 1,
          "solution": "Doğru cevap Yargıtay, anayasal sistemin önemli bir parçasıdır..",
          "id": "e2_q107",
          "no": 107
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'Danıştay' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-15)",
          "options": [
            "A) Danıştay sadece köylerde bulunur.",
            "B) Danıştay yabancı bir kurumdur.",
            "C) Danıştay yasaklanmıştır.",
            "D) Danıştay özel bir şirkettir.",
            "E) Danıştay, anayasal sistemin önemli bir parçasıdır."
          ],
          "correct": 4,
          "solution": "Doğru cevap Danıştay, anayasal sistemin önemli bir parçasıdır..",
          "id": "e2_q108",
          "no": 108
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'TBMM' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-16)",
          "options": [
            "A) TBMM yasaklanmıştır.",
            "B) TBMM özel bir şirkettir.",
            "C) TBMM sadece köylerde bulunur.",
            "D) TBMM, anayasal sistemin önemli bir parçasıdır.",
            "E) TBMM yabancı bir kurumdur."
          ],
          "correct": 3,
          "solution": "Doğru cevap TBMM, anayasal sistemin önemli bir parçasıdır..",
          "id": "e2_q109",
          "no": 109
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'Cumhurbaşkanlığı' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-17)",
          "options": [
            "A) Cumhurbaşkanlığı sadece köylerde bulunur.",
            "B) Cumhurbaşkanlığı, anayasal sistemin önemli bir parçasıdır.",
            "C) Cumhurbaşkanlığı yabancı bir kurumdur.",
            "D) Cumhurbaşkanlığı yasaklanmıştır.",
            "E) Cumhurbaşkanlığı özel bir şirkettir."
          ],
          "correct": 1,
          "solution": "Doğru cevap Cumhurbaşkanlığı, anayasal sistemin önemli bir parçasıdır..",
          "id": "e2_q110",
          "no": 110
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'Sayıştay' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-18)",
          "options": [
            "A) Sayıştay, anayasal sistemin önemli bir parçasıdır.",
            "B) Sayıştay sadece köylerde bulunur.",
            "C) Sayıştay özel bir şirkettir.",
            "D) Sayıştay yasaklanmıştır.",
            "E) Sayıştay yabancı bir kurumdur."
          ],
          "correct": 0,
          "solution": "Doğru cevap Sayıştay, anayasal sistemin önemli bir parçasıdır..",
          "id": "e2_q111",
          "no": 111
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'YSK' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-19)",
          "options": [
            "A) YSK sadece köylerde bulunur.",
            "B) YSK, anayasal sistemin önemli bir parçasıdır.",
            "C) YSK yasaklanmıştır.",
            "D) YSK özel bir şirkettir.",
            "E) YSK yabancı bir kurumdur."
          ],
          "correct": 1,
          "solution": "Doğru cevap YSK, anayasal sistemin önemli bir parçasıdır..",
          "id": "e2_q112",
          "no": 112
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'HSK' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-20)",
          "options": [
            "A) HSK sadece köylerde bulunur.",
            "B) HSK yabancı bir kurumdur.",
            "C) HSK, anayasal sistemin önemli bir parçasıdır.",
            "D) HSK özel bir şirkettir.",
            "E) HSK yasaklanmıştır."
          ],
          "correct": 2,
          "solution": "Doğru cevap HSK, anayasal sistemin önemli bir parçasıdır..",
          "id": "e2_q113",
          "no": 113
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'Belediye' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-21)",
          "options": [
            "A) Belediye, anayasal sistemin önemli bir parçasıdır.",
            "B) Belediye yabancı bir kurumdur.",
            "C) Belediye sadece köylerde bulunur.",
            "D) Belediye özel bir şirkettir.",
            "E) Belediye yasaklanmıştır."
          ],
          "correct": 0,
          "solution": "Doğru cevap Belediye, anayasal sistemin önemli bir parçasıdır..",
          "id": "e2_q114",
          "no": 114
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'Valilik' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-22)",
          "options": [
            "A) Valilik özel bir şirkettir.",
            "B) Valilik sadece köylerde bulunur.",
            "C) Valilik, anayasal sistemin önemli bir parçasıdır.",
            "D) Valilik yasaklanmıştır.",
            "E) Valilik yabancı bir kurumdur."
          ],
          "correct": 2,
          "solution": "Doğru cevap Valilik, anayasal sistemin önemli bir parçasıdır..",
          "id": "e2_q115",
          "no": 115
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'Kaymakamlık' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-23)",
          "options": [
            "A) Kaymakamlık sadece köylerde bulunur.",
            "B) Kaymakamlık, anayasal sistemin önemli bir parçasıdır.",
            "C) Kaymakamlık yabancı bir kurumdur.",
            "D) Kaymakamlık yasaklanmıştır.",
            "E) Kaymakamlık özel bir şirkettir."
          ],
          "correct": 1,
          "solution": "Doğru cevap Kaymakamlık, anayasal sistemin önemli bir parçasıdır..",
          "id": "e2_q116",
          "no": 116
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'İl Genel Meclisi' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-24)",
          "options": [
            "A) İl Genel Meclisi, anayasal sistemin önemli bir parçasıdır.",
            "B) İl Genel Meclisi sadece köylerde bulunur.",
            "C) İl Genel Meclisi yabancı bir kurumdur.",
            "D) İl Genel Meclisi yasaklanmıştır.",
            "E) İl Genel Meclisi özel bir şirkettir."
          ],
          "correct": 0,
          "solution": "Doğru cevap İl Genel Meclisi, anayasal sistemin önemli bir parçasıdır..",
          "id": "e2_q117",
          "no": 117
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'Kamu Denetçiliği Kurumu' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-25)",
          "options": [
            "A) Kamu Denetçiliği Kurumu yabancı bir kurumdur.",
            "B) Kamu Denetçiliği Kurumu sadece köylerde bulunur.",
            "C) Kamu Denetçiliği Kurumu özel bir şirkettir.",
            "D) Kamu Denetçiliği Kurumu, anayasal sistemin önemli bir parçasıdır.",
            "E) Kamu Denetçiliği Kurumu yasaklanmıştır."
          ],
          "correct": 3,
          "solution": "Doğru cevap Kamu Denetçiliği Kurumu, anayasal sistemin önemli bir parçasıdır..",
          "id": "e2_q118",
          "no": 118
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'Anayasa Mahkemesi' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-26)",
          "options": [
            "A) Anayasa Mahkemesi yasaklanmıştır.",
            "B) Anayasa Mahkemesi sadece köylerde bulunur.",
            "C) Anayasa Mahkemesi özel bir şirkettir.",
            "D) Anayasa Mahkemesi yabancı bir kurumdur.",
            "E) Anayasa Mahkemesi, anayasal sistemin önemli bir parçasıdır."
          ],
          "correct": 4,
          "solution": "Doğru cevap Anayasa Mahkemesi, anayasal sistemin önemli bir parçasıdır..",
          "id": "e2_q119",
          "no": 119
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'Yargıtay' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-27)",
          "options": [
            "A) Yargıtay sadece köylerde bulunur.",
            "B) Yargıtay, anayasal sistemin önemli bir parçasıdır.",
            "C) Yargıtay yabancı bir kurumdur.",
            "D) Yargıtay yasaklanmıştır.",
            "E) Yargıtay özel bir şirkettir."
          ],
          "correct": 1,
          "solution": "Doğru cevap Yargıtay, anayasal sistemin önemli bir parçasıdır..",
          "id": "e2_q120",
          "no": 120
        }
      ]
    },
    {
      "id": "deneme_3",
      "name": "3. Deneme Sınavı",
      "totalQuestions": 120,
      "duration": 130,
      "distribution": {
        "Türkçe": 30,
        "Matematik": 30,
        "Tarih": 27,
        "Coğrafya": 18,
        "Vatandaşlık": 15
      },
      "questions": [
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde 'hiç kimse' kelimesinin yazımıyla ilgili bir kural hatırlatılmaktadır? (T-55)",
          "options": [
            "A) hiç kimse kelimesi yabancı kökenlidir.",
            "B) hiç kimse cümlede özne olamaz.",
            "C) hiç kimse kelimesi her zaman ayrı yazılır.",
            "D) hiç kimse kelimesi fiildir.",
            "E) 'hiç kimse' kelimesinin doğru yazımına dikkat edilmelidir."
          ],
          "correct": 4,
          "solution": "Doğru cevap 'hiç kimse' kelimesinin doğru yazımına dikkat edilmelidir..",
          "id": "e3_q1",
          "no": 1
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde mecaz anlamlı bir sözcük kullanılmıştır? (T-56)",
          "options": [
            "A) Suyu dolaptan soğuk içti.",
            "B) Buzdolabı soğuk üflüyor.",
            "C) Kışın havalar soğuk olur.",
            "D) Hava bugün çok soğuk.",
            "E) Olaylara karşı çok 'soğuk' davranıyordu."
          ],
          "correct": 4,
          "solution": "Doğru cevap Olaylara karşı çok 'soğuk' davranıyordu..",
          "id": "e3_q2",
          "no": 2
        },
        {
          "subject": "Türkçe",
          "text": "Bilim tarih boyunca insanlığın en büyük rehberlerinden biri olmuştur. Toplumlar Bilim sayesinde sınırlarını aşmış, geleceğe umutla bakabilmiştir. (P-57)\nBu parçanın ana düşüncesi nedir?",
          "options": [
            "A) Bilim sadece bireyseldir.",
            "B) Bilim sadece geçmişte kalmıştır.",
            "C) Bilim zaman kaybıdır.",
            "D) Bilim, toplumsal ilerleme ve vizyon için vazgeçilmezdir.",
            "E) İnsanlar Bilim ile ilgilenmemelidir."
          ],
          "correct": 3,
          "solution": "Doğru cevap Bilim, toplumsal ilerleme ve vizyon için vazgeçilmezdir..",
          "id": "e3_q3",
          "no": 3
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde 'herkes' kelimesinin yazımıyla ilgili bir kural hatırlatılmaktadır? (T-58)",
          "options": [
            "A) herkes kelimesi yabancı kökenlidir.",
            "B) herkes kelimesi her zaman ayrı yazılır.",
            "C) 'herkes' kelimesinin doğru yazımına dikkat edilmelidir.",
            "D) herkes cümlede özne olamaz.",
            "E) herkes kelimesi fiildir."
          ],
          "correct": 2,
          "solution": "Doğru cevap 'herkes' kelimesinin doğru yazımına dikkat edilmelidir..",
          "id": "e3_q4",
          "no": 4
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde mecaz anlamlı bir sözcük kullanılmıştır? (T-59)",
          "options": [
            "A) Suyu dolaptan soğuk içti.",
            "B) Kışın havalar soğuk olur.",
            "C) Hava bugün çok soğuk.",
            "D) Buzdolabı soğuk üflüyor.",
            "E) Olaylara karşı çok 'soğuk' davranıyordu."
          ],
          "correct": 4,
          "solution": "Doğru cevap Olaylara karşı çok 'soğuk' davranıyordu..",
          "id": "e3_q5",
          "no": 5
        },
        {
          "subject": "Türkçe",
          "text": "Sanat tarih boyunca insanlığın en büyük rehberlerinden biri olmuştur. Toplumlar Sanat sayesinde sınırlarını aşmış, geleceğe umutla bakabilmiştir. (P-60)\nBu parçanın ana düşüncesi nedir?",
          "options": [
            "A) Sanat, toplumsal ilerleme ve vizyon için vazgeçilmezdir.",
            "B) Sanat sadece geçmişte kalmıştır.",
            "C) İnsanlar Sanat ile ilgilenmemelidir.",
            "D) Sanat sadece bireyseldir.",
            "E) Sanat zaman kaybıdır."
          ],
          "correct": 0,
          "solution": "Doğru cevap Sanat, toplumsal ilerleme ve vizyon için vazgeçilmezdir..",
          "id": "e3_q6",
          "no": 6
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde 'bugün' kelimesinin yazımıyla ilgili bir kural hatırlatılmaktadır? (T-61)",
          "options": [
            "A) bugün kelimesi her zaman ayrı yazılır.",
            "B) bugün kelimesi yabancı kökenlidir.",
            "C) bugün cümlede özne olamaz.",
            "D) 'bugün' kelimesinin doğru yazımına dikkat edilmelidir.",
            "E) bugün kelimesi fiildir."
          ],
          "correct": 3,
          "solution": "Doğru cevap 'bugün' kelimesinin doğru yazımına dikkat edilmelidir..",
          "id": "e3_q7",
          "no": 7
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde mecaz anlamlı bir sözcük kullanılmıştır? (T-62)",
          "options": [
            "A) Kışın havalar soğuk olur.",
            "B) Suyu dolaptan soğuk içti.",
            "C) Buzdolabı soğuk üflüyor.",
            "D) Olaylara karşı çok 'soğuk' davranıyordu.",
            "E) Hava bugün çok soğuk."
          ],
          "correct": 3,
          "solution": "Doğru cevap Olaylara karşı çok 'soğuk' davranıyordu..",
          "id": "e3_q8",
          "no": 8
        },
        {
          "subject": "Türkçe",
          "text": "Teknoloji tarih boyunca insanlığın en büyük rehberlerinden biri olmuştur. Toplumlar Teknoloji sayesinde sınırlarını aşmış, geleceğe umutla bakabilmiştir. (P-63)\nBu parçanın ana düşüncesi nedir?",
          "options": [
            "A) Teknoloji sadece geçmişte kalmıştır.",
            "B) İnsanlar Teknoloji ile ilgilenmemelidir.",
            "C) Teknoloji, toplumsal ilerleme ve vizyon için vazgeçilmezdir.",
            "D) Teknoloji sadece bireyseldir.",
            "E) Teknoloji zaman kaybıdır."
          ],
          "correct": 2,
          "solution": "Doğru cevap Teknoloji, toplumsal ilerleme ve vizyon için vazgeçilmezdir..",
          "id": "e3_q9",
          "no": 9
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde 'yalnız' kelimesinin yazımıyla ilgili bir kural hatırlatılmaktadır? (T-64)",
          "options": [
            "A) yalnız kelimesi her zaman ayrı yazılır.",
            "B) yalnız kelimesi yabancı kökenlidir.",
            "C) yalnız kelimesi fiildir.",
            "D) 'yalnız' kelimesinin doğru yazımına dikkat edilmelidir.",
            "E) yalnız cümlede özne olamaz."
          ],
          "correct": 3,
          "solution": "Doğru cevap 'yalnız' kelimesinin doğru yazımına dikkat edilmelidir..",
          "id": "e3_q10",
          "no": 10
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde mecaz anlamlı bir sözcük kullanılmıştır? (T-65)",
          "options": [
            "A) Buzdolabı soğuk üflüyor.",
            "B) Kışın havalar soğuk olur.",
            "C) Hava bugün çok soğuk.",
            "D) Olaylara karşı çok 'soğuk' davranıyordu.",
            "E) Suyu dolaptan soğuk içti."
          ],
          "correct": 3,
          "solution": "Doğru cevap Olaylara karşı çok 'soğuk' davranıyordu..",
          "id": "e3_q11",
          "no": 11
        },
        {
          "subject": "Türkçe",
          "text": "Doğa tarih boyunca insanlığın en büyük rehberlerinden biri olmuştur. Toplumlar Doğa sayesinde sınırlarını aşmış, geleceğe umutla bakabilmiştir. (P-66)\nBu parçanın ana düşüncesi nedir?",
          "options": [
            "A) Doğa sadece bireyseldir.",
            "B) Doğa zaman kaybıdır.",
            "C) Doğa sadece geçmişte kalmıştır.",
            "D) İnsanlar Doğa ile ilgilenmemelidir.",
            "E) Doğa, toplumsal ilerleme ve vizyon için vazgeçilmezdir."
          ],
          "correct": 4,
          "solution": "Doğru cevap Doğa, toplumsal ilerleme ve vizyon için vazgeçilmezdir..",
          "id": "e3_q12",
          "no": 12
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde 'hiçbir' kelimesinin yazımıyla ilgili bir kural hatırlatılmaktadır? (T-67)",
          "options": [
            "A) 'hiçbir' kelimesinin doğru yazımına dikkat edilmelidir.",
            "B) hiçbir cümlede özne olamaz.",
            "C) hiçbir kelimesi fiildir.",
            "D) hiçbir kelimesi her zaman ayrı yazılır.",
            "E) hiçbir kelimesi yabancı kökenlidir."
          ],
          "correct": 0,
          "solution": "Doğru cevap 'hiçbir' kelimesinin doğru yazımına dikkat edilmelidir..",
          "id": "e3_q13",
          "no": 13
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde mecaz anlamlı bir sözcük kullanılmıştır? (T-68)",
          "options": [
            "A) Suyu dolaptan soğuk içti.",
            "B) Kışın havalar soğuk olur.",
            "C) Olaylara karşı çok 'soğuk' davranıyordu.",
            "D) Hava bugün çok soğuk.",
            "E) Buzdolabı soğuk üflüyor."
          ],
          "correct": 2,
          "solution": "Doğru cevap Olaylara karşı çok 'soğuk' davranıyordu..",
          "id": "e3_q14",
          "no": 14
        },
        {
          "subject": "Türkçe",
          "text": "Psikoloji tarih boyunca insanlığın en büyük rehberlerinden biri olmuştur. Toplumlar Psikoloji sayesinde sınırlarını aşmış, geleceğe umutla bakabilmiştir. (P-69)\nBu parçanın ana düşüncesi nedir?",
          "options": [
            "A) İnsanlar Psikoloji ile ilgilenmemelidir.",
            "B) Psikoloji sadece geçmişte kalmıştır.",
            "C) Psikoloji, toplumsal ilerleme ve vizyon için vazgeçilmezdir.",
            "D) Psikoloji sadece bireyseldir.",
            "E) Psikoloji zaman kaybıdır."
          ],
          "correct": 2,
          "solution": "Doğru cevap Psikoloji, toplumsal ilerleme ve vizyon için vazgeçilmezdir..",
          "id": "e3_q15",
          "no": 15
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde 'her şey' kelimesinin yazımıyla ilgili bir kural hatırlatılmaktadır? (T-70)",
          "options": [
            "A) her şey kelimesi yabancı kökenlidir.",
            "B) her şey kelimesi fiildir.",
            "C) her şey kelimesi her zaman ayrı yazılır.",
            "D) her şey cümlede özne olamaz.",
            "E) 'her şey' kelimesinin doğru yazımına dikkat edilmelidir."
          ],
          "correct": 4,
          "solution": "Doğru cevap 'her şey' kelimesinin doğru yazımına dikkat edilmelidir..",
          "id": "e3_q16",
          "no": 16
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde mecaz anlamlı bir sözcük kullanılmıştır? (T-71)",
          "options": [
            "A) Buzdolabı soğuk üflüyor.",
            "B) Kışın havalar soğuk olur.",
            "C) Olaylara karşı çok 'soğuk' davranıyordu.",
            "D) Suyu dolaptan soğuk içti.",
            "E) Hava bugün çok soğuk."
          ],
          "correct": 2,
          "solution": "Doğru cevap Olaylara karşı çok 'soğuk' davranıyordu..",
          "id": "e3_q17",
          "no": 17
        },
        {
          "subject": "Türkçe",
          "text": "Eğitim tarih boyunca insanlığın en büyük rehberlerinden biri olmuştur. Toplumlar Eğitim sayesinde sınırlarını aşmış, geleceğe umutla bakabilmiştir. (P-72)\nBu parçanın ana düşüncesi nedir?",
          "options": [
            "A) Eğitim, toplumsal ilerleme ve vizyon için vazgeçilmezdir.",
            "B) Eğitim sadece bireyseldir.",
            "C) Eğitim zaman kaybıdır.",
            "D) İnsanlar Eğitim ile ilgilenmemelidir.",
            "E) Eğitim sadece geçmişte kalmıştır."
          ],
          "correct": 0,
          "solution": "Doğru cevap Eğitim, toplumsal ilerleme ve vizyon için vazgeçilmezdir..",
          "id": "e3_q18",
          "no": 18
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde 'yanlış' kelimesinin yazımıyla ilgili bir kural hatırlatılmaktadır? (T-73)",
          "options": [
            "A) 'yanlış' kelimesinin doğru yazımına dikkat edilmelidir.",
            "B) yanlış kelimesi her zaman ayrı yazılır.",
            "C) yanlış kelimesi yabancı kökenlidir.",
            "D) yanlış kelimesi fiildir.",
            "E) yanlış cümlede özne olamaz."
          ],
          "correct": 0,
          "solution": "Doğru cevap 'yanlış' kelimesinin doğru yazımına dikkat edilmelidir..",
          "id": "e3_q19",
          "no": 19
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde mecaz anlamlı bir sözcük kullanılmıştır? (T-74)",
          "options": [
            "A) Kışın havalar soğuk olur.",
            "B) Suyu dolaptan soğuk içti.",
            "C) Hava bugün çok soğuk.",
            "D) Buzdolabı soğuk üflüyor.",
            "E) Olaylara karşı çok 'soğuk' davranıyordu."
          ],
          "correct": 4,
          "solution": "Doğru cevap Olaylara karşı çok 'soğuk' davranıyordu..",
          "id": "e3_q20",
          "no": 20
        },
        {
          "subject": "Türkçe",
          "text": "Kültür tarih boyunca insanlığın en büyük rehberlerinden biri olmuştur. Toplumlar Kültür sayesinde sınırlarını aşmış, geleceğe umutla bakabilmiştir. (P-75)\nBu parçanın ana düşüncesi nedir?",
          "options": [
            "A) İnsanlar Kültür ile ilgilenmemelidir.",
            "B) Kültür sadece geçmişte kalmıştır.",
            "C) Kültür zaman kaybıdır.",
            "D) Kültür, toplumsal ilerleme ve vizyon için vazgeçilmezdir.",
            "E) Kültür sadece bireyseldir."
          ],
          "correct": 3,
          "solution": "Doğru cevap Kültür, toplumsal ilerleme ve vizyon için vazgeçilmezdir..",
          "id": "e3_q21",
          "no": 21
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde 'birkaç' kelimesinin yazımıyla ilgili bir kural hatırlatılmaktadır? (T-76)",
          "options": [
            "A) birkaç kelimesi yabancı kökenlidir.",
            "B) birkaç kelimesi her zaman ayrı yazılır.",
            "C) 'birkaç' kelimesinin doğru yazımına dikkat edilmelidir.",
            "D) birkaç kelimesi fiildir.",
            "E) birkaç cümlede özne olamaz."
          ],
          "correct": 2,
          "solution": "Doğru cevap 'birkaç' kelimesinin doğru yazımına dikkat edilmelidir..",
          "id": "e3_q22",
          "no": 22
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde mecaz anlamlı bir sözcük kullanılmıştır? (T-77)",
          "options": [
            "A) Kışın havalar soğuk olur.",
            "B) Suyu dolaptan soğuk içti.",
            "C) Buzdolabı soğuk üflüyor.",
            "D) Hava bugün çok soğuk.",
            "E) Olaylara karşı çok 'soğuk' davranıyordu."
          ],
          "correct": 4,
          "solution": "Doğru cevap Olaylara karşı çok 'soğuk' davranıyordu..",
          "id": "e3_q23",
          "no": 23
        },
        {
          "subject": "Türkçe",
          "text": "Felsefe tarih boyunca insanlığın en büyük rehberlerinden biri olmuştur. Toplumlar Felsefe sayesinde sınırlarını aşmış, geleceğe umutla bakabilmiştir. (P-78)\nBu parçanın ana düşüncesi nedir?",
          "options": [
            "A) Felsefe, toplumsal ilerleme ve vizyon için vazgeçilmezdir.",
            "B) Felsefe sadece bireyseldir.",
            "C) Felsefe sadece geçmişte kalmıştır.",
            "D) Felsefe zaman kaybıdır.",
            "E) İnsanlar Felsefe ile ilgilenmemelidir."
          ],
          "correct": 0,
          "solution": "Doğru cevap Felsefe, toplumsal ilerleme ve vizyon için vazgeçilmezdir..",
          "id": "e3_q24",
          "no": 24
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde 'hiç kimse' kelimesinin yazımıyla ilgili bir kural hatırlatılmaktadır? (T-79)",
          "options": [
            "A) hiç kimse kelimesi fiildir.",
            "B) hiç kimse kelimesi her zaman ayrı yazılır.",
            "C) hiç kimse kelimesi yabancı kökenlidir.",
            "D) 'hiç kimse' kelimesinin doğru yazımına dikkat edilmelidir.",
            "E) hiç kimse cümlede özne olamaz."
          ],
          "correct": 3,
          "solution": "Doğru cevap 'hiç kimse' kelimesinin doğru yazımına dikkat edilmelidir..",
          "id": "e3_q25",
          "no": 25
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde mecaz anlamlı bir sözcük kullanılmıştır? (T-80)",
          "options": [
            "A) Kışın havalar soğuk olur.",
            "B) Hava bugün çok soğuk.",
            "C) Olaylara karşı çok 'soğuk' davranıyordu.",
            "D) Suyu dolaptan soğuk içti.",
            "E) Buzdolabı soğuk üflüyor."
          ],
          "correct": 2,
          "solution": "Doğru cevap Olaylara karşı çok 'soğuk' davranıyordu..",
          "id": "e3_q26",
          "no": 26
        },
        {
          "subject": "Türkçe",
          "text": "Edebiyat tarih boyunca insanlığın en büyük rehberlerinden biri olmuştur. Toplumlar Edebiyat sayesinde sınırlarını aşmış, geleceğe umutla bakabilmiştir. (P-81)\nBu parçanın ana düşüncesi nedir?",
          "options": [
            "A) Edebiyat zaman kaybıdır.",
            "B) Edebiyat sadece bireyseldir.",
            "C) Edebiyat, toplumsal ilerleme ve vizyon için vazgeçilmezdir.",
            "D) İnsanlar Edebiyat ile ilgilenmemelidir.",
            "E) Edebiyat sadece geçmişte kalmıştır."
          ],
          "correct": 2,
          "solution": "Doğru cevap Edebiyat, toplumsal ilerleme ve vizyon için vazgeçilmezdir..",
          "id": "e3_q27",
          "no": 27
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde 'herkes' kelimesinin yazımıyla ilgili bir kural hatırlatılmaktadır? (T-82)",
          "options": [
            "A) herkes kelimesi fiildir.",
            "B) 'herkes' kelimesinin doğru yazımına dikkat edilmelidir.",
            "C) herkes kelimesi her zaman ayrı yazılır.",
            "D) herkes kelimesi yabancı kökenlidir.",
            "E) herkes cümlede özne olamaz."
          ],
          "correct": 1,
          "solution": "Doğru cevap 'herkes' kelimesinin doğru yazımına dikkat edilmelidir..",
          "id": "e3_q28",
          "no": 28
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde mecaz anlamlı bir sözcük kullanılmıştır? (T-83)",
          "options": [
            "A) Olaylara karşı çok 'soğuk' davranıyordu.",
            "B) Suyu dolaptan soğuk içti.",
            "C) Hava bugün çok soğuk.",
            "D) Kışın havalar soğuk olur.",
            "E) Buzdolabı soğuk üflüyor."
          ],
          "correct": 0,
          "solution": "Doğru cevap Olaylara karşı çok 'soğuk' davranıyordu..",
          "id": "e3_q29",
          "no": 29
        },
        {
          "subject": "Türkçe",
          "text": "Tarih tarih boyunca insanlığın en büyük rehberlerinden biri olmuştur. Toplumlar Tarih sayesinde sınırlarını aşmış, geleceğe umutla bakabilmiştir. (P-84)\nBu parçanın ana düşüncesi nedir?",
          "options": [
            "A) Tarih sadece bireyseldir.",
            "B) Tarih, toplumsal ilerleme ve vizyon için vazgeçilmezdir.",
            "C) İnsanlar Tarih ile ilgilenmemelidir.",
            "D) Tarih zaman kaybıdır.",
            "E) Tarih sadece geçmişte kalmıştır."
          ],
          "correct": 1,
          "solution": "Doğru cevap Tarih, toplumsal ilerleme ve vizyon için vazgeçilmezdir..",
          "id": "e3_q30",
          "no": 30
        },
        {
          "subject": "Matematik",
          "text": "6x + 50 = 68 denkleminde x kaçtır? (SoruID: M60)",
          "options": [
            "A) 4",
            "B) 5",
            "C) 2",
            "D) 6",
            "E) 3"
          ],
          "correct": 4,
          "solution": "Doğru cevap 3.",
          "id": "e3_q31",
          "no": 31
        },
        {
          "subject": "Matematik",
          "text": "130 sayısının %10'si kaçtır? (SoruID: M61)",
          "options": [
            "A) 23",
            "B) 13",
            "C) 8",
            "D) 28",
            "E) 18"
          ],
          "correct": 1,
          "solution": "Doğru cevap 13.",
          "id": "e3_q32",
          "no": 32
        },
        {
          "subject": "Matematik",
          "text": "26, 13 ve 12 sayılarının aritmetik ortalaması kaçtır? (SoruID: M62)",
          "options": [
            "A) 17",
            "B) 16",
            "C) 15",
            "D) 19",
            "E) 18"
          ],
          "correct": 0,
          "solution": "Doğru cevap 17.",
          "id": "e3_q33",
          "no": 33
        },
        {
          "subject": "Matematik",
          "text": "Ali 19, Ayşe 11 yaşındadır. 6 yıl sonra yaşları toplamı kaç olur? (SoruID: M63)",
          "options": [
            "A) 42",
            "B) 43",
            "C) 41",
            "D) 36",
            "E) 48"
          ],
          "correct": 0,
          "solution": "Doğru cevap 42.",
          "id": "e3_q34",
          "no": 34
        },
        {
          "subject": "Matematik",
          "text": "√49 + √16 işleminin sonucu kaçtır? (SoruID: M64)",
          "options": [
            "A) 9",
            "B) 11",
            "C) 10",
            "D) 12",
            "E) 13"
          ],
          "correct": 1,
          "solution": "Doğru cevap 11.",
          "id": "e3_q35",
          "no": 35
        },
        {
          "subject": "Matematik",
          "text": "9x + 27 = 90 denkleminde x kaçtır? (SoruID: M65)",
          "options": [
            "A) 9",
            "B) 7",
            "C) 6",
            "D) 8",
            "E) 10"
          ],
          "correct": 1,
          "solution": "Doğru cevap 7.",
          "id": "e3_q36",
          "no": 36
        },
        {
          "subject": "Matematik",
          "text": "90 sayısının %50'si kaçtır? (SoruID: M66)",
          "options": [
            "A) 50",
            "B) 40",
            "C) 45",
            "D) 55",
            "E) 60"
          ],
          "correct": 2,
          "solution": "Doğru cevap 45.",
          "id": "e3_q37",
          "no": 37
        },
        {
          "subject": "Matematik",
          "text": "13, 26 ve 30 sayılarının aritmetik ortalaması kaçtır? (SoruID: M67)",
          "options": [
            "A) 25",
            "B) 24",
            "C) 21",
            "D) 22",
            "E) 23"
          ],
          "correct": 4,
          "solution": "Doğru cevap 23.",
          "id": "e3_q38",
          "no": 38
        },
        {
          "subject": "Matematik",
          "text": "Ali 19, Ayşe 16 yaşındadır. 5 yıl sonra yaşları toplamı kaç olur? (SoruID: M68)",
          "options": [
            "A) 46",
            "B) 40",
            "C) 45",
            "D) 50",
            "E) 44"
          ],
          "correct": 2,
          "solution": "Doğru cevap 45.",
          "id": "e3_q39",
          "no": 39
        },
        {
          "subject": "Matematik",
          "text": "√49 + √81 işleminin sonucu kaçtır? (SoruID: M69)",
          "options": [
            "A) 18",
            "B) 15",
            "C) 17",
            "D) 14",
            "E) 16"
          ],
          "correct": 4,
          "solution": "Doğru cevap 16.",
          "id": "e3_q40",
          "no": 40
        },
        {
          "subject": "Matematik",
          "text": "6x + 12 = 78 denkleminde x kaçtır? (SoruID: M70)",
          "options": [
            "A) 14",
            "B) 11",
            "C) 12",
            "D) 13",
            "E) 10"
          ],
          "correct": 1,
          "solution": "Doğru cevap 11.",
          "id": "e3_q41",
          "no": 41
        },
        {
          "subject": "Matematik",
          "text": "200 sayısının %30'si kaçtır? (SoruID: M71)",
          "options": [
            "A) 60",
            "B) 70",
            "C) 75",
            "D) 65",
            "E) 55"
          ],
          "correct": 0,
          "solution": "Doğru cevap 60.",
          "id": "e3_q42",
          "no": 42
        },
        {
          "subject": "Matematik",
          "text": "12, 12 ve 12 sayılarının aritmetik ortalaması kaçtır? (SoruID: M72)",
          "options": [
            "A) 10",
            "B) 12",
            "C) 13",
            "D) 11",
            "E) 14"
          ],
          "correct": 1,
          "solution": "Doğru cevap 12.",
          "id": "e3_q43",
          "no": 43
        },
        {
          "subject": "Matematik",
          "text": "Ali 15, Ayşe 20 yaşındadır. 9 yıl sonra yaşları toplamı kaç olur? (SoruID: M73)",
          "options": [
            "A) 53",
            "B) 54",
            "C) 62",
            "D) 44",
            "E) 52"
          ],
          "correct": 0,
          "solution": "Doğru cevap 53.",
          "id": "e3_q44",
          "no": 44
        },
        {
          "subject": "Matematik",
          "text": "√64 + √49 işleminin sonucu kaçtır? (SoruID: M74)",
          "options": [
            "A) 14",
            "B) 15",
            "C) 17",
            "D) 13",
            "E) 16"
          ],
          "correct": 1,
          "solution": "Doğru cevap 15.",
          "id": "e3_q45",
          "no": 45
        },
        {
          "subject": "Matematik",
          "text": "7x + 27 = 118 denkleminde x kaçtır? (SoruID: M75)",
          "options": [
            "A) 14",
            "B) 12",
            "C) 13",
            "D) 16",
            "E) 15"
          ],
          "correct": 2,
          "solution": "Doğru cevap 13.",
          "id": "e3_q46",
          "no": 46
        },
        {
          "subject": "Matematik",
          "text": "180 sayısının %25'si kaçtır? (SoruID: M76)",
          "options": [
            "A) 60",
            "B) 45",
            "C) 55",
            "D) 40",
            "E) 50"
          ],
          "correct": 1,
          "solution": "Doğru cevap 45.",
          "id": "e3_q47",
          "no": 47
        },
        {
          "subject": "Matematik",
          "text": "20, 18 ve 25 sayılarının aritmetik ortalaması kaçtır? (SoruID: M77)",
          "options": [
            "A) 21",
            "B) 23",
            "C) 19",
            "D) 22",
            "E) 20"
          ],
          "correct": 0,
          "solution": "Doğru cevap 21.",
          "id": "e3_q48",
          "no": 48
        },
        {
          "subject": "Matematik",
          "text": "Ali 17, Ayşe 20 yaşındadır. 5 yıl sonra yaşları toplamı kaç olur? (SoruID: M78)",
          "options": [
            "A) 48",
            "B) 42",
            "C) 52",
            "D) 47",
            "E) 46"
          ],
          "correct": 3,
          "solution": "Doğru cevap 47.",
          "id": "e3_q49",
          "no": 49
        },
        {
          "subject": "Matematik",
          "text": "√81 + √64 işleminin sonucu kaçtır? (SoruID: M79)",
          "options": [
            "A) 15",
            "B) 18",
            "C) 16",
            "D) 17",
            "E) 19"
          ],
          "correct": 3,
          "solution": "Doğru cevap 17.",
          "id": "e3_q50",
          "no": 50
        },
        {
          "subject": "Matematik",
          "text": "8x + 11 = 59 denkleminde x kaçtır? (SoruID: M80)",
          "options": [
            "A) 6",
            "B) 5",
            "C) 9",
            "D) 7",
            "E) 8"
          ],
          "correct": 0,
          "solution": "Doğru cevap 6.",
          "id": "e3_q51",
          "no": 51
        },
        {
          "subject": "Matematik",
          "text": "140 sayısının %10'si kaçtır? (SoruID: M81)",
          "options": [
            "A) 9",
            "B) 29",
            "C) 14",
            "D) 24",
            "E) 19"
          ],
          "correct": 2,
          "solution": "Doğru cevap 14.",
          "id": "e3_q52",
          "no": 52
        },
        {
          "subject": "Matematik",
          "text": "27, 18 ve 15 sayılarının aritmetik ortalaması kaçtır? (SoruID: M82)",
          "options": [
            "A) 20",
            "B) 18",
            "C) 21",
            "D) 22",
            "E) 19"
          ],
          "correct": 0,
          "solution": "Doğru cevap 20.",
          "id": "e3_q53",
          "no": 53
        },
        {
          "subject": "Matematik",
          "text": "Ali 20, Ayşe 10 yaşındadır. 3 yıl sonra yaşları toplamı kaç olur? (SoruID: M83)",
          "options": [
            "A) 37",
            "B) 35",
            "C) 33",
            "D) 36",
            "E) 39"
          ],
          "correct": 3,
          "solution": "Doğru cevap 36.",
          "id": "e3_q54",
          "no": 54
        },
        {
          "subject": "Matematik",
          "text": "√49 + √4 işleminin sonucu kaçtır? (SoruID: M84)",
          "options": [
            "A) 9",
            "B) 7",
            "C) 8",
            "D) 11",
            "E) 10"
          ],
          "correct": 0,
          "solution": "Doğru cevap 9.",
          "id": "e3_q55",
          "no": 55
        },
        {
          "subject": "Matematik",
          "text": "7x + 40 = 54 denkleminde x kaçtır? (SoruID: M85)",
          "options": [
            "A) 5",
            "B) 1",
            "C) 4",
            "D) 2",
            "E) 3"
          ],
          "correct": 3,
          "solution": "Doğru cevap 2.",
          "id": "e3_q56",
          "no": 56
        },
        {
          "subject": "Matematik",
          "text": "140 sayısının %30'si kaçtır? (SoruID: M86)",
          "options": [
            "A) 57",
            "B) 42",
            "C) 37",
            "D) 52",
            "E) 47"
          ],
          "correct": 1,
          "solution": "Doğru cevap 42.",
          "id": "e3_q57",
          "no": 57
        },
        {
          "subject": "Matematik",
          "text": "19, 12 ve 29 sayılarının aritmetik ortalaması kaçtır? (SoruID: M87)",
          "options": [
            "A) 18",
            "B) 19",
            "C) 20",
            "D) 21",
            "E) 22"
          ],
          "correct": 2,
          "solution": "Doğru cevap 20.",
          "id": "e3_q58",
          "no": 58
        },
        {
          "subject": "Matematik",
          "text": "Ali 18, Ayşe 23 yaşındadır. 3 yıl sonra yaşları toplamı kaç olur? (SoruID: M88)",
          "options": [
            "A) 47",
            "B) 44",
            "C) 48",
            "D) 46",
            "E) 50"
          ],
          "correct": 0,
          "solution": "Doğru cevap 47.",
          "id": "e3_q59",
          "no": 59
        },
        {
          "subject": "Matematik",
          "text": "√49 + √49 işleminin sonucu kaçtır? (SoruID: M89)",
          "options": [
            "A) 14",
            "B) 12",
            "C) 15",
            "D) 16",
            "E) 13"
          ],
          "correct": 0,
          "solution": "Doğru cevap 14.",
          "id": "e3_q60",
          "no": 60
        },
        {
          "subject": "Tarih",
          "text": "Türk siyasi ve askerî tarihinde büyük öneme sahip olan 'Balkan Savaşları' süreci ile ilgili aşağıdakilerden hangisi söylenebilir? (H-51)",
          "options": [
            "A) Avrupa'da gerçekleşmiştir.",
            "B) Sadece ekonomik bir olaydır.",
            "C) Hiçbir etkisi olmamıştır.",
            "D) Balkan Savaşları dönemin en kritik gelişmelerinden biridir.",
            "E) Osmanlı'nın kuruluş dönemine aittir."
          ],
          "correct": 3,
          "solution": "Doğru cevap Balkan Savaşları dönemin en kritik gelişmelerinden biridir..",
          "id": "e3_q61",
          "no": 61
        },
        {
          "subject": "Tarih",
          "text": "Aşağıdaki tarihî gelişmelerden hangisi 'I. Dünya Savaşı' ile doğrudan veya dolaylı olarak bağlantılıdır? (H-52)",
          "options": [
            "A) Fransız İhtilali",
            "B) Kavimler Göçü",
            "C) Coğrafi Keşifler",
            "D) I. Dünya Savaşı öncesi ve sonrası yaşanan siyasi krizler.",
            "E) Sanayi İnkılabı"
          ],
          "correct": 3,
          "solution": "Doğru cevap I. Dünya Savaşı öncesi ve sonrası yaşanan siyasi krizler..",
          "id": "e3_q62",
          "no": 62
        },
        {
          "subject": "Tarih",
          "text": "Millî Mücadele ve inkılaplar tarihi incelendiğinde 'Çanakkale Cephesi' olayının temel amacı aşağıdakilerden hangisidir? (H-53)",
          "options": [
            "A) Feodaliteyi kurmak",
            "B) Yeni sömürgeler elde etmek",
            "C) Bağımsızlık ve egemenliği pekiştirmek",
            "D) Saltanatı güçlendirmek",
            "E) Avrupa'ya göç etmek"
          ],
          "correct": 2,
          "solution": "Doğru cevap Bağımsızlık ve egemenliği pekiştirmek.",
          "id": "e3_q63",
          "no": 63
        },
        {
          "subject": "Tarih",
          "text": "Türk siyasi ve askerî tarihinde büyük öneme sahip olan 'Sakarya Meydan Muharebesi' süreci ile ilgili aşağıdakilerden hangisi söylenebilir? (H-54)",
          "options": [
            "A) Avrupa'da gerçekleşmiştir.",
            "B) Sadece ekonomik bir olaydır.",
            "C) Sakarya Meydan Muharebesi dönemin en kritik gelişmelerinden biridir.",
            "D) Osmanlı'nın kuruluş dönemine aittir.",
            "E) Hiçbir etkisi olmamıştır."
          ],
          "correct": 2,
          "solution": "Doğru cevap Sakarya Meydan Muharebesi dönemin en kritik gelişmelerinden biridir..",
          "id": "e3_q64",
          "no": 64
        },
        {
          "subject": "Tarih",
          "text": "Aşağıdaki tarihî gelişmelerden hangisi 'Büyük Taarruz' ile doğrudan veya dolaylı olarak bağlantılıdır? (H-55)",
          "options": [
            "A) Coğrafi Keşifler",
            "B) Kavimler Göçü",
            "C) Fransız İhtilali",
            "D) Büyük Taarruz öncesi ve sonrası yaşanan siyasi krizler.",
            "E) Sanayi İnkılabı"
          ],
          "correct": 3,
          "solution": "Doğru cevap Büyük Taarruz öncesi ve sonrası yaşanan siyasi krizler..",
          "id": "e3_q65",
          "no": 65
        },
        {
          "subject": "Tarih",
          "text": "Millî Mücadele ve inkılaplar tarihi incelendiğinde 'I. İnönü Muharebesi' olayının temel amacı aşağıdakilerden hangisidir? (H-56)",
          "options": [
            "A) Saltanatı güçlendirmek",
            "B) Avrupa'ya göç etmek",
            "C) Bağımsızlık ve egemenliği pekiştirmek",
            "D) Feodaliteyi kurmak",
            "E) Yeni sömürgeler elde etmek"
          ],
          "correct": 2,
          "solution": "Doğru cevap Bağımsızlık ve egemenliği pekiştirmek.",
          "id": "e3_q66",
          "no": 66
        },
        {
          "subject": "Tarih",
          "text": "Türk siyasi ve askerî tarihinde büyük öneme sahip olan 'II. İnönü Muharebesi' süreci ile ilgili aşağıdakilerden hangisi söylenebilir? (H-57)",
          "options": [
            "A) Osmanlı'nın kuruluş dönemine aittir.",
            "B) Avrupa'da gerçekleşmiştir.",
            "C) Sadece ekonomik bir olaydır.",
            "D) II. İnönü Muharebesi dönemin en kritik gelişmelerinden biridir.",
            "E) Hiçbir etkisi olmamıştır."
          ],
          "correct": 3,
          "solution": "Doğru cevap II. İnönü Muharebesi dönemin en kritik gelişmelerinden biridir..",
          "id": "e3_q67",
          "no": 67
        },
        {
          "subject": "Tarih",
          "text": "Aşağıdaki tarihî gelişmelerden hangisi 'Kars Antlaşması' ile doğrudan veya dolaylı olarak bağlantılıdır? (H-58)",
          "options": [
            "A) Coğrafi Keşifler",
            "B) Fransız İhtilali",
            "C) Kavimler Göçü",
            "D) Sanayi İnkılabı",
            "E) Kars Antlaşması öncesi ve sonrası yaşanan siyasi krizler."
          ],
          "correct": 4,
          "solution": "Doğru cevap Kars Antlaşması öncesi ve sonrası yaşanan siyasi krizler..",
          "id": "e3_q68",
          "no": 68
        },
        {
          "subject": "Tarih",
          "text": "Millî Mücadele ve inkılaplar tarihi incelendiğinde 'Ankara Antlaşması' olayının temel amacı aşağıdakilerden hangisidir? (H-59)",
          "options": [
            "A) Saltanatı güçlendirmek",
            "B) Bağımsızlık ve egemenliği pekiştirmek",
            "C) Yeni sömürgeler elde etmek",
            "D) Feodaliteyi kurmak",
            "E) Avrupa'ya göç etmek"
          ],
          "correct": 1,
          "solution": "Doğru cevap Bağımsızlık ve egemenliği pekiştirmek.",
          "id": "e3_q69",
          "no": 69
        },
        {
          "subject": "Tarih",
          "text": "Türk siyasi ve askerî tarihinde büyük öneme sahip olan 'Sivas Kongresi' süreci ile ilgili aşağıdakilerden hangisi söylenebilir? (H-60)",
          "options": [
            "A) Sadece ekonomik bir olaydır.",
            "B) Sivas Kongresi dönemin en kritik gelişmelerinden biridir.",
            "C) Osmanlı'nın kuruluş dönemine aittir.",
            "D) Avrupa'da gerçekleşmiştir.",
            "E) Hiçbir etkisi olmamıştır."
          ],
          "correct": 1,
          "solution": "Doğru cevap Sivas Kongresi dönemin en kritik gelişmelerinden biridir..",
          "id": "e3_q70",
          "no": 70
        },
        {
          "subject": "Tarih",
          "text": "Aşağıdaki tarihî gelişmelerden hangisi 'Erzurum Kongresi' ile doğrudan veya dolaylı olarak bağlantılıdır? (H-61)",
          "options": [
            "A) Sanayi İnkılabı",
            "B) Fransız İhtilali",
            "C) Kavimler Göçü",
            "D) Erzurum Kongresi öncesi ve sonrası yaşanan siyasi krizler.",
            "E) Coğrafi Keşifler"
          ],
          "correct": 3,
          "solution": "Doğru cevap Erzurum Kongresi öncesi ve sonrası yaşanan siyasi krizler..",
          "id": "e3_q71",
          "no": 71
        },
        {
          "subject": "Tarih",
          "text": "Millî Mücadele ve inkılaplar tarihi incelendiğinde 'Amasya Genelgesi' olayının temel amacı aşağıdakilerden hangisidir? (H-62)",
          "options": [
            "A) Yeni sömürgeler elde etmek",
            "B) Saltanatı güçlendirmek",
            "C) Feodaliteyi kurmak",
            "D) Avrupa'ya göç etmek",
            "E) Bağımsızlık ve egemenliği pekiştirmek"
          ],
          "correct": 4,
          "solution": "Doğru cevap Bağımsızlık ve egemenliği pekiştirmek.",
          "id": "e3_q72",
          "no": 72
        },
        {
          "subject": "Tarih",
          "text": "Türk siyasi ve askerî tarihinde büyük öneme sahip olan 'Lozan Antlaşması' süreci ile ilgili aşağıdakilerden hangisi söylenebilir? (H-63)",
          "options": [
            "A) Avrupa'da gerçekleşmiştir.",
            "B) Hiçbir etkisi olmamıştır.",
            "C) Sadece ekonomik bir olaydır.",
            "D) Lozan Antlaşması dönemin en kritik gelişmelerinden biridir.",
            "E) Osmanlı'nın kuruluş dönemine aittir."
          ],
          "correct": 3,
          "solution": "Doğru cevap Lozan Antlaşması dönemin en kritik gelişmelerinden biridir..",
          "id": "e3_q73",
          "no": 73
        },
        {
          "subject": "Tarih",
          "text": "Aşağıdaki tarihî gelişmelerden hangisi 'Cumhuriyetin İlanı' ile doğrudan veya dolaylı olarak bağlantılıdır? (H-64)",
          "options": [
            "A) Fransız İhtilali",
            "B) Coğrafi Keşifler",
            "C) Cumhuriyetin İlanı öncesi ve sonrası yaşanan siyasi krizler.",
            "D) Kavimler Göçü",
            "E) Sanayi İnkılabı"
          ],
          "correct": 2,
          "solution": "Doğru cevap Cumhuriyetin İlanı öncesi ve sonrası yaşanan siyasi krizler..",
          "id": "e3_q74",
          "no": 74
        },
        {
          "subject": "Tarih",
          "text": "Millî Mücadele ve inkılaplar tarihi incelendiğinde 'TBMM'nin Açılışı' olayının temel amacı aşağıdakilerden hangisidir? (H-65)",
          "options": [
            "A) Bağımsızlık ve egemenliği pekiştirmek",
            "B) Avrupa'ya göç etmek",
            "C) Feodaliteyi kurmak",
            "D) Saltanatı güçlendirmek",
            "E) Yeni sömürgeler elde etmek"
          ],
          "correct": 0,
          "solution": "Doğru cevap Bağımsızlık ve egemenliği pekiştirmek.",
          "id": "e3_q75",
          "no": 75
        },
        {
          "subject": "Tarih",
          "text": "Türk siyasi ve askerî tarihinde büyük öneme sahip olan 'Mudanya Mütarekesi' süreci ile ilgili aşağıdakilerden hangisi söylenebilir? (H-66)",
          "options": [
            "A) Avrupa'da gerçekleşmiştir.",
            "B) Sadece ekonomik bir olaydır.",
            "C) Osmanlı'nın kuruluş dönemine aittir.",
            "D) Hiçbir etkisi olmamıştır.",
            "E) Mudanya Mütarekesi dönemin en kritik gelişmelerinden biridir."
          ],
          "correct": 4,
          "solution": "Doğru cevap Mudanya Mütarekesi dönemin en kritik gelişmelerinden biridir..",
          "id": "e3_q76",
          "no": 76
        },
        {
          "subject": "Tarih",
          "text": "Aşağıdaki tarihî gelişmelerden hangisi 'Saltanatın Kaldırılması' ile doğrudan veya dolaylı olarak bağlantılıdır? (H-67)",
          "options": [
            "A) Coğrafi Keşifler",
            "B) Saltanatın Kaldırılması öncesi ve sonrası yaşanan siyasi krizler.",
            "C) Kavimler Göçü",
            "D) Sanayi İnkılabı",
            "E) Fransız İhtilali"
          ],
          "correct": 1,
          "solution": "Doğru cevap Saltanatın Kaldırılması öncesi ve sonrası yaşanan siyasi krizler..",
          "id": "e3_q77",
          "no": 77
        },
        {
          "subject": "Tarih",
          "text": "Millî Mücadele ve inkılaplar tarihi incelendiğinde 'Halifeliğin Kaldırılması' olayının temel amacı aşağıdakilerden hangisidir? (H-68)",
          "options": [
            "A) Bağımsızlık ve egemenliği pekiştirmek",
            "B) Feodaliteyi kurmak",
            "C) Saltanatı güçlendirmek",
            "D) Yeni sömürgeler elde etmek",
            "E) Avrupa'ya göç etmek"
          ],
          "correct": 0,
          "solution": "Doğru cevap Bağımsızlık ve egemenliği pekiştirmek.",
          "id": "e3_q78",
          "no": 78
        },
        {
          "subject": "Tarih",
          "text": "Türk siyasi ve askerî tarihinde büyük öneme sahip olan 'Tevhid-i Tedrisat' süreci ile ilgili aşağıdakilerden hangisi söylenebilir? (H-69)",
          "options": [
            "A) Osmanlı'nın kuruluş dönemine aittir.",
            "B) Tevhid-i Tedrisat dönemin en kritik gelişmelerinden biridir.",
            "C) Sadece ekonomik bir olaydır.",
            "D) Hiçbir etkisi olmamıştır.",
            "E) Avrupa'da gerçekleşmiştir."
          ],
          "correct": 1,
          "solution": "Doğru cevap Tevhid-i Tedrisat dönemin en kritik gelişmelerinden biridir..",
          "id": "e3_q79",
          "no": 79
        },
        {
          "subject": "Tarih",
          "text": "Aşağıdaki tarihî gelişmelerden hangisi 'Trablusgarp Savaşı' ile doğrudan veya dolaylı olarak bağlantılıdır? (H-70)",
          "options": [
            "A) Sanayi İnkılabı",
            "B) Fransız İhtilali",
            "C) Trablusgarp Savaşı öncesi ve sonrası yaşanan siyasi krizler.",
            "D) Coğrafi Keşifler",
            "E) Kavimler Göçü"
          ],
          "correct": 2,
          "solution": "Doğru cevap Trablusgarp Savaşı öncesi ve sonrası yaşanan siyasi krizler..",
          "id": "e3_q80",
          "no": 80
        },
        {
          "subject": "Tarih",
          "text": "Millî Mücadele ve inkılaplar tarihi incelendiğinde 'Balkan Savaşları' olayının temel amacı aşağıdakilerden hangisidir? (H-71)",
          "options": [
            "A) Bağımsızlık ve egemenliği pekiştirmek",
            "B) Yeni sömürgeler elde etmek",
            "C) Avrupa'ya göç etmek",
            "D) Saltanatı güçlendirmek",
            "E) Feodaliteyi kurmak"
          ],
          "correct": 0,
          "solution": "Doğru cevap Bağımsızlık ve egemenliği pekiştirmek.",
          "id": "e3_q81",
          "no": 81
        },
        {
          "subject": "Tarih",
          "text": "Türk siyasi ve askerî tarihinde büyük öneme sahip olan 'I. Dünya Savaşı' süreci ile ilgili aşağıdakilerden hangisi söylenebilir? (H-72)",
          "options": [
            "A) Hiçbir etkisi olmamıştır.",
            "B) I. Dünya Savaşı dönemin en kritik gelişmelerinden biridir.",
            "C) Avrupa'da gerçekleşmiştir.",
            "D) Osmanlı'nın kuruluş dönemine aittir.",
            "E) Sadece ekonomik bir olaydır."
          ],
          "correct": 1,
          "solution": "Doğru cevap I. Dünya Savaşı dönemin en kritik gelişmelerinden biridir..",
          "id": "e3_q82",
          "no": 82
        },
        {
          "subject": "Tarih",
          "text": "Aşağıdaki tarihî gelişmelerden hangisi 'Çanakkale Cephesi' ile doğrudan veya dolaylı olarak bağlantılıdır? (H-73)",
          "options": [
            "A) Çanakkale Cephesi öncesi ve sonrası yaşanan siyasi krizler.",
            "B) Coğrafi Keşifler",
            "C) Sanayi İnkılabı",
            "D) Fransız İhtilali",
            "E) Kavimler Göçü"
          ],
          "correct": 0,
          "solution": "Doğru cevap Çanakkale Cephesi öncesi ve sonrası yaşanan siyasi krizler..",
          "id": "e3_q83",
          "no": 83
        },
        {
          "subject": "Tarih",
          "text": "Millî Mücadele ve inkılaplar tarihi incelendiğinde 'Sakarya Meydan Muharebesi' olayının temel amacı aşağıdakilerden hangisidir? (H-74)",
          "options": [
            "A) Yeni sömürgeler elde etmek",
            "B) Bağımsızlık ve egemenliği pekiştirmek",
            "C) Saltanatı güçlendirmek",
            "D) Avrupa'ya göç etmek",
            "E) Feodaliteyi kurmak"
          ],
          "correct": 1,
          "solution": "Doğru cevap Bağımsızlık ve egemenliği pekiştirmek.",
          "id": "e3_q84",
          "no": 84
        },
        {
          "subject": "Tarih",
          "text": "Türk siyasi ve askerî tarihinde büyük öneme sahip olan 'Büyük Taarruz' süreci ile ilgili aşağıdakilerden hangisi söylenebilir? (H-75)",
          "options": [
            "A) Büyük Taarruz dönemin en kritik gelişmelerinden biridir.",
            "B) Sadece ekonomik bir olaydır.",
            "C) Osmanlı'nın kuruluş dönemine aittir.",
            "D) Hiçbir etkisi olmamıştır.",
            "E) Avrupa'da gerçekleşmiştir."
          ],
          "correct": 0,
          "solution": "Doğru cevap Büyük Taarruz dönemin en kritik gelişmelerinden biridir..",
          "id": "e3_q85",
          "no": 85
        },
        {
          "subject": "Tarih",
          "text": "Aşağıdaki tarihî gelişmelerden hangisi 'I. İnönü Muharebesi' ile doğrudan veya dolaylı olarak bağlantılıdır? (H-76)",
          "options": [
            "A) I. İnönü Muharebesi öncesi ve sonrası yaşanan siyasi krizler.",
            "B) Kavimler Göçü",
            "C) Sanayi İnkılabı",
            "D) Fransız İhtilali",
            "E) Coğrafi Keşifler"
          ],
          "correct": 0,
          "solution": "Doğru cevap I. İnönü Muharebesi öncesi ve sonrası yaşanan siyasi krizler..",
          "id": "e3_q86",
          "no": 86
        },
        {
          "subject": "Tarih",
          "text": "Millî Mücadele ve inkılaplar tarihi incelendiğinde 'II. İnönü Muharebesi' olayının temel amacı aşağıdakilerden hangisidir? (H-77)",
          "options": [
            "A) Feodaliteyi kurmak",
            "B) Yeni sömürgeler elde etmek",
            "C) Saltanatı güçlendirmek",
            "D) Avrupa'ya göç etmek",
            "E) Bağımsızlık ve egemenliği pekiştirmek"
          ],
          "correct": 4,
          "solution": "Doğru cevap Bağımsızlık ve egemenliği pekiştirmek.",
          "id": "e3_q87",
          "no": 87
        },
        {
          "subject": "Coğrafya",
          "text": "Türkiye'nin fiziki coğrafyası düşünüldüğünde 'Tuz Gölü' için aşağıdakilerden hangisi doğrudur? (C-34)",
          "options": [
            "A) Tuz Gölü bir çöldür.",
            "B) Tuz Gölü, ülkemizin önemli yeryüzü şekillerinden biridir.",
            "C) Tuz Gölü tarıma kapalıdır.",
            "D) Tuz Gölü Marmara'dadır.",
            "E) Tuz Gölü yapay bir kanaldır."
          ],
          "correct": 1,
          "solution": "Doğru cevap Tuz Gölü, ülkemizin önemli yeryüzü şekillerinden biridir..",
          "id": "e3_q88",
          "no": 88
        },
        {
          "subject": "Coğrafya",
          "text": "Coğrafi özellikleri ve turizm potansiyeli göz önüne alındığında 'Çukurova' hangi alanda daha çok öne çıkar? (C-35)",
          "options": [
            "A) Sadece madencilik",
            "B) Okyanus balıkçılığı",
            "C) Sadece ağır sanayi",
            "D) Çöl iklimi araştırmaları",
            "E) Doğal güzellikleri ve turizm/coğrafi önemi"
          ],
          "correct": 4,
          "solution": "Doğru cevap Doğal güzellikleri ve turizm/coğrafi önemi.",
          "id": "e3_q89",
          "no": 89
        },
        {
          "subject": "Coğrafya",
          "text": "Türkiye'nin fiziki coğrafyası düşünüldüğünde 'Bafra Ovası' için aşağıdakilerden hangisi doğrudur? (C-36)",
          "options": [
            "A) Bafra Ovası yapay bir kanaldır.",
            "B) Bafra Ovası bir çöldür.",
            "C) Bafra Ovası Marmara'dadır.",
            "D) Bafra Ovası, ülkemizin önemli yeryüzü şekillerinden biridir.",
            "E) Bafra Ovası tarıma kapalıdır."
          ],
          "correct": 3,
          "solution": "Doğru cevap Bafra Ovası, ülkemizin önemli yeryüzü şekillerinden biridir..",
          "id": "e3_q90",
          "no": 90
        },
        {
          "subject": "Coğrafya",
          "text": "Coğrafi özellikleri ve turizm potansiyeli göz önüne alındığında 'Kaçkar Dağları' hangi alanda daha çok öne çıkar? (C-37)",
          "options": [
            "A) Doğal güzellikleri ve turizm/coğrafi önemi",
            "B) Çöl iklimi araştırmaları",
            "C) Okyanus balıkçılığı",
            "D) Sadece madencilik",
            "E) Sadece ağır sanayi"
          ],
          "correct": 0,
          "solution": "Doğru cevap Doğal güzellikleri ve turizm/coğrafi önemi.",
          "id": "e3_q91",
          "no": 91
        },
        {
          "subject": "Coğrafya",
          "text": "Türkiye'nin fiziki coğrafyası düşünüldüğünde 'Gediz Nehri' için aşağıdakilerden hangisi doğrudur? (C-38)",
          "options": [
            "A) Gediz Nehri Marmara'dadır.",
            "B) Gediz Nehri, ülkemizin önemli yeryüzü şekillerinden biridir.",
            "C) Gediz Nehri tarıma kapalıdır.",
            "D) Gediz Nehri yapay bir kanaldır.",
            "E) Gediz Nehri bir çöldür."
          ],
          "correct": 1,
          "solution": "Doğru cevap Gediz Nehri, ülkemizin önemli yeryüzü şekillerinden biridir..",
          "id": "e3_q92",
          "no": 92
        },
        {
          "subject": "Coğrafya",
          "text": "Coğrafi özellikleri ve turizm potansiyeli göz önüne alındığında 'Salda Gölü' hangi alanda daha çok öne çıkar? (C-39)",
          "options": [
            "A) Sadece ağır sanayi",
            "B) Okyanus balıkçılığı",
            "C) Doğal güzellikleri ve turizm/coğrafi önemi",
            "D) Çöl iklimi araştırmaları",
            "E) Sadece madencilik"
          ],
          "correct": 2,
          "solution": "Doğru cevap Doğal güzellikleri ve turizm/coğrafi önemi.",
          "id": "e3_q93",
          "no": 93
        },
        {
          "subject": "Coğrafya",
          "text": "Türkiye'nin fiziki coğrafyası düşünüldüğünde 'Kapadokya' için aşağıdakilerden hangisi doğrudur? (C-40)",
          "options": [
            "A) Kapadokya tarıma kapalıdır.",
            "B) Kapadokya yapay bir kanaldır.",
            "C) Kapadokya bir çöldür.",
            "D) Kapadokya Marmara'dadır.",
            "E) Kapadokya, ülkemizin önemli yeryüzü şekillerinden biridir."
          ],
          "correct": 4,
          "solution": "Doğru cevap Kapadokya, ülkemizin önemli yeryüzü şekillerinden biridir..",
          "id": "e3_q94",
          "no": 94
        },
        {
          "subject": "Coğrafya",
          "text": "Coğrafi özellikleri ve turizm potansiyeli göz önüne alındığında 'Pamukkale' hangi alanda daha çok öne çıkar? (C-41)",
          "options": [
            "A) Sadece ağır sanayi",
            "B) Sadece madencilik",
            "C) Okyanus balıkçılığı",
            "D) Doğal güzellikleri ve turizm/coğrafi önemi",
            "E) Çöl iklimi araştırmaları"
          ],
          "correct": 3,
          "solution": "Doğru cevap Doğal güzellikleri ve turizm/coğrafi önemi.",
          "id": "e3_q95",
          "no": 95
        },
        {
          "subject": "Coğrafya",
          "text": "Türkiye'nin fiziki coğrafyası düşünüldüğünde 'Nemrut Dağı' için aşağıdakilerden hangisi doğrudur? (C-42)",
          "options": [
            "A) Nemrut Dağı, ülkemizin önemli yeryüzü şekillerinden biridir.",
            "B) Nemrut Dağı Marmara'dadır.",
            "C) Nemrut Dağı bir çöldür.",
            "D) Nemrut Dağı yapay bir kanaldır.",
            "E) Nemrut Dağı tarıma kapalıdır."
          ],
          "correct": 0,
          "solution": "Doğru cevap Nemrut Dağı, ülkemizin önemli yeryüzü şekillerinden biridir..",
          "id": "e3_q96",
          "no": 96
        },
        {
          "subject": "Coğrafya",
          "text": "Coğrafi özellikleri ve turizm potansiyeli göz önüne alındığında 'Sümela Manastırı' hangi alanda daha çok öne çıkar? (C-43)",
          "options": [
            "A) Okyanus balıkçılığı",
            "B) Sadece ağır sanayi",
            "C) Sadece madencilik",
            "D) Çöl iklimi araştırmaları",
            "E) Doğal güzellikleri ve turizm/coğrafi önemi"
          ],
          "correct": 4,
          "solution": "Doğru cevap Doğal güzellikleri ve turizm/coğrafi önemi.",
          "id": "e3_q97",
          "no": 97
        },
        {
          "subject": "Coğrafya",
          "text": "Türkiye'nin fiziki coğrafyası düşünüldüğünde 'Uludağ' için aşağıdakilerden hangisi doğrudur? (C-44)",
          "options": [
            "A) Uludağ Marmara'dadır.",
            "B) Uludağ, ülkemizin önemli yeryüzü şekillerinden biridir.",
            "C) Uludağ tarıma kapalıdır.",
            "D) Uludağ yapay bir kanaldır.",
            "E) Uludağ bir çöldür."
          ],
          "correct": 1,
          "solution": "Doğru cevap Uludağ, ülkemizin önemli yeryüzü şekillerinden biridir..",
          "id": "e3_q98",
          "no": 98
        },
        {
          "subject": "Coğrafya",
          "text": "Coğrafi özellikleri ve turizm potansiyeli göz önüne alındığında 'Van Gölü' hangi alanda daha çok öne çıkar? (C-45)",
          "options": [
            "A) Çöl iklimi araştırmaları",
            "B) Sadece madencilik",
            "C) Sadece ağır sanayi",
            "D) Doğal güzellikleri ve turizm/coğrafi önemi",
            "E) Okyanus balıkçılığı"
          ],
          "correct": 3,
          "solution": "Doğru cevap Doğal güzellikleri ve turizm/coğrafi önemi.",
          "id": "e3_q99",
          "no": 99
        },
        {
          "subject": "Coğrafya",
          "text": "Türkiye'nin fiziki coğrafyası düşünüldüğünde 'Ağrı Dağı' için aşağıdakilerden hangisi doğrudur? (C-46)",
          "options": [
            "A) Ağrı Dağı yapay bir kanaldır.",
            "B) Ağrı Dağı tarıma kapalıdır.",
            "C) Ağrı Dağı bir çöldür.",
            "D) Ağrı Dağı Marmara'dadır.",
            "E) Ağrı Dağı, ülkemizin önemli yeryüzü şekillerinden biridir."
          ],
          "correct": 4,
          "solution": "Doğru cevap Ağrı Dağı, ülkemizin önemli yeryüzü şekillerinden biridir..",
          "id": "e3_q100",
          "no": 100
        },
        {
          "subject": "Coğrafya",
          "text": "Coğrafi özellikleri ve turizm potansiyeli göz önüne alındığında 'Kızılırmak' hangi alanda daha çok öne çıkar? (C-47)",
          "options": [
            "A) Doğal güzellikleri ve turizm/coğrafi önemi",
            "B) Sadece ağır sanayi",
            "C) Sadece madencilik",
            "D) Okyanus balıkçılığı",
            "E) Çöl iklimi araştırmaları"
          ],
          "correct": 0,
          "solution": "Doğru cevap Doğal güzellikleri ve turizm/coğrafi önemi.",
          "id": "e3_q101",
          "no": 101
        },
        {
          "subject": "Coğrafya",
          "text": "Türkiye'nin fiziki coğrafyası düşünüldüğünde 'Erciyes Dağı' için aşağıdakilerden hangisi doğrudur? (C-48)",
          "options": [
            "A) Erciyes Dağı, ülkemizin önemli yeryüzü şekillerinden biridir.",
            "B) Erciyes Dağı Marmara'dadır.",
            "C) Erciyes Dağı yapay bir kanaldır.",
            "D) Erciyes Dağı bir çöldür.",
            "E) Erciyes Dağı tarıma kapalıdır."
          ],
          "correct": 0,
          "solution": "Doğru cevap Erciyes Dağı, ülkemizin önemli yeryüzü şekillerinden biridir..",
          "id": "e3_q102",
          "no": 102
        },
        {
          "subject": "Coğrafya",
          "text": "Coğrafi özellikleri ve turizm potansiyeli göz önüne alındığında 'Tuz Gölü' hangi alanda daha çok öne çıkar? (C-49)",
          "options": [
            "A) Çöl iklimi araştırmaları",
            "B) Sadece ağır sanayi",
            "C) Sadece madencilik",
            "D) Okyanus balıkçılığı",
            "E) Doğal güzellikleri ve turizm/coğrafi önemi"
          ],
          "correct": 4,
          "solution": "Doğru cevap Doğal güzellikleri ve turizm/coğrafi önemi.",
          "id": "e3_q103",
          "no": 103
        },
        {
          "subject": "Coğrafya",
          "text": "Türkiye'nin fiziki coğrafyası düşünüldüğünde 'Çukurova' için aşağıdakilerden hangisi doğrudur? (C-50)",
          "options": [
            "A) Çukurova Marmara'dadır.",
            "B) Çukurova bir çöldür.",
            "C) Çukurova, ülkemizin önemli yeryüzü şekillerinden biridir.",
            "D) Çukurova yapay bir kanaldır.",
            "E) Çukurova tarıma kapalıdır."
          ],
          "correct": 2,
          "solution": "Doğru cevap Çukurova, ülkemizin önemli yeryüzü şekillerinden biridir..",
          "id": "e3_q104",
          "no": 104
        },
        {
          "subject": "Coğrafya",
          "text": "Coğrafi özellikleri ve turizm potansiyeli göz önüne alındığında 'Bafra Ovası' hangi alanda daha çok öne çıkar? (C-51)",
          "options": [
            "A) Okyanus balıkçılığı",
            "B) Sadece madencilik",
            "C) Sadece ağır sanayi",
            "D) Çöl iklimi araştırmaları",
            "E) Doğal güzellikleri ve turizm/coğrafi önemi"
          ],
          "correct": 4,
          "solution": "Doğru cevap Doğal güzellikleri ve turizm/coğrafi önemi.",
          "id": "e3_q105",
          "no": 105
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'Danıştay' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-28)",
          "options": [
            "A) Danıştay yasaklanmıştır.",
            "B) Danıştay, anayasal sistemin önemli bir parçasıdır.",
            "C) Danıştay sadece köylerde bulunur.",
            "D) Danıştay yabancı bir kurumdur.",
            "E) Danıştay özel bir şirkettir."
          ],
          "correct": 1,
          "solution": "Doğru cevap Danıştay, anayasal sistemin önemli bir parçasıdır..",
          "id": "e3_q106",
          "no": 106
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'TBMM' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-29)",
          "options": [
            "A) TBMM, anayasal sistemin önemli bir parçasıdır.",
            "B) TBMM sadece köylerde bulunur.",
            "C) TBMM özel bir şirkettir.",
            "D) TBMM yabancı bir kurumdur.",
            "E) TBMM yasaklanmıştır."
          ],
          "correct": 0,
          "solution": "Doğru cevap TBMM, anayasal sistemin önemli bir parçasıdır..",
          "id": "e3_q107",
          "no": 107
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'Cumhurbaşkanlığı' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-30)",
          "options": [
            "A) Cumhurbaşkanlığı yasaklanmıştır.",
            "B) Cumhurbaşkanlığı özel bir şirkettir.",
            "C) Cumhurbaşkanlığı yabancı bir kurumdur.",
            "D) Cumhurbaşkanlığı, anayasal sistemin önemli bir parçasıdır.",
            "E) Cumhurbaşkanlığı sadece köylerde bulunur."
          ],
          "correct": 3,
          "solution": "Doğru cevap Cumhurbaşkanlığı, anayasal sistemin önemli bir parçasıdır..",
          "id": "e3_q108",
          "no": 108
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'Sayıştay' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-31)",
          "options": [
            "A) Sayıştay özel bir şirkettir.",
            "B) Sayıştay sadece köylerde bulunur.",
            "C) Sayıştay, anayasal sistemin önemli bir parçasıdır.",
            "D) Sayıştay yasaklanmıştır.",
            "E) Sayıştay yabancı bir kurumdur."
          ],
          "correct": 2,
          "solution": "Doğru cevap Sayıştay, anayasal sistemin önemli bir parçasıdır..",
          "id": "e3_q109",
          "no": 109
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'YSK' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-32)",
          "options": [
            "A) YSK sadece köylerde bulunur.",
            "B) YSK, anayasal sistemin önemli bir parçasıdır.",
            "C) YSK yabancı bir kurumdur.",
            "D) YSK özel bir şirkettir.",
            "E) YSK yasaklanmıştır."
          ],
          "correct": 1,
          "solution": "Doğru cevap YSK, anayasal sistemin önemli bir parçasıdır..",
          "id": "e3_q110",
          "no": 110
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'HSK' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-33)",
          "options": [
            "A) HSK sadece köylerde bulunur.",
            "B) HSK özel bir şirkettir.",
            "C) HSK, anayasal sistemin önemli bir parçasıdır.",
            "D) HSK yabancı bir kurumdur.",
            "E) HSK yasaklanmıştır."
          ],
          "correct": 2,
          "solution": "Doğru cevap HSK, anayasal sistemin önemli bir parçasıdır..",
          "id": "e3_q111",
          "no": 111
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'Belediye' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-34)",
          "options": [
            "A) Belediye özel bir şirkettir.",
            "B) Belediye sadece köylerde bulunur.",
            "C) Belediye, anayasal sistemin önemli bir parçasıdır.",
            "D) Belediye yasaklanmıştır.",
            "E) Belediye yabancı bir kurumdur."
          ],
          "correct": 2,
          "solution": "Doğru cevap Belediye, anayasal sistemin önemli bir parçasıdır..",
          "id": "e3_q112",
          "no": 112
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'Valilik' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-35)",
          "options": [
            "A) Valilik sadece köylerde bulunur.",
            "B) Valilik yabancı bir kurumdur.",
            "C) Valilik yasaklanmıştır.",
            "D) Valilik, anayasal sistemin önemli bir parçasıdır.",
            "E) Valilik özel bir şirkettir."
          ],
          "correct": 3,
          "solution": "Doğru cevap Valilik, anayasal sistemin önemli bir parçasıdır..",
          "id": "e3_q113",
          "no": 113
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'Kaymakamlık' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-36)",
          "options": [
            "A) Kaymakamlık, anayasal sistemin önemli bir parçasıdır.",
            "B) Kaymakamlık yasaklanmıştır.",
            "C) Kaymakamlık sadece köylerde bulunur.",
            "D) Kaymakamlık özel bir şirkettir.",
            "E) Kaymakamlık yabancı bir kurumdur."
          ],
          "correct": 0,
          "solution": "Doğru cevap Kaymakamlık, anayasal sistemin önemli bir parçasıdır..",
          "id": "e3_q114",
          "no": 114
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'İl Genel Meclisi' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-37)",
          "options": [
            "A) İl Genel Meclisi yasaklanmıştır.",
            "B) İl Genel Meclisi yabancı bir kurumdur.",
            "C) İl Genel Meclisi özel bir şirkettir.",
            "D) İl Genel Meclisi, anayasal sistemin önemli bir parçasıdır.",
            "E) İl Genel Meclisi sadece köylerde bulunur."
          ],
          "correct": 3,
          "solution": "Doğru cevap İl Genel Meclisi, anayasal sistemin önemli bir parçasıdır..",
          "id": "e3_q115",
          "no": 115
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'Kamu Denetçiliği Kurumu' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-38)",
          "options": [
            "A) Kamu Denetçiliği Kurumu yasaklanmıştır.",
            "B) Kamu Denetçiliği Kurumu özel bir şirkettir.",
            "C) Kamu Denetçiliği Kurumu yabancı bir kurumdur.",
            "D) Kamu Denetçiliği Kurumu sadece köylerde bulunur.",
            "E) Kamu Denetçiliği Kurumu, anayasal sistemin önemli bir parçasıdır."
          ],
          "correct": 4,
          "solution": "Doğru cevap Kamu Denetçiliği Kurumu, anayasal sistemin önemli bir parçasıdır..",
          "id": "e3_q116",
          "no": 116
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'Anayasa Mahkemesi' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-39)",
          "options": [
            "A) Anayasa Mahkemesi sadece köylerde bulunur.",
            "B) Anayasa Mahkemesi özel bir şirkettir.",
            "C) Anayasa Mahkemesi yasaklanmıştır.",
            "D) Anayasa Mahkemesi yabancı bir kurumdur.",
            "E) Anayasa Mahkemesi, anayasal sistemin önemli bir parçasıdır."
          ],
          "correct": 4,
          "solution": "Doğru cevap Anayasa Mahkemesi, anayasal sistemin önemli bir parçasıdır..",
          "id": "e3_q117",
          "no": 117
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'Yargıtay' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-40)",
          "options": [
            "A) Yargıtay yasaklanmıştır.",
            "B) Yargıtay yabancı bir kurumdur.",
            "C) Yargıtay özel bir şirkettir.",
            "D) Yargıtay, anayasal sistemin önemli bir parçasıdır.",
            "E) Yargıtay sadece köylerde bulunur."
          ],
          "correct": 3,
          "solution": "Doğru cevap Yargıtay, anayasal sistemin önemli bir parçasıdır..",
          "id": "e3_q118",
          "no": 118
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'Danıştay' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-41)",
          "options": [
            "A) Danıştay yasaklanmıştır.",
            "B) Danıştay, anayasal sistemin önemli bir parçasıdır.",
            "C) Danıştay sadece köylerde bulunur.",
            "D) Danıştay özel bir şirkettir.",
            "E) Danıştay yabancı bir kurumdur."
          ],
          "correct": 1,
          "solution": "Doğru cevap Danıştay, anayasal sistemin önemli bir parçasıdır..",
          "id": "e3_q119",
          "no": 119
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'TBMM' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-42)",
          "options": [
            "A) TBMM yabancı bir kurumdur.",
            "B) TBMM, anayasal sistemin önemli bir parçasıdır.",
            "C) TBMM yasaklanmıştır.",
            "D) TBMM özel bir şirkettir.",
            "E) TBMM sadece köylerde bulunur."
          ],
          "correct": 1,
          "solution": "Doğru cevap TBMM, anayasal sistemin önemli bir parçasıdır..",
          "id": "e3_q120",
          "no": 120
        }
      ]
    },
    {
      "id": "deneme_4",
      "name": "4. Deneme Sınavı",
      "totalQuestions": 120,
      "duration": 130,
      "distribution": {
        "Türkçe": 30,
        "Matematik": 30,
        "Tarih": 27,
        "Coğrafya": 18,
        "Vatandaşlık": 15
      },
      "questions": [
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde 'bugün' kelimesinin yazımıyla ilgili bir kural hatırlatılmaktadır? (T-85)",
          "options": [
            "A) bugün kelimesi fiildir.",
            "B) 'bugün' kelimesinin doğru yazımına dikkat edilmelidir.",
            "C) bugün kelimesi yabancı kökenlidir.",
            "D) bugün cümlede özne olamaz.",
            "E) bugün kelimesi her zaman ayrı yazılır."
          ],
          "correct": 1,
          "solution": "Doğru cevap 'bugün' kelimesinin doğru yazımına dikkat edilmelidir..",
          "id": "e4_q1",
          "no": 1
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde mecaz anlamlı bir sözcük kullanılmıştır? (T-86)",
          "options": [
            "A) Suyu dolaptan soğuk içti.",
            "B) Buzdolabı soğuk üflüyor.",
            "C) Olaylara karşı çok 'soğuk' davranıyordu.",
            "D) Hava bugün çok soğuk.",
            "E) Kışın havalar soğuk olur."
          ],
          "correct": 2,
          "solution": "Doğru cevap Olaylara karşı çok 'soğuk' davranıyordu..",
          "id": "e4_q2",
          "no": 2
        },
        {
          "subject": "Türkçe",
          "text": "Bilim tarih boyunca insanlığın en büyük rehberlerinden biri olmuştur. Toplumlar Bilim sayesinde sınırlarını aşmış, geleceğe umutla bakabilmiştir. (P-87)\nBu parçanın ana düşüncesi nedir?",
          "options": [
            "A) Bilim sadece bireyseldir.",
            "B) Bilim, toplumsal ilerleme ve vizyon için vazgeçilmezdir.",
            "C) Bilim sadece geçmişte kalmıştır.",
            "D) Bilim zaman kaybıdır.",
            "E) İnsanlar Bilim ile ilgilenmemelidir."
          ],
          "correct": 1,
          "solution": "Doğru cevap Bilim, toplumsal ilerleme ve vizyon için vazgeçilmezdir..",
          "id": "e4_q3",
          "no": 3
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde 'yalnız' kelimesinin yazımıyla ilgili bir kural hatırlatılmaktadır? (T-88)",
          "options": [
            "A) yalnız kelimesi fiildir.",
            "B) 'yalnız' kelimesinin doğru yazımına dikkat edilmelidir.",
            "C) yalnız kelimesi yabancı kökenlidir.",
            "D) yalnız kelimesi her zaman ayrı yazılır.",
            "E) yalnız cümlede özne olamaz."
          ],
          "correct": 1,
          "solution": "Doğru cevap 'yalnız' kelimesinin doğru yazımına dikkat edilmelidir..",
          "id": "e4_q4",
          "no": 4
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde mecaz anlamlı bir sözcük kullanılmıştır? (T-89)",
          "options": [
            "A) Suyu dolaptan soğuk içti.",
            "B) Kışın havalar soğuk olur.",
            "C) Olaylara karşı çok 'soğuk' davranıyordu.",
            "D) Buzdolabı soğuk üflüyor.",
            "E) Hava bugün çok soğuk."
          ],
          "correct": 2,
          "solution": "Doğru cevap Olaylara karşı çok 'soğuk' davranıyordu..",
          "id": "e4_q5",
          "no": 5
        },
        {
          "subject": "Türkçe",
          "text": "Sanat tarih boyunca insanlığın en büyük rehberlerinden biri olmuştur. Toplumlar Sanat sayesinde sınırlarını aşmış, geleceğe umutla bakabilmiştir. (P-90)\nBu parçanın ana düşüncesi nedir?",
          "options": [
            "A) Sanat, toplumsal ilerleme ve vizyon için vazgeçilmezdir.",
            "B) Sanat sadece geçmişte kalmıştır.",
            "C) Sanat sadece bireyseldir.",
            "D) Sanat zaman kaybıdır.",
            "E) İnsanlar Sanat ile ilgilenmemelidir."
          ],
          "correct": 0,
          "solution": "Doğru cevap Sanat, toplumsal ilerleme ve vizyon için vazgeçilmezdir..",
          "id": "e4_q6",
          "no": 6
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde 'hiçbir' kelimesinin yazımıyla ilgili bir kural hatırlatılmaktadır? (T-91)",
          "options": [
            "A) 'hiçbir' kelimesinin doğru yazımına dikkat edilmelidir.",
            "B) hiçbir kelimesi fiildir.",
            "C) hiçbir kelimesi her zaman ayrı yazılır.",
            "D) hiçbir kelimesi yabancı kökenlidir.",
            "E) hiçbir cümlede özne olamaz."
          ],
          "correct": 0,
          "solution": "Doğru cevap 'hiçbir' kelimesinin doğru yazımına dikkat edilmelidir..",
          "id": "e4_q7",
          "no": 7
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde mecaz anlamlı bir sözcük kullanılmıştır? (T-92)",
          "options": [
            "A) Suyu dolaptan soğuk içti.",
            "B) Buzdolabı soğuk üflüyor.",
            "C) Kışın havalar soğuk olur.",
            "D) Olaylara karşı çok 'soğuk' davranıyordu.",
            "E) Hava bugün çok soğuk."
          ],
          "correct": 3,
          "solution": "Doğru cevap Olaylara karşı çok 'soğuk' davranıyordu..",
          "id": "e4_q8",
          "no": 8
        },
        {
          "subject": "Türkçe",
          "text": "Teknoloji tarih boyunca insanlığın en büyük rehberlerinden biri olmuştur. Toplumlar Teknoloji sayesinde sınırlarını aşmış, geleceğe umutla bakabilmiştir. (P-93)\nBu parçanın ana düşüncesi nedir?",
          "options": [
            "A) Teknoloji zaman kaybıdır.",
            "B) Teknoloji sadece geçmişte kalmıştır.",
            "C) Teknoloji, toplumsal ilerleme ve vizyon için vazgeçilmezdir.",
            "D) Teknoloji sadece bireyseldir.",
            "E) İnsanlar Teknoloji ile ilgilenmemelidir."
          ],
          "correct": 2,
          "solution": "Doğru cevap Teknoloji, toplumsal ilerleme ve vizyon için vazgeçilmezdir..",
          "id": "e4_q9",
          "no": 9
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde 'her şey' kelimesinin yazımıyla ilgili bir kural hatırlatılmaktadır? (T-94)",
          "options": [
            "A) her şey kelimesi fiildir.",
            "B) her şey cümlede özne olamaz.",
            "C) 'her şey' kelimesinin doğru yazımına dikkat edilmelidir.",
            "D) her şey kelimesi yabancı kökenlidir.",
            "E) her şey kelimesi her zaman ayrı yazılır."
          ],
          "correct": 2,
          "solution": "Doğru cevap 'her şey' kelimesinin doğru yazımına dikkat edilmelidir..",
          "id": "e4_q10",
          "no": 10
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde mecaz anlamlı bir sözcük kullanılmıştır? (T-95)",
          "options": [
            "A) Hava bugün çok soğuk.",
            "B) Kışın havalar soğuk olur.",
            "C) Buzdolabı soğuk üflüyor.",
            "D) Olaylara karşı çok 'soğuk' davranıyordu.",
            "E) Suyu dolaptan soğuk içti."
          ],
          "correct": 3,
          "solution": "Doğru cevap Olaylara karşı çok 'soğuk' davranıyordu..",
          "id": "e4_q11",
          "no": 11
        },
        {
          "subject": "Türkçe",
          "text": "Doğa tarih boyunca insanlığın en büyük rehberlerinden biri olmuştur. Toplumlar Doğa sayesinde sınırlarını aşmış, geleceğe umutla bakabilmiştir. (P-96)\nBu parçanın ana düşüncesi nedir?",
          "options": [
            "A) Doğa sadece bireyseldir.",
            "B) İnsanlar Doğa ile ilgilenmemelidir.",
            "C) Doğa zaman kaybıdır.",
            "D) Doğa, toplumsal ilerleme ve vizyon için vazgeçilmezdir.",
            "E) Doğa sadece geçmişte kalmıştır."
          ],
          "correct": 3,
          "solution": "Doğru cevap Doğa, toplumsal ilerleme ve vizyon için vazgeçilmezdir..",
          "id": "e4_q12",
          "no": 12
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde 'yanlış' kelimesinin yazımıyla ilgili bir kural hatırlatılmaktadır? (T-97)",
          "options": [
            "A) 'yanlış' kelimesinin doğru yazımına dikkat edilmelidir.",
            "B) yanlış kelimesi her zaman ayrı yazılır.",
            "C) yanlış cümlede özne olamaz.",
            "D) yanlış kelimesi yabancı kökenlidir.",
            "E) yanlış kelimesi fiildir."
          ],
          "correct": 0,
          "solution": "Doğru cevap 'yanlış' kelimesinin doğru yazımına dikkat edilmelidir..",
          "id": "e4_q13",
          "no": 13
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde mecaz anlamlı bir sözcük kullanılmıştır? (T-98)",
          "options": [
            "A) Kışın havalar soğuk olur.",
            "B) Olaylara karşı çok 'soğuk' davranıyordu.",
            "C) Suyu dolaptan soğuk içti.",
            "D) Hava bugün çok soğuk.",
            "E) Buzdolabı soğuk üflüyor."
          ],
          "correct": 1,
          "solution": "Doğru cevap Olaylara karşı çok 'soğuk' davranıyordu..",
          "id": "e4_q14",
          "no": 14
        },
        {
          "subject": "Türkçe",
          "text": "Psikoloji tarih boyunca insanlığın en büyük rehberlerinden biri olmuştur. Toplumlar Psikoloji sayesinde sınırlarını aşmış, geleceğe umutla bakabilmiştir. (P-99)\nBu parçanın ana düşüncesi nedir?",
          "options": [
            "A) Psikoloji zaman kaybıdır.",
            "B) Psikoloji sadece geçmişte kalmıştır.",
            "C) İnsanlar Psikoloji ile ilgilenmemelidir.",
            "D) Psikoloji sadece bireyseldir.",
            "E) Psikoloji, toplumsal ilerleme ve vizyon için vazgeçilmezdir."
          ],
          "correct": 4,
          "solution": "Doğru cevap Psikoloji, toplumsal ilerleme ve vizyon için vazgeçilmezdir..",
          "id": "e4_q15",
          "no": 15
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde 'birkaç' kelimesinin yazımıyla ilgili bir kural hatırlatılmaktadır? (T-100)",
          "options": [
            "A) birkaç kelimesi her zaman ayrı yazılır.",
            "B) birkaç cümlede özne olamaz.",
            "C) 'birkaç' kelimesinin doğru yazımına dikkat edilmelidir.",
            "D) birkaç kelimesi fiildir.",
            "E) birkaç kelimesi yabancı kökenlidir."
          ],
          "correct": 2,
          "solution": "Doğru cevap 'birkaç' kelimesinin doğru yazımına dikkat edilmelidir..",
          "id": "e4_q16",
          "no": 16
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde mecaz anlamlı bir sözcük kullanılmıştır? (T-101)",
          "options": [
            "A) Hava bugün çok soğuk.",
            "B) Kışın havalar soğuk olur.",
            "C) Olaylara karşı çok 'soğuk' davranıyordu.",
            "D) Suyu dolaptan soğuk içti.",
            "E) Buzdolabı soğuk üflüyor."
          ],
          "correct": 2,
          "solution": "Doğru cevap Olaylara karşı çok 'soğuk' davranıyordu..",
          "id": "e4_q17",
          "no": 17
        },
        {
          "subject": "Türkçe",
          "text": "Eğitim tarih boyunca insanlığın en büyük rehberlerinden biri olmuştur. Toplumlar Eğitim sayesinde sınırlarını aşmış, geleceğe umutla bakabilmiştir. (P-102)\nBu parçanın ana düşüncesi nedir?",
          "options": [
            "A) İnsanlar Eğitim ile ilgilenmemelidir.",
            "B) Eğitim, toplumsal ilerleme ve vizyon için vazgeçilmezdir.",
            "C) Eğitim sadece geçmişte kalmıştır.",
            "D) Eğitim zaman kaybıdır.",
            "E) Eğitim sadece bireyseldir."
          ],
          "correct": 1,
          "solution": "Doğru cevap Eğitim, toplumsal ilerleme ve vizyon için vazgeçilmezdir..",
          "id": "e4_q18",
          "no": 18
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde 'hiç kimse' kelimesinin yazımıyla ilgili bir kural hatırlatılmaktadır? (T-103)",
          "options": [
            "A) hiç kimse kelimesi fiildir.",
            "B) 'hiç kimse' kelimesinin doğru yazımına dikkat edilmelidir.",
            "C) hiç kimse kelimesi yabancı kökenlidir.",
            "D) hiç kimse cümlede özne olamaz.",
            "E) hiç kimse kelimesi her zaman ayrı yazılır."
          ],
          "correct": 1,
          "solution": "Doğru cevap 'hiç kimse' kelimesinin doğru yazımına dikkat edilmelidir..",
          "id": "e4_q19",
          "no": 19
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde mecaz anlamlı bir sözcük kullanılmıştır? (T-104)",
          "options": [
            "A) Suyu dolaptan soğuk içti.",
            "B) Buzdolabı soğuk üflüyor.",
            "C) Hava bugün çok soğuk.",
            "D) Kışın havalar soğuk olur.",
            "E) Olaylara karşı çok 'soğuk' davranıyordu."
          ],
          "correct": 4,
          "solution": "Doğru cevap Olaylara karşı çok 'soğuk' davranıyordu..",
          "id": "e4_q20",
          "no": 20
        },
        {
          "subject": "Türkçe",
          "text": "Kültür tarih boyunca insanlığın en büyük rehberlerinden biri olmuştur. Toplumlar Kültür sayesinde sınırlarını aşmış, geleceğe umutla bakabilmiştir. (P-105)\nBu parçanın ana düşüncesi nedir?",
          "options": [
            "A) Kültür, toplumsal ilerleme ve vizyon için vazgeçilmezdir.",
            "B) Kültür sadece bireyseldir.",
            "C) Kültür sadece geçmişte kalmıştır.",
            "D) Kültür zaman kaybıdır.",
            "E) İnsanlar Kültür ile ilgilenmemelidir."
          ],
          "correct": 0,
          "solution": "Doğru cevap Kültür, toplumsal ilerleme ve vizyon için vazgeçilmezdir..",
          "id": "e4_q21",
          "no": 21
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde 'herkes' kelimesinin yazımıyla ilgili bir kural hatırlatılmaktadır? (T-106)",
          "options": [
            "A) herkes cümlede özne olamaz.",
            "B) herkes kelimesi fiildir.",
            "C) 'herkes' kelimesinin doğru yazımına dikkat edilmelidir.",
            "D) herkes kelimesi her zaman ayrı yazılır.",
            "E) herkes kelimesi yabancı kökenlidir."
          ],
          "correct": 2,
          "solution": "Doğru cevap 'herkes' kelimesinin doğru yazımına dikkat edilmelidir..",
          "id": "e4_q22",
          "no": 22
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde mecaz anlamlı bir sözcük kullanılmıştır? (T-107)",
          "options": [
            "A) Kışın havalar soğuk olur.",
            "B) Hava bugün çok soğuk.",
            "C) Olaylara karşı çok 'soğuk' davranıyordu.",
            "D) Suyu dolaptan soğuk içti.",
            "E) Buzdolabı soğuk üflüyor."
          ],
          "correct": 2,
          "solution": "Doğru cevap Olaylara karşı çok 'soğuk' davranıyordu..",
          "id": "e4_q23",
          "no": 23
        },
        {
          "subject": "Türkçe",
          "text": "Felsefe tarih boyunca insanlığın en büyük rehberlerinden biri olmuştur. Toplumlar Felsefe sayesinde sınırlarını aşmış, geleceğe umutla bakabilmiştir. (P-108)\nBu parçanın ana düşüncesi nedir?",
          "options": [
            "A) Felsefe sadece geçmişte kalmıştır.",
            "B) Felsefe, toplumsal ilerleme ve vizyon için vazgeçilmezdir.",
            "C) Felsefe sadece bireyseldir.",
            "D) İnsanlar Felsefe ile ilgilenmemelidir.",
            "E) Felsefe zaman kaybıdır."
          ],
          "correct": 1,
          "solution": "Doğru cevap Felsefe, toplumsal ilerleme ve vizyon için vazgeçilmezdir..",
          "id": "e4_q24",
          "no": 24
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde 'bugün' kelimesinin yazımıyla ilgili bir kural hatırlatılmaktadır? (T-109)",
          "options": [
            "A) bugün kelimesi fiildir.",
            "B) bugün kelimesi yabancı kökenlidir.",
            "C) bugün kelimesi her zaman ayrı yazılır.",
            "D) bugün cümlede özne olamaz.",
            "E) 'bugün' kelimesinin doğru yazımına dikkat edilmelidir."
          ],
          "correct": 4,
          "solution": "Doğru cevap 'bugün' kelimesinin doğru yazımına dikkat edilmelidir..",
          "id": "e4_q25",
          "no": 25
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde mecaz anlamlı bir sözcük kullanılmıştır? (T-110)",
          "options": [
            "A) Olaylara karşı çok 'soğuk' davranıyordu.",
            "B) Suyu dolaptan soğuk içti.",
            "C) Hava bugün çok soğuk.",
            "D) Kışın havalar soğuk olur.",
            "E) Buzdolabı soğuk üflüyor."
          ],
          "correct": 0,
          "solution": "Doğru cevap Olaylara karşı çok 'soğuk' davranıyordu..",
          "id": "e4_q26",
          "no": 26
        },
        {
          "subject": "Türkçe",
          "text": "Edebiyat tarih boyunca insanlığın en büyük rehberlerinden biri olmuştur. Toplumlar Edebiyat sayesinde sınırlarını aşmış, geleceğe umutla bakabilmiştir. (P-111)\nBu parçanın ana düşüncesi nedir?",
          "options": [
            "A) Edebiyat sadece bireyseldir.",
            "B) Edebiyat, toplumsal ilerleme ve vizyon için vazgeçilmezdir.",
            "C) İnsanlar Edebiyat ile ilgilenmemelidir.",
            "D) Edebiyat sadece geçmişte kalmıştır.",
            "E) Edebiyat zaman kaybıdır."
          ],
          "correct": 1,
          "solution": "Doğru cevap Edebiyat, toplumsal ilerleme ve vizyon için vazgeçilmezdir..",
          "id": "e4_q27",
          "no": 27
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde 'yalnız' kelimesinin yazımıyla ilgili bir kural hatırlatılmaktadır? (T-112)",
          "options": [
            "A) yalnız kelimesi her zaman ayrı yazılır.",
            "B) yalnız kelimesi fiildir.",
            "C) yalnız kelimesi yabancı kökenlidir.",
            "D) 'yalnız' kelimesinin doğru yazımına dikkat edilmelidir.",
            "E) yalnız cümlede özne olamaz."
          ],
          "correct": 3,
          "solution": "Doğru cevap 'yalnız' kelimesinin doğru yazımına dikkat edilmelidir..",
          "id": "e4_q28",
          "no": 28
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde mecaz anlamlı bir sözcük kullanılmıştır? (T-113)",
          "options": [
            "A) Kışın havalar soğuk olur.",
            "B) Hava bugün çok soğuk.",
            "C) Buzdolabı soğuk üflüyor.",
            "D) Olaylara karşı çok 'soğuk' davranıyordu.",
            "E) Suyu dolaptan soğuk içti."
          ],
          "correct": 3,
          "solution": "Doğru cevap Olaylara karşı çok 'soğuk' davranıyordu..",
          "id": "e4_q29",
          "no": 29
        },
        {
          "subject": "Türkçe",
          "text": "Tarih tarih boyunca insanlığın en büyük rehberlerinden biri olmuştur. Toplumlar Tarih sayesinde sınırlarını aşmış, geleceğe umutla bakabilmiştir. (P-114)\nBu parçanın ana düşüncesi nedir?",
          "options": [
            "A) Tarih sadece geçmişte kalmıştır.",
            "B) Tarih, toplumsal ilerleme ve vizyon için vazgeçilmezdir.",
            "C) Tarih zaman kaybıdır.",
            "D) Tarih sadece bireyseldir.",
            "E) İnsanlar Tarih ile ilgilenmemelidir."
          ],
          "correct": 1,
          "solution": "Doğru cevap Tarih, toplumsal ilerleme ve vizyon için vazgeçilmezdir..",
          "id": "e4_q30",
          "no": 30
        },
        {
          "subject": "Matematik",
          "text": "7x + 21 = 119 denkleminde x kaçtır? (SoruID: M90)",
          "options": [
            "A) 15",
            "B) 13",
            "C) 17",
            "D) 16",
            "E) 14"
          ],
          "correct": 4,
          "solution": "Doğru cevap 14.",
          "id": "e4_q31",
          "no": 31
        },
        {
          "subject": "Matematik",
          "text": "190 sayısının %50'si kaçtır? (SoruID: M91)",
          "options": [
            "A) 110",
            "B) 105",
            "C) 95",
            "D) 100",
            "E) 90"
          ],
          "correct": 2,
          "solution": "Doğru cevap 95.",
          "id": "e4_q32",
          "no": 32
        },
        {
          "subject": "Matematik",
          "text": "18, 26 ve 22 sayılarının aritmetik ortalaması kaçtır? (SoruID: M92)",
          "options": [
            "A) 24",
            "B) 22",
            "C) 20",
            "D) 23",
            "E) 21"
          ],
          "correct": 1,
          "solution": "Doğru cevap 22.",
          "id": "e4_q33",
          "no": 33
        },
        {
          "subject": "Matematik",
          "text": "Ali 23, Ayşe 12 yaşındadır. 7 yıl sonra yaşları toplamı kaç olur? (SoruID: M93)",
          "options": [
            "A) 48",
            "B) 56",
            "C) 42",
            "D) 49",
            "E) 50"
          ],
          "correct": 3,
          "solution": "Doğru cevap 49.",
          "id": "e4_q34",
          "no": 34
        },
        {
          "subject": "Matematik",
          "text": "√81 + √49 işleminin sonucu kaçtır? (SoruID: M94)",
          "options": [
            "A) 17",
            "B) 18",
            "C) 16",
            "D) 14",
            "E) 15"
          ],
          "correct": 2,
          "solution": "Doğru cevap 16.",
          "id": "e4_q35",
          "no": 35
        },
        {
          "subject": "Matematik",
          "text": "4x + 21 = 73 denkleminde x kaçtır? (SoruID: M95)",
          "options": [
            "A) 14",
            "B) 13",
            "C) 12",
            "D) 15",
            "E) 16"
          ],
          "correct": 1,
          "solution": "Doğru cevap 13.",
          "id": "e4_q36",
          "no": 36
        },
        {
          "subject": "Matematik",
          "text": "100 sayısının %10'si kaçtır? (SoruID: M96)",
          "options": [
            "A) 5",
            "B) 25",
            "C) 10",
            "D) 20",
            "E) 15"
          ],
          "correct": 2,
          "solution": "Doğru cevap 10.",
          "id": "e4_q37",
          "no": 37
        },
        {
          "subject": "Matematik",
          "text": "26, 26 ve 14 sayılarının aritmetik ortalaması kaçtır? (SoruID: M97)",
          "options": [
            "A) 22",
            "B) 21",
            "C) 24",
            "D) 23",
            "E) 20"
          ],
          "correct": 0,
          "solution": "Doğru cevap 22.",
          "id": "e4_q38",
          "no": 38
        },
        {
          "subject": "Matematik",
          "text": "Ali 14, Ayşe 20 yaşındadır. 8 yıl sonra yaşları toplamı kaç olur? (SoruID: M98)",
          "options": [
            "A) 49",
            "B) 42",
            "C) 50",
            "D) 58",
            "E) 51"
          ],
          "correct": 2,
          "solution": "Doğru cevap 50.",
          "id": "e4_q39",
          "no": 39
        },
        {
          "subject": "Matematik",
          "text": "√16 + √16 işleminin sonucu kaçtır? (SoruID: M99)",
          "options": [
            "A) 9",
            "B) 10",
            "C) 7",
            "D) 8",
            "E) 6"
          ],
          "correct": 3,
          "solution": "Doğru cevap 8.",
          "id": "e4_q40",
          "no": 40
        },
        {
          "subject": "Matematik",
          "text": "6x + 24 = 102 denkleminde x kaçtır? (SoruID: M100)",
          "options": [
            "A) 13",
            "B) 12",
            "C) 15",
            "D) 16",
            "E) 14"
          ],
          "correct": 0,
          "solution": "Doğru cevap 13.",
          "id": "e4_q41",
          "no": 41
        },
        {
          "subject": "Matematik",
          "text": "80 sayısının %75'si kaçtır? (SoruID: M101)",
          "options": [
            "A) 65",
            "B) 60",
            "C) 55",
            "D) 75",
            "E) 70"
          ],
          "correct": 1,
          "solution": "Doğru cevap 60.",
          "id": "e4_q42",
          "no": 42
        },
        {
          "subject": "Matematik",
          "text": "15, 14 ve 25 sayılarının aritmetik ortalaması kaçtır? (SoruID: M102)",
          "options": [
            "A) 19",
            "B) 18",
            "C) 17",
            "D) 20",
            "E) 16"
          ],
          "correct": 1,
          "solution": "Doğru cevap 18.",
          "id": "e4_q43",
          "no": 43
        },
        {
          "subject": "Matematik",
          "text": "Ali 19, Ayşe 17 yaşındadır. 8 yıl sonra yaşları toplamı kaç olur? (SoruID: M103)",
          "options": [
            "A) 53",
            "B) 44",
            "C) 60",
            "D) 52",
            "E) 51"
          ],
          "correct": 3,
          "solution": "Doğru cevap 52.",
          "id": "e4_q44",
          "no": 44
        },
        {
          "subject": "Matematik",
          "text": "√16 + √49 işleminin sonucu kaçtır? (SoruID: M104)",
          "options": [
            "A) 10",
            "B) 13",
            "C) 9",
            "D) 11",
            "E) 12"
          ],
          "correct": 3,
          "solution": "Doğru cevap 11.",
          "id": "e4_q45",
          "no": 45
        },
        {
          "subject": "Matematik",
          "text": "2x + 27 = 31 denkleminde x kaçtır? (SoruID: M105)",
          "options": [
            "A) 4",
            "B) 2",
            "C) 3",
            "D) 1",
            "E) 5"
          ],
          "correct": 1,
          "solution": "Doğru cevap 2.",
          "id": "e4_q46",
          "no": 46
        },
        {
          "subject": "Matematik",
          "text": "90 sayısının %30'si kaçtır? (SoruID: M106)",
          "options": [
            "A) 42",
            "B) 37",
            "C) 22",
            "D) 32",
            "E) 27"
          ],
          "correct": 4,
          "solution": "Doğru cevap 27.",
          "id": "e4_q47",
          "no": 47
        },
        {
          "subject": "Matematik",
          "text": "16, 15 ve 17 sayılarının aritmetik ortalaması kaçtır? (SoruID: M107)",
          "options": [
            "A) 15",
            "B) 14",
            "C) 16",
            "D) 18",
            "E) 17"
          ],
          "correct": 2,
          "solution": "Doğru cevap 16.",
          "id": "e4_q48",
          "no": 48
        },
        {
          "subject": "Matematik",
          "text": "Ali 15, Ayşe 23 yaşındadır. 9 yıl sonra yaşları toplamı kaç olur? (SoruID: M108)",
          "options": [
            "A) 65",
            "B) 56",
            "C) 55",
            "D) 47",
            "E) 57"
          ],
          "correct": 1,
          "solution": "Doğru cevap 56.",
          "id": "e4_q49",
          "no": 49
        },
        {
          "subject": "Matematik",
          "text": "√36 + √81 işleminin sonucu kaçtır? (SoruID: M109)",
          "options": [
            "A) 16",
            "B) 14",
            "C) 15",
            "D) 17",
            "E) 13"
          ],
          "correct": 2,
          "solution": "Doğru cevap 15.",
          "id": "e4_q50",
          "no": 50
        },
        {
          "subject": "Matematik",
          "text": "5x + 10 = 20 denkleminde x kaçtır? (SoruID: M110)",
          "options": [
            "A) 4",
            "B) 5",
            "C) 2",
            "D) 3",
            "E) 1"
          ],
          "correct": 2,
          "solution": "Doğru cevap 2.",
          "id": "e4_q51",
          "no": 51
        },
        {
          "subject": "Matematik",
          "text": "100 sayısının %60'si kaçtır? (SoruID: M111)",
          "options": [
            "A) 75",
            "B) 55",
            "C) 60",
            "D) 65",
            "E) 70"
          ],
          "correct": 2,
          "solution": "Doğru cevap 60.",
          "id": "e4_q52",
          "no": 52
        },
        {
          "subject": "Matematik",
          "text": "30, 30 ve 18 sayılarının aritmetik ortalaması kaçtır? (SoruID: M112)",
          "options": [
            "A) 28",
            "B) 26",
            "C) 27",
            "D) 24",
            "E) 25"
          ],
          "correct": 1,
          "solution": "Doğru cevap 26.",
          "id": "e4_q53",
          "no": 53
        },
        {
          "subject": "Matematik",
          "text": "Ali 25, Ayşe 24 yaşındadır. 7 yıl sonra yaşları toplamı kaç olur? (SoruID: M113)",
          "options": [
            "A) 70",
            "B) 62",
            "C) 63",
            "D) 64",
            "E) 56"
          ],
          "correct": 2,
          "solution": "Doğru cevap 63.",
          "id": "e4_q54",
          "no": 54
        },
        {
          "subject": "Matematik",
          "text": "√16 + √25 işleminin sonucu kaçtır? (SoruID: M114)",
          "options": [
            "A) 7",
            "B) 9",
            "C) 10",
            "D) 11",
            "E) 8"
          ],
          "correct": 1,
          "solution": "Doğru cevap 9.",
          "id": "e4_q55",
          "no": 55
        },
        {
          "subject": "Matematik",
          "text": "7x + 21 = 112 denkleminde x kaçtır? (SoruID: M115)",
          "options": [
            "A) 16",
            "B) 12",
            "C) 14",
            "D) 15",
            "E) 13"
          ],
          "correct": 4,
          "solution": "Doğru cevap 13.",
          "id": "e4_q56",
          "no": 56
        },
        {
          "subject": "Matematik",
          "text": "200 sayısının %20'si kaçtır? (SoruID: M116)",
          "options": [
            "A) 50",
            "B) 45",
            "C) 40",
            "D) 55",
            "E) 35"
          ],
          "correct": 2,
          "solution": "Doğru cevap 40.",
          "id": "e4_q57",
          "no": 57
        },
        {
          "subject": "Matematik",
          "text": "28, 11 ve 12 sayılarının aritmetik ortalaması kaçtır? (SoruID: M117)",
          "options": [
            "A) 18",
            "B) 17",
            "C) 16",
            "D) 19",
            "E) 15"
          ],
          "correct": 1,
          "solution": "Doğru cevap 17.",
          "id": "e4_q58",
          "no": 58
        },
        {
          "subject": "Matematik",
          "text": "Ali 22, Ayşe 24 yaşındadır. 10 yıl sonra yaşları toplamı kaç olur? (SoruID: M118)",
          "options": [
            "A) 56",
            "B) 76",
            "C) 67",
            "D) 66",
            "E) 65"
          ],
          "correct": 3,
          "solution": "Doğru cevap 66.",
          "id": "e4_q59",
          "no": 59
        },
        {
          "subject": "Matematik",
          "text": "√16 + √4 işleminin sonucu kaçtır? (SoruID: M119)",
          "options": [
            "A) 7",
            "B) 5",
            "C) 4",
            "D) 8",
            "E) 6"
          ],
          "correct": 4,
          "solution": "Doğru cevap 6.",
          "id": "e4_q60",
          "no": 60
        },
        {
          "subject": "Tarih",
          "text": "Türk siyasi ve askerî tarihinde büyük öneme sahip olan 'Kars Antlaşması' süreci ile ilgili aşağıdakilerden hangisi söylenebilir? (H-78)",
          "options": [
            "A) Kars Antlaşması dönemin en kritik gelişmelerinden biridir.",
            "B) Avrupa'da gerçekleşmiştir.",
            "C) Sadece ekonomik bir olaydır.",
            "D) Osmanlı'nın kuruluş dönemine aittir.",
            "E) Hiçbir etkisi olmamıştır."
          ],
          "correct": 0,
          "solution": "Doğru cevap Kars Antlaşması dönemin en kritik gelişmelerinden biridir..",
          "id": "e4_q61",
          "no": 61
        },
        {
          "subject": "Tarih",
          "text": "Aşağıdaki tarihî gelişmelerden hangisi 'Ankara Antlaşması' ile doğrudan veya dolaylı olarak bağlantılıdır? (H-79)",
          "options": [
            "A) Coğrafi Keşifler",
            "B) Ankara Antlaşması öncesi ve sonrası yaşanan siyasi krizler.",
            "C) Kavimler Göçü",
            "D) Sanayi İnkılabı",
            "E) Fransız İhtilali"
          ],
          "correct": 1,
          "solution": "Doğru cevap Ankara Antlaşması öncesi ve sonrası yaşanan siyasi krizler..",
          "id": "e4_q62",
          "no": 62
        },
        {
          "subject": "Tarih",
          "text": "Millî Mücadele ve inkılaplar tarihi incelendiğinde 'Sivas Kongresi' olayının temel amacı aşağıdakilerden hangisidir? (H-80)",
          "options": [
            "A) Avrupa'ya göç etmek",
            "B) Bağımsızlık ve egemenliği pekiştirmek",
            "C) Yeni sömürgeler elde etmek",
            "D) Feodaliteyi kurmak",
            "E) Saltanatı güçlendirmek"
          ],
          "correct": 1,
          "solution": "Doğru cevap Bağımsızlık ve egemenliği pekiştirmek.",
          "id": "e4_q63",
          "no": 63
        },
        {
          "subject": "Tarih",
          "text": "Türk siyasi ve askerî tarihinde büyük öneme sahip olan 'Erzurum Kongresi' süreci ile ilgili aşağıdakilerden hangisi söylenebilir? (H-81)",
          "options": [
            "A) Osmanlı'nın kuruluş dönemine aittir.",
            "B) Sadece ekonomik bir olaydır.",
            "C) Erzurum Kongresi dönemin en kritik gelişmelerinden biridir.",
            "D) Hiçbir etkisi olmamıştır.",
            "E) Avrupa'da gerçekleşmiştir."
          ],
          "correct": 2,
          "solution": "Doğru cevap Erzurum Kongresi dönemin en kritik gelişmelerinden biridir..",
          "id": "e4_q64",
          "no": 64
        },
        {
          "subject": "Tarih",
          "text": "Aşağıdaki tarihî gelişmelerden hangisi 'Amasya Genelgesi' ile doğrudan veya dolaylı olarak bağlantılıdır? (H-82)",
          "options": [
            "A) Kavimler Göçü",
            "B) Sanayi İnkılabı",
            "C) Amasya Genelgesi öncesi ve sonrası yaşanan siyasi krizler.",
            "D) Fransız İhtilali",
            "E) Coğrafi Keşifler"
          ],
          "correct": 2,
          "solution": "Doğru cevap Amasya Genelgesi öncesi ve sonrası yaşanan siyasi krizler..",
          "id": "e4_q65",
          "no": 65
        },
        {
          "subject": "Tarih",
          "text": "Millî Mücadele ve inkılaplar tarihi incelendiğinde 'Lozan Antlaşması' olayının temel amacı aşağıdakilerden hangisidir? (H-83)",
          "options": [
            "A) Bağımsızlık ve egemenliği pekiştirmek",
            "B) Saltanatı güçlendirmek",
            "C) Feodaliteyi kurmak",
            "D) Yeni sömürgeler elde etmek",
            "E) Avrupa'ya göç etmek"
          ],
          "correct": 0,
          "solution": "Doğru cevap Bağımsızlık ve egemenliği pekiştirmek.",
          "id": "e4_q66",
          "no": 66
        },
        {
          "subject": "Tarih",
          "text": "Türk siyasi ve askerî tarihinde büyük öneme sahip olan 'Cumhuriyetin İlanı' süreci ile ilgili aşağıdakilerden hangisi söylenebilir? (H-84)",
          "options": [
            "A) Osmanlı'nın kuruluş dönemine aittir.",
            "B) Sadece ekonomik bir olaydır.",
            "C) Cumhuriyetin İlanı dönemin en kritik gelişmelerinden biridir.",
            "D) Avrupa'da gerçekleşmiştir.",
            "E) Hiçbir etkisi olmamıştır."
          ],
          "correct": 2,
          "solution": "Doğru cevap Cumhuriyetin İlanı dönemin en kritik gelişmelerinden biridir..",
          "id": "e4_q67",
          "no": 67
        },
        {
          "subject": "Tarih",
          "text": "Aşağıdaki tarihî gelişmelerden hangisi 'TBMM'nin Açılışı' ile doğrudan veya dolaylı olarak bağlantılıdır? (H-85)",
          "options": [
            "A) Kavimler Göçü",
            "B) TBMM'nin Açılışı öncesi ve sonrası yaşanan siyasi krizler.",
            "C) Coğrafi Keşifler",
            "D) Fransız İhtilali",
            "E) Sanayi İnkılabı"
          ],
          "correct": 1,
          "solution": "Doğru cevap TBMM'nin Açılışı öncesi ve sonrası yaşanan siyasi krizler..",
          "id": "e4_q68",
          "no": 68
        },
        {
          "subject": "Tarih",
          "text": "Millî Mücadele ve inkılaplar tarihi incelendiğinde 'Mudanya Mütarekesi' olayının temel amacı aşağıdakilerden hangisidir? (H-86)",
          "options": [
            "A) Yeni sömürgeler elde etmek",
            "B) Feodaliteyi kurmak",
            "C) Bağımsızlık ve egemenliği pekiştirmek",
            "D) Saltanatı güçlendirmek",
            "E) Avrupa'ya göç etmek"
          ],
          "correct": 2,
          "solution": "Doğru cevap Bağımsızlık ve egemenliği pekiştirmek.",
          "id": "e4_q69",
          "no": 69
        },
        {
          "subject": "Tarih",
          "text": "Türk siyasi ve askerî tarihinde büyük öneme sahip olan 'Saltanatın Kaldırılması' süreci ile ilgili aşağıdakilerden hangisi söylenebilir? (H-87)",
          "options": [
            "A) Hiçbir etkisi olmamıştır.",
            "B) Osmanlı'nın kuruluş dönemine aittir.",
            "C) Avrupa'da gerçekleşmiştir.",
            "D) Saltanatın Kaldırılması dönemin en kritik gelişmelerinden biridir.",
            "E) Sadece ekonomik bir olaydır."
          ],
          "correct": 3,
          "solution": "Doğru cevap Saltanatın Kaldırılması dönemin en kritik gelişmelerinden biridir..",
          "id": "e4_q70",
          "no": 70
        },
        {
          "subject": "Tarih",
          "text": "Aşağıdaki tarihî gelişmelerden hangisi 'Halifeliğin Kaldırılması' ile doğrudan veya dolaylı olarak bağlantılıdır? (H-88)",
          "options": [
            "A) Coğrafi Keşifler",
            "B) Fransız İhtilali",
            "C) Halifeliğin Kaldırılması öncesi ve sonrası yaşanan siyasi krizler.",
            "D) Kavimler Göçü",
            "E) Sanayi İnkılabı"
          ],
          "correct": 2,
          "solution": "Doğru cevap Halifeliğin Kaldırılması öncesi ve sonrası yaşanan siyasi krizler..",
          "id": "e4_q71",
          "no": 71
        },
        {
          "subject": "Tarih",
          "text": "Millî Mücadele ve inkılaplar tarihi incelendiğinde 'Tevhid-i Tedrisat' olayının temel amacı aşağıdakilerden hangisidir? (H-89)",
          "options": [
            "A) Bağımsızlık ve egemenliği pekiştirmek",
            "B) Avrupa'ya göç etmek",
            "C) Feodaliteyi kurmak",
            "D) Saltanatı güçlendirmek",
            "E) Yeni sömürgeler elde etmek"
          ],
          "correct": 0,
          "solution": "Doğru cevap Bağımsızlık ve egemenliği pekiştirmek.",
          "id": "e4_q72",
          "no": 72
        },
        {
          "subject": "Tarih",
          "text": "Türk siyasi ve askerî tarihinde büyük öneme sahip olan 'Trablusgarp Savaşı' süreci ile ilgili aşağıdakilerden hangisi söylenebilir? (H-90)",
          "options": [
            "A) Sadece ekonomik bir olaydır.",
            "B) Hiçbir etkisi olmamıştır.",
            "C) Avrupa'da gerçekleşmiştir.",
            "D) Osmanlı'nın kuruluş dönemine aittir.",
            "E) Trablusgarp Savaşı dönemin en kritik gelişmelerinden biridir."
          ],
          "correct": 4,
          "solution": "Doğru cevap Trablusgarp Savaşı dönemin en kritik gelişmelerinden biridir..",
          "id": "e4_q73",
          "no": 73
        },
        {
          "subject": "Tarih",
          "text": "Aşağıdaki tarihî gelişmelerden hangisi 'Balkan Savaşları' ile doğrudan veya dolaylı olarak bağlantılıdır? (H-91)",
          "options": [
            "A) Balkan Savaşları öncesi ve sonrası yaşanan siyasi krizler.",
            "B) Fransız İhtilali",
            "C) Kavimler Göçü",
            "D) Coğrafi Keşifler",
            "E) Sanayi İnkılabı"
          ],
          "correct": 0,
          "solution": "Doğru cevap Balkan Savaşları öncesi ve sonrası yaşanan siyasi krizler..",
          "id": "e4_q74",
          "no": 74
        },
        {
          "subject": "Tarih",
          "text": "Millî Mücadele ve inkılaplar tarihi incelendiğinde 'I. Dünya Savaşı' olayının temel amacı aşağıdakilerden hangisidir? (H-92)",
          "options": [
            "A) Avrupa'ya göç etmek",
            "B) Bağımsızlık ve egemenliği pekiştirmek",
            "C) Yeni sömürgeler elde etmek",
            "D) Feodaliteyi kurmak",
            "E) Saltanatı güçlendirmek"
          ],
          "correct": 1,
          "solution": "Doğru cevap Bağımsızlık ve egemenliği pekiştirmek.",
          "id": "e4_q75",
          "no": 75
        },
        {
          "subject": "Tarih",
          "text": "Türk siyasi ve askerî tarihinde büyük öneme sahip olan 'Çanakkale Cephesi' süreci ile ilgili aşağıdakilerden hangisi söylenebilir? (H-93)",
          "options": [
            "A) Osmanlı'nın kuruluş dönemine aittir.",
            "B) Avrupa'da gerçekleşmiştir.",
            "C) Sadece ekonomik bir olaydır.",
            "D) Hiçbir etkisi olmamıştır.",
            "E) Çanakkale Cephesi dönemin en kritik gelişmelerinden biridir."
          ],
          "correct": 4,
          "solution": "Doğru cevap Çanakkale Cephesi dönemin en kritik gelişmelerinden biridir..",
          "id": "e4_q76",
          "no": 76
        },
        {
          "subject": "Tarih",
          "text": "Aşağıdaki tarihî gelişmelerden hangisi 'Sakarya Meydan Muharebesi' ile doğrudan veya dolaylı olarak bağlantılıdır? (H-94)",
          "options": [
            "A) Sanayi İnkılabı",
            "B) Sakarya Meydan Muharebesi öncesi ve sonrası yaşanan siyasi krizler.",
            "C) Fransız İhtilali",
            "D) Kavimler Göçü",
            "E) Coğrafi Keşifler"
          ],
          "correct": 1,
          "solution": "Doğru cevap Sakarya Meydan Muharebesi öncesi ve sonrası yaşanan siyasi krizler..",
          "id": "e4_q77",
          "no": 77
        },
        {
          "subject": "Tarih",
          "text": "Millî Mücadele ve inkılaplar tarihi incelendiğinde 'Büyük Taarruz' olayının temel amacı aşağıdakilerden hangisidir? (H-95)",
          "options": [
            "A) Saltanatı güçlendirmek",
            "B) Feodaliteyi kurmak",
            "C) Bağımsızlık ve egemenliği pekiştirmek",
            "D) Avrupa'ya göç etmek",
            "E) Yeni sömürgeler elde etmek"
          ],
          "correct": 2,
          "solution": "Doğru cevap Bağımsızlık ve egemenliği pekiştirmek.",
          "id": "e4_q78",
          "no": 78
        },
        {
          "subject": "Tarih",
          "text": "Türk siyasi ve askerî tarihinde büyük öneme sahip olan 'I. İnönü Muharebesi' süreci ile ilgili aşağıdakilerden hangisi söylenebilir? (H-96)",
          "options": [
            "A) Avrupa'da gerçekleşmiştir.",
            "B) Sadece ekonomik bir olaydır.",
            "C) I. İnönü Muharebesi dönemin en kritik gelişmelerinden biridir.",
            "D) Hiçbir etkisi olmamıştır.",
            "E) Osmanlı'nın kuruluş dönemine aittir."
          ],
          "correct": 2,
          "solution": "Doğru cevap I. İnönü Muharebesi dönemin en kritik gelişmelerinden biridir..",
          "id": "e4_q79",
          "no": 79
        },
        {
          "subject": "Tarih",
          "text": "Aşağıdaki tarihî gelişmelerden hangisi 'II. İnönü Muharebesi' ile doğrudan veya dolaylı olarak bağlantılıdır? (H-97)",
          "options": [
            "A) Coğrafi Keşifler",
            "B) Sanayi İnkılabı",
            "C) II. İnönü Muharebesi öncesi ve sonrası yaşanan siyasi krizler.",
            "D) Fransız İhtilali",
            "E) Kavimler Göçü"
          ],
          "correct": 2,
          "solution": "Doğru cevap II. İnönü Muharebesi öncesi ve sonrası yaşanan siyasi krizler..",
          "id": "e4_q80",
          "no": 80
        },
        {
          "subject": "Tarih",
          "text": "Millî Mücadele ve inkılaplar tarihi incelendiğinde 'Kars Antlaşması' olayının temel amacı aşağıdakilerden hangisidir? (H-98)",
          "options": [
            "A) Bağımsızlık ve egemenliği pekiştirmek",
            "B) Feodaliteyi kurmak",
            "C) Avrupa'ya göç etmek",
            "D) Yeni sömürgeler elde etmek",
            "E) Saltanatı güçlendirmek"
          ],
          "correct": 0,
          "solution": "Doğru cevap Bağımsızlık ve egemenliği pekiştirmek.",
          "id": "e4_q81",
          "no": 81
        },
        {
          "subject": "Tarih",
          "text": "Türk siyasi ve askerî tarihinde büyük öneme sahip olan 'Ankara Antlaşması' süreci ile ilgili aşağıdakilerden hangisi söylenebilir? (H-99)",
          "options": [
            "A) Ankara Antlaşması dönemin en kritik gelişmelerinden biridir.",
            "B) Osmanlı'nın kuruluş dönemine aittir.",
            "C) Hiçbir etkisi olmamıştır.",
            "D) Avrupa'da gerçekleşmiştir.",
            "E) Sadece ekonomik bir olaydır."
          ],
          "correct": 0,
          "solution": "Doğru cevap Ankara Antlaşması dönemin en kritik gelişmelerinden biridir..",
          "id": "e4_q82",
          "no": 82
        },
        {
          "subject": "Tarih",
          "text": "Aşağıdaki tarihî gelişmelerden hangisi 'Sivas Kongresi' ile doğrudan veya dolaylı olarak bağlantılıdır? (H-100)",
          "options": [
            "A) Coğrafi Keşifler",
            "B) Kavimler Göçü",
            "C) Sivas Kongresi öncesi ve sonrası yaşanan siyasi krizler.",
            "D) Sanayi İnkılabı",
            "E) Fransız İhtilali"
          ],
          "correct": 2,
          "solution": "Doğru cevap Sivas Kongresi öncesi ve sonrası yaşanan siyasi krizler..",
          "id": "e4_q83",
          "no": 83
        },
        {
          "subject": "Tarih",
          "text": "Millî Mücadele ve inkılaplar tarihi incelendiğinde 'Erzurum Kongresi' olayının temel amacı aşağıdakilerden hangisidir? (H-101)",
          "options": [
            "A) Feodaliteyi kurmak",
            "B) Saltanatı güçlendirmek",
            "C) Bağımsızlık ve egemenliği pekiştirmek",
            "D) Yeni sömürgeler elde etmek",
            "E) Avrupa'ya göç etmek"
          ],
          "correct": 2,
          "solution": "Doğru cevap Bağımsızlık ve egemenliği pekiştirmek.",
          "id": "e4_q84",
          "no": 84
        },
        {
          "subject": "Tarih",
          "text": "Türk siyasi ve askerî tarihinde büyük öneme sahip olan 'Amasya Genelgesi' süreci ile ilgili aşağıdakilerden hangisi söylenebilir? (H-102)",
          "options": [
            "A) Hiçbir etkisi olmamıştır.",
            "B) Osmanlı'nın kuruluş dönemine aittir.",
            "C) Avrupa'da gerçekleşmiştir.",
            "D) Sadece ekonomik bir olaydır.",
            "E) Amasya Genelgesi dönemin en kritik gelişmelerinden biridir."
          ],
          "correct": 4,
          "solution": "Doğru cevap Amasya Genelgesi dönemin en kritik gelişmelerinden biridir..",
          "id": "e4_q85",
          "no": 85
        },
        {
          "subject": "Tarih",
          "text": "Aşağıdaki tarihî gelişmelerden hangisi 'Lozan Antlaşması' ile doğrudan veya dolaylı olarak bağlantılıdır? (H-103)",
          "options": [
            "A) Fransız İhtilali",
            "B) Lozan Antlaşması öncesi ve sonrası yaşanan siyasi krizler.",
            "C) Coğrafi Keşifler",
            "D) Sanayi İnkılabı",
            "E) Kavimler Göçü"
          ],
          "correct": 1,
          "solution": "Doğru cevap Lozan Antlaşması öncesi ve sonrası yaşanan siyasi krizler..",
          "id": "e4_q86",
          "no": 86
        },
        {
          "subject": "Tarih",
          "text": "Millî Mücadele ve inkılaplar tarihi incelendiğinde 'Cumhuriyetin İlanı' olayının temel amacı aşağıdakilerden hangisidir? (H-104)",
          "options": [
            "A) Bağımsızlık ve egemenliği pekiştirmek",
            "B) Avrupa'ya göç etmek",
            "C) Saltanatı güçlendirmek",
            "D) Feodaliteyi kurmak",
            "E) Yeni sömürgeler elde etmek"
          ],
          "correct": 0,
          "solution": "Doğru cevap Bağımsızlık ve egemenliği pekiştirmek.",
          "id": "e4_q87",
          "no": 87
        },
        {
          "subject": "Coğrafya",
          "text": "Türkiye'nin fiziki coğrafyası düşünüldüğünde 'Kaçkar Dağları' için aşağıdakilerden hangisi doğrudur? (C-52)",
          "options": [
            "A) Kaçkar Dağları, ülkemizin önemli yeryüzü şekillerinden biridir.",
            "B) Kaçkar Dağları tarıma kapalıdır.",
            "C) Kaçkar Dağları bir çöldür.",
            "D) Kaçkar Dağları yapay bir kanaldır.",
            "E) Kaçkar Dağları Marmara'dadır."
          ],
          "correct": 0,
          "solution": "Doğru cevap Kaçkar Dağları, ülkemizin önemli yeryüzü şekillerinden biridir..",
          "id": "e4_q88",
          "no": 88
        },
        {
          "subject": "Coğrafya",
          "text": "Coğrafi özellikleri ve turizm potansiyeli göz önüne alındığında 'Gediz Nehri' hangi alanda daha çok öne çıkar? (C-53)",
          "options": [
            "A) Sadece ağır sanayi",
            "B) Okyanus balıkçılığı",
            "C) Çöl iklimi araştırmaları",
            "D) Doğal güzellikleri ve turizm/coğrafi önemi",
            "E) Sadece madencilik"
          ],
          "correct": 3,
          "solution": "Doğru cevap Doğal güzellikleri ve turizm/coğrafi önemi.",
          "id": "e4_q89",
          "no": 89
        },
        {
          "subject": "Coğrafya",
          "text": "Türkiye'nin fiziki coğrafyası düşünüldüğünde 'Salda Gölü' için aşağıdakilerden hangisi doğrudur? (C-54)",
          "options": [
            "A) Salda Gölü tarıma kapalıdır.",
            "B) Salda Gölü yapay bir kanaldır.",
            "C) Salda Gölü bir çöldür.",
            "D) Salda Gölü Marmara'dadır.",
            "E) Salda Gölü, ülkemizin önemli yeryüzü şekillerinden biridir."
          ],
          "correct": 4,
          "solution": "Doğru cevap Salda Gölü, ülkemizin önemli yeryüzü şekillerinden biridir..",
          "id": "e4_q90",
          "no": 90
        },
        {
          "subject": "Coğrafya",
          "text": "Coğrafi özellikleri ve turizm potansiyeli göz önüne alındığında 'Kapadokya' hangi alanda daha çok öne çıkar? (C-55)",
          "options": [
            "A) Okyanus balıkçılığı",
            "B) Doğal güzellikleri ve turizm/coğrafi önemi",
            "C) Sadece ağır sanayi",
            "D) Çöl iklimi araştırmaları",
            "E) Sadece madencilik"
          ],
          "correct": 1,
          "solution": "Doğru cevap Doğal güzellikleri ve turizm/coğrafi önemi.",
          "id": "e4_q91",
          "no": 91
        },
        {
          "subject": "Coğrafya",
          "text": "Türkiye'nin fiziki coğrafyası düşünüldüğünde 'Pamukkale' için aşağıdakilerden hangisi doğrudur? (C-56)",
          "options": [
            "A) Pamukkale, ülkemizin önemli yeryüzü şekillerinden biridir.",
            "B) Pamukkale tarıma kapalıdır.",
            "C) Pamukkale bir çöldür.",
            "D) Pamukkale Marmara'dadır.",
            "E) Pamukkale yapay bir kanaldır."
          ],
          "correct": 0,
          "solution": "Doğru cevap Pamukkale, ülkemizin önemli yeryüzü şekillerinden biridir..",
          "id": "e4_q92",
          "no": 92
        },
        {
          "subject": "Coğrafya",
          "text": "Coğrafi özellikleri ve turizm potansiyeli göz önüne alındığında 'Nemrut Dağı' hangi alanda daha çok öne çıkar? (C-57)",
          "options": [
            "A) Okyanus balıkçılığı",
            "B) Çöl iklimi araştırmaları",
            "C) Sadece ağır sanayi",
            "D) Doğal güzellikleri ve turizm/coğrafi önemi",
            "E) Sadece madencilik"
          ],
          "correct": 3,
          "solution": "Doğru cevap Doğal güzellikleri ve turizm/coğrafi önemi.",
          "id": "e4_q93",
          "no": 93
        },
        {
          "subject": "Coğrafya",
          "text": "Türkiye'nin fiziki coğrafyası düşünüldüğünde 'Sümela Manastırı' için aşağıdakilerden hangisi doğrudur? (C-58)",
          "options": [
            "A) Sümela Manastırı, ülkemizin önemli yeryüzü şekillerinden biridir.",
            "B) Sümela Manastırı bir çöldür.",
            "C) Sümela Manastırı yapay bir kanaldır.",
            "D) Sümela Manastırı Marmara'dadır.",
            "E) Sümela Manastırı tarıma kapalıdır."
          ],
          "correct": 0,
          "solution": "Doğru cevap Sümela Manastırı, ülkemizin önemli yeryüzü şekillerinden biridir..",
          "id": "e4_q94",
          "no": 94
        },
        {
          "subject": "Coğrafya",
          "text": "Coğrafi özellikleri ve turizm potansiyeli göz önüne alındığında 'Uludağ' hangi alanda daha çok öne çıkar? (C-59)",
          "options": [
            "A) Çöl iklimi araştırmaları",
            "B) Okyanus balıkçılığı",
            "C) Sadece ağır sanayi",
            "D) Doğal güzellikleri ve turizm/coğrafi önemi",
            "E) Sadece madencilik"
          ],
          "correct": 3,
          "solution": "Doğru cevap Doğal güzellikleri ve turizm/coğrafi önemi.",
          "id": "e4_q95",
          "no": 95
        },
        {
          "subject": "Coğrafya",
          "text": "Türkiye'nin fiziki coğrafyası düşünüldüğünde 'Van Gölü' için aşağıdakilerden hangisi doğrudur? (C-60)",
          "options": [
            "A) Van Gölü tarıma kapalıdır.",
            "B) Van Gölü, ülkemizin önemli yeryüzü şekillerinden biridir.",
            "C) Van Gölü bir çöldür.",
            "D) Van Gölü Marmara'dadır.",
            "E) Van Gölü yapay bir kanaldır."
          ],
          "correct": 1,
          "solution": "Doğru cevap Van Gölü, ülkemizin önemli yeryüzü şekillerinden biridir..",
          "id": "e4_q96",
          "no": 96
        },
        {
          "subject": "Coğrafya",
          "text": "Coğrafi özellikleri ve turizm potansiyeli göz önüne alındığında 'Ağrı Dağı' hangi alanda daha çok öne çıkar? (C-61)",
          "options": [
            "A) Çöl iklimi araştırmaları",
            "B) Doğal güzellikleri ve turizm/coğrafi önemi",
            "C) Sadece ağır sanayi",
            "D) Okyanus balıkçılığı",
            "E) Sadece madencilik"
          ],
          "correct": 1,
          "solution": "Doğru cevap Doğal güzellikleri ve turizm/coğrafi önemi.",
          "id": "e4_q97",
          "no": 97
        },
        {
          "subject": "Coğrafya",
          "text": "Türkiye'nin fiziki coğrafyası düşünüldüğünde 'Kızılırmak' için aşağıdakilerden hangisi doğrudur? (C-62)",
          "options": [
            "A) Kızılırmak bir çöldür.",
            "B) Kızılırmak tarıma kapalıdır.",
            "C) Kızılırmak yapay bir kanaldır.",
            "D) Kızılırmak Marmara'dadır.",
            "E) Kızılırmak, ülkemizin önemli yeryüzü şekillerinden biridir."
          ],
          "correct": 4,
          "solution": "Doğru cevap Kızılırmak, ülkemizin önemli yeryüzü şekillerinden biridir..",
          "id": "e4_q98",
          "no": 98
        },
        {
          "subject": "Coğrafya",
          "text": "Coğrafi özellikleri ve turizm potansiyeli göz önüne alındığında 'Erciyes Dağı' hangi alanda daha çok öne çıkar? (C-63)",
          "options": [
            "A) Sadece madencilik",
            "B) Çöl iklimi araştırmaları",
            "C) Sadece ağır sanayi",
            "D) Okyanus balıkçılığı",
            "E) Doğal güzellikleri ve turizm/coğrafi önemi"
          ],
          "correct": 4,
          "solution": "Doğru cevap Doğal güzellikleri ve turizm/coğrafi önemi.",
          "id": "e4_q99",
          "no": 99
        },
        {
          "subject": "Coğrafya",
          "text": "Türkiye'nin fiziki coğrafyası düşünüldüğünde 'Tuz Gölü' için aşağıdakilerden hangisi doğrudur? (C-64)",
          "options": [
            "A) Tuz Gölü tarıma kapalıdır.",
            "B) Tuz Gölü, ülkemizin önemli yeryüzü şekillerinden biridir.",
            "C) Tuz Gölü yapay bir kanaldır.",
            "D) Tuz Gölü bir çöldür.",
            "E) Tuz Gölü Marmara'dadır."
          ],
          "correct": 1,
          "solution": "Doğru cevap Tuz Gölü, ülkemizin önemli yeryüzü şekillerinden biridir..",
          "id": "e4_q100",
          "no": 100
        },
        {
          "subject": "Coğrafya",
          "text": "Coğrafi özellikleri ve turizm potansiyeli göz önüne alındığında 'Çukurova' hangi alanda daha çok öne çıkar? (C-65)",
          "options": [
            "A) Okyanus balıkçılığı",
            "B) Doğal güzellikleri ve turizm/coğrafi önemi",
            "C) Sadece ağır sanayi",
            "D) Sadece madencilik",
            "E) Çöl iklimi araştırmaları"
          ],
          "correct": 1,
          "solution": "Doğru cevap Doğal güzellikleri ve turizm/coğrafi önemi.",
          "id": "e4_q101",
          "no": 101
        },
        {
          "subject": "Coğrafya",
          "text": "Türkiye'nin fiziki coğrafyası düşünüldüğünde 'Bafra Ovası' için aşağıdakilerden hangisi doğrudur? (C-66)",
          "options": [
            "A) Bafra Ovası yapay bir kanaldır.",
            "B) Bafra Ovası bir çöldür.",
            "C) Bafra Ovası, ülkemizin önemli yeryüzü şekillerinden biridir.",
            "D) Bafra Ovası tarıma kapalıdır.",
            "E) Bafra Ovası Marmara'dadır."
          ],
          "correct": 2,
          "solution": "Doğru cevap Bafra Ovası, ülkemizin önemli yeryüzü şekillerinden biridir..",
          "id": "e4_q102",
          "no": 102
        },
        {
          "subject": "Coğrafya",
          "text": "Coğrafi özellikleri ve turizm potansiyeli göz önüne alındığında 'Kaçkar Dağları' hangi alanda daha çok öne çıkar? (C-67)",
          "options": [
            "A) Okyanus balıkçılığı",
            "B) Doğal güzellikleri ve turizm/coğrafi önemi",
            "C) Sadece ağır sanayi",
            "D) Çöl iklimi araştırmaları",
            "E) Sadece madencilik"
          ],
          "correct": 1,
          "solution": "Doğru cevap Doğal güzellikleri ve turizm/coğrafi önemi.",
          "id": "e4_q103",
          "no": 103
        },
        {
          "subject": "Coğrafya",
          "text": "Türkiye'nin fiziki coğrafyası düşünüldüğünde 'Gediz Nehri' için aşağıdakilerden hangisi doğrudur? (C-68)",
          "options": [
            "A) Gediz Nehri, ülkemizin önemli yeryüzü şekillerinden biridir.",
            "B) Gediz Nehri Marmara'dadır.",
            "C) Gediz Nehri bir çöldür.",
            "D) Gediz Nehri yapay bir kanaldır.",
            "E) Gediz Nehri tarıma kapalıdır."
          ],
          "correct": 0,
          "solution": "Doğru cevap Gediz Nehri, ülkemizin önemli yeryüzü şekillerinden biridir..",
          "id": "e4_q104",
          "no": 104
        },
        {
          "subject": "Coğrafya",
          "text": "Coğrafi özellikleri ve turizm potansiyeli göz önüne alındığında 'Salda Gölü' hangi alanda daha çok öne çıkar? (C-69)",
          "options": [
            "A) Çöl iklimi araştırmaları",
            "B) Sadece madencilik",
            "C) Okyanus balıkçılığı",
            "D) Doğal güzellikleri ve turizm/coğrafi önemi",
            "E) Sadece ağır sanayi"
          ],
          "correct": 3,
          "solution": "Doğru cevap Doğal güzellikleri ve turizm/coğrafi önemi.",
          "id": "e4_q105",
          "no": 105
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'Cumhurbaşkanlığı' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-43)",
          "options": [
            "A) Cumhurbaşkanlığı yabancı bir kurumdur.",
            "B) Cumhurbaşkanlığı özel bir şirkettir.",
            "C) Cumhurbaşkanlığı yasaklanmıştır.",
            "D) Cumhurbaşkanlığı sadece köylerde bulunur.",
            "E) Cumhurbaşkanlığı, anayasal sistemin önemli bir parçasıdır."
          ],
          "correct": 4,
          "solution": "Doğru cevap Cumhurbaşkanlığı, anayasal sistemin önemli bir parçasıdır..",
          "id": "e4_q106",
          "no": 106
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'Sayıştay' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-44)",
          "options": [
            "A) Sayıştay yasaklanmıştır.",
            "B) Sayıştay özel bir şirkettir.",
            "C) Sayıştay sadece köylerde bulunur.",
            "D) Sayıştay, anayasal sistemin önemli bir parçasıdır.",
            "E) Sayıştay yabancı bir kurumdur."
          ],
          "correct": 3,
          "solution": "Doğru cevap Sayıştay, anayasal sistemin önemli bir parçasıdır..",
          "id": "e4_q107",
          "no": 107
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'YSK' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-45)",
          "options": [
            "A) YSK özel bir şirkettir.",
            "B) YSK yabancı bir kurumdur.",
            "C) YSK yasaklanmıştır.",
            "D) YSK sadece köylerde bulunur.",
            "E) YSK, anayasal sistemin önemli bir parçasıdır."
          ],
          "correct": 4,
          "solution": "Doğru cevap YSK, anayasal sistemin önemli bir parçasıdır..",
          "id": "e4_q108",
          "no": 108
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'HSK' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-46)",
          "options": [
            "A) HSK sadece köylerde bulunur.",
            "B) HSK yabancı bir kurumdur.",
            "C) HSK yasaklanmıştır.",
            "D) HSK özel bir şirkettir.",
            "E) HSK, anayasal sistemin önemli bir parçasıdır."
          ],
          "correct": 4,
          "solution": "Doğru cevap HSK, anayasal sistemin önemli bir parçasıdır..",
          "id": "e4_q109",
          "no": 109
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'Belediye' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-47)",
          "options": [
            "A) Belediye sadece köylerde bulunur.",
            "B) Belediye yabancı bir kurumdur.",
            "C) Belediye özel bir şirkettir.",
            "D) Belediye yasaklanmıştır.",
            "E) Belediye, anayasal sistemin önemli bir parçasıdır."
          ],
          "correct": 4,
          "solution": "Doğru cevap Belediye, anayasal sistemin önemli bir parçasıdır..",
          "id": "e4_q110",
          "no": 110
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'Valilik' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-48)",
          "options": [
            "A) Valilik, anayasal sistemin önemli bir parçasıdır.",
            "B) Valilik sadece köylerde bulunur.",
            "C) Valilik özel bir şirkettir.",
            "D) Valilik yasaklanmıştır.",
            "E) Valilik yabancı bir kurumdur."
          ],
          "correct": 0,
          "solution": "Doğru cevap Valilik, anayasal sistemin önemli bir parçasıdır..",
          "id": "e4_q111",
          "no": 111
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'Kaymakamlık' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-49)",
          "options": [
            "A) Kaymakamlık sadece köylerde bulunur.",
            "B) Kaymakamlık yabancı bir kurumdur.",
            "C) Kaymakamlık özel bir şirkettir.",
            "D) Kaymakamlık yasaklanmıştır.",
            "E) Kaymakamlık, anayasal sistemin önemli bir parçasıdır."
          ],
          "correct": 4,
          "solution": "Doğru cevap Kaymakamlık, anayasal sistemin önemli bir parçasıdır..",
          "id": "e4_q112",
          "no": 112
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'İl Genel Meclisi' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-50)",
          "options": [
            "A) İl Genel Meclisi yasaklanmıştır.",
            "B) İl Genel Meclisi yabancı bir kurumdur.",
            "C) İl Genel Meclisi, anayasal sistemin önemli bir parçasıdır.",
            "D) İl Genel Meclisi özel bir şirkettir.",
            "E) İl Genel Meclisi sadece köylerde bulunur."
          ],
          "correct": 2,
          "solution": "Doğru cevap İl Genel Meclisi, anayasal sistemin önemli bir parçasıdır..",
          "id": "e4_q113",
          "no": 113
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'Kamu Denetçiliği Kurumu' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-51)",
          "options": [
            "A) Kamu Denetçiliği Kurumu, anayasal sistemin önemli bir parçasıdır.",
            "B) Kamu Denetçiliği Kurumu özel bir şirkettir.",
            "C) Kamu Denetçiliği Kurumu yabancı bir kurumdur.",
            "D) Kamu Denetçiliği Kurumu sadece köylerde bulunur.",
            "E) Kamu Denetçiliği Kurumu yasaklanmıştır."
          ],
          "correct": 0,
          "solution": "Doğru cevap Kamu Denetçiliği Kurumu, anayasal sistemin önemli bir parçasıdır..",
          "id": "e4_q114",
          "no": 114
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'Anayasa Mahkemesi' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-52)",
          "options": [
            "A) Anayasa Mahkemesi, anayasal sistemin önemli bir parçasıdır.",
            "B) Anayasa Mahkemesi sadece köylerde bulunur.",
            "C) Anayasa Mahkemesi yabancı bir kurumdur.",
            "D) Anayasa Mahkemesi yasaklanmıştır.",
            "E) Anayasa Mahkemesi özel bir şirkettir."
          ],
          "correct": 0,
          "solution": "Doğru cevap Anayasa Mahkemesi, anayasal sistemin önemli bir parçasıdır..",
          "id": "e4_q115",
          "no": 115
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'Yargıtay' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-53)",
          "options": [
            "A) Yargıtay, anayasal sistemin önemli bir parçasıdır.",
            "B) Yargıtay sadece köylerde bulunur.",
            "C) Yargıtay özel bir şirkettir.",
            "D) Yargıtay yasaklanmıştır.",
            "E) Yargıtay yabancı bir kurumdur."
          ],
          "correct": 0,
          "solution": "Doğru cevap Yargıtay, anayasal sistemin önemli bir parçasıdır..",
          "id": "e4_q116",
          "no": 116
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'Danıştay' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-54)",
          "options": [
            "A) Danıştay yabancı bir kurumdur.",
            "B) Danıştay yasaklanmıştır.",
            "C) Danıştay, anayasal sistemin önemli bir parçasıdır.",
            "D) Danıştay sadece köylerde bulunur.",
            "E) Danıştay özel bir şirkettir."
          ],
          "correct": 2,
          "solution": "Doğru cevap Danıştay, anayasal sistemin önemli bir parçasıdır..",
          "id": "e4_q117",
          "no": 117
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'TBMM' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-55)",
          "options": [
            "A) TBMM yabancı bir kurumdur.",
            "B) TBMM sadece köylerde bulunur.",
            "C) TBMM özel bir şirkettir.",
            "D) TBMM yasaklanmıştır.",
            "E) TBMM, anayasal sistemin önemli bir parçasıdır."
          ],
          "correct": 4,
          "solution": "Doğru cevap TBMM, anayasal sistemin önemli bir parçasıdır..",
          "id": "e4_q118",
          "no": 118
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'Cumhurbaşkanlığı' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-56)",
          "options": [
            "A) Cumhurbaşkanlığı özel bir şirkettir.",
            "B) Cumhurbaşkanlığı yabancı bir kurumdur.",
            "C) Cumhurbaşkanlığı sadece köylerde bulunur.",
            "D) Cumhurbaşkanlığı yasaklanmıştır.",
            "E) Cumhurbaşkanlığı, anayasal sistemin önemli bir parçasıdır."
          ],
          "correct": 4,
          "solution": "Doğru cevap Cumhurbaşkanlığı, anayasal sistemin önemli bir parçasıdır..",
          "id": "e4_q119",
          "no": 119
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'Sayıştay' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-57)",
          "options": [
            "A) Sayıştay özel bir şirkettir.",
            "B) Sayıştay yasaklanmıştır.",
            "C) Sayıştay sadece köylerde bulunur.",
            "D) Sayıştay, anayasal sistemin önemli bir parçasıdır.",
            "E) Sayıştay yabancı bir kurumdur."
          ],
          "correct": 3,
          "solution": "Doğru cevap Sayıştay, anayasal sistemin önemli bir parçasıdır..",
          "id": "e4_q120",
          "no": 120
        }
      ]
    },
    {
      "id": "deneme_5",
      "name": "5. Deneme Sınavı",
      "totalQuestions": 120,
      "duration": 130,
      "distribution": {
        "Türkçe": 30,
        "Matematik": 30,
        "Tarih": 27,
        "Coğrafya": 18,
        "Vatandaşlık": 15
      },
      "questions": [
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde 'hiçbir' kelimesinin yazımıyla ilgili bir kural hatırlatılmaktadır? (T-115)",
          "options": [
            "A) hiçbir cümlede özne olamaz.",
            "B) hiçbir kelimesi fiildir.",
            "C) hiçbir kelimesi yabancı kökenlidir.",
            "D) hiçbir kelimesi her zaman ayrı yazılır.",
            "E) 'hiçbir' kelimesinin doğru yazımına dikkat edilmelidir."
          ],
          "correct": 4,
          "solution": "Doğru cevap 'hiçbir' kelimesinin doğru yazımına dikkat edilmelidir..",
          "id": "e5_q1",
          "no": 1
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde mecaz anlamlı bir sözcük kullanılmıştır? (T-116)",
          "options": [
            "A) Kışın havalar soğuk olur.",
            "B) Buzdolabı soğuk üflüyor.",
            "C) Suyu dolaptan soğuk içti.",
            "D) Hava bugün çok soğuk.",
            "E) Olaylara karşı çok 'soğuk' davranıyordu."
          ],
          "correct": 4,
          "solution": "Doğru cevap Olaylara karşı çok 'soğuk' davranıyordu..",
          "id": "e5_q2",
          "no": 2
        },
        {
          "subject": "Türkçe",
          "text": "Bilim tarih boyunca insanlığın en büyük rehberlerinden biri olmuştur. Toplumlar Bilim sayesinde sınırlarını aşmış, geleceğe umutla bakabilmiştir. (P-117)\nBu parçanın ana düşüncesi nedir?",
          "options": [
            "A) Bilim, toplumsal ilerleme ve vizyon için vazgeçilmezdir.",
            "B) İnsanlar Bilim ile ilgilenmemelidir.",
            "C) Bilim sadece bireyseldir.",
            "D) Bilim sadece geçmişte kalmıştır.",
            "E) Bilim zaman kaybıdır."
          ],
          "correct": 0,
          "solution": "Doğru cevap Bilim, toplumsal ilerleme ve vizyon için vazgeçilmezdir..",
          "id": "e5_q3",
          "no": 3
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde 'her şey' kelimesinin yazımıyla ilgili bir kural hatırlatılmaktadır? (T-118)",
          "options": [
            "A) 'her şey' kelimesinin doğru yazımına dikkat edilmelidir.",
            "B) her şey cümlede özne olamaz.",
            "C) her şey kelimesi fiildir.",
            "D) her şey kelimesi her zaman ayrı yazılır.",
            "E) her şey kelimesi yabancı kökenlidir."
          ],
          "correct": 0,
          "solution": "Doğru cevap 'her şey' kelimesinin doğru yazımına dikkat edilmelidir..",
          "id": "e5_q4",
          "no": 4
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde mecaz anlamlı bir sözcük kullanılmıştır? (T-119)",
          "options": [
            "A) Hava bugün çok soğuk.",
            "B) Buzdolabı soğuk üflüyor.",
            "C) Olaylara karşı çok 'soğuk' davranıyordu.",
            "D) Suyu dolaptan soğuk içti.",
            "E) Kışın havalar soğuk olur."
          ],
          "correct": 2,
          "solution": "Doğru cevap Olaylara karşı çok 'soğuk' davranıyordu..",
          "id": "e5_q5",
          "no": 5
        },
        {
          "subject": "Türkçe",
          "text": "Sanat tarih boyunca insanlığın en büyük rehberlerinden biri olmuştur. Toplumlar Sanat sayesinde sınırlarını aşmış, geleceğe umutla bakabilmiştir. (P-120)\nBu parçanın ana düşüncesi nedir?",
          "options": [
            "A) İnsanlar Sanat ile ilgilenmemelidir.",
            "B) Sanat sadece geçmişte kalmıştır.",
            "C) Sanat zaman kaybıdır.",
            "D) Sanat, toplumsal ilerleme ve vizyon için vazgeçilmezdir.",
            "E) Sanat sadece bireyseldir."
          ],
          "correct": 3,
          "solution": "Doğru cevap Sanat, toplumsal ilerleme ve vizyon için vazgeçilmezdir..",
          "id": "e5_q6",
          "no": 6
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde 'yanlış' kelimesinin yazımıyla ilgili bir kural hatırlatılmaktadır? (T-121)",
          "options": [
            "A) yanlış kelimesi fiildir.",
            "B) yanlış kelimesi yabancı kökenlidir.",
            "C) 'yanlış' kelimesinin doğru yazımına dikkat edilmelidir.",
            "D) yanlış kelimesi her zaman ayrı yazılır.",
            "E) yanlış cümlede özne olamaz."
          ],
          "correct": 2,
          "solution": "Doğru cevap 'yanlış' kelimesinin doğru yazımına dikkat edilmelidir..",
          "id": "e5_q7",
          "no": 7
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde mecaz anlamlı bir sözcük kullanılmıştır? (T-122)",
          "options": [
            "A) Suyu dolaptan soğuk içti.",
            "B) Buzdolabı soğuk üflüyor.",
            "C) Kışın havalar soğuk olur.",
            "D) Olaylara karşı çok 'soğuk' davranıyordu.",
            "E) Hava bugün çok soğuk."
          ],
          "correct": 3,
          "solution": "Doğru cevap Olaylara karşı çok 'soğuk' davranıyordu..",
          "id": "e5_q8",
          "no": 8
        },
        {
          "subject": "Türkçe",
          "text": "Teknoloji tarih boyunca insanlığın en büyük rehberlerinden biri olmuştur. Toplumlar Teknoloji sayesinde sınırlarını aşmış, geleceğe umutla bakabilmiştir. (P-123)\nBu parçanın ana düşüncesi nedir?",
          "options": [
            "A) İnsanlar Teknoloji ile ilgilenmemelidir.",
            "B) Teknoloji zaman kaybıdır.",
            "C) Teknoloji sadece bireyseldir.",
            "D) Teknoloji sadece geçmişte kalmıştır.",
            "E) Teknoloji, toplumsal ilerleme ve vizyon için vazgeçilmezdir."
          ],
          "correct": 4,
          "solution": "Doğru cevap Teknoloji, toplumsal ilerleme ve vizyon için vazgeçilmezdir..",
          "id": "e5_q9",
          "no": 9
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde 'birkaç' kelimesinin yazımıyla ilgili bir kural hatırlatılmaktadır? (T-124)",
          "options": [
            "A) birkaç cümlede özne olamaz.",
            "B) 'birkaç' kelimesinin doğru yazımına dikkat edilmelidir.",
            "C) birkaç kelimesi yabancı kökenlidir.",
            "D) birkaç kelimesi her zaman ayrı yazılır.",
            "E) birkaç kelimesi fiildir."
          ],
          "correct": 1,
          "solution": "Doğru cevap 'birkaç' kelimesinin doğru yazımına dikkat edilmelidir..",
          "id": "e5_q10",
          "no": 10
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde mecaz anlamlı bir sözcük kullanılmıştır? (T-125)",
          "options": [
            "A) Hava bugün çok soğuk.",
            "B) Buzdolabı soğuk üflüyor.",
            "C) Suyu dolaptan soğuk içti.",
            "D) Kışın havalar soğuk olur.",
            "E) Olaylara karşı çok 'soğuk' davranıyordu."
          ],
          "correct": 4,
          "solution": "Doğru cevap Olaylara karşı çok 'soğuk' davranıyordu..",
          "id": "e5_q11",
          "no": 11
        },
        {
          "subject": "Türkçe",
          "text": "Doğa tarih boyunca insanlığın en büyük rehberlerinden biri olmuştur. Toplumlar Doğa sayesinde sınırlarını aşmış, geleceğe umutla bakabilmiştir. (P-126)\nBu parçanın ana düşüncesi nedir?",
          "options": [
            "A) Doğa, toplumsal ilerleme ve vizyon için vazgeçilmezdir.",
            "B) Doğa sadece bireyseldir.",
            "C) İnsanlar Doğa ile ilgilenmemelidir.",
            "D) Doğa sadece geçmişte kalmıştır.",
            "E) Doğa zaman kaybıdır."
          ],
          "correct": 0,
          "solution": "Doğru cevap Doğa, toplumsal ilerleme ve vizyon için vazgeçilmezdir..",
          "id": "e5_q12",
          "no": 12
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde 'hiç kimse' kelimesinin yazımıyla ilgili bir kural hatırlatılmaktadır? (T-127)",
          "options": [
            "A) hiç kimse kelimesi fiildir.",
            "B) hiç kimse kelimesi her zaman ayrı yazılır.",
            "C) 'hiç kimse' kelimesinin doğru yazımına dikkat edilmelidir.",
            "D) hiç kimse cümlede özne olamaz.",
            "E) hiç kimse kelimesi yabancı kökenlidir."
          ],
          "correct": 2,
          "solution": "Doğru cevap 'hiç kimse' kelimesinin doğru yazımına dikkat edilmelidir..",
          "id": "e5_q13",
          "no": 13
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde mecaz anlamlı bir sözcük kullanılmıştır? (T-128)",
          "options": [
            "A) Buzdolabı soğuk üflüyor.",
            "B) Olaylara karşı çok 'soğuk' davranıyordu.",
            "C) Kışın havalar soğuk olur.",
            "D) Suyu dolaptan soğuk içti.",
            "E) Hava bugün çok soğuk."
          ],
          "correct": 1,
          "solution": "Doğru cevap Olaylara karşı çok 'soğuk' davranıyordu..",
          "id": "e5_q14",
          "no": 14
        },
        {
          "subject": "Türkçe",
          "text": "Psikoloji tarih boyunca insanlığın en büyük rehberlerinden biri olmuştur. Toplumlar Psikoloji sayesinde sınırlarını aşmış, geleceğe umutla bakabilmiştir. (P-129)\nBu parçanın ana düşüncesi nedir?",
          "options": [
            "A) İnsanlar Psikoloji ile ilgilenmemelidir.",
            "B) Psikoloji sadece geçmişte kalmıştır.",
            "C) Psikoloji sadece bireyseldir.",
            "D) Psikoloji zaman kaybıdır.",
            "E) Psikoloji, toplumsal ilerleme ve vizyon için vazgeçilmezdir."
          ],
          "correct": 4,
          "solution": "Doğru cevap Psikoloji, toplumsal ilerleme ve vizyon için vazgeçilmezdir..",
          "id": "e5_q15",
          "no": 15
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde 'herkes' kelimesinin yazımıyla ilgili bir kural hatırlatılmaktadır? (T-130)",
          "options": [
            "A) herkes cümlede özne olamaz.",
            "B) herkes kelimesi fiildir.",
            "C) 'herkes' kelimesinin doğru yazımına dikkat edilmelidir.",
            "D) herkes kelimesi yabancı kökenlidir.",
            "E) herkes kelimesi her zaman ayrı yazılır."
          ],
          "correct": 2,
          "solution": "Doğru cevap 'herkes' kelimesinin doğru yazımına dikkat edilmelidir..",
          "id": "e5_q16",
          "no": 16
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde mecaz anlamlı bir sözcük kullanılmıştır? (T-131)",
          "options": [
            "A) Suyu dolaptan soğuk içti.",
            "B) Buzdolabı soğuk üflüyor.",
            "C) Olaylara karşı çok 'soğuk' davranıyordu.",
            "D) Kışın havalar soğuk olur.",
            "E) Hava bugün çok soğuk."
          ],
          "correct": 2,
          "solution": "Doğru cevap Olaylara karşı çok 'soğuk' davranıyordu..",
          "id": "e5_q17",
          "no": 17
        },
        {
          "subject": "Türkçe",
          "text": "Eğitim tarih boyunca insanlığın en büyük rehberlerinden biri olmuştur. Toplumlar Eğitim sayesinde sınırlarını aşmış, geleceğe umutla bakabilmiştir. (P-132)\nBu parçanın ana düşüncesi nedir?",
          "options": [
            "A) Eğitim sadece bireyseldir.",
            "B) Eğitim sadece geçmişte kalmıştır.",
            "C) Eğitim zaman kaybıdır.",
            "D) Eğitim, toplumsal ilerleme ve vizyon için vazgeçilmezdir.",
            "E) İnsanlar Eğitim ile ilgilenmemelidir."
          ],
          "correct": 3,
          "solution": "Doğru cevap Eğitim, toplumsal ilerleme ve vizyon için vazgeçilmezdir..",
          "id": "e5_q18",
          "no": 18
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde 'bugün' kelimesinin yazımıyla ilgili bir kural hatırlatılmaktadır? (T-133)",
          "options": [
            "A) bugün kelimesi her zaman ayrı yazılır.",
            "B) bugün kelimesi yabancı kökenlidir.",
            "C) bugün cümlede özne olamaz.",
            "D) 'bugün' kelimesinin doğru yazımına dikkat edilmelidir.",
            "E) bugün kelimesi fiildir."
          ],
          "correct": 3,
          "solution": "Doğru cevap 'bugün' kelimesinin doğru yazımına dikkat edilmelidir..",
          "id": "e5_q19",
          "no": 19
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde mecaz anlamlı bir sözcük kullanılmıştır? (T-134)",
          "options": [
            "A) Olaylara karşı çok 'soğuk' davranıyordu.",
            "B) Hava bugün çok soğuk.",
            "C) Buzdolabı soğuk üflüyor.",
            "D) Suyu dolaptan soğuk içti.",
            "E) Kışın havalar soğuk olur."
          ],
          "correct": 0,
          "solution": "Doğru cevap Olaylara karşı çok 'soğuk' davranıyordu..",
          "id": "e5_q20",
          "no": 20
        },
        {
          "subject": "Türkçe",
          "text": "Kültür tarih boyunca insanlığın en büyük rehberlerinden biri olmuştur. Toplumlar Kültür sayesinde sınırlarını aşmış, geleceğe umutla bakabilmiştir. (P-135)\nBu parçanın ana düşüncesi nedir?",
          "options": [
            "A) Kültür sadece bireyseldir.",
            "B) İnsanlar Kültür ile ilgilenmemelidir.",
            "C) Kültür sadece geçmişte kalmıştır.",
            "D) Kültür zaman kaybıdır.",
            "E) Kültür, toplumsal ilerleme ve vizyon için vazgeçilmezdir."
          ],
          "correct": 4,
          "solution": "Doğru cevap Kültür, toplumsal ilerleme ve vizyon için vazgeçilmezdir..",
          "id": "e5_q21",
          "no": 21
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde 'yalnız' kelimesinin yazımıyla ilgili bir kural hatırlatılmaktadır? (T-136)",
          "options": [
            "A) yalnız cümlede özne olamaz.",
            "B) yalnız kelimesi yabancı kökenlidir.",
            "C) yalnız kelimesi fiildir.",
            "D) yalnız kelimesi her zaman ayrı yazılır.",
            "E) 'yalnız' kelimesinin doğru yazımına dikkat edilmelidir."
          ],
          "correct": 4,
          "solution": "Doğru cevap 'yalnız' kelimesinin doğru yazımına dikkat edilmelidir..",
          "id": "e5_q22",
          "no": 22
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde mecaz anlamlı bir sözcük kullanılmıştır? (T-137)",
          "options": [
            "A) Buzdolabı soğuk üflüyor.",
            "B) Olaylara karşı çok 'soğuk' davranıyordu.",
            "C) Suyu dolaptan soğuk içti.",
            "D) Hava bugün çok soğuk.",
            "E) Kışın havalar soğuk olur."
          ],
          "correct": 1,
          "solution": "Doğru cevap Olaylara karşı çok 'soğuk' davranıyordu..",
          "id": "e5_q23",
          "no": 23
        },
        {
          "subject": "Türkçe",
          "text": "Felsefe tarih boyunca insanlığın en büyük rehberlerinden biri olmuştur. Toplumlar Felsefe sayesinde sınırlarını aşmış, geleceğe umutla bakabilmiştir. (P-138)\nBu parçanın ana düşüncesi nedir?",
          "options": [
            "A) Felsefe, toplumsal ilerleme ve vizyon için vazgeçilmezdir.",
            "B) Felsefe sadece geçmişte kalmıştır.",
            "C) Felsefe zaman kaybıdır.",
            "D) İnsanlar Felsefe ile ilgilenmemelidir.",
            "E) Felsefe sadece bireyseldir."
          ],
          "correct": 0,
          "solution": "Doğru cevap Felsefe, toplumsal ilerleme ve vizyon için vazgeçilmezdir..",
          "id": "e5_q24",
          "no": 24
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde 'hiçbir' kelimesinin yazımıyla ilgili bir kural hatırlatılmaktadır? (T-139)",
          "options": [
            "A) hiçbir kelimesi fiildir.",
            "B) 'hiçbir' kelimesinin doğru yazımına dikkat edilmelidir.",
            "C) hiçbir kelimesi her zaman ayrı yazılır.",
            "D) hiçbir kelimesi yabancı kökenlidir.",
            "E) hiçbir cümlede özne olamaz."
          ],
          "correct": 1,
          "solution": "Doğru cevap 'hiçbir' kelimesinin doğru yazımına dikkat edilmelidir..",
          "id": "e5_q25",
          "no": 25
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde mecaz anlamlı bir sözcük kullanılmıştır? (T-140)",
          "options": [
            "A) Suyu dolaptan soğuk içti.",
            "B) Hava bugün çok soğuk.",
            "C) Kışın havalar soğuk olur.",
            "D) Olaylara karşı çok 'soğuk' davranıyordu.",
            "E) Buzdolabı soğuk üflüyor."
          ],
          "correct": 3,
          "solution": "Doğru cevap Olaylara karşı çok 'soğuk' davranıyordu..",
          "id": "e5_q26",
          "no": 26
        },
        {
          "subject": "Türkçe",
          "text": "Edebiyat tarih boyunca insanlığın en büyük rehberlerinden biri olmuştur. Toplumlar Edebiyat sayesinde sınırlarını aşmış, geleceğe umutla bakabilmiştir. (P-141)\nBu parçanın ana düşüncesi nedir?",
          "options": [
            "A) Edebiyat zaman kaybıdır.",
            "B) Edebiyat, toplumsal ilerleme ve vizyon için vazgeçilmezdir.",
            "C) Edebiyat sadece bireyseldir.",
            "D) İnsanlar Edebiyat ile ilgilenmemelidir.",
            "E) Edebiyat sadece geçmişte kalmıştır."
          ],
          "correct": 1,
          "solution": "Doğru cevap Edebiyat, toplumsal ilerleme ve vizyon için vazgeçilmezdir..",
          "id": "e5_q27",
          "no": 27
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde 'her şey' kelimesinin yazımıyla ilgili bir kural hatırlatılmaktadır? (T-142)",
          "options": [
            "A) her şey kelimesi yabancı kökenlidir.",
            "B) 'her şey' kelimesinin doğru yazımına dikkat edilmelidir.",
            "C) her şey kelimesi fiildir.",
            "D) her şey cümlede özne olamaz.",
            "E) her şey kelimesi her zaman ayrı yazılır."
          ],
          "correct": 1,
          "solution": "Doğru cevap 'her şey' kelimesinin doğru yazımına dikkat edilmelidir..",
          "id": "e5_q28",
          "no": 28
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde mecaz anlamlı bir sözcük kullanılmıştır? (T-143)",
          "options": [
            "A) Hava bugün çok soğuk.",
            "B) Kışın havalar soğuk olur.",
            "C) Buzdolabı soğuk üflüyor.",
            "D) Suyu dolaptan soğuk içti.",
            "E) Olaylara karşı çok 'soğuk' davranıyordu."
          ],
          "correct": 4,
          "solution": "Doğru cevap Olaylara karşı çok 'soğuk' davranıyordu..",
          "id": "e5_q29",
          "no": 29
        },
        {
          "subject": "Türkçe",
          "text": "Tarih tarih boyunca insanlığın en büyük rehberlerinden biri olmuştur. Toplumlar Tarih sayesinde sınırlarını aşmış, geleceğe umutla bakabilmiştir. (P-144)\nBu parçanın ana düşüncesi nedir?",
          "options": [
            "A) Tarih, toplumsal ilerleme ve vizyon için vazgeçilmezdir.",
            "B) Tarih sadece bireyseldir.",
            "C) Tarih zaman kaybıdır.",
            "D) İnsanlar Tarih ile ilgilenmemelidir.",
            "E) Tarih sadece geçmişte kalmıştır."
          ],
          "correct": 0,
          "solution": "Doğru cevap Tarih, toplumsal ilerleme ve vizyon için vazgeçilmezdir..",
          "id": "e5_q30",
          "no": 30
        },
        {
          "subject": "Matematik",
          "text": "6x + 7 = 13 denkleminde x kaçtır? (SoruID: M120)",
          "options": [
            "A) 3",
            "B) 2",
            "C) 0",
            "D) 4",
            "E) 1"
          ],
          "correct": 4,
          "solution": "Doğru cevap 1.",
          "id": "e5_q31",
          "no": 31
        },
        {
          "subject": "Matematik",
          "text": "80 sayısının %40'si kaçtır? (SoruID: M121)",
          "options": [
            "A) 32",
            "B) 27",
            "C) 47",
            "D) 42",
            "E) 37"
          ],
          "correct": 0,
          "solution": "Doğru cevap 32.",
          "id": "e5_q32",
          "no": 32
        },
        {
          "subject": "Matematik",
          "text": "17, 22 ve 18 sayılarının aritmetik ortalaması kaçtır? (SoruID: M122)",
          "options": [
            "A) 21",
            "B) 19",
            "C) 20",
            "D) 18",
            "E) 17"
          ],
          "correct": 1,
          "solution": "Doğru cevap 19.",
          "id": "e5_q33",
          "no": 33
        },
        {
          "subject": "Matematik",
          "text": "Ali 25, Ayşe 17 yaşındadır. 5 yıl sonra yaşları toplamı kaç olur? (SoruID: M123)",
          "options": [
            "A) 47",
            "B) 51",
            "C) 52",
            "D) 57",
            "E) 53"
          ],
          "correct": 2,
          "solution": "Doğru cevap 52.",
          "id": "e5_q34",
          "no": 34
        },
        {
          "subject": "Matematik",
          "text": "√64 + √81 işleminin sonucu kaçtır? (SoruID: M124)",
          "options": [
            "A) 16",
            "B) 19",
            "C) 18",
            "D) 17",
            "E) 15"
          ],
          "correct": 3,
          "solution": "Doğru cevap 17.",
          "id": "e5_q35",
          "no": 35
        },
        {
          "subject": "Matematik",
          "text": "8x + 7 = 103 denkleminde x kaçtır? (SoruID: M125)",
          "options": [
            "A) 11",
            "B) 13",
            "C) 12",
            "D) 14",
            "E) 15"
          ],
          "correct": 2,
          "solution": "Doğru cevap 12.",
          "id": "e5_q36",
          "no": 36
        },
        {
          "subject": "Matematik",
          "text": "110 sayısının %50'si kaçtır? (SoruID: M126)",
          "options": [
            "A) 65",
            "B) 55",
            "C) 70",
            "D) 60",
            "E) 50"
          ],
          "correct": 1,
          "solution": "Doğru cevap 55.",
          "id": "e5_q37",
          "no": 37
        },
        {
          "subject": "Matematik",
          "text": "21, 29 ve 28 sayılarının aritmetik ortalaması kaçtır? (SoruID: M127)",
          "options": [
            "A) 28",
            "B) 24",
            "C) 25",
            "D) 26",
            "E) 27"
          ],
          "correct": 3,
          "solution": "Doğru cevap 26.",
          "id": "e5_q38",
          "no": 38
        },
        {
          "subject": "Matematik",
          "text": "Ali 16, Ayşe 12 yaşındadır. 5 yıl sonra yaşları toplamı kaç olur? (SoruID: M128)",
          "options": [
            "A) 43",
            "B) 33",
            "C) 38",
            "D) 37",
            "E) 39"
          ],
          "correct": 2,
          "solution": "Doğru cevap 38.",
          "id": "e5_q39",
          "no": 39
        },
        {
          "subject": "Matematik",
          "text": "√64 + √64 işleminin sonucu kaçtır? (SoruID: M129)",
          "options": [
            "A) 18",
            "B) 15",
            "C) 14",
            "D) 17",
            "E) 16"
          ],
          "correct": 4,
          "solution": "Doğru cevap 16.",
          "id": "e5_q40",
          "no": 40
        },
        {
          "subject": "Matematik",
          "text": "6x + 15 = 93 denkleminde x kaçtır? (SoruID: M130)",
          "options": [
            "A) 15",
            "B) 13",
            "C) 14",
            "D) 12",
            "E) 16"
          ],
          "correct": 1,
          "solution": "Doğru cevap 13.",
          "id": "e5_q41",
          "no": 41
        },
        {
          "subject": "Matematik",
          "text": "120 sayısının %25'si kaçtır? (SoruID: M131)",
          "options": [
            "A) 35",
            "B) 45",
            "C) 25",
            "D) 40",
            "E) 30"
          ],
          "correct": 4,
          "solution": "Doğru cevap 30.",
          "id": "e5_q42",
          "no": 42
        },
        {
          "subject": "Matematik",
          "text": "24, 27 ve 12 sayılarının aritmetik ortalaması kaçtır? (SoruID: M132)",
          "options": [
            "A) 22",
            "B) 21",
            "C) 19",
            "D) 23",
            "E) 20"
          ],
          "correct": 1,
          "solution": "Doğru cevap 21.",
          "id": "e5_q43",
          "no": 43
        },
        {
          "subject": "Matematik",
          "text": "Ali 16, Ayşe 25 yaşındadır. 3 yıl sonra yaşları toplamı kaç olur? (SoruID: M133)",
          "options": [
            "A) 50",
            "B) 46",
            "C) 48",
            "D) 47",
            "E) 44"
          ],
          "correct": 3,
          "solution": "Doğru cevap 47.",
          "id": "e5_q44",
          "no": 44
        },
        {
          "subject": "Matematik",
          "text": "√36 + √25 işleminin sonucu kaçtır? (SoruID: M134)",
          "options": [
            "A) 12",
            "B) 9",
            "C) 13",
            "D) 10",
            "E) 11"
          ],
          "correct": 4,
          "solution": "Doğru cevap 11.",
          "id": "e5_q45",
          "no": 45
        },
        {
          "subject": "Matematik",
          "text": "9x + 21 = 156 denkleminde x kaçtır? (SoruID: M135)",
          "options": [
            "A) 17",
            "B) 18",
            "C) 14",
            "D) 16",
            "E) 15"
          ],
          "correct": 4,
          "solution": "Doğru cevap 15.",
          "id": "e5_q46",
          "no": 46
        },
        {
          "subject": "Matematik",
          "text": "190 sayısının %10'si kaçtır? (SoruID: M136)",
          "options": [
            "A) 24",
            "B) 29",
            "C) 19",
            "D) 14",
            "E) 34"
          ],
          "correct": 2,
          "solution": "Doğru cevap 19.",
          "id": "e5_q47",
          "no": 47
        },
        {
          "subject": "Matematik",
          "text": "24, 12 ve 18 sayılarının aritmetik ortalaması kaçtır? (SoruID: M137)",
          "options": [
            "A) 20",
            "B) 17",
            "C) 19",
            "D) 16",
            "E) 18"
          ],
          "correct": 4,
          "solution": "Doğru cevap 18.",
          "id": "e5_q48",
          "no": 48
        },
        {
          "subject": "Matematik",
          "text": "Ali 12, Ayşe 24 yaşındadır. 5 yıl sonra yaşları toplamı kaç olur? (SoruID: M138)",
          "options": [
            "A) 47",
            "B) 41",
            "C) 46",
            "D) 45",
            "E) 51"
          ],
          "correct": 2,
          "solution": "Doğru cevap 46.",
          "id": "e5_q49",
          "no": 49
        },
        {
          "subject": "Matematik",
          "text": "√49 + √64 işleminin sonucu kaçtır? (SoruID: M139)",
          "options": [
            "A) 13",
            "B) 15",
            "C) 17",
            "D) 16",
            "E) 14"
          ],
          "correct": 1,
          "solution": "Doğru cevap 15.",
          "id": "e5_q50",
          "no": 50
        },
        {
          "subject": "Matematik",
          "text": "2x + 9 = 21 denkleminde x kaçtır? (SoruID: M140)",
          "options": [
            "A) 5",
            "B) 6",
            "C) 8",
            "D) 9",
            "E) 7"
          ],
          "correct": 1,
          "solution": "Doğru cevap 6.",
          "id": "e5_q51",
          "no": 51
        },
        {
          "subject": "Matematik",
          "text": "140 sayısının %25'si kaçtır? (SoruID: M141)",
          "options": [
            "A) 45",
            "B) 30",
            "C) 50",
            "D) 35",
            "E) 40"
          ],
          "correct": 3,
          "solution": "Doğru cevap 35.",
          "id": "e5_q52",
          "no": 52
        },
        {
          "subject": "Matematik",
          "text": "22, 12 ve 26 sayılarının aritmetik ortalaması kaçtır? (SoruID: M142)",
          "options": [
            "A) 20",
            "B) 21",
            "C) 18",
            "D) 19",
            "E) 22"
          ],
          "correct": 0,
          "solution": "Doğru cevap 20.",
          "id": "e5_q53",
          "no": 53
        },
        {
          "subject": "Matematik",
          "text": "Ali 12, Ayşe 10 yaşındadır. 7 yıl sonra yaşları toplamı kaç olur? (SoruID: M143)",
          "options": [
            "A) 29",
            "B) 37",
            "C) 35",
            "D) 36",
            "E) 43"
          ],
          "correct": 3,
          "solution": "Doğru cevap 36.",
          "id": "e5_q54",
          "no": 54
        },
        {
          "subject": "Matematik",
          "text": "√36 + √16 işleminin sonucu kaçtır? (SoruID: M144)",
          "options": [
            "A) 8",
            "B) 11",
            "C) 12",
            "D) 10",
            "E) 9"
          ],
          "correct": 3,
          "solution": "Doğru cevap 10.",
          "id": "e5_q55",
          "no": 55
        },
        {
          "subject": "Matematik",
          "text": "4x + 34 = 82 denkleminde x kaçtır? (SoruID: M145)",
          "options": [
            "A) 11",
            "B) 13",
            "C) 14",
            "D) 12",
            "E) 15"
          ],
          "correct": 3,
          "solution": "Doğru cevap 12.",
          "id": "e5_q56",
          "no": 56
        },
        {
          "subject": "Matematik",
          "text": "90 sayısının %75'si kaçtır? (SoruID: M146)",
          "options": [
            "A) 77",
            "B) 62",
            "C) 72",
            "D) 82",
            "E) 67"
          ],
          "correct": 4,
          "solution": "Doğru cevap 67.",
          "id": "e5_q57",
          "no": 57
        },
        {
          "subject": "Matematik",
          "text": "29, 26 ve 20 sayılarının aritmetik ortalaması kaçtır? (SoruID: M147)",
          "options": [
            "A) 24",
            "B) 25",
            "C) 23",
            "D) 27",
            "E) 26"
          ],
          "correct": 1,
          "solution": "Doğru cevap 25.",
          "id": "e5_q58",
          "no": 58
        },
        {
          "subject": "Matematik",
          "text": "Ali 24, Ayşe 19 yaşındadır. 5 yıl sonra yaşları toplamı kaç olur? (SoruID: M148)",
          "options": [
            "A) 48",
            "B) 52",
            "C) 58",
            "D) 53",
            "E) 54"
          ],
          "correct": 3,
          "solution": "Doğru cevap 53.",
          "id": "e5_q59",
          "no": 59
        },
        {
          "subject": "Matematik",
          "text": "√9 + √25 işleminin sonucu kaçtır? (SoruID: M149)",
          "options": [
            "A) 6",
            "B) 9",
            "C) 8",
            "D) 10",
            "E) 7"
          ],
          "correct": 2,
          "solution": "Doğru cevap 8.",
          "id": "e5_q60",
          "no": 60
        },
        {
          "subject": "Tarih",
          "text": "Türk siyasi ve askerî tarihinde büyük öneme sahip olan 'TBMM'nin Açılışı' süreci ile ilgili aşağıdakilerden hangisi söylenebilir? (H-105)",
          "options": [
            "A) Avrupa'da gerçekleşmiştir.",
            "B) Sadece ekonomik bir olaydır.",
            "C) TBMM'nin Açılışı dönemin en kritik gelişmelerinden biridir.",
            "D) Hiçbir etkisi olmamıştır.",
            "E) Osmanlı'nın kuruluş dönemine aittir."
          ],
          "correct": 2,
          "solution": "Doğru cevap TBMM'nin Açılışı dönemin en kritik gelişmelerinden biridir..",
          "id": "e5_q61",
          "no": 61
        },
        {
          "subject": "Tarih",
          "text": "Aşağıdaki tarihî gelişmelerden hangisi 'Mudanya Mütarekesi' ile doğrudan veya dolaylı olarak bağlantılıdır? (H-106)",
          "options": [
            "A) Sanayi İnkılabı",
            "B) Coğrafi Keşifler",
            "C) Fransız İhtilali",
            "D) Mudanya Mütarekesi öncesi ve sonrası yaşanan siyasi krizler.",
            "E) Kavimler Göçü"
          ],
          "correct": 3,
          "solution": "Doğru cevap Mudanya Mütarekesi öncesi ve sonrası yaşanan siyasi krizler..",
          "id": "e5_q62",
          "no": 62
        },
        {
          "subject": "Tarih",
          "text": "Millî Mücadele ve inkılaplar tarihi incelendiğinde 'Saltanatın Kaldırılması' olayının temel amacı aşağıdakilerden hangisidir? (H-107)",
          "options": [
            "A) Avrupa'ya göç etmek",
            "B) Bağımsızlık ve egemenliği pekiştirmek",
            "C) Feodaliteyi kurmak",
            "D) Yeni sömürgeler elde etmek",
            "E) Saltanatı güçlendirmek"
          ],
          "correct": 1,
          "solution": "Doğru cevap Bağımsızlık ve egemenliği pekiştirmek.",
          "id": "e5_q63",
          "no": 63
        },
        {
          "subject": "Tarih",
          "text": "Türk siyasi ve askerî tarihinde büyük öneme sahip olan 'Halifeliğin Kaldırılması' süreci ile ilgili aşağıdakilerden hangisi söylenebilir? (H-108)",
          "options": [
            "A) Hiçbir etkisi olmamıştır.",
            "B) Avrupa'da gerçekleşmiştir.",
            "C) Halifeliğin Kaldırılması dönemin en kritik gelişmelerinden biridir.",
            "D) Sadece ekonomik bir olaydır.",
            "E) Osmanlı'nın kuruluş dönemine aittir."
          ],
          "correct": 2,
          "solution": "Doğru cevap Halifeliğin Kaldırılması dönemin en kritik gelişmelerinden biridir..",
          "id": "e5_q64",
          "no": 64
        },
        {
          "subject": "Tarih",
          "text": "Aşağıdaki tarihî gelişmelerden hangisi 'Tevhid-i Tedrisat' ile doğrudan veya dolaylı olarak bağlantılıdır? (H-109)",
          "options": [
            "A) Fransız İhtilali",
            "B) Tevhid-i Tedrisat öncesi ve sonrası yaşanan siyasi krizler.",
            "C) Sanayi İnkılabı",
            "D) Coğrafi Keşifler",
            "E) Kavimler Göçü"
          ],
          "correct": 1,
          "solution": "Doğru cevap Tevhid-i Tedrisat öncesi ve sonrası yaşanan siyasi krizler..",
          "id": "e5_q65",
          "no": 65
        },
        {
          "subject": "Tarih",
          "text": "Millî Mücadele ve inkılaplar tarihi incelendiğinde 'Trablusgarp Savaşı' olayının temel amacı aşağıdakilerden hangisidir? (H-110)",
          "options": [
            "A) Avrupa'ya göç etmek",
            "B) Bağımsızlık ve egemenliği pekiştirmek",
            "C) Saltanatı güçlendirmek",
            "D) Yeni sömürgeler elde etmek",
            "E) Feodaliteyi kurmak"
          ],
          "correct": 1,
          "solution": "Doğru cevap Bağımsızlık ve egemenliği pekiştirmek.",
          "id": "e5_q66",
          "no": 66
        },
        {
          "subject": "Tarih",
          "text": "Türk siyasi ve askerî tarihinde büyük öneme sahip olan 'Balkan Savaşları' süreci ile ilgili aşağıdakilerden hangisi söylenebilir? (H-111)",
          "options": [
            "A) Balkan Savaşları dönemin en kritik gelişmelerinden biridir.",
            "B) Avrupa'da gerçekleşmiştir.",
            "C) Sadece ekonomik bir olaydır.",
            "D) Hiçbir etkisi olmamıştır.",
            "E) Osmanlı'nın kuruluş dönemine aittir."
          ],
          "correct": 0,
          "solution": "Doğru cevap Balkan Savaşları dönemin en kritik gelişmelerinden biridir..",
          "id": "e5_q67",
          "no": 67
        },
        {
          "subject": "Tarih",
          "text": "Aşağıdaki tarihî gelişmelerden hangisi 'I. Dünya Savaşı' ile doğrudan veya dolaylı olarak bağlantılıdır? (H-112)",
          "options": [
            "A) Sanayi İnkılabı",
            "B) Coğrafi Keşifler",
            "C) Kavimler Göçü",
            "D) I. Dünya Savaşı öncesi ve sonrası yaşanan siyasi krizler.",
            "E) Fransız İhtilali"
          ],
          "correct": 3,
          "solution": "Doğru cevap I. Dünya Savaşı öncesi ve sonrası yaşanan siyasi krizler..",
          "id": "e5_q68",
          "no": 68
        },
        {
          "subject": "Tarih",
          "text": "Millî Mücadele ve inkılaplar tarihi incelendiğinde 'Çanakkale Cephesi' olayının temel amacı aşağıdakilerden hangisidir? (H-113)",
          "options": [
            "A) Bağımsızlık ve egemenliği pekiştirmek",
            "B) Feodaliteyi kurmak",
            "C) Saltanatı güçlendirmek",
            "D) Yeni sömürgeler elde etmek",
            "E) Avrupa'ya göç etmek"
          ],
          "correct": 0,
          "solution": "Doğru cevap Bağımsızlık ve egemenliği pekiştirmek.",
          "id": "e5_q69",
          "no": 69
        },
        {
          "subject": "Tarih",
          "text": "Türk siyasi ve askerî tarihinde büyük öneme sahip olan 'Sakarya Meydan Muharebesi' süreci ile ilgili aşağıdakilerden hangisi söylenebilir? (H-114)",
          "options": [
            "A) Osmanlı'nın kuruluş dönemine aittir.",
            "B) Hiçbir etkisi olmamıştır.",
            "C) Avrupa'da gerçekleşmiştir.",
            "D) Sadece ekonomik bir olaydır.",
            "E) Sakarya Meydan Muharebesi dönemin en kritik gelişmelerinden biridir."
          ],
          "correct": 4,
          "solution": "Doğru cevap Sakarya Meydan Muharebesi dönemin en kritik gelişmelerinden biridir..",
          "id": "e5_q70",
          "no": 70
        },
        {
          "subject": "Tarih",
          "text": "Aşağıdaki tarihî gelişmelerden hangisi 'Büyük Taarruz' ile doğrudan veya dolaylı olarak bağlantılıdır? (H-115)",
          "options": [
            "A) Kavimler Göçü",
            "B) Coğrafi Keşifler",
            "C) Sanayi İnkılabı",
            "D) Fransız İhtilali",
            "E) Büyük Taarruz öncesi ve sonrası yaşanan siyasi krizler."
          ],
          "correct": 4,
          "solution": "Doğru cevap Büyük Taarruz öncesi ve sonrası yaşanan siyasi krizler..",
          "id": "e5_q71",
          "no": 71
        },
        {
          "subject": "Tarih",
          "text": "Millî Mücadele ve inkılaplar tarihi incelendiğinde 'I. İnönü Muharebesi' olayının temel amacı aşağıdakilerden hangisidir? (H-116)",
          "options": [
            "A) Yeni sömürgeler elde etmek",
            "B) Feodaliteyi kurmak",
            "C) Bağımsızlık ve egemenliği pekiştirmek",
            "D) Saltanatı güçlendirmek",
            "E) Avrupa'ya göç etmek"
          ],
          "correct": 2,
          "solution": "Doğru cevap Bağımsızlık ve egemenliği pekiştirmek.",
          "id": "e5_q72",
          "no": 72
        },
        {
          "subject": "Tarih",
          "text": "Türk siyasi ve askerî tarihinde büyük öneme sahip olan 'II. İnönü Muharebesi' süreci ile ilgili aşağıdakilerden hangisi söylenebilir? (H-117)",
          "options": [
            "A) II. İnönü Muharebesi dönemin en kritik gelişmelerinden biridir.",
            "B) Osmanlı'nın kuruluş dönemine aittir.",
            "C) Hiçbir etkisi olmamıştır.",
            "D) Sadece ekonomik bir olaydır.",
            "E) Avrupa'da gerçekleşmiştir."
          ],
          "correct": 0,
          "solution": "Doğru cevap II. İnönü Muharebesi dönemin en kritik gelişmelerinden biridir..",
          "id": "e5_q73",
          "no": 73
        },
        {
          "subject": "Tarih",
          "text": "Aşağıdaki tarihî gelişmelerden hangisi 'Kars Antlaşması' ile doğrudan veya dolaylı olarak bağlantılıdır? (H-118)",
          "options": [
            "A) Fransız İhtilali",
            "B) Kars Antlaşması öncesi ve sonrası yaşanan siyasi krizler.",
            "C) Sanayi İnkılabı",
            "D) Kavimler Göçü",
            "E) Coğrafi Keşifler"
          ],
          "correct": 1,
          "solution": "Doğru cevap Kars Antlaşması öncesi ve sonrası yaşanan siyasi krizler..",
          "id": "e5_q74",
          "no": 74
        },
        {
          "subject": "Tarih",
          "text": "Millî Mücadele ve inkılaplar tarihi incelendiğinde 'Ankara Antlaşması' olayının temel amacı aşağıdakilerden hangisidir? (H-119)",
          "options": [
            "A) Feodaliteyi kurmak",
            "B) Saltanatı güçlendirmek",
            "C) Bağımsızlık ve egemenliği pekiştirmek",
            "D) Avrupa'ya göç etmek",
            "E) Yeni sömürgeler elde etmek"
          ],
          "correct": 2,
          "solution": "Doğru cevap Bağımsızlık ve egemenliği pekiştirmek.",
          "id": "e5_q75",
          "no": 75
        },
        {
          "subject": "Tarih",
          "text": "Türk siyasi ve askerî tarihinde büyük öneme sahip olan 'Sivas Kongresi' süreci ile ilgili aşağıdakilerden hangisi söylenebilir? (H-120)",
          "options": [
            "A) Sivas Kongresi dönemin en kritik gelişmelerinden biridir.",
            "B) Avrupa'da gerçekleşmiştir.",
            "C) Hiçbir etkisi olmamıştır.",
            "D) Sadece ekonomik bir olaydır.",
            "E) Osmanlı'nın kuruluş dönemine aittir."
          ],
          "correct": 0,
          "solution": "Doğru cevap Sivas Kongresi dönemin en kritik gelişmelerinden biridir..",
          "id": "e5_q76",
          "no": 76
        },
        {
          "subject": "Tarih",
          "text": "Aşağıdaki tarihî gelişmelerden hangisi 'Erzurum Kongresi' ile doğrudan veya dolaylı olarak bağlantılıdır? (H-121)",
          "options": [
            "A) Sanayi İnkılabı",
            "B) Erzurum Kongresi öncesi ve sonrası yaşanan siyasi krizler.",
            "C) Kavimler Göçü",
            "D) Coğrafi Keşifler",
            "E) Fransız İhtilali"
          ],
          "correct": 1,
          "solution": "Doğru cevap Erzurum Kongresi öncesi ve sonrası yaşanan siyasi krizler..",
          "id": "e5_q77",
          "no": 77
        },
        {
          "subject": "Tarih",
          "text": "Millî Mücadele ve inkılaplar tarihi incelendiğinde 'Amasya Genelgesi' olayının temel amacı aşağıdakilerden hangisidir? (H-122)",
          "options": [
            "A) Yeni sömürgeler elde etmek",
            "B) Avrupa'ya göç etmek",
            "C) Bağımsızlık ve egemenliği pekiştirmek",
            "D) Feodaliteyi kurmak",
            "E) Saltanatı güçlendirmek"
          ],
          "correct": 2,
          "solution": "Doğru cevap Bağımsızlık ve egemenliği pekiştirmek.",
          "id": "e5_q78",
          "no": 78
        },
        {
          "subject": "Tarih",
          "text": "Türk siyasi ve askerî tarihinde büyük öneme sahip olan 'Lozan Antlaşması' süreci ile ilgili aşağıdakilerden hangisi söylenebilir? (H-123)",
          "options": [
            "A) Sadece ekonomik bir olaydır.",
            "B) Avrupa'da gerçekleşmiştir.",
            "C) Osmanlı'nın kuruluş dönemine aittir.",
            "D) Hiçbir etkisi olmamıştır.",
            "E) Lozan Antlaşması dönemin en kritik gelişmelerinden biridir."
          ],
          "correct": 4,
          "solution": "Doğru cevap Lozan Antlaşması dönemin en kritik gelişmelerinden biridir..",
          "id": "e5_q79",
          "no": 79
        },
        {
          "subject": "Tarih",
          "text": "Aşağıdaki tarihî gelişmelerden hangisi 'Cumhuriyetin İlanı' ile doğrudan veya dolaylı olarak bağlantılıdır? (H-124)",
          "options": [
            "A) Coğrafi Keşifler",
            "B) Fransız İhtilali",
            "C) Kavimler Göçü",
            "D) Cumhuriyetin İlanı öncesi ve sonrası yaşanan siyasi krizler.",
            "E) Sanayi İnkılabı"
          ],
          "correct": 3,
          "solution": "Doğru cevap Cumhuriyetin İlanı öncesi ve sonrası yaşanan siyasi krizler..",
          "id": "e5_q80",
          "no": 80
        },
        {
          "subject": "Tarih",
          "text": "Millî Mücadele ve inkılaplar tarihi incelendiğinde 'TBMM'nin Açılışı' olayının temel amacı aşağıdakilerden hangisidir? (H-125)",
          "options": [
            "A) Bağımsızlık ve egemenliği pekiştirmek",
            "B) Avrupa'ya göç etmek",
            "C) Yeni sömürgeler elde etmek",
            "D) Feodaliteyi kurmak",
            "E) Saltanatı güçlendirmek"
          ],
          "correct": 0,
          "solution": "Doğru cevap Bağımsızlık ve egemenliği pekiştirmek.",
          "id": "e5_q81",
          "no": 81
        },
        {
          "subject": "Tarih",
          "text": "Türk siyasi ve askerî tarihinde büyük öneme sahip olan 'Mudanya Mütarekesi' süreci ile ilgili aşağıdakilerden hangisi söylenebilir? (H-126)",
          "options": [
            "A) Osmanlı'nın kuruluş dönemine aittir.",
            "B) Avrupa'da gerçekleşmiştir.",
            "C) Mudanya Mütarekesi dönemin en kritik gelişmelerinden biridir.",
            "D) Hiçbir etkisi olmamıştır.",
            "E) Sadece ekonomik bir olaydır."
          ],
          "correct": 2,
          "solution": "Doğru cevap Mudanya Mütarekesi dönemin en kritik gelişmelerinden biridir..",
          "id": "e5_q82",
          "no": 82
        },
        {
          "subject": "Tarih",
          "text": "Aşağıdaki tarihî gelişmelerden hangisi 'Saltanatın Kaldırılması' ile doğrudan veya dolaylı olarak bağlantılıdır? (H-127)",
          "options": [
            "A) Sanayi İnkılabı",
            "B) Fransız İhtilali",
            "C) Saltanatın Kaldırılması öncesi ve sonrası yaşanan siyasi krizler.",
            "D) Kavimler Göçü",
            "E) Coğrafi Keşifler"
          ],
          "correct": 2,
          "solution": "Doğru cevap Saltanatın Kaldırılması öncesi ve sonrası yaşanan siyasi krizler..",
          "id": "e5_q83",
          "no": 83
        },
        {
          "subject": "Tarih",
          "text": "Millî Mücadele ve inkılaplar tarihi incelendiğinde 'Halifeliğin Kaldırılması' olayının temel amacı aşağıdakilerden hangisidir? (H-128)",
          "options": [
            "A) Bağımsızlık ve egemenliği pekiştirmek",
            "B) Feodaliteyi kurmak",
            "C) Saltanatı güçlendirmek",
            "D) Avrupa'ya göç etmek",
            "E) Yeni sömürgeler elde etmek"
          ],
          "correct": 0,
          "solution": "Doğru cevap Bağımsızlık ve egemenliği pekiştirmek.",
          "id": "e5_q84",
          "no": 84
        },
        {
          "subject": "Tarih",
          "text": "Türk siyasi ve askerî tarihinde büyük öneme sahip olan 'Tevhid-i Tedrisat' süreci ile ilgili aşağıdakilerden hangisi söylenebilir? (H-129)",
          "options": [
            "A) Sadece ekonomik bir olaydır.",
            "B) Avrupa'da gerçekleşmiştir.",
            "C) Hiçbir etkisi olmamıştır.",
            "D) Tevhid-i Tedrisat dönemin en kritik gelişmelerinden biridir.",
            "E) Osmanlı'nın kuruluş dönemine aittir."
          ],
          "correct": 3,
          "solution": "Doğru cevap Tevhid-i Tedrisat dönemin en kritik gelişmelerinden biridir..",
          "id": "e5_q85",
          "no": 85
        },
        {
          "subject": "Tarih",
          "text": "Aşağıdaki tarihî gelişmelerden hangisi 'Trablusgarp Savaşı' ile doğrudan veya dolaylı olarak bağlantılıdır? (H-130)",
          "options": [
            "A) Trablusgarp Savaşı öncesi ve sonrası yaşanan siyasi krizler.",
            "B) Sanayi İnkılabı",
            "C) Fransız İhtilali",
            "D) Coğrafi Keşifler",
            "E) Kavimler Göçü"
          ],
          "correct": 0,
          "solution": "Doğru cevap Trablusgarp Savaşı öncesi ve sonrası yaşanan siyasi krizler..",
          "id": "e5_q86",
          "no": 86
        },
        {
          "subject": "Tarih",
          "text": "Millî Mücadele ve inkılaplar tarihi incelendiğinde 'Balkan Savaşları' olayının temel amacı aşağıdakilerden hangisidir? (H-131)",
          "options": [
            "A) Saltanatı güçlendirmek",
            "B) Avrupa'ya göç etmek",
            "C) Feodaliteyi kurmak",
            "D) Bağımsızlık ve egemenliği pekiştirmek",
            "E) Yeni sömürgeler elde etmek"
          ],
          "correct": 3,
          "solution": "Doğru cevap Bağımsızlık ve egemenliği pekiştirmek.",
          "id": "e5_q87",
          "no": 87
        },
        {
          "subject": "Coğrafya",
          "text": "Türkiye'nin fiziki coğrafyası düşünüldüğünde 'Kapadokya' için aşağıdakilerden hangisi doğrudur? (C-70)",
          "options": [
            "A) Kapadokya bir çöldür.",
            "B) Kapadokya tarıma kapalıdır.",
            "C) Kapadokya Marmara'dadır.",
            "D) Kapadokya, ülkemizin önemli yeryüzü şekillerinden biridir.",
            "E) Kapadokya yapay bir kanaldır."
          ],
          "correct": 3,
          "solution": "Doğru cevap Kapadokya, ülkemizin önemli yeryüzü şekillerinden biridir..",
          "id": "e5_q88",
          "no": 88
        },
        {
          "subject": "Coğrafya",
          "text": "Coğrafi özellikleri ve turizm potansiyeli göz önüne alındığında 'Pamukkale' hangi alanda daha çok öne çıkar? (C-71)",
          "options": [
            "A) Doğal güzellikleri ve turizm/coğrafi önemi",
            "B) Sadece madencilik",
            "C) Sadece ağır sanayi",
            "D) Çöl iklimi araştırmaları",
            "E) Okyanus balıkçılığı"
          ],
          "correct": 0,
          "solution": "Doğru cevap Doğal güzellikleri ve turizm/coğrafi önemi.",
          "id": "e5_q89",
          "no": 89
        },
        {
          "subject": "Coğrafya",
          "text": "Türkiye'nin fiziki coğrafyası düşünüldüğünde 'Nemrut Dağı' için aşağıdakilerden hangisi doğrudur? (C-72)",
          "options": [
            "A) Nemrut Dağı Marmara'dadır.",
            "B) Nemrut Dağı bir çöldür.",
            "C) Nemrut Dağı tarıma kapalıdır.",
            "D) Nemrut Dağı yapay bir kanaldır.",
            "E) Nemrut Dağı, ülkemizin önemli yeryüzü şekillerinden biridir."
          ],
          "correct": 4,
          "solution": "Doğru cevap Nemrut Dağı, ülkemizin önemli yeryüzü şekillerinden biridir..",
          "id": "e5_q90",
          "no": 90
        },
        {
          "subject": "Coğrafya",
          "text": "Coğrafi özellikleri ve turizm potansiyeli göz önüne alındığında 'Sümela Manastırı' hangi alanda daha çok öne çıkar? (C-73)",
          "options": [
            "A) Çöl iklimi araştırmaları",
            "B) Sadece ağır sanayi",
            "C) Doğal güzellikleri ve turizm/coğrafi önemi",
            "D) Sadece madencilik",
            "E) Okyanus balıkçılığı"
          ],
          "correct": 2,
          "solution": "Doğru cevap Doğal güzellikleri ve turizm/coğrafi önemi.",
          "id": "e5_q91",
          "no": 91
        },
        {
          "subject": "Coğrafya",
          "text": "Türkiye'nin fiziki coğrafyası düşünüldüğünde 'Uludağ' için aşağıdakilerden hangisi doğrudur? (C-74)",
          "options": [
            "A) Uludağ yapay bir kanaldır.",
            "B) Uludağ tarıma kapalıdır.",
            "C) Uludağ bir çöldür.",
            "D) Uludağ Marmara'dadır.",
            "E) Uludağ, ülkemizin önemli yeryüzü şekillerinden biridir."
          ],
          "correct": 4,
          "solution": "Doğru cevap Uludağ, ülkemizin önemli yeryüzü şekillerinden biridir..",
          "id": "e5_q92",
          "no": 92
        },
        {
          "subject": "Coğrafya",
          "text": "Coğrafi özellikleri ve turizm potansiyeli göz önüne alındığında 'Van Gölü' hangi alanda daha çok öne çıkar? (C-75)",
          "options": [
            "A) Sadece madencilik",
            "B) Doğal güzellikleri ve turizm/coğrafi önemi",
            "C) Sadece ağır sanayi",
            "D) Okyanus balıkçılığı",
            "E) Çöl iklimi araştırmaları"
          ],
          "correct": 1,
          "solution": "Doğru cevap Doğal güzellikleri ve turizm/coğrafi önemi.",
          "id": "e5_q93",
          "no": 93
        },
        {
          "subject": "Coğrafya",
          "text": "Türkiye'nin fiziki coğrafyası düşünüldüğünde 'Ağrı Dağı' için aşağıdakilerden hangisi doğrudur? (C-76)",
          "options": [
            "A) Ağrı Dağı yapay bir kanaldır.",
            "B) Ağrı Dağı, ülkemizin önemli yeryüzü şekillerinden biridir.",
            "C) Ağrı Dağı Marmara'dadır.",
            "D) Ağrı Dağı tarıma kapalıdır.",
            "E) Ağrı Dağı bir çöldür."
          ],
          "correct": 1,
          "solution": "Doğru cevap Ağrı Dağı, ülkemizin önemli yeryüzü şekillerinden biridir..",
          "id": "e5_q94",
          "no": 94
        },
        {
          "subject": "Coğrafya",
          "text": "Coğrafi özellikleri ve turizm potansiyeli göz önüne alındığında 'Kızılırmak' hangi alanda daha çok öne çıkar? (C-77)",
          "options": [
            "A) Doğal güzellikleri ve turizm/coğrafi önemi",
            "B) Sadece madencilik",
            "C) Çöl iklimi araştırmaları",
            "D) Okyanus balıkçılığı",
            "E) Sadece ağır sanayi"
          ],
          "correct": 0,
          "solution": "Doğru cevap Doğal güzellikleri ve turizm/coğrafi önemi.",
          "id": "e5_q95",
          "no": 95
        },
        {
          "subject": "Coğrafya",
          "text": "Türkiye'nin fiziki coğrafyası düşünüldüğünde 'Erciyes Dağı' için aşağıdakilerden hangisi doğrudur? (C-78)",
          "options": [
            "A) Erciyes Dağı yapay bir kanaldır.",
            "B) Erciyes Dağı, ülkemizin önemli yeryüzü şekillerinden biridir.",
            "C) Erciyes Dağı tarıma kapalıdır.",
            "D) Erciyes Dağı Marmara'dadır.",
            "E) Erciyes Dağı bir çöldür."
          ],
          "correct": 1,
          "solution": "Doğru cevap Erciyes Dağı, ülkemizin önemli yeryüzü şekillerinden biridir..",
          "id": "e5_q96",
          "no": 96
        },
        {
          "subject": "Coğrafya",
          "text": "Coğrafi özellikleri ve turizm potansiyeli göz önüne alındığında 'Tuz Gölü' hangi alanda daha çok öne çıkar? (C-79)",
          "options": [
            "A) Doğal güzellikleri ve turizm/coğrafi önemi",
            "B) Çöl iklimi araştırmaları",
            "C) Sadece ağır sanayi",
            "D) Sadece madencilik",
            "E) Okyanus balıkçılığı"
          ],
          "correct": 0,
          "solution": "Doğru cevap Doğal güzellikleri ve turizm/coğrafi önemi.",
          "id": "e5_q97",
          "no": 97
        },
        {
          "subject": "Coğrafya",
          "text": "Türkiye'nin fiziki coğrafyası düşünüldüğünde 'Çukurova' için aşağıdakilerden hangisi doğrudur? (C-80)",
          "options": [
            "A) Çukurova bir çöldür.",
            "B) Çukurova yapay bir kanaldır.",
            "C) Çukurova tarıma kapalıdır.",
            "D) Çukurova Marmara'dadır.",
            "E) Çukurova, ülkemizin önemli yeryüzü şekillerinden biridir."
          ],
          "correct": 4,
          "solution": "Doğru cevap Çukurova, ülkemizin önemli yeryüzü şekillerinden biridir..",
          "id": "e5_q98",
          "no": 98
        },
        {
          "subject": "Coğrafya",
          "text": "Coğrafi özellikleri ve turizm potansiyeli göz önüne alındığında 'Bafra Ovası' hangi alanda daha çok öne çıkar? (C-81)",
          "options": [
            "A) Sadece madencilik",
            "B) Okyanus balıkçılığı",
            "C) Çöl iklimi araştırmaları",
            "D) Sadece ağır sanayi",
            "E) Doğal güzellikleri ve turizm/coğrafi önemi"
          ],
          "correct": 4,
          "solution": "Doğru cevap Doğal güzellikleri ve turizm/coğrafi önemi.",
          "id": "e5_q99",
          "no": 99
        },
        {
          "subject": "Coğrafya",
          "text": "Türkiye'nin fiziki coğrafyası düşünüldüğünde 'Kaçkar Dağları' için aşağıdakilerden hangisi doğrudur? (C-82)",
          "options": [
            "A) Kaçkar Dağları bir çöldür.",
            "B) Kaçkar Dağları, ülkemizin önemli yeryüzü şekillerinden biridir.",
            "C) Kaçkar Dağları yapay bir kanaldır.",
            "D) Kaçkar Dağları tarıma kapalıdır.",
            "E) Kaçkar Dağları Marmara'dadır."
          ],
          "correct": 1,
          "solution": "Doğru cevap Kaçkar Dağları, ülkemizin önemli yeryüzü şekillerinden biridir..",
          "id": "e5_q100",
          "no": 100
        },
        {
          "subject": "Coğrafya",
          "text": "Coğrafi özellikleri ve turizm potansiyeli göz önüne alındığında 'Gediz Nehri' hangi alanda daha çok öne çıkar? (C-83)",
          "options": [
            "A) Okyanus balıkçılığı",
            "B) Sadece madencilik",
            "C) Çöl iklimi araştırmaları",
            "D) Doğal güzellikleri ve turizm/coğrafi önemi",
            "E) Sadece ağır sanayi"
          ],
          "correct": 3,
          "solution": "Doğru cevap Doğal güzellikleri ve turizm/coğrafi önemi.",
          "id": "e5_q101",
          "no": 101
        },
        {
          "subject": "Coğrafya",
          "text": "Türkiye'nin fiziki coğrafyası düşünüldüğünde 'Salda Gölü' için aşağıdakilerden hangisi doğrudur? (C-84)",
          "options": [
            "A) Salda Gölü yapay bir kanaldır.",
            "B) Salda Gölü Marmara'dadır.",
            "C) Salda Gölü bir çöldür.",
            "D) Salda Gölü, ülkemizin önemli yeryüzü şekillerinden biridir.",
            "E) Salda Gölü tarıma kapalıdır."
          ],
          "correct": 3,
          "solution": "Doğru cevap Salda Gölü, ülkemizin önemli yeryüzü şekillerinden biridir..",
          "id": "e5_q102",
          "no": 102
        },
        {
          "subject": "Coğrafya",
          "text": "Coğrafi özellikleri ve turizm potansiyeli göz önüne alındığında 'Kapadokya' hangi alanda daha çok öne çıkar? (C-85)",
          "options": [
            "A) Çöl iklimi araştırmaları",
            "B) Doğal güzellikleri ve turizm/coğrafi önemi",
            "C) Okyanus balıkçılığı",
            "D) Sadece madencilik",
            "E) Sadece ağır sanayi"
          ],
          "correct": 1,
          "solution": "Doğru cevap Doğal güzellikleri ve turizm/coğrafi önemi.",
          "id": "e5_q103",
          "no": 103
        },
        {
          "subject": "Coğrafya",
          "text": "Türkiye'nin fiziki coğrafyası düşünüldüğünde 'Pamukkale' için aşağıdakilerden hangisi doğrudur? (C-86)",
          "options": [
            "A) Pamukkale, ülkemizin önemli yeryüzü şekillerinden biridir.",
            "B) Pamukkale tarıma kapalıdır.",
            "C) Pamukkale Marmara'dadır.",
            "D) Pamukkale yapay bir kanaldır.",
            "E) Pamukkale bir çöldür."
          ],
          "correct": 0,
          "solution": "Doğru cevap Pamukkale, ülkemizin önemli yeryüzü şekillerinden biridir..",
          "id": "e5_q104",
          "no": 104
        },
        {
          "subject": "Coğrafya",
          "text": "Coğrafi özellikleri ve turizm potansiyeli göz önüne alındığında 'Nemrut Dağı' hangi alanda daha çok öne çıkar? (C-87)",
          "options": [
            "A) Okyanus balıkçılığı",
            "B) Doğal güzellikleri ve turizm/coğrafi önemi",
            "C) Çöl iklimi araştırmaları",
            "D) Sadece ağır sanayi",
            "E) Sadece madencilik"
          ],
          "correct": 1,
          "solution": "Doğru cevap Doğal güzellikleri ve turizm/coğrafi önemi.",
          "id": "e5_q105",
          "no": 105
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'YSK' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-58)",
          "options": [
            "A) YSK yasaklanmıştır.",
            "B) YSK sadece köylerde bulunur.",
            "C) YSK, anayasal sistemin önemli bir parçasıdır.",
            "D) YSK yabancı bir kurumdur.",
            "E) YSK özel bir şirkettir."
          ],
          "correct": 2,
          "solution": "Doğru cevap YSK, anayasal sistemin önemli bir parçasıdır..",
          "id": "e5_q106",
          "no": 106
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'HSK' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-59)",
          "options": [
            "A) HSK yasaklanmıştır.",
            "B) HSK, anayasal sistemin önemli bir parçasıdır.",
            "C) HSK yabancı bir kurumdur.",
            "D) HSK özel bir şirkettir.",
            "E) HSK sadece köylerde bulunur."
          ],
          "correct": 1,
          "solution": "Doğru cevap HSK, anayasal sistemin önemli bir parçasıdır..",
          "id": "e5_q107",
          "no": 107
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'Belediye' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-60)",
          "options": [
            "A) Belediye yabancı bir kurumdur.",
            "B) Belediye yasaklanmıştır.",
            "C) Belediye, anayasal sistemin önemli bir parçasıdır.",
            "D) Belediye özel bir şirkettir.",
            "E) Belediye sadece köylerde bulunur."
          ],
          "correct": 2,
          "solution": "Doğru cevap Belediye, anayasal sistemin önemli bir parçasıdır..",
          "id": "e5_q108",
          "no": 108
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'Valilik' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-61)",
          "options": [
            "A) Valilik, anayasal sistemin önemli bir parçasıdır.",
            "B) Valilik özel bir şirkettir.",
            "C) Valilik yabancı bir kurumdur.",
            "D) Valilik sadece köylerde bulunur.",
            "E) Valilik yasaklanmıştır."
          ],
          "correct": 0,
          "solution": "Doğru cevap Valilik, anayasal sistemin önemli bir parçasıdır..",
          "id": "e5_q109",
          "no": 109
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'Kaymakamlık' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-62)",
          "options": [
            "A) Kaymakamlık sadece köylerde bulunur.",
            "B) Kaymakamlık yasaklanmıştır.",
            "C) Kaymakamlık özel bir şirkettir.",
            "D) Kaymakamlık, anayasal sistemin önemli bir parçasıdır.",
            "E) Kaymakamlık yabancı bir kurumdur."
          ],
          "correct": 3,
          "solution": "Doğru cevap Kaymakamlık, anayasal sistemin önemli bir parçasıdır..",
          "id": "e5_q110",
          "no": 110
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'İl Genel Meclisi' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-63)",
          "options": [
            "A) İl Genel Meclisi yabancı bir kurumdur.",
            "B) İl Genel Meclisi yasaklanmıştır.",
            "C) İl Genel Meclisi sadece köylerde bulunur.",
            "D) İl Genel Meclisi özel bir şirkettir.",
            "E) İl Genel Meclisi, anayasal sistemin önemli bir parçasıdır."
          ],
          "correct": 4,
          "solution": "Doğru cevap İl Genel Meclisi, anayasal sistemin önemli bir parçasıdır..",
          "id": "e5_q111",
          "no": 111
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'Kamu Denetçiliği Kurumu' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-64)",
          "options": [
            "A) Kamu Denetçiliği Kurumu yasaklanmıştır.",
            "B) Kamu Denetçiliği Kurumu yabancı bir kurumdur.",
            "C) Kamu Denetçiliği Kurumu özel bir şirkettir.",
            "D) Kamu Denetçiliği Kurumu sadece köylerde bulunur.",
            "E) Kamu Denetçiliği Kurumu, anayasal sistemin önemli bir parçasıdır."
          ],
          "correct": 4,
          "solution": "Doğru cevap Kamu Denetçiliği Kurumu, anayasal sistemin önemli bir parçasıdır..",
          "id": "e5_q112",
          "no": 112
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'Anayasa Mahkemesi' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-65)",
          "options": [
            "A) Anayasa Mahkemesi yasaklanmıştır.",
            "B) Anayasa Mahkemesi yabancı bir kurumdur.",
            "C) Anayasa Mahkemesi özel bir şirkettir.",
            "D) Anayasa Mahkemesi sadece köylerde bulunur.",
            "E) Anayasa Mahkemesi, anayasal sistemin önemli bir parçasıdır."
          ],
          "correct": 4,
          "solution": "Doğru cevap Anayasa Mahkemesi, anayasal sistemin önemli bir parçasıdır..",
          "id": "e5_q113",
          "no": 113
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'Yargıtay' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-66)",
          "options": [
            "A) Yargıtay, anayasal sistemin önemli bir parçasıdır.",
            "B) Yargıtay yasaklanmıştır.",
            "C) Yargıtay yabancı bir kurumdur.",
            "D) Yargıtay özel bir şirkettir.",
            "E) Yargıtay sadece köylerde bulunur."
          ],
          "correct": 0,
          "solution": "Doğru cevap Yargıtay, anayasal sistemin önemli bir parçasıdır..",
          "id": "e5_q114",
          "no": 114
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'Danıştay' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-67)",
          "options": [
            "A) Danıştay, anayasal sistemin önemli bir parçasıdır.",
            "B) Danıştay yasaklanmıştır.",
            "C) Danıştay özel bir şirkettir.",
            "D) Danıştay sadece köylerde bulunur.",
            "E) Danıştay yabancı bir kurumdur."
          ],
          "correct": 0,
          "solution": "Doğru cevap Danıştay, anayasal sistemin önemli bir parçasıdır..",
          "id": "e5_q115",
          "no": 115
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'TBMM' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-68)",
          "options": [
            "A) TBMM yabancı bir kurumdur.",
            "B) TBMM, anayasal sistemin önemli bir parçasıdır.",
            "C) TBMM özel bir şirkettir.",
            "D) TBMM yasaklanmıştır.",
            "E) TBMM sadece köylerde bulunur."
          ],
          "correct": 1,
          "solution": "Doğru cevap TBMM, anayasal sistemin önemli bir parçasıdır..",
          "id": "e5_q116",
          "no": 116
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'Cumhurbaşkanlığı' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-69)",
          "options": [
            "A) Cumhurbaşkanlığı özel bir şirkettir.",
            "B) Cumhurbaşkanlığı, anayasal sistemin önemli bir parçasıdır.",
            "C) Cumhurbaşkanlığı sadece köylerde bulunur.",
            "D) Cumhurbaşkanlığı yasaklanmıştır.",
            "E) Cumhurbaşkanlığı yabancı bir kurumdur."
          ],
          "correct": 1,
          "solution": "Doğru cevap Cumhurbaşkanlığı, anayasal sistemin önemli bir parçasıdır..",
          "id": "e5_q117",
          "no": 117
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'Sayıştay' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-70)",
          "options": [
            "A) Sayıştay sadece köylerde bulunur.",
            "B) Sayıştay yasaklanmıştır.",
            "C) Sayıştay yabancı bir kurumdur.",
            "D) Sayıştay özel bir şirkettir.",
            "E) Sayıştay, anayasal sistemin önemli bir parçasıdır."
          ],
          "correct": 4,
          "solution": "Doğru cevap Sayıştay, anayasal sistemin önemli bir parçasıdır..",
          "id": "e5_q118",
          "no": 118
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'YSK' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-71)",
          "options": [
            "A) YSK yabancı bir kurumdur.",
            "B) YSK, anayasal sistemin önemli bir parçasıdır.",
            "C) YSK sadece köylerde bulunur.",
            "D) YSK özel bir şirkettir.",
            "E) YSK yasaklanmıştır."
          ],
          "correct": 1,
          "solution": "Doğru cevap YSK, anayasal sistemin önemli bir parçasıdır..",
          "id": "e5_q119",
          "no": 119
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'HSK' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-72)",
          "options": [
            "A) HSK yabancı bir kurumdur.",
            "B) HSK özel bir şirkettir.",
            "C) HSK, anayasal sistemin önemli bir parçasıdır.",
            "D) HSK sadece köylerde bulunur.",
            "E) HSK yasaklanmıştır."
          ],
          "correct": 2,
          "solution": "Doğru cevap HSK, anayasal sistemin önemli bir parçasıdır..",
          "id": "e5_q120",
          "no": 120
        }
      ]
    },
    {
      "id": "deneme_6",
      "name": "6. Deneme Sınavı",
      "totalQuestions": 120,
      "duration": 130,
      "distribution": {
        "Türkçe": 30,
        "Matematik": 30,
        "Tarih": 27,
        "Coğrafya": 18,
        "Vatandaşlık": 15
      },
      "questions": [
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde 'yanlış' kelimesinin yazımıyla ilgili bir kural hatırlatılmaktadır? (T-145)",
          "options": [
            "A) yanlış cümlede özne olamaz.",
            "B) yanlış kelimesi yabancı kökenlidir.",
            "C) yanlış kelimesi her zaman ayrı yazılır.",
            "D) yanlış kelimesi fiildir.",
            "E) 'yanlış' kelimesinin doğru yazımına dikkat edilmelidir."
          ],
          "correct": 4,
          "solution": "Doğru cevap 'yanlış' kelimesinin doğru yazımına dikkat edilmelidir..",
          "id": "e6_q1",
          "no": 1
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde mecaz anlamlı bir sözcük kullanılmıştır? (T-146)",
          "options": [
            "A) Buzdolabı soğuk üflüyor.",
            "B) Hava bugün çok soğuk.",
            "C) Kışın havalar soğuk olur.",
            "D) Olaylara karşı çok 'soğuk' davranıyordu.",
            "E) Suyu dolaptan soğuk içti."
          ],
          "correct": 3,
          "solution": "Doğru cevap Olaylara karşı çok 'soğuk' davranıyordu..",
          "id": "e6_q2",
          "no": 2
        },
        {
          "subject": "Türkçe",
          "text": "Bilim tarih boyunca insanlığın en büyük rehberlerinden biri olmuştur. Toplumlar Bilim sayesinde sınırlarını aşmış, geleceğe umutla bakabilmiştir. (P-147)\nBu parçanın ana düşüncesi nedir?",
          "options": [
            "A) Bilim sadece geçmişte kalmıştır.",
            "B) Bilim, toplumsal ilerleme ve vizyon için vazgeçilmezdir.",
            "C) Bilim sadece bireyseldir.",
            "D) İnsanlar Bilim ile ilgilenmemelidir.",
            "E) Bilim zaman kaybıdır."
          ],
          "correct": 1,
          "solution": "Doğru cevap Bilim, toplumsal ilerleme ve vizyon için vazgeçilmezdir..",
          "id": "e6_q3",
          "no": 3
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde 'birkaç' kelimesinin yazımıyla ilgili bir kural hatırlatılmaktadır? (T-148)",
          "options": [
            "A) birkaç kelimesi fiildir.",
            "B) 'birkaç' kelimesinin doğru yazımına dikkat edilmelidir.",
            "C) birkaç cümlede özne olamaz.",
            "D) birkaç kelimesi yabancı kökenlidir.",
            "E) birkaç kelimesi her zaman ayrı yazılır."
          ],
          "correct": 1,
          "solution": "Doğru cevap 'birkaç' kelimesinin doğru yazımına dikkat edilmelidir..",
          "id": "e6_q4",
          "no": 4
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde mecaz anlamlı bir sözcük kullanılmıştır? (T-149)",
          "options": [
            "A) Buzdolabı soğuk üflüyor.",
            "B) Suyu dolaptan soğuk içti.",
            "C) Kışın havalar soğuk olur.",
            "D) Hava bugün çok soğuk.",
            "E) Olaylara karşı çok 'soğuk' davranıyordu."
          ],
          "correct": 4,
          "solution": "Doğru cevap Olaylara karşı çok 'soğuk' davranıyordu..",
          "id": "e6_q5",
          "no": 5
        },
        {
          "subject": "Türkçe",
          "text": "Sanat tarih boyunca insanlığın en büyük rehberlerinden biri olmuştur. Toplumlar Sanat sayesinde sınırlarını aşmış, geleceğe umutla bakabilmiştir. (P-150)\nBu parçanın ana düşüncesi nedir?",
          "options": [
            "A) Sanat sadece geçmişte kalmıştır.",
            "B) İnsanlar Sanat ile ilgilenmemelidir.",
            "C) Sanat sadece bireyseldir.",
            "D) Sanat, toplumsal ilerleme ve vizyon için vazgeçilmezdir.",
            "E) Sanat zaman kaybıdır."
          ],
          "correct": 3,
          "solution": "Doğru cevap Sanat, toplumsal ilerleme ve vizyon için vazgeçilmezdir..",
          "id": "e6_q6",
          "no": 6
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde 'hiç kimse' kelimesinin yazımıyla ilgili bir kural hatırlatılmaktadır? (T-151)",
          "options": [
            "A) hiç kimse kelimesi her zaman ayrı yazılır.",
            "B) hiç kimse kelimesi fiildir.",
            "C) hiç kimse kelimesi yabancı kökenlidir.",
            "D) hiç kimse cümlede özne olamaz.",
            "E) 'hiç kimse' kelimesinin doğru yazımına dikkat edilmelidir."
          ],
          "correct": 4,
          "solution": "Doğru cevap 'hiç kimse' kelimesinin doğru yazımına dikkat edilmelidir..",
          "id": "e6_q7",
          "no": 7
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde mecaz anlamlı bir sözcük kullanılmıştır? (T-152)",
          "options": [
            "A) Kışın havalar soğuk olur.",
            "B) Hava bugün çok soğuk.",
            "C) Olaylara karşı çok 'soğuk' davranıyordu.",
            "D) Buzdolabı soğuk üflüyor.",
            "E) Suyu dolaptan soğuk içti."
          ],
          "correct": 2,
          "solution": "Doğru cevap Olaylara karşı çok 'soğuk' davranıyordu..",
          "id": "e6_q8",
          "no": 8
        },
        {
          "subject": "Türkçe",
          "text": "Teknoloji tarih boyunca insanlığın en büyük rehberlerinden biri olmuştur. Toplumlar Teknoloji sayesinde sınırlarını aşmış, geleceğe umutla bakabilmiştir. (P-153)\nBu parçanın ana düşüncesi nedir?",
          "options": [
            "A) Teknoloji sadece geçmişte kalmıştır.",
            "B) Teknoloji zaman kaybıdır.",
            "C) Teknoloji sadece bireyseldir.",
            "D) Teknoloji, toplumsal ilerleme ve vizyon için vazgeçilmezdir.",
            "E) İnsanlar Teknoloji ile ilgilenmemelidir."
          ],
          "correct": 3,
          "solution": "Doğru cevap Teknoloji, toplumsal ilerleme ve vizyon için vazgeçilmezdir..",
          "id": "e6_q9",
          "no": 9
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde 'herkes' kelimesinin yazımıyla ilgili bir kural hatırlatılmaktadır? (T-154)",
          "options": [
            "A) herkes kelimesi yabancı kökenlidir.",
            "B) herkes kelimesi fiildir.",
            "C) herkes kelimesi her zaman ayrı yazılır.",
            "D) herkes cümlede özne olamaz.",
            "E) 'herkes' kelimesinin doğru yazımına dikkat edilmelidir."
          ],
          "correct": 4,
          "solution": "Doğru cevap 'herkes' kelimesinin doğru yazımına dikkat edilmelidir..",
          "id": "e6_q10",
          "no": 10
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde mecaz anlamlı bir sözcük kullanılmıştır? (T-155)",
          "options": [
            "A) Hava bugün çok soğuk.",
            "B) Buzdolabı soğuk üflüyor.",
            "C) Kışın havalar soğuk olur.",
            "D) Olaylara karşı çok 'soğuk' davranıyordu.",
            "E) Suyu dolaptan soğuk içti."
          ],
          "correct": 3,
          "solution": "Doğru cevap Olaylara karşı çok 'soğuk' davranıyordu..",
          "id": "e6_q11",
          "no": 11
        },
        {
          "subject": "Türkçe",
          "text": "Doğa tarih boyunca insanlığın en büyük rehberlerinden biri olmuştur. Toplumlar Doğa sayesinde sınırlarını aşmış, geleceğe umutla bakabilmiştir. (P-156)\nBu parçanın ana düşüncesi nedir?",
          "options": [
            "A) Doğa sadece bireyseldir.",
            "B) Doğa, toplumsal ilerleme ve vizyon için vazgeçilmezdir.",
            "C) İnsanlar Doğa ile ilgilenmemelidir.",
            "D) Doğa sadece geçmişte kalmıştır.",
            "E) Doğa zaman kaybıdır."
          ],
          "correct": 1,
          "solution": "Doğru cevap Doğa, toplumsal ilerleme ve vizyon için vazgeçilmezdir..",
          "id": "e6_q12",
          "no": 12
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde 'bugün' kelimesinin yazımıyla ilgili bir kural hatırlatılmaktadır? (T-157)",
          "options": [
            "A) bugün kelimesi yabancı kökenlidir.",
            "B) 'bugün' kelimesinin doğru yazımına dikkat edilmelidir.",
            "C) bugün kelimesi her zaman ayrı yazılır.",
            "D) bugün kelimesi fiildir.",
            "E) bugün cümlede özne olamaz."
          ],
          "correct": 1,
          "solution": "Doğru cevap 'bugün' kelimesinin doğru yazımına dikkat edilmelidir..",
          "id": "e6_q13",
          "no": 13
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde mecaz anlamlı bir sözcük kullanılmıştır? (T-158)",
          "options": [
            "A) Hava bugün çok soğuk.",
            "B) Olaylara karşı çok 'soğuk' davranıyordu.",
            "C) Kışın havalar soğuk olur.",
            "D) Buzdolabı soğuk üflüyor.",
            "E) Suyu dolaptan soğuk içti."
          ],
          "correct": 1,
          "solution": "Doğru cevap Olaylara karşı çok 'soğuk' davranıyordu..",
          "id": "e6_q14",
          "no": 14
        },
        {
          "subject": "Türkçe",
          "text": "Psikoloji tarih boyunca insanlığın en büyük rehberlerinden biri olmuştur. Toplumlar Psikoloji sayesinde sınırlarını aşmış, geleceğe umutla bakabilmiştir. (P-159)\nBu parçanın ana düşüncesi nedir?",
          "options": [
            "A) İnsanlar Psikoloji ile ilgilenmemelidir.",
            "B) Psikoloji zaman kaybıdır.",
            "C) Psikoloji, toplumsal ilerleme ve vizyon için vazgeçilmezdir.",
            "D) Psikoloji sadece geçmişte kalmıştır.",
            "E) Psikoloji sadece bireyseldir."
          ],
          "correct": 2,
          "solution": "Doğru cevap Psikoloji, toplumsal ilerleme ve vizyon için vazgeçilmezdir..",
          "id": "e6_q15",
          "no": 15
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde 'yalnız' kelimesinin yazımıyla ilgili bir kural hatırlatılmaktadır? (T-160)",
          "options": [
            "A) 'yalnız' kelimesinin doğru yazımına dikkat edilmelidir.",
            "B) yalnız kelimesi fiildir.",
            "C) yalnız kelimesi yabancı kökenlidir.",
            "D) yalnız kelimesi her zaman ayrı yazılır.",
            "E) yalnız cümlede özne olamaz."
          ],
          "correct": 0,
          "solution": "Doğru cevap 'yalnız' kelimesinin doğru yazımına dikkat edilmelidir..",
          "id": "e6_q16",
          "no": 16
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde mecaz anlamlı bir sözcük kullanılmıştır? (T-161)",
          "options": [
            "A) Hava bugün çok soğuk.",
            "B) Olaylara karşı çok 'soğuk' davranıyordu.",
            "C) Buzdolabı soğuk üflüyor.",
            "D) Suyu dolaptan soğuk içti.",
            "E) Kışın havalar soğuk olur."
          ],
          "correct": 1,
          "solution": "Doğru cevap Olaylara karşı çok 'soğuk' davranıyordu..",
          "id": "e6_q17",
          "no": 17
        },
        {
          "subject": "Türkçe",
          "text": "Eğitim tarih boyunca insanlığın en büyük rehberlerinden biri olmuştur. Toplumlar Eğitim sayesinde sınırlarını aşmış, geleceğe umutla bakabilmiştir. (P-162)\nBu parçanın ana düşüncesi nedir?",
          "options": [
            "A) Eğitim zaman kaybıdır.",
            "B) İnsanlar Eğitim ile ilgilenmemelidir.",
            "C) Eğitim sadece bireyseldir.",
            "D) Eğitim, toplumsal ilerleme ve vizyon için vazgeçilmezdir.",
            "E) Eğitim sadece geçmişte kalmıştır."
          ],
          "correct": 3,
          "solution": "Doğru cevap Eğitim, toplumsal ilerleme ve vizyon için vazgeçilmezdir..",
          "id": "e6_q18",
          "no": 18
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde 'hiçbir' kelimesinin yazımıyla ilgili bir kural hatırlatılmaktadır? (T-163)",
          "options": [
            "A) hiçbir kelimesi her zaman ayrı yazılır.",
            "B) hiçbir cümlede özne olamaz.",
            "C) hiçbir kelimesi yabancı kökenlidir.",
            "D) 'hiçbir' kelimesinin doğru yazımına dikkat edilmelidir.",
            "E) hiçbir kelimesi fiildir."
          ],
          "correct": 3,
          "solution": "Doğru cevap 'hiçbir' kelimesinin doğru yazımına dikkat edilmelidir..",
          "id": "e6_q19",
          "no": 19
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde mecaz anlamlı bir sözcük kullanılmıştır? (T-164)",
          "options": [
            "A) Kışın havalar soğuk olur.",
            "B) Hava bugün çok soğuk.",
            "C) Buzdolabı soğuk üflüyor.",
            "D) Suyu dolaptan soğuk içti.",
            "E) Olaylara karşı çok 'soğuk' davranıyordu."
          ],
          "correct": 4,
          "solution": "Doğru cevap Olaylara karşı çok 'soğuk' davranıyordu..",
          "id": "e6_q20",
          "no": 20
        },
        {
          "subject": "Türkçe",
          "text": "Kültür tarih boyunca insanlığın en büyük rehberlerinden biri olmuştur. Toplumlar Kültür sayesinde sınırlarını aşmış, geleceğe umutla bakabilmiştir. (P-165)\nBu parçanın ana düşüncesi nedir?",
          "options": [
            "A) Kültür sadece geçmişte kalmıştır.",
            "B) Kültür zaman kaybıdır.",
            "C) İnsanlar Kültür ile ilgilenmemelidir.",
            "D) Kültür, toplumsal ilerleme ve vizyon için vazgeçilmezdir.",
            "E) Kültür sadece bireyseldir."
          ],
          "correct": 3,
          "solution": "Doğru cevap Kültür, toplumsal ilerleme ve vizyon için vazgeçilmezdir..",
          "id": "e6_q21",
          "no": 21
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde 'her şey' kelimesinin yazımıyla ilgili bir kural hatırlatılmaktadır? (T-166)",
          "options": [
            "A) 'her şey' kelimesinin doğru yazımına dikkat edilmelidir.",
            "B) her şey kelimesi yabancı kökenlidir.",
            "C) her şey cümlede özne olamaz.",
            "D) her şey kelimesi fiildir.",
            "E) her şey kelimesi her zaman ayrı yazılır."
          ],
          "correct": 0,
          "solution": "Doğru cevap 'her şey' kelimesinin doğru yazımına dikkat edilmelidir..",
          "id": "e6_q22",
          "no": 22
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde mecaz anlamlı bir sözcük kullanılmıştır? (T-167)",
          "options": [
            "A) Hava bugün çok soğuk.",
            "B) Buzdolabı soğuk üflüyor.",
            "C) Kışın havalar soğuk olur.",
            "D) Suyu dolaptan soğuk içti.",
            "E) Olaylara karşı çok 'soğuk' davranıyordu."
          ],
          "correct": 4,
          "solution": "Doğru cevap Olaylara karşı çok 'soğuk' davranıyordu..",
          "id": "e6_q23",
          "no": 23
        },
        {
          "subject": "Türkçe",
          "text": "Felsefe tarih boyunca insanlığın en büyük rehberlerinden biri olmuştur. Toplumlar Felsefe sayesinde sınırlarını aşmış, geleceğe umutla bakabilmiştir. (P-168)\nBu parçanın ana düşüncesi nedir?",
          "options": [
            "A) Felsefe sadece bireyseldir.",
            "B) Felsefe, toplumsal ilerleme ve vizyon için vazgeçilmezdir.",
            "C) İnsanlar Felsefe ile ilgilenmemelidir.",
            "D) Felsefe zaman kaybıdır.",
            "E) Felsefe sadece geçmişte kalmıştır."
          ],
          "correct": 1,
          "solution": "Doğru cevap Felsefe, toplumsal ilerleme ve vizyon için vazgeçilmezdir..",
          "id": "e6_q24",
          "no": 24
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde 'yanlış' kelimesinin yazımıyla ilgili bir kural hatırlatılmaktadır? (T-169)",
          "options": [
            "A) yanlış kelimesi her zaman ayrı yazılır.",
            "B) yanlış kelimesi yabancı kökenlidir.",
            "C) yanlış cümlede özne olamaz.",
            "D) 'yanlış' kelimesinin doğru yazımına dikkat edilmelidir.",
            "E) yanlış kelimesi fiildir."
          ],
          "correct": 3,
          "solution": "Doğru cevap 'yanlış' kelimesinin doğru yazımına dikkat edilmelidir..",
          "id": "e6_q25",
          "no": 25
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde mecaz anlamlı bir sözcük kullanılmıştır? (T-170)",
          "options": [
            "A) Olaylara karşı çok 'soğuk' davranıyordu.",
            "B) Hava bugün çok soğuk.",
            "C) Buzdolabı soğuk üflüyor.",
            "D) Kışın havalar soğuk olur.",
            "E) Suyu dolaptan soğuk içti."
          ],
          "correct": 0,
          "solution": "Doğru cevap Olaylara karşı çok 'soğuk' davranıyordu..",
          "id": "e6_q26",
          "no": 26
        },
        {
          "subject": "Türkçe",
          "text": "Edebiyat tarih boyunca insanlığın en büyük rehberlerinden biri olmuştur. Toplumlar Edebiyat sayesinde sınırlarını aşmış, geleceğe umutla bakabilmiştir. (P-171)\nBu parçanın ana düşüncesi nedir?",
          "options": [
            "A) İnsanlar Edebiyat ile ilgilenmemelidir.",
            "B) Edebiyat sadece bireyseldir.",
            "C) Edebiyat zaman kaybıdır.",
            "D) Edebiyat, toplumsal ilerleme ve vizyon için vazgeçilmezdir.",
            "E) Edebiyat sadece geçmişte kalmıştır."
          ],
          "correct": 3,
          "solution": "Doğru cevap Edebiyat, toplumsal ilerleme ve vizyon için vazgeçilmezdir..",
          "id": "e6_q27",
          "no": 27
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde 'birkaç' kelimesinin yazımıyla ilgili bir kural hatırlatılmaktadır? (T-172)",
          "options": [
            "A) birkaç cümlede özne olamaz.",
            "B) birkaç kelimesi her zaman ayrı yazılır.",
            "C) birkaç kelimesi yabancı kökenlidir.",
            "D) birkaç kelimesi fiildir.",
            "E) 'birkaç' kelimesinin doğru yazımına dikkat edilmelidir."
          ],
          "correct": 4,
          "solution": "Doğru cevap 'birkaç' kelimesinin doğru yazımına dikkat edilmelidir..",
          "id": "e6_q28",
          "no": 28
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde mecaz anlamlı bir sözcük kullanılmıştır? (T-173)",
          "options": [
            "A) Buzdolabı soğuk üflüyor.",
            "B) Suyu dolaptan soğuk içti.",
            "C) Kışın havalar soğuk olur.",
            "D) Hava bugün çok soğuk.",
            "E) Olaylara karşı çok 'soğuk' davranıyordu."
          ],
          "correct": 4,
          "solution": "Doğru cevap Olaylara karşı çok 'soğuk' davranıyordu..",
          "id": "e6_q29",
          "no": 29
        },
        {
          "subject": "Türkçe",
          "text": "Tarih tarih boyunca insanlığın en büyük rehberlerinden biri olmuştur. Toplumlar Tarih sayesinde sınırlarını aşmış, geleceğe umutla bakabilmiştir. (P-174)\nBu parçanın ana düşüncesi nedir?",
          "options": [
            "A) İnsanlar Tarih ile ilgilenmemelidir.",
            "B) Tarih, toplumsal ilerleme ve vizyon için vazgeçilmezdir.",
            "C) Tarih sadece geçmişte kalmıştır.",
            "D) Tarih sadece bireyseldir.",
            "E) Tarih zaman kaybıdır."
          ],
          "correct": 1,
          "solution": "Doğru cevap Tarih, toplumsal ilerleme ve vizyon için vazgeçilmezdir..",
          "id": "e6_q30",
          "no": 30
        },
        {
          "subject": "Matematik",
          "text": "6x + 33 = 81 denkleminde x kaçtır? (SoruID: M150)",
          "options": [
            "A) 8",
            "B) 10",
            "C) 9",
            "D) 11",
            "E) 7"
          ],
          "correct": 0,
          "solution": "Doğru cevap 8.",
          "id": "e6_q31",
          "no": 31
        },
        {
          "subject": "Matematik",
          "text": "190 sayısının %40'si kaçtır? (SoruID: M151)",
          "options": [
            "A) 81",
            "B) 91",
            "C) 76",
            "D) 86",
            "E) 71"
          ],
          "correct": 2,
          "solution": "Doğru cevap 76.",
          "id": "e6_q32",
          "no": 32
        },
        {
          "subject": "Matematik",
          "text": "16, 16 ve 19 sayılarının aritmetik ortalaması kaçtır? (SoruID: M152)",
          "options": [
            "A) 17",
            "B) 15",
            "C) 16",
            "D) 18",
            "E) 19"
          ],
          "correct": 0,
          "solution": "Doğru cevap 17.",
          "id": "e6_q33",
          "no": 33
        },
        {
          "subject": "Matematik",
          "text": "Ali 15, Ayşe 13 yaşındadır. 6 yıl sonra yaşları toplamı kaç olur? (SoruID: M153)",
          "options": [
            "A) 40",
            "B) 39",
            "C) 34",
            "D) 46",
            "E) 41"
          ],
          "correct": 0,
          "solution": "Doğru cevap 40.",
          "id": "e6_q34",
          "no": 34
        },
        {
          "subject": "Matematik",
          "text": "√64 + √25 işleminin sonucu kaçtır? (SoruID: M154)",
          "options": [
            "A) 13",
            "B) 14",
            "C) 15",
            "D) 12",
            "E) 11"
          ],
          "correct": 0,
          "solution": "Doğru cevap 13.",
          "id": "e6_q35",
          "no": 35
        },
        {
          "subject": "Matematik",
          "text": "6x + 33 = 69 denkleminde x kaçtır? (SoruID: M155)",
          "options": [
            "A) 6",
            "B) 8",
            "C) 5",
            "D) 9",
            "E) 7"
          ],
          "correct": 0,
          "solution": "Doğru cevap 6.",
          "id": "e6_q36",
          "no": 36
        },
        {
          "subject": "Matematik",
          "text": "50 sayısının %30'si kaçtır? (SoruID: M156)",
          "options": [
            "A) 30",
            "B) 15",
            "C) 20",
            "D) 25",
            "E) 10"
          ],
          "correct": 1,
          "solution": "Doğru cevap 15.",
          "id": "e6_q37",
          "no": 37
        },
        {
          "subject": "Matematik",
          "text": "24, 22 ve 32 sayılarının aritmetik ortalaması kaçtır? (SoruID: M157)",
          "options": [
            "A) 24",
            "B) 27",
            "C) 25",
            "D) 26",
            "E) 28"
          ],
          "correct": 3,
          "solution": "Doğru cevap 26.",
          "id": "e6_q38",
          "no": 38
        },
        {
          "subject": "Matematik",
          "text": "Ali 11, Ayşe 20 yaşındadır. 7 yıl sonra yaşları toplamı kaç olur? (SoruID: M158)",
          "options": [
            "A) 45",
            "B) 44",
            "C) 38",
            "D) 52",
            "E) 46"
          ],
          "correct": 0,
          "solution": "Doğru cevap 45.",
          "id": "e6_q39",
          "no": 39
        },
        {
          "subject": "Matematik",
          "text": "√49 + √49 işleminin sonucu kaçtır? (SoruID: M159)",
          "options": [
            "A) 13",
            "B) 12",
            "C) 14",
            "D) 15",
            "E) 16"
          ],
          "correct": 2,
          "solution": "Doğru cevap 14.",
          "id": "e6_q40",
          "no": 40
        },
        {
          "subject": "Matematik",
          "text": "8x + 44 = 100 denkleminde x kaçtır? (SoruID: M160)",
          "options": [
            "A) 7",
            "B) 9",
            "C) 10",
            "D) 8",
            "E) 6"
          ],
          "correct": 0,
          "solution": "Doğru cevap 7.",
          "id": "e6_q41",
          "no": 41
        },
        {
          "subject": "Matematik",
          "text": "150 sayısının %10'si kaçtır? (SoruID: M161)",
          "options": [
            "A) 20",
            "B) 10",
            "C) 30",
            "D) 25",
            "E) 15"
          ],
          "correct": 4,
          "solution": "Doğru cevap 15.",
          "id": "e6_q42",
          "no": 42
        },
        {
          "subject": "Matematik",
          "text": "25, 29 ve 24 sayılarının aritmetik ortalaması kaçtır? (SoruID: M162)",
          "options": [
            "A) 25",
            "B) 26",
            "C) 24",
            "D) 27",
            "E) 28"
          ],
          "correct": 1,
          "solution": "Doğru cevap 26.",
          "id": "e6_q43",
          "no": 43
        },
        {
          "subject": "Matematik",
          "text": "Ali 21, Ayşe 10 yaşındadır. 4 yıl sonra yaşları toplamı kaç olur? (SoruID: M163)",
          "options": [
            "A) 35",
            "B) 43",
            "C) 40",
            "D) 38",
            "E) 39"
          ],
          "correct": 4,
          "solution": "Doğru cevap 39.",
          "id": "e6_q44",
          "no": 44
        },
        {
          "subject": "Matematik",
          "text": "√9 + √81 işleminin sonucu kaçtır? (SoruID: M164)",
          "options": [
            "A) 13",
            "B) 12",
            "C) 14",
            "D) 11",
            "E) 10"
          ],
          "correct": 1,
          "solution": "Doğru cevap 12.",
          "id": "e6_q45",
          "no": 45
        },
        {
          "subject": "Matematik",
          "text": "8x + 25 = 57 denkleminde x kaçtır? (SoruID: M165)",
          "options": [
            "A) 5",
            "B) 7",
            "C) 6",
            "D) 4",
            "E) 3"
          ],
          "correct": 3,
          "solution": "Doğru cevap 4.",
          "id": "e6_q46",
          "no": 46
        },
        {
          "subject": "Matematik",
          "text": "140 sayısının %25'si kaçtır? (SoruID: M166)",
          "options": [
            "A) 45",
            "B) 30",
            "C) 35",
            "D) 50",
            "E) 40"
          ],
          "correct": 2,
          "solution": "Doğru cevap 35.",
          "id": "e6_q47",
          "no": 47
        },
        {
          "subject": "Matematik",
          "text": "16, 27 ve 26 sayılarının aritmetik ortalaması kaçtır? (SoruID: M167)",
          "options": [
            "A) 25",
            "B) 21",
            "C) 23",
            "D) 24",
            "E) 22"
          ],
          "correct": 2,
          "solution": "Doğru cevap 23.",
          "id": "e6_q48",
          "no": 48
        },
        {
          "subject": "Matematik",
          "text": "Ali 21, Ayşe 17 yaşındadır. 5 yıl sonra yaşları toplamı kaç olur? (SoruID: M168)",
          "options": [
            "A) 43",
            "B) 53",
            "C) 48",
            "D) 47",
            "E) 49"
          ],
          "correct": 2,
          "solution": "Doğru cevap 48.",
          "id": "e6_q49",
          "no": 49
        },
        {
          "subject": "Matematik",
          "text": "√16 + √9 işleminin sonucu kaçtır? (SoruID: M169)",
          "options": [
            "A) 6",
            "B) 5",
            "C) 8",
            "D) 9",
            "E) 7"
          ],
          "correct": 4,
          "solution": "Doğru cevap 7.",
          "id": "e6_q50",
          "no": 50
        },
        {
          "subject": "Matematik",
          "text": "9x + 8 = 80 denkleminde x kaçtır? (SoruID: M170)",
          "options": [
            "A) 7",
            "B) 8",
            "C) 9",
            "D) 11",
            "E) 10"
          ],
          "correct": 1,
          "solution": "Doğru cevap 8.",
          "id": "e6_q51",
          "no": 51
        },
        {
          "subject": "Matematik",
          "text": "50 sayısının %60'si kaçtır? (SoruID: M171)",
          "options": [
            "A) 45",
            "B) 30",
            "C) 25",
            "D) 35",
            "E) 40"
          ],
          "correct": 1,
          "solution": "Doğru cevap 30.",
          "id": "e6_q52",
          "no": 52
        },
        {
          "subject": "Matematik",
          "text": "18, 27 ve 27 sayılarının aritmetik ortalaması kaçtır? (SoruID: M172)",
          "options": [
            "A) 23",
            "B) 22",
            "C) 24",
            "D) 26",
            "E) 25"
          ],
          "correct": 2,
          "solution": "Doğru cevap 24.",
          "id": "e6_q53",
          "no": 53
        },
        {
          "subject": "Matematik",
          "text": "Ali 15, Ayşe 10 yaşındadır. 5 yıl sonra yaşları toplamı kaç olur? (SoruID: M173)",
          "options": [
            "A) 35",
            "B) 36",
            "C) 40",
            "D) 30",
            "E) 34"
          ],
          "correct": 0,
          "solution": "Doğru cevap 35.",
          "id": "e6_q54",
          "no": 54
        },
        {
          "subject": "Matematik",
          "text": "√9 + √25 işleminin sonucu kaçtır? (SoruID: M174)",
          "options": [
            "A) 6",
            "B) 10",
            "C) 9",
            "D) 8",
            "E) 7"
          ],
          "correct": 3,
          "solution": "Doğru cevap 8.",
          "id": "e6_q55",
          "no": 55
        },
        {
          "subject": "Matematik",
          "text": "6x + 32 = 68 denkleminde x kaçtır? (SoruID: M175)",
          "options": [
            "A) 7",
            "B) 8",
            "C) 6",
            "D) 5",
            "E) 9"
          ],
          "correct": 2,
          "solution": "Doğru cevap 6.",
          "id": "e6_q56",
          "no": 56
        },
        {
          "subject": "Matematik",
          "text": "200 sayısının %60'si kaçtır? (SoruID: M176)",
          "options": [
            "A) 125",
            "B) 130",
            "C) 135",
            "D) 120",
            "E) 115"
          ],
          "correct": 3,
          "solution": "Doğru cevap 120.",
          "id": "e6_q57",
          "no": 57
        },
        {
          "subject": "Matematik",
          "text": "26, 24 ve 19 sayılarının aritmetik ortalaması kaçtır? (SoruID: M177)",
          "options": [
            "A) 21",
            "B) 24",
            "C) 23",
            "D) 22",
            "E) 25"
          ],
          "correct": 2,
          "solution": "Doğru cevap 23.",
          "id": "e6_q58",
          "no": 58
        },
        {
          "subject": "Matematik",
          "text": "Ali 15, Ayşe 21 yaşındadır. 7 yıl sonra yaşları toplamı kaç olur? (SoruID: M178)",
          "options": [
            "A) 57",
            "B) 51",
            "C) 50",
            "D) 49",
            "E) 43"
          ],
          "correct": 2,
          "solution": "Doğru cevap 50.",
          "id": "e6_q59",
          "no": 59
        },
        {
          "subject": "Matematik",
          "text": "√4 + √25 işleminin sonucu kaçtır? (SoruID: M179)",
          "options": [
            "A) 7",
            "B) 8",
            "C) 9",
            "D) 6",
            "E) 5"
          ],
          "correct": 0,
          "solution": "Doğru cevap 7.",
          "id": "e6_q60",
          "no": 60
        },
        {
          "subject": "Tarih",
          "text": "Türk siyasi ve askerî tarihinde büyük öneme sahip olan 'I. Dünya Savaşı' süreci ile ilgili aşağıdakilerden hangisi söylenebilir? (H-132)",
          "options": [
            "A) Sadece ekonomik bir olaydır.",
            "B) Hiçbir etkisi olmamıştır.",
            "C) Osmanlı'nın kuruluş dönemine aittir.",
            "D) I. Dünya Savaşı dönemin en kritik gelişmelerinden biridir.",
            "E) Avrupa'da gerçekleşmiştir."
          ],
          "correct": 3,
          "solution": "Doğru cevap I. Dünya Savaşı dönemin en kritik gelişmelerinden biridir..",
          "id": "e6_q61",
          "no": 61
        },
        {
          "subject": "Tarih",
          "text": "Aşağıdaki tarihî gelişmelerden hangisi 'Çanakkale Cephesi' ile doğrudan veya dolaylı olarak bağlantılıdır? (H-133)",
          "options": [
            "A) Çanakkale Cephesi öncesi ve sonrası yaşanan siyasi krizler.",
            "B) Fransız İhtilali",
            "C) Coğrafi Keşifler",
            "D) Sanayi İnkılabı",
            "E) Kavimler Göçü"
          ],
          "correct": 0,
          "solution": "Doğru cevap Çanakkale Cephesi öncesi ve sonrası yaşanan siyasi krizler..",
          "id": "e6_q62",
          "no": 62
        },
        {
          "subject": "Tarih",
          "text": "Millî Mücadele ve inkılaplar tarihi incelendiğinde 'Sakarya Meydan Muharebesi' olayının temel amacı aşağıdakilerden hangisidir? (H-134)",
          "options": [
            "A) Avrupa'ya göç etmek",
            "B) Bağımsızlık ve egemenliği pekiştirmek",
            "C) Feodaliteyi kurmak",
            "D) Saltanatı güçlendirmek",
            "E) Yeni sömürgeler elde etmek"
          ],
          "correct": 1,
          "solution": "Doğru cevap Bağımsızlık ve egemenliği pekiştirmek.",
          "id": "e6_q63",
          "no": 63
        },
        {
          "subject": "Tarih",
          "text": "Türk siyasi ve askerî tarihinde büyük öneme sahip olan 'Büyük Taarruz' süreci ile ilgili aşağıdakilerden hangisi söylenebilir? (H-135)",
          "options": [
            "A) Büyük Taarruz dönemin en kritik gelişmelerinden biridir.",
            "B) Avrupa'da gerçekleşmiştir.",
            "C) Sadece ekonomik bir olaydır.",
            "D) Hiçbir etkisi olmamıştır.",
            "E) Osmanlı'nın kuruluş dönemine aittir."
          ],
          "correct": 0,
          "solution": "Doğru cevap Büyük Taarruz dönemin en kritik gelişmelerinden biridir..",
          "id": "e6_q64",
          "no": 64
        },
        {
          "subject": "Tarih",
          "text": "Aşağıdaki tarihî gelişmelerden hangisi 'I. İnönü Muharebesi' ile doğrudan veya dolaylı olarak bağlantılıdır? (H-136)",
          "options": [
            "A) Sanayi İnkılabı",
            "B) Kavimler Göçü",
            "C) I. İnönü Muharebesi öncesi ve sonrası yaşanan siyasi krizler.",
            "D) Coğrafi Keşifler",
            "E) Fransız İhtilali"
          ],
          "correct": 2,
          "solution": "Doğru cevap I. İnönü Muharebesi öncesi ve sonrası yaşanan siyasi krizler..",
          "id": "e6_q65",
          "no": 65
        },
        {
          "subject": "Tarih",
          "text": "Millî Mücadele ve inkılaplar tarihi incelendiğinde 'II. İnönü Muharebesi' olayının temel amacı aşağıdakilerden hangisidir? (H-137)",
          "options": [
            "A) Avrupa'ya göç etmek",
            "B) Bağımsızlık ve egemenliği pekiştirmek",
            "C) Feodaliteyi kurmak",
            "D) Yeni sömürgeler elde etmek",
            "E) Saltanatı güçlendirmek"
          ],
          "correct": 1,
          "solution": "Doğru cevap Bağımsızlık ve egemenliği pekiştirmek.",
          "id": "e6_q66",
          "no": 66
        },
        {
          "subject": "Tarih",
          "text": "Türk siyasi ve askerî tarihinde büyük öneme sahip olan 'Kars Antlaşması' süreci ile ilgili aşağıdakilerden hangisi söylenebilir? (H-138)",
          "options": [
            "A) Osmanlı'nın kuruluş dönemine aittir.",
            "B) Avrupa'da gerçekleşmiştir.",
            "C) Sadece ekonomik bir olaydır.",
            "D) Kars Antlaşması dönemin en kritik gelişmelerinden biridir.",
            "E) Hiçbir etkisi olmamıştır."
          ],
          "correct": 3,
          "solution": "Doğru cevap Kars Antlaşması dönemin en kritik gelişmelerinden biridir..",
          "id": "e6_q67",
          "no": 67
        },
        {
          "subject": "Tarih",
          "text": "Aşağıdaki tarihî gelişmelerden hangisi 'Ankara Antlaşması' ile doğrudan veya dolaylı olarak bağlantılıdır? (H-139)",
          "options": [
            "A) Coğrafi Keşifler",
            "B) Fransız İhtilali",
            "C) Ankara Antlaşması öncesi ve sonrası yaşanan siyasi krizler.",
            "D) Sanayi İnkılabı",
            "E) Kavimler Göçü"
          ],
          "correct": 2,
          "solution": "Doğru cevap Ankara Antlaşması öncesi ve sonrası yaşanan siyasi krizler..",
          "id": "e6_q68",
          "no": 68
        },
        {
          "subject": "Tarih",
          "text": "Millî Mücadele ve inkılaplar tarihi incelendiğinde 'Sivas Kongresi' olayının temel amacı aşağıdakilerden hangisidir? (H-140)",
          "options": [
            "A) Yeni sömürgeler elde etmek",
            "B) Saltanatı güçlendirmek",
            "C) Bağımsızlık ve egemenliği pekiştirmek",
            "D) Avrupa'ya göç etmek",
            "E) Feodaliteyi kurmak"
          ],
          "correct": 2,
          "solution": "Doğru cevap Bağımsızlık ve egemenliği pekiştirmek.",
          "id": "e6_q69",
          "no": 69
        },
        {
          "subject": "Tarih",
          "text": "Türk siyasi ve askerî tarihinde büyük öneme sahip olan 'Erzurum Kongresi' süreci ile ilgili aşağıdakilerden hangisi söylenebilir? (H-141)",
          "options": [
            "A) Osmanlı'nın kuruluş dönemine aittir.",
            "B) Erzurum Kongresi dönemin en kritik gelişmelerinden biridir.",
            "C) Hiçbir etkisi olmamıştır.",
            "D) Avrupa'da gerçekleşmiştir.",
            "E) Sadece ekonomik bir olaydır."
          ],
          "correct": 1,
          "solution": "Doğru cevap Erzurum Kongresi dönemin en kritik gelişmelerinden biridir..",
          "id": "e6_q70",
          "no": 70
        },
        {
          "subject": "Tarih",
          "text": "Aşağıdaki tarihî gelişmelerden hangisi 'Amasya Genelgesi' ile doğrudan veya dolaylı olarak bağlantılıdır? (H-142)",
          "options": [
            "A) Coğrafi Keşifler",
            "B) Fransız İhtilali",
            "C) Kavimler Göçü",
            "D) Amasya Genelgesi öncesi ve sonrası yaşanan siyasi krizler.",
            "E) Sanayi İnkılabı"
          ],
          "correct": 3,
          "solution": "Doğru cevap Amasya Genelgesi öncesi ve sonrası yaşanan siyasi krizler..",
          "id": "e6_q71",
          "no": 71
        },
        {
          "subject": "Tarih",
          "text": "Millî Mücadele ve inkılaplar tarihi incelendiğinde 'Lozan Antlaşması' olayının temel amacı aşağıdakilerden hangisidir? (H-143)",
          "options": [
            "A) Saltanatı güçlendirmek",
            "B) Yeni sömürgeler elde etmek",
            "C) Bağımsızlık ve egemenliği pekiştirmek",
            "D) Avrupa'ya göç etmek",
            "E) Feodaliteyi kurmak"
          ],
          "correct": 2,
          "solution": "Doğru cevap Bağımsızlık ve egemenliği pekiştirmek.",
          "id": "e6_q72",
          "no": 72
        },
        {
          "subject": "Tarih",
          "text": "Türk siyasi ve askerî tarihinde büyük öneme sahip olan 'Cumhuriyetin İlanı' süreci ile ilgili aşağıdakilerden hangisi söylenebilir? (H-144)",
          "options": [
            "A) Hiçbir etkisi olmamıştır.",
            "B) Avrupa'da gerçekleşmiştir.",
            "C) Osmanlı'nın kuruluş dönemine aittir.",
            "D) Sadece ekonomik bir olaydır.",
            "E) Cumhuriyetin İlanı dönemin en kritik gelişmelerinden biridir."
          ],
          "correct": 4,
          "solution": "Doğru cevap Cumhuriyetin İlanı dönemin en kritik gelişmelerinden biridir..",
          "id": "e6_q73",
          "no": 73
        },
        {
          "subject": "Tarih",
          "text": "Aşağıdaki tarihî gelişmelerden hangisi 'TBMM'nin Açılışı' ile doğrudan veya dolaylı olarak bağlantılıdır? (H-145)",
          "options": [
            "A) Fransız İhtilali",
            "B) Kavimler Göçü",
            "C) Coğrafi Keşifler",
            "D) TBMM'nin Açılışı öncesi ve sonrası yaşanan siyasi krizler.",
            "E) Sanayi İnkılabı"
          ],
          "correct": 3,
          "solution": "Doğru cevap TBMM'nin Açılışı öncesi ve sonrası yaşanan siyasi krizler..",
          "id": "e6_q74",
          "no": 74
        },
        {
          "subject": "Tarih",
          "text": "Millî Mücadele ve inkılaplar tarihi incelendiğinde 'Mudanya Mütarekesi' olayının temel amacı aşağıdakilerden hangisidir? (H-146)",
          "options": [
            "A) Bağımsızlık ve egemenliği pekiştirmek",
            "B) Saltanatı güçlendirmek",
            "C) Avrupa'ya göç etmek",
            "D) Feodaliteyi kurmak",
            "E) Yeni sömürgeler elde etmek"
          ],
          "correct": 0,
          "solution": "Doğru cevap Bağımsızlık ve egemenliği pekiştirmek.",
          "id": "e6_q75",
          "no": 75
        },
        {
          "subject": "Tarih",
          "text": "Türk siyasi ve askerî tarihinde büyük öneme sahip olan 'Saltanatın Kaldırılması' süreci ile ilgili aşağıdakilerden hangisi söylenebilir? (H-147)",
          "options": [
            "A) Hiçbir etkisi olmamıştır.",
            "B) Saltanatın Kaldırılması dönemin en kritik gelişmelerinden biridir.",
            "C) Avrupa'da gerçekleşmiştir.",
            "D) Sadece ekonomik bir olaydır.",
            "E) Osmanlı'nın kuruluş dönemine aittir."
          ],
          "correct": 1,
          "solution": "Doğru cevap Saltanatın Kaldırılması dönemin en kritik gelişmelerinden biridir..",
          "id": "e6_q76",
          "no": 76
        },
        {
          "subject": "Tarih",
          "text": "Aşağıdaki tarihî gelişmelerden hangisi 'Halifeliğin Kaldırılması' ile doğrudan veya dolaylı olarak bağlantılıdır? (H-148)",
          "options": [
            "A) Coğrafi Keşifler",
            "B) Fransız İhtilali",
            "C) Halifeliğin Kaldırılması öncesi ve sonrası yaşanan siyasi krizler.",
            "D) Kavimler Göçü",
            "E) Sanayi İnkılabı"
          ],
          "correct": 2,
          "solution": "Doğru cevap Halifeliğin Kaldırılması öncesi ve sonrası yaşanan siyasi krizler..",
          "id": "e6_q77",
          "no": 77
        },
        {
          "subject": "Tarih",
          "text": "Millî Mücadele ve inkılaplar tarihi incelendiğinde 'Tevhid-i Tedrisat' olayının temel amacı aşağıdakilerden hangisidir? (H-149)",
          "options": [
            "A) Avrupa'ya göç etmek",
            "B) Yeni sömürgeler elde etmek",
            "C) Saltanatı güçlendirmek",
            "D) Bağımsızlık ve egemenliği pekiştirmek",
            "E) Feodaliteyi kurmak"
          ],
          "correct": 3,
          "solution": "Doğru cevap Bağımsızlık ve egemenliği pekiştirmek.",
          "id": "e6_q78",
          "no": 78
        },
        {
          "subject": "Tarih",
          "text": "Türk siyasi ve askerî tarihinde büyük öneme sahip olan 'Trablusgarp Savaşı' süreci ile ilgili aşağıdakilerden hangisi söylenebilir? (H-150)",
          "options": [
            "A) Osmanlı'nın kuruluş dönemine aittir.",
            "B) Trablusgarp Savaşı dönemin en kritik gelişmelerinden biridir.",
            "C) Hiçbir etkisi olmamıştır.",
            "D) Avrupa'da gerçekleşmiştir.",
            "E) Sadece ekonomik bir olaydır."
          ],
          "correct": 1,
          "solution": "Doğru cevap Trablusgarp Savaşı dönemin en kritik gelişmelerinden biridir..",
          "id": "e6_q79",
          "no": 79
        },
        {
          "subject": "Tarih",
          "text": "Aşağıdaki tarihî gelişmelerden hangisi 'Balkan Savaşları' ile doğrudan veya dolaylı olarak bağlantılıdır? (H-151)",
          "options": [
            "A) Balkan Savaşları öncesi ve sonrası yaşanan siyasi krizler.",
            "B) Fransız İhtilali",
            "C) Coğrafi Keşifler",
            "D) Sanayi İnkılabı",
            "E) Kavimler Göçü"
          ],
          "correct": 0,
          "solution": "Doğru cevap Balkan Savaşları öncesi ve sonrası yaşanan siyasi krizler..",
          "id": "e6_q80",
          "no": 80
        },
        {
          "subject": "Tarih",
          "text": "Millî Mücadele ve inkılaplar tarihi incelendiğinde 'I. Dünya Savaşı' olayının temel amacı aşağıdakilerden hangisidir? (H-152)",
          "options": [
            "A) Bağımsızlık ve egemenliği pekiştirmek",
            "B) Feodaliteyi kurmak",
            "C) Avrupa'ya göç etmek",
            "D) Yeni sömürgeler elde etmek",
            "E) Saltanatı güçlendirmek"
          ],
          "correct": 0,
          "solution": "Doğru cevap Bağımsızlık ve egemenliği pekiştirmek.",
          "id": "e6_q81",
          "no": 81
        },
        {
          "subject": "Tarih",
          "text": "Türk siyasi ve askerî tarihinde büyük öneme sahip olan 'Çanakkale Cephesi' süreci ile ilgili aşağıdakilerden hangisi söylenebilir? (H-153)",
          "options": [
            "A) Hiçbir etkisi olmamıştır.",
            "B) Çanakkale Cephesi dönemin en kritik gelişmelerinden biridir.",
            "C) Osmanlı'nın kuruluş dönemine aittir.",
            "D) Avrupa'da gerçekleşmiştir.",
            "E) Sadece ekonomik bir olaydır."
          ],
          "correct": 1,
          "solution": "Doğru cevap Çanakkale Cephesi dönemin en kritik gelişmelerinden biridir..",
          "id": "e6_q82",
          "no": 82
        },
        {
          "subject": "Tarih",
          "text": "Aşağıdaki tarihî gelişmelerden hangisi 'Sakarya Meydan Muharebesi' ile doğrudan veya dolaylı olarak bağlantılıdır? (H-154)",
          "options": [
            "A) Sanayi İnkılabı",
            "B) Coğrafi Keşifler",
            "C) Sakarya Meydan Muharebesi öncesi ve sonrası yaşanan siyasi krizler.",
            "D) Kavimler Göçü",
            "E) Fransız İhtilali"
          ],
          "correct": 2,
          "solution": "Doğru cevap Sakarya Meydan Muharebesi öncesi ve sonrası yaşanan siyasi krizler..",
          "id": "e6_q83",
          "no": 83
        },
        {
          "subject": "Tarih",
          "text": "Millî Mücadele ve inkılaplar tarihi incelendiğinde 'Büyük Taarruz' olayının temel amacı aşağıdakilerden hangisidir? (H-155)",
          "options": [
            "A) Feodaliteyi kurmak",
            "B) Avrupa'ya göç etmek",
            "C) Yeni sömürgeler elde etmek",
            "D) Bağımsızlık ve egemenliği pekiştirmek",
            "E) Saltanatı güçlendirmek"
          ],
          "correct": 3,
          "solution": "Doğru cevap Bağımsızlık ve egemenliği pekiştirmek.",
          "id": "e6_q84",
          "no": 84
        },
        {
          "subject": "Tarih",
          "text": "Türk siyasi ve askerî tarihinde büyük öneme sahip olan 'I. İnönü Muharebesi' süreci ile ilgili aşağıdakilerden hangisi söylenebilir? (H-156)",
          "options": [
            "A) Osmanlı'nın kuruluş dönemine aittir.",
            "B) Hiçbir etkisi olmamıştır.",
            "C) Sadece ekonomik bir olaydır.",
            "D) I. İnönü Muharebesi dönemin en kritik gelişmelerinden biridir.",
            "E) Avrupa'da gerçekleşmiştir."
          ],
          "correct": 3,
          "solution": "Doğru cevap I. İnönü Muharebesi dönemin en kritik gelişmelerinden biridir..",
          "id": "e6_q85",
          "no": 85
        },
        {
          "subject": "Tarih",
          "text": "Aşağıdaki tarihî gelişmelerden hangisi 'II. İnönü Muharebesi' ile doğrudan veya dolaylı olarak bağlantılıdır? (H-157)",
          "options": [
            "A) Sanayi İnkılabı",
            "B) Coğrafi Keşifler",
            "C) II. İnönü Muharebesi öncesi ve sonrası yaşanan siyasi krizler.",
            "D) Fransız İhtilali",
            "E) Kavimler Göçü"
          ],
          "correct": 2,
          "solution": "Doğru cevap II. İnönü Muharebesi öncesi ve sonrası yaşanan siyasi krizler..",
          "id": "e6_q86",
          "no": 86
        },
        {
          "subject": "Tarih",
          "text": "Millî Mücadele ve inkılaplar tarihi incelendiğinde 'Kars Antlaşması' olayının temel amacı aşağıdakilerden hangisidir? (H-158)",
          "options": [
            "A) Avrupa'ya göç etmek",
            "B) Saltanatı güçlendirmek",
            "C) Feodaliteyi kurmak",
            "D) Bağımsızlık ve egemenliği pekiştirmek",
            "E) Yeni sömürgeler elde etmek"
          ],
          "correct": 3,
          "solution": "Doğru cevap Bağımsızlık ve egemenliği pekiştirmek.",
          "id": "e6_q87",
          "no": 87
        },
        {
          "subject": "Coğrafya",
          "text": "Türkiye'nin fiziki coğrafyası düşünüldüğünde 'Sümela Manastırı' için aşağıdakilerden hangisi doğrudur? (C-88)",
          "options": [
            "A) Sümela Manastırı tarıma kapalıdır.",
            "B) Sümela Manastırı Marmara'dadır.",
            "C) Sümela Manastırı, ülkemizin önemli yeryüzü şekillerinden biridir.",
            "D) Sümela Manastırı yapay bir kanaldır.",
            "E) Sümela Manastırı bir çöldür."
          ],
          "correct": 2,
          "solution": "Doğru cevap Sümela Manastırı, ülkemizin önemli yeryüzü şekillerinden biridir..",
          "id": "e6_q88",
          "no": 88
        },
        {
          "subject": "Coğrafya",
          "text": "Coğrafi özellikleri ve turizm potansiyeli göz önüne alındığında 'Uludağ' hangi alanda daha çok öne çıkar? (C-89)",
          "options": [
            "A) Okyanus balıkçılığı",
            "B) Doğal güzellikleri ve turizm/coğrafi önemi",
            "C) Sadece madencilik",
            "D) Sadece ağır sanayi",
            "E) Çöl iklimi araştırmaları"
          ],
          "correct": 1,
          "solution": "Doğru cevap Doğal güzellikleri ve turizm/coğrafi önemi.",
          "id": "e6_q89",
          "no": 89
        },
        {
          "subject": "Coğrafya",
          "text": "Türkiye'nin fiziki coğrafyası düşünüldüğünde 'Van Gölü' için aşağıdakilerden hangisi doğrudur? (C-90)",
          "options": [
            "A) Van Gölü bir çöldür.",
            "B) Van Gölü, ülkemizin önemli yeryüzü şekillerinden biridir.",
            "C) Van Gölü yapay bir kanaldır.",
            "D) Van Gölü tarıma kapalıdır.",
            "E) Van Gölü Marmara'dadır."
          ],
          "correct": 1,
          "solution": "Doğru cevap Van Gölü, ülkemizin önemli yeryüzü şekillerinden biridir..",
          "id": "e6_q90",
          "no": 90
        },
        {
          "subject": "Coğrafya",
          "text": "Coğrafi özellikleri ve turizm potansiyeli göz önüne alındığında 'Ağrı Dağı' hangi alanda daha çok öne çıkar? (C-91)",
          "options": [
            "A) Okyanus balıkçılığı",
            "B) Sadece ağır sanayi",
            "C) Sadece madencilik",
            "D) Çöl iklimi araştırmaları",
            "E) Doğal güzellikleri ve turizm/coğrafi önemi"
          ],
          "correct": 4,
          "solution": "Doğru cevap Doğal güzellikleri ve turizm/coğrafi önemi.",
          "id": "e6_q91",
          "no": 91
        },
        {
          "subject": "Coğrafya",
          "text": "Türkiye'nin fiziki coğrafyası düşünüldüğünde 'Kızılırmak' için aşağıdakilerden hangisi doğrudur? (C-92)",
          "options": [
            "A) Kızılırmak yapay bir kanaldır.",
            "B) Kızılırmak tarıma kapalıdır.",
            "C) Kızılırmak Marmara'dadır.",
            "D) Kızılırmak bir çöldür.",
            "E) Kızılırmak, ülkemizin önemli yeryüzü şekillerinden biridir."
          ],
          "correct": 4,
          "solution": "Doğru cevap Kızılırmak, ülkemizin önemli yeryüzü şekillerinden biridir..",
          "id": "e6_q92",
          "no": 92
        },
        {
          "subject": "Coğrafya",
          "text": "Coğrafi özellikleri ve turizm potansiyeli göz önüne alındığında 'Erciyes Dağı' hangi alanda daha çok öne çıkar? (C-93)",
          "options": [
            "A) Doğal güzellikleri ve turizm/coğrafi önemi",
            "B) Sadece madencilik",
            "C) Çöl iklimi araştırmaları",
            "D) Okyanus balıkçılığı",
            "E) Sadece ağır sanayi"
          ],
          "correct": 0,
          "solution": "Doğru cevap Doğal güzellikleri ve turizm/coğrafi önemi.",
          "id": "e6_q93",
          "no": 93
        },
        {
          "subject": "Coğrafya",
          "text": "Türkiye'nin fiziki coğrafyası düşünüldüğünde 'Tuz Gölü' için aşağıdakilerden hangisi doğrudur? (C-94)",
          "options": [
            "A) Tuz Gölü yapay bir kanaldır.",
            "B) Tuz Gölü tarıma kapalıdır.",
            "C) Tuz Gölü bir çöldür.",
            "D) Tuz Gölü, ülkemizin önemli yeryüzü şekillerinden biridir.",
            "E) Tuz Gölü Marmara'dadır."
          ],
          "correct": 3,
          "solution": "Doğru cevap Tuz Gölü, ülkemizin önemli yeryüzü şekillerinden biridir..",
          "id": "e6_q94",
          "no": 94
        },
        {
          "subject": "Coğrafya",
          "text": "Coğrafi özellikleri ve turizm potansiyeli göz önüne alındığında 'Çukurova' hangi alanda daha çok öne çıkar? (C-95)",
          "options": [
            "A) Çöl iklimi araştırmaları",
            "B) Okyanus balıkçılığı",
            "C) Sadece ağır sanayi",
            "D) Sadece madencilik",
            "E) Doğal güzellikleri ve turizm/coğrafi önemi"
          ],
          "correct": 4,
          "solution": "Doğru cevap Doğal güzellikleri ve turizm/coğrafi önemi.",
          "id": "e6_q95",
          "no": 95
        },
        {
          "subject": "Coğrafya",
          "text": "Türkiye'nin fiziki coğrafyası düşünüldüğünde 'Bafra Ovası' için aşağıdakilerden hangisi doğrudur? (C-96)",
          "options": [
            "A) Bafra Ovası yapay bir kanaldır.",
            "B) Bafra Ovası bir çöldür.",
            "C) Bafra Ovası tarıma kapalıdır.",
            "D) Bafra Ovası Marmara'dadır.",
            "E) Bafra Ovası, ülkemizin önemli yeryüzü şekillerinden biridir."
          ],
          "correct": 4,
          "solution": "Doğru cevap Bafra Ovası, ülkemizin önemli yeryüzü şekillerinden biridir..",
          "id": "e6_q96",
          "no": 96
        },
        {
          "subject": "Coğrafya",
          "text": "Coğrafi özellikleri ve turizm potansiyeli göz önüne alındığında 'Kaçkar Dağları' hangi alanda daha çok öne çıkar? (C-97)",
          "options": [
            "A) Doğal güzellikleri ve turizm/coğrafi önemi",
            "B) Sadece ağır sanayi",
            "C) Okyanus balıkçılığı",
            "D) Sadece madencilik",
            "E) Çöl iklimi araştırmaları"
          ],
          "correct": 0,
          "solution": "Doğru cevap Doğal güzellikleri ve turizm/coğrafi önemi.",
          "id": "e6_q97",
          "no": 97
        },
        {
          "subject": "Coğrafya",
          "text": "Türkiye'nin fiziki coğrafyası düşünüldüğünde 'Gediz Nehri' için aşağıdakilerden hangisi doğrudur? (C-98)",
          "options": [
            "A) Gediz Nehri, ülkemizin önemli yeryüzü şekillerinden biridir.",
            "B) Gediz Nehri Marmara'dadır.",
            "C) Gediz Nehri tarıma kapalıdır.",
            "D) Gediz Nehri bir çöldür.",
            "E) Gediz Nehri yapay bir kanaldır."
          ],
          "correct": 0,
          "solution": "Doğru cevap Gediz Nehri, ülkemizin önemli yeryüzü şekillerinden biridir..",
          "id": "e6_q98",
          "no": 98
        },
        {
          "subject": "Coğrafya",
          "text": "Coğrafi özellikleri ve turizm potansiyeli göz önüne alındığında 'Salda Gölü' hangi alanda daha çok öne çıkar? (C-99)",
          "options": [
            "A) Okyanus balıkçılığı",
            "B) Sadece madencilik",
            "C) Çöl iklimi araştırmaları",
            "D) Doğal güzellikleri ve turizm/coğrafi önemi",
            "E) Sadece ağır sanayi"
          ],
          "correct": 3,
          "solution": "Doğru cevap Doğal güzellikleri ve turizm/coğrafi önemi.",
          "id": "e6_q99",
          "no": 99
        },
        {
          "subject": "Coğrafya",
          "text": "Türkiye'nin fiziki coğrafyası düşünüldüğünde 'Kapadokya' için aşağıdakilerden hangisi doğrudur? (C-100)",
          "options": [
            "A) Kapadokya, ülkemizin önemli yeryüzü şekillerinden biridir.",
            "B) Kapadokya Marmara'dadır.",
            "C) Kapadokya tarıma kapalıdır.",
            "D) Kapadokya bir çöldür.",
            "E) Kapadokya yapay bir kanaldır."
          ],
          "correct": 0,
          "solution": "Doğru cevap Kapadokya, ülkemizin önemli yeryüzü şekillerinden biridir..",
          "id": "e6_q100",
          "no": 100
        },
        {
          "subject": "Coğrafya",
          "text": "Coğrafi özellikleri ve turizm potansiyeli göz önüne alındığında 'Pamukkale' hangi alanda daha çok öne çıkar? (C-101)",
          "options": [
            "A) Okyanus balıkçılığı",
            "B) Çöl iklimi araştırmaları",
            "C) Doğal güzellikleri ve turizm/coğrafi önemi",
            "D) Sadece ağır sanayi",
            "E) Sadece madencilik"
          ],
          "correct": 2,
          "solution": "Doğru cevap Doğal güzellikleri ve turizm/coğrafi önemi.",
          "id": "e6_q101",
          "no": 101
        },
        {
          "subject": "Coğrafya",
          "text": "Türkiye'nin fiziki coğrafyası düşünüldüğünde 'Nemrut Dağı' için aşağıdakilerden hangisi doğrudur? (C-102)",
          "options": [
            "A) Nemrut Dağı yapay bir kanaldır.",
            "B) Nemrut Dağı Marmara'dadır.",
            "C) Nemrut Dağı, ülkemizin önemli yeryüzü şekillerinden biridir.",
            "D) Nemrut Dağı tarıma kapalıdır.",
            "E) Nemrut Dağı bir çöldür."
          ],
          "correct": 2,
          "solution": "Doğru cevap Nemrut Dağı, ülkemizin önemli yeryüzü şekillerinden biridir..",
          "id": "e6_q102",
          "no": 102
        },
        {
          "subject": "Coğrafya",
          "text": "Coğrafi özellikleri ve turizm potansiyeli göz önüne alındığında 'Sümela Manastırı' hangi alanda daha çok öne çıkar? (C-103)",
          "options": [
            "A) Doğal güzellikleri ve turizm/coğrafi önemi",
            "B) Çöl iklimi araştırmaları",
            "C) Okyanus balıkçılığı",
            "D) Sadece madencilik",
            "E) Sadece ağır sanayi"
          ],
          "correct": 0,
          "solution": "Doğru cevap Doğal güzellikleri ve turizm/coğrafi önemi.",
          "id": "e6_q103",
          "no": 103
        },
        {
          "subject": "Coğrafya",
          "text": "Türkiye'nin fiziki coğrafyası düşünüldüğünde 'Uludağ' için aşağıdakilerden hangisi doğrudur? (C-104)",
          "options": [
            "A) Uludağ, ülkemizin önemli yeryüzü şekillerinden biridir.",
            "B) Uludağ Marmara'dadır.",
            "C) Uludağ bir çöldür.",
            "D) Uludağ yapay bir kanaldır.",
            "E) Uludağ tarıma kapalıdır."
          ],
          "correct": 0,
          "solution": "Doğru cevap Uludağ, ülkemizin önemli yeryüzü şekillerinden biridir..",
          "id": "e6_q104",
          "no": 104
        },
        {
          "subject": "Coğrafya",
          "text": "Coğrafi özellikleri ve turizm potansiyeli göz önüne alındığında 'Van Gölü' hangi alanda daha çok öne çıkar? (C-105)",
          "options": [
            "A) Sadece ağır sanayi",
            "B) Sadece madencilik",
            "C) Çöl iklimi araştırmaları",
            "D) Okyanus balıkçılığı",
            "E) Doğal güzellikleri ve turizm/coğrafi önemi"
          ],
          "correct": 4,
          "solution": "Doğru cevap Doğal güzellikleri ve turizm/coğrafi önemi.",
          "id": "e6_q105",
          "no": 105
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'Belediye' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-73)",
          "options": [
            "A) Belediye, anayasal sistemin önemli bir parçasıdır.",
            "B) Belediye sadece köylerde bulunur.",
            "C) Belediye özel bir şirkettir.",
            "D) Belediye yasaklanmıştır.",
            "E) Belediye yabancı bir kurumdur."
          ],
          "correct": 0,
          "solution": "Doğru cevap Belediye, anayasal sistemin önemli bir parçasıdır..",
          "id": "e6_q106",
          "no": 106
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'Valilik' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-74)",
          "options": [
            "A) Valilik sadece köylerde bulunur.",
            "B) Valilik yasaklanmıştır.",
            "C) Valilik, anayasal sistemin önemli bir parçasıdır.",
            "D) Valilik özel bir şirkettir.",
            "E) Valilik yabancı bir kurumdur."
          ],
          "correct": 2,
          "solution": "Doğru cevap Valilik, anayasal sistemin önemli bir parçasıdır..",
          "id": "e6_q107",
          "no": 107
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'Kaymakamlık' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-75)",
          "options": [
            "A) Kaymakamlık özel bir şirkettir.",
            "B) Kaymakamlık, anayasal sistemin önemli bir parçasıdır.",
            "C) Kaymakamlık sadece köylerde bulunur.",
            "D) Kaymakamlık yabancı bir kurumdur.",
            "E) Kaymakamlık yasaklanmıştır."
          ],
          "correct": 1,
          "solution": "Doğru cevap Kaymakamlık, anayasal sistemin önemli bir parçasıdır..",
          "id": "e6_q108",
          "no": 108
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'İl Genel Meclisi' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-76)",
          "options": [
            "A) İl Genel Meclisi yabancı bir kurumdur.",
            "B) İl Genel Meclisi sadece köylerde bulunur.",
            "C) İl Genel Meclisi yasaklanmıştır.",
            "D) İl Genel Meclisi özel bir şirkettir.",
            "E) İl Genel Meclisi, anayasal sistemin önemli bir parçasıdır."
          ],
          "correct": 4,
          "solution": "Doğru cevap İl Genel Meclisi, anayasal sistemin önemli bir parçasıdır..",
          "id": "e6_q109",
          "no": 109
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'Kamu Denetçiliği Kurumu' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-77)",
          "options": [
            "A) Kamu Denetçiliği Kurumu sadece köylerde bulunur.",
            "B) Kamu Denetçiliği Kurumu özel bir şirkettir.",
            "C) Kamu Denetçiliği Kurumu, anayasal sistemin önemli bir parçasıdır.",
            "D) Kamu Denetçiliği Kurumu yabancı bir kurumdur.",
            "E) Kamu Denetçiliği Kurumu yasaklanmıştır."
          ],
          "correct": 2,
          "solution": "Doğru cevap Kamu Denetçiliği Kurumu, anayasal sistemin önemli bir parçasıdır..",
          "id": "e6_q110",
          "no": 110
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'Anayasa Mahkemesi' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-78)",
          "options": [
            "A) Anayasa Mahkemesi sadece köylerde bulunur.",
            "B) Anayasa Mahkemesi, anayasal sistemin önemli bir parçasıdır.",
            "C) Anayasa Mahkemesi yasaklanmıştır.",
            "D) Anayasa Mahkemesi yabancı bir kurumdur.",
            "E) Anayasa Mahkemesi özel bir şirkettir."
          ],
          "correct": 1,
          "solution": "Doğru cevap Anayasa Mahkemesi, anayasal sistemin önemli bir parçasıdır..",
          "id": "e6_q111",
          "no": 111
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'Yargıtay' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-79)",
          "options": [
            "A) Yargıtay özel bir şirkettir.",
            "B) Yargıtay yabancı bir kurumdur.",
            "C) Yargıtay yasaklanmıştır.",
            "D) Yargıtay sadece köylerde bulunur.",
            "E) Yargıtay, anayasal sistemin önemli bir parçasıdır."
          ],
          "correct": 4,
          "solution": "Doğru cevap Yargıtay, anayasal sistemin önemli bir parçasıdır..",
          "id": "e6_q112",
          "no": 112
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'Danıştay' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-80)",
          "options": [
            "A) Danıştay yabancı bir kurumdur.",
            "B) Danıştay yasaklanmıştır.",
            "C) Danıştay sadece köylerde bulunur.",
            "D) Danıştay özel bir şirkettir.",
            "E) Danıştay, anayasal sistemin önemli bir parçasıdır."
          ],
          "correct": 4,
          "solution": "Doğru cevap Danıştay, anayasal sistemin önemli bir parçasıdır..",
          "id": "e6_q113",
          "no": 113
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'TBMM' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-81)",
          "options": [
            "A) TBMM özel bir şirkettir.",
            "B) TBMM yabancı bir kurumdur.",
            "C) TBMM yasaklanmıştır.",
            "D) TBMM, anayasal sistemin önemli bir parçasıdır.",
            "E) TBMM sadece köylerde bulunur."
          ],
          "correct": 3,
          "solution": "Doğru cevap TBMM, anayasal sistemin önemli bir parçasıdır..",
          "id": "e6_q114",
          "no": 114
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'Cumhurbaşkanlığı' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-82)",
          "options": [
            "A) Cumhurbaşkanlığı yasaklanmıştır.",
            "B) Cumhurbaşkanlığı özel bir şirkettir.",
            "C) Cumhurbaşkanlığı, anayasal sistemin önemli bir parçasıdır.",
            "D) Cumhurbaşkanlığı sadece köylerde bulunur.",
            "E) Cumhurbaşkanlığı yabancı bir kurumdur."
          ],
          "correct": 2,
          "solution": "Doğru cevap Cumhurbaşkanlığı, anayasal sistemin önemli bir parçasıdır..",
          "id": "e6_q115",
          "no": 115
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'Sayıştay' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-83)",
          "options": [
            "A) Sayıştay yasaklanmıştır.",
            "B) Sayıştay özel bir şirkettir.",
            "C) Sayıştay, anayasal sistemin önemli bir parçasıdır.",
            "D) Sayıştay yabancı bir kurumdur.",
            "E) Sayıştay sadece köylerde bulunur."
          ],
          "correct": 2,
          "solution": "Doğru cevap Sayıştay, anayasal sistemin önemli bir parçasıdır..",
          "id": "e6_q116",
          "no": 116
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'YSK' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-84)",
          "options": [
            "A) YSK, anayasal sistemin önemli bir parçasıdır.",
            "B) YSK sadece köylerde bulunur.",
            "C) YSK yasaklanmıştır.",
            "D) YSK özel bir şirkettir.",
            "E) YSK yabancı bir kurumdur."
          ],
          "correct": 0,
          "solution": "Doğru cevap YSK, anayasal sistemin önemli bir parçasıdır..",
          "id": "e6_q117",
          "no": 117
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'HSK' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-85)",
          "options": [
            "A) HSK sadece köylerde bulunur.",
            "B) HSK, anayasal sistemin önemli bir parçasıdır.",
            "C) HSK yasaklanmıştır.",
            "D) HSK yabancı bir kurumdur.",
            "E) HSK özel bir şirkettir."
          ],
          "correct": 1,
          "solution": "Doğru cevap HSK, anayasal sistemin önemli bir parçasıdır..",
          "id": "e6_q118",
          "no": 118
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'Belediye' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-86)",
          "options": [
            "A) Belediye yasaklanmıştır.",
            "B) Belediye özel bir şirkettir.",
            "C) Belediye, anayasal sistemin önemli bir parçasıdır.",
            "D) Belediye yabancı bir kurumdur.",
            "E) Belediye sadece köylerde bulunur."
          ],
          "correct": 2,
          "solution": "Doğru cevap Belediye, anayasal sistemin önemli bir parçasıdır..",
          "id": "e6_q119",
          "no": 119
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'Valilik' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-87)",
          "options": [
            "A) Valilik sadece köylerde bulunur.",
            "B) Valilik yasaklanmıştır.",
            "C) Valilik yabancı bir kurumdur.",
            "D) Valilik, anayasal sistemin önemli bir parçasıdır.",
            "E) Valilik özel bir şirkettir."
          ],
          "correct": 3,
          "solution": "Doğru cevap Valilik, anayasal sistemin önemli bir parçasıdır..",
          "id": "e6_q120",
          "no": 120
        }
      ]
    },
    {
      "id": "deneme_7",
      "name": "7. Deneme Sınavı",
      "totalQuestions": 120,
      "duration": 130,
      "distribution": {
        "Türkçe": 30,
        "Matematik": 30,
        "Tarih": 27,
        "Coğrafya": 18,
        "Vatandaşlık": 15
      },
      "questions": [
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde 'hiç kimse' kelimesinin yazımıyla ilgili bir kural hatırlatılmaktadır? (T-175)",
          "options": [
            "A) 'hiç kimse' kelimesinin doğru yazımına dikkat edilmelidir.",
            "B) hiç kimse kelimesi her zaman ayrı yazılır.",
            "C) hiç kimse kelimesi fiildir.",
            "D) hiç kimse cümlede özne olamaz.",
            "E) hiç kimse kelimesi yabancı kökenlidir."
          ],
          "correct": 0,
          "solution": "Doğru cevap 'hiç kimse' kelimesinin doğru yazımına dikkat edilmelidir..",
          "id": "e7_q1",
          "no": 1
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde mecaz anlamlı bir sözcük kullanılmıştır? (T-176)",
          "options": [
            "A) Olaylara karşı çok 'soğuk' davranıyordu.",
            "B) Suyu dolaptan soğuk içti.",
            "C) Hava bugün çok soğuk.",
            "D) Buzdolabı soğuk üflüyor.",
            "E) Kışın havalar soğuk olur."
          ],
          "correct": 0,
          "solution": "Doğru cevap Olaylara karşı çok 'soğuk' davranıyordu..",
          "id": "e7_q2",
          "no": 2
        },
        {
          "subject": "Türkçe",
          "text": "Bilim tarih boyunca insanlığın en büyük rehberlerinden biri olmuştur. Toplumlar Bilim sayesinde sınırlarını aşmış, geleceğe umutla bakabilmiştir. (P-177)\nBu parçanın ana düşüncesi nedir?",
          "options": [
            "A) Bilim zaman kaybıdır.",
            "B) Bilim, toplumsal ilerleme ve vizyon için vazgeçilmezdir.",
            "C) Bilim sadece geçmişte kalmıştır.",
            "D) İnsanlar Bilim ile ilgilenmemelidir.",
            "E) Bilim sadece bireyseldir."
          ],
          "correct": 1,
          "solution": "Doğru cevap Bilim, toplumsal ilerleme ve vizyon için vazgeçilmezdir..",
          "id": "e7_q3",
          "no": 3
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde 'herkes' kelimesinin yazımıyla ilgili bir kural hatırlatılmaktadır? (T-178)",
          "options": [
            "A) herkes kelimesi yabancı kökenlidir.",
            "B) herkes kelimesi fiildir.",
            "C) herkes kelimesi her zaman ayrı yazılır.",
            "D) 'herkes' kelimesinin doğru yazımına dikkat edilmelidir.",
            "E) herkes cümlede özne olamaz."
          ],
          "correct": 3,
          "solution": "Doğru cevap 'herkes' kelimesinin doğru yazımına dikkat edilmelidir..",
          "id": "e7_q4",
          "no": 4
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde mecaz anlamlı bir sözcük kullanılmıştır? (T-179)",
          "options": [
            "A) Kışın havalar soğuk olur.",
            "B) Buzdolabı soğuk üflüyor.",
            "C) Olaylara karşı çok 'soğuk' davranıyordu.",
            "D) Suyu dolaptan soğuk içti.",
            "E) Hava bugün çok soğuk."
          ],
          "correct": 2,
          "solution": "Doğru cevap Olaylara karşı çok 'soğuk' davranıyordu..",
          "id": "e7_q5",
          "no": 5
        },
        {
          "subject": "Türkçe",
          "text": "Sanat tarih boyunca insanlığın en büyük rehberlerinden biri olmuştur. Toplumlar Sanat sayesinde sınırlarını aşmış, geleceğe umutla bakabilmiştir. (P-180)\nBu parçanın ana düşüncesi nedir?",
          "options": [
            "A) Sanat sadece bireyseldir.",
            "B) Sanat sadece geçmişte kalmıştır.",
            "C) Sanat zaman kaybıdır.",
            "D) Sanat, toplumsal ilerleme ve vizyon için vazgeçilmezdir.",
            "E) İnsanlar Sanat ile ilgilenmemelidir."
          ],
          "correct": 3,
          "solution": "Doğru cevap Sanat, toplumsal ilerleme ve vizyon için vazgeçilmezdir..",
          "id": "e7_q6",
          "no": 6
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde 'bugün' kelimesinin yazımıyla ilgili bir kural hatırlatılmaktadır? (T-181)",
          "options": [
            "A) 'bugün' kelimesinin doğru yazımına dikkat edilmelidir.",
            "B) bugün kelimesi her zaman ayrı yazılır.",
            "C) bugün kelimesi yabancı kökenlidir.",
            "D) bugün kelimesi fiildir.",
            "E) bugün cümlede özne olamaz."
          ],
          "correct": 0,
          "solution": "Doğru cevap 'bugün' kelimesinin doğru yazımına dikkat edilmelidir..",
          "id": "e7_q7",
          "no": 7
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde mecaz anlamlı bir sözcük kullanılmıştır? (T-182)",
          "options": [
            "A) Buzdolabı soğuk üflüyor.",
            "B) Suyu dolaptan soğuk içti.",
            "C) Hava bugün çok soğuk.",
            "D) Olaylara karşı çok 'soğuk' davranıyordu.",
            "E) Kışın havalar soğuk olur."
          ],
          "correct": 3,
          "solution": "Doğru cevap Olaylara karşı çok 'soğuk' davranıyordu..",
          "id": "e7_q8",
          "no": 8
        },
        {
          "subject": "Türkçe",
          "text": "Teknoloji tarih boyunca insanlığın en büyük rehberlerinden biri olmuştur. Toplumlar Teknoloji sayesinde sınırlarını aşmış, geleceğe umutla bakabilmiştir. (P-183)\nBu parçanın ana düşüncesi nedir?",
          "options": [
            "A) Teknoloji sadece geçmişte kalmıştır.",
            "B) İnsanlar Teknoloji ile ilgilenmemelidir.",
            "C) Teknoloji zaman kaybıdır.",
            "D) Teknoloji, toplumsal ilerleme ve vizyon için vazgeçilmezdir.",
            "E) Teknoloji sadece bireyseldir."
          ],
          "correct": 3,
          "solution": "Doğru cevap Teknoloji, toplumsal ilerleme ve vizyon için vazgeçilmezdir..",
          "id": "e7_q9",
          "no": 9
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde 'yalnız' kelimesinin yazımıyla ilgili bir kural hatırlatılmaktadır? (T-184)",
          "options": [
            "A) 'yalnız' kelimesinin doğru yazımına dikkat edilmelidir.",
            "B) yalnız kelimesi her zaman ayrı yazılır.",
            "C) yalnız kelimesi yabancı kökenlidir.",
            "D) yalnız kelimesi fiildir.",
            "E) yalnız cümlede özne olamaz."
          ],
          "correct": 0,
          "solution": "Doğru cevap 'yalnız' kelimesinin doğru yazımına dikkat edilmelidir..",
          "id": "e7_q10",
          "no": 10
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde mecaz anlamlı bir sözcük kullanılmıştır? (T-185)",
          "options": [
            "A) Buzdolabı soğuk üflüyor.",
            "B) Olaylara karşı çok 'soğuk' davranıyordu.",
            "C) Suyu dolaptan soğuk içti.",
            "D) Hava bugün çok soğuk.",
            "E) Kışın havalar soğuk olur."
          ],
          "correct": 1,
          "solution": "Doğru cevap Olaylara karşı çok 'soğuk' davranıyordu..",
          "id": "e7_q11",
          "no": 11
        },
        {
          "subject": "Türkçe",
          "text": "Doğa tarih boyunca insanlığın en büyük rehberlerinden biri olmuştur. Toplumlar Doğa sayesinde sınırlarını aşmış, geleceğe umutla bakabilmiştir. (P-186)\nBu parçanın ana düşüncesi nedir?",
          "options": [
            "A) Doğa sadece bireyseldir.",
            "B) Doğa, toplumsal ilerleme ve vizyon için vazgeçilmezdir.",
            "C) Doğa zaman kaybıdır.",
            "D) İnsanlar Doğa ile ilgilenmemelidir.",
            "E) Doğa sadece geçmişte kalmıştır."
          ],
          "correct": 1,
          "solution": "Doğru cevap Doğa, toplumsal ilerleme ve vizyon için vazgeçilmezdir..",
          "id": "e7_q12",
          "no": 12
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde 'hiçbir' kelimesinin yazımıyla ilgili bir kural hatırlatılmaktadır? (T-187)",
          "options": [
            "A) hiçbir kelimesi yabancı kökenlidir.",
            "B) hiçbir kelimesi her zaman ayrı yazılır.",
            "C) hiçbir kelimesi fiildir.",
            "D) 'hiçbir' kelimesinin doğru yazımına dikkat edilmelidir.",
            "E) hiçbir cümlede özne olamaz."
          ],
          "correct": 3,
          "solution": "Doğru cevap 'hiçbir' kelimesinin doğru yazımına dikkat edilmelidir..",
          "id": "e7_q13",
          "no": 13
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde mecaz anlamlı bir sözcük kullanılmıştır? (T-188)",
          "options": [
            "A) Hava bugün çok soğuk.",
            "B) Suyu dolaptan soğuk içti.",
            "C) Buzdolabı soğuk üflüyor.",
            "D) Kışın havalar soğuk olur.",
            "E) Olaylara karşı çok 'soğuk' davranıyordu."
          ],
          "correct": 4,
          "solution": "Doğru cevap Olaylara karşı çok 'soğuk' davranıyordu..",
          "id": "e7_q14",
          "no": 14
        },
        {
          "subject": "Türkçe",
          "text": "Psikoloji tarih boyunca insanlığın en büyük rehberlerinden biri olmuştur. Toplumlar Psikoloji sayesinde sınırlarını aşmış, geleceğe umutla bakabilmiştir. (P-189)\nBu parçanın ana düşüncesi nedir?",
          "options": [
            "A) İnsanlar Psikoloji ile ilgilenmemelidir.",
            "B) Psikoloji sadece geçmişte kalmıştır.",
            "C) Psikoloji, toplumsal ilerleme ve vizyon için vazgeçilmezdir.",
            "D) Psikoloji zaman kaybıdır.",
            "E) Psikoloji sadece bireyseldir."
          ],
          "correct": 2,
          "solution": "Doğru cevap Psikoloji, toplumsal ilerleme ve vizyon için vazgeçilmezdir..",
          "id": "e7_q15",
          "no": 15
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde 'her şey' kelimesinin yazımıyla ilgili bir kural hatırlatılmaktadır? (T-190)",
          "options": [
            "A) her şey kelimesi her zaman ayrı yazılır.",
            "B) her şey cümlede özne olamaz.",
            "C) her şey kelimesi yabancı kökenlidir.",
            "D) 'her şey' kelimesinin doğru yazımına dikkat edilmelidir.",
            "E) her şey kelimesi fiildir."
          ],
          "correct": 3,
          "solution": "Doğru cevap 'her şey' kelimesinin doğru yazımına dikkat edilmelidir..",
          "id": "e7_q16",
          "no": 16
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde mecaz anlamlı bir sözcük kullanılmıştır? (T-191)",
          "options": [
            "A) Suyu dolaptan soğuk içti.",
            "B) Kışın havalar soğuk olur.",
            "C) Olaylara karşı çok 'soğuk' davranıyordu.",
            "D) Buzdolabı soğuk üflüyor.",
            "E) Hava bugün çok soğuk."
          ],
          "correct": 2,
          "solution": "Doğru cevap Olaylara karşı çok 'soğuk' davranıyordu..",
          "id": "e7_q17",
          "no": 17
        },
        {
          "subject": "Türkçe",
          "text": "Eğitim tarih boyunca insanlığın en büyük rehberlerinden biri olmuştur. Toplumlar Eğitim sayesinde sınırlarını aşmış, geleceğe umutla bakabilmiştir. (P-192)\nBu parçanın ana düşüncesi nedir?",
          "options": [
            "A) İnsanlar Eğitim ile ilgilenmemelidir.",
            "B) Eğitim, toplumsal ilerleme ve vizyon için vazgeçilmezdir.",
            "C) Eğitim zaman kaybıdır.",
            "D) Eğitim sadece bireyseldir.",
            "E) Eğitim sadece geçmişte kalmıştır."
          ],
          "correct": 1,
          "solution": "Doğru cevap Eğitim, toplumsal ilerleme ve vizyon için vazgeçilmezdir..",
          "id": "e7_q18",
          "no": 18
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde 'yanlış' kelimesinin yazımıyla ilgili bir kural hatırlatılmaktadır? (T-193)",
          "options": [
            "A) yanlış cümlede özne olamaz.",
            "B) yanlış kelimesi her zaman ayrı yazılır.",
            "C) 'yanlış' kelimesinin doğru yazımına dikkat edilmelidir.",
            "D) yanlış kelimesi yabancı kökenlidir.",
            "E) yanlış kelimesi fiildir."
          ],
          "correct": 2,
          "solution": "Doğru cevap 'yanlış' kelimesinin doğru yazımına dikkat edilmelidir..",
          "id": "e7_q19",
          "no": 19
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde mecaz anlamlı bir sözcük kullanılmıştır? (T-194)",
          "options": [
            "A) Olaylara karşı çok 'soğuk' davranıyordu.",
            "B) Kışın havalar soğuk olur.",
            "C) Suyu dolaptan soğuk içti.",
            "D) Buzdolabı soğuk üflüyor.",
            "E) Hava bugün çok soğuk."
          ],
          "correct": 0,
          "solution": "Doğru cevap Olaylara karşı çok 'soğuk' davranıyordu..",
          "id": "e7_q20",
          "no": 20
        },
        {
          "subject": "Türkçe",
          "text": "Kültür tarih boyunca insanlığın en büyük rehberlerinden biri olmuştur. Toplumlar Kültür sayesinde sınırlarını aşmış, geleceğe umutla bakabilmiştir. (P-195)\nBu parçanın ana düşüncesi nedir?",
          "options": [
            "A) Kültür, toplumsal ilerleme ve vizyon için vazgeçilmezdir.",
            "B) Kültür sadece bireyseldir.",
            "C) Kültür zaman kaybıdır.",
            "D) Kültür sadece geçmişte kalmıştır.",
            "E) İnsanlar Kültür ile ilgilenmemelidir."
          ],
          "correct": 0,
          "solution": "Doğru cevap Kültür, toplumsal ilerleme ve vizyon için vazgeçilmezdir..",
          "id": "e7_q21",
          "no": 21
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde 'birkaç' kelimesinin yazımıyla ilgili bir kural hatırlatılmaktadır? (T-196)",
          "options": [
            "A) birkaç kelimesi yabancı kökenlidir.",
            "B) 'birkaç' kelimesinin doğru yazımına dikkat edilmelidir.",
            "C) birkaç kelimesi fiildir.",
            "D) birkaç kelimesi her zaman ayrı yazılır.",
            "E) birkaç cümlede özne olamaz."
          ],
          "correct": 1,
          "solution": "Doğru cevap 'birkaç' kelimesinin doğru yazımına dikkat edilmelidir..",
          "id": "e7_q22",
          "no": 22
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde mecaz anlamlı bir sözcük kullanılmıştır? (T-197)",
          "options": [
            "A) Buzdolabı soğuk üflüyor.",
            "B) Olaylara karşı çok 'soğuk' davranıyordu.",
            "C) Hava bugün çok soğuk.",
            "D) Suyu dolaptan soğuk içti.",
            "E) Kışın havalar soğuk olur."
          ],
          "correct": 1,
          "solution": "Doğru cevap Olaylara karşı çok 'soğuk' davranıyordu..",
          "id": "e7_q23",
          "no": 23
        },
        {
          "subject": "Türkçe",
          "text": "Felsefe tarih boyunca insanlığın en büyük rehberlerinden biri olmuştur. Toplumlar Felsefe sayesinde sınırlarını aşmış, geleceğe umutla bakabilmiştir. (P-198)\nBu parçanın ana düşüncesi nedir?",
          "options": [
            "A) Felsefe zaman kaybıdır.",
            "B) Felsefe sadece geçmişte kalmıştır.",
            "C) Felsefe, toplumsal ilerleme ve vizyon için vazgeçilmezdir.",
            "D) İnsanlar Felsefe ile ilgilenmemelidir.",
            "E) Felsefe sadece bireyseldir."
          ],
          "correct": 2,
          "solution": "Doğru cevap Felsefe, toplumsal ilerleme ve vizyon için vazgeçilmezdir..",
          "id": "e7_q24",
          "no": 24
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde 'hiç kimse' kelimesinin yazımıyla ilgili bir kural hatırlatılmaktadır? (T-199)",
          "options": [
            "A) hiç kimse cümlede özne olamaz.",
            "B) hiç kimse kelimesi yabancı kökenlidir.",
            "C) 'hiç kimse' kelimesinin doğru yazımına dikkat edilmelidir.",
            "D) hiç kimse kelimesi fiildir.",
            "E) hiç kimse kelimesi her zaman ayrı yazılır."
          ],
          "correct": 2,
          "solution": "Doğru cevap 'hiç kimse' kelimesinin doğru yazımına dikkat edilmelidir..",
          "id": "e7_q25",
          "no": 25
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde mecaz anlamlı bir sözcük kullanılmıştır? (T-200)",
          "options": [
            "A) Buzdolabı soğuk üflüyor.",
            "B) Hava bugün çok soğuk.",
            "C) Kışın havalar soğuk olur.",
            "D) Suyu dolaptan soğuk içti.",
            "E) Olaylara karşı çok 'soğuk' davranıyordu."
          ],
          "correct": 4,
          "solution": "Doğru cevap Olaylara karşı çok 'soğuk' davranıyordu..",
          "id": "e7_q26",
          "no": 26
        },
        {
          "subject": "Türkçe",
          "text": "Edebiyat tarih boyunca insanlığın en büyük rehberlerinden biri olmuştur. Toplumlar Edebiyat sayesinde sınırlarını aşmış, geleceğe umutla bakabilmiştir. (P-201)\nBu parçanın ana düşüncesi nedir?",
          "options": [
            "A) Edebiyat zaman kaybıdır.",
            "B) Edebiyat sadece geçmişte kalmıştır.",
            "C) Edebiyat sadece bireyseldir.",
            "D) İnsanlar Edebiyat ile ilgilenmemelidir.",
            "E) Edebiyat, toplumsal ilerleme ve vizyon için vazgeçilmezdir."
          ],
          "correct": 4,
          "solution": "Doğru cevap Edebiyat, toplumsal ilerleme ve vizyon için vazgeçilmezdir..",
          "id": "e7_q27",
          "no": 27
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde 'herkes' kelimesinin yazımıyla ilgili bir kural hatırlatılmaktadır? (T-202)",
          "options": [
            "A) 'herkes' kelimesinin doğru yazımına dikkat edilmelidir.",
            "B) herkes kelimesi yabancı kökenlidir.",
            "C) herkes kelimesi her zaman ayrı yazılır.",
            "D) herkes cümlede özne olamaz.",
            "E) herkes kelimesi fiildir."
          ],
          "correct": 0,
          "solution": "Doğru cevap 'herkes' kelimesinin doğru yazımına dikkat edilmelidir..",
          "id": "e7_q28",
          "no": 28
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde mecaz anlamlı bir sözcük kullanılmıştır? (T-203)",
          "options": [
            "A) Kışın havalar soğuk olur.",
            "B) Buzdolabı soğuk üflüyor.",
            "C) Hava bugün çok soğuk.",
            "D) Olaylara karşı çok 'soğuk' davranıyordu.",
            "E) Suyu dolaptan soğuk içti."
          ],
          "correct": 3,
          "solution": "Doğru cevap Olaylara karşı çok 'soğuk' davranıyordu..",
          "id": "e7_q29",
          "no": 29
        },
        {
          "subject": "Türkçe",
          "text": "Tarih tarih boyunca insanlığın en büyük rehberlerinden biri olmuştur. Toplumlar Tarih sayesinde sınırlarını aşmış, geleceğe umutla bakabilmiştir. (P-204)\nBu parçanın ana düşüncesi nedir?",
          "options": [
            "A) Tarih sadece geçmişte kalmıştır.",
            "B) Tarih zaman kaybıdır.",
            "C) İnsanlar Tarih ile ilgilenmemelidir.",
            "D) Tarih sadece bireyseldir.",
            "E) Tarih, toplumsal ilerleme ve vizyon için vazgeçilmezdir."
          ],
          "correct": 4,
          "solution": "Doğru cevap Tarih, toplumsal ilerleme ve vizyon için vazgeçilmezdir..",
          "id": "e7_q30",
          "no": 30
        },
        {
          "subject": "Matematik",
          "text": "3x + 26 = 59 denkleminde x kaçtır? (SoruID: M180)",
          "options": [
            "A) 11",
            "B) 12",
            "C) 10",
            "D) 14",
            "E) 13"
          ],
          "correct": 0,
          "solution": "Doğru cevap 11.",
          "id": "e7_q31",
          "no": 31
        },
        {
          "subject": "Matematik",
          "text": "160 sayısının %20'si kaçtır? (SoruID: M181)",
          "options": [
            "A) 32",
            "B) 42",
            "C) 47",
            "D) 37",
            "E) 27"
          ],
          "correct": 0,
          "solution": "Doğru cevap 32.",
          "id": "e7_q32",
          "no": 32
        },
        {
          "subject": "Matematik",
          "text": "28, 20 ve 30 sayılarının aritmetik ortalaması kaçtır? (SoruID: M182)",
          "options": [
            "A) 24",
            "B) 27",
            "C) 26",
            "D) 25",
            "E) 28"
          ],
          "correct": 2,
          "solution": "Doğru cevap 26.",
          "id": "e7_q33",
          "no": 33
        },
        {
          "subject": "Matematik",
          "text": "Ali 22, Ayşe 21 yaşındadır. 7 yıl sonra yaşları toplamı kaç olur? (SoruID: M183)",
          "options": [
            "A) 56",
            "B) 50",
            "C) 64",
            "D) 57",
            "E) 58"
          ],
          "correct": 3,
          "solution": "Doğru cevap 57.",
          "id": "e7_q34",
          "no": 34
        },
        {
          "subject": "Matematik",
          "text": "√81 + √4 işleminin sonucu kaçtır? (SoruID: M184)",
          "options": [
            "A) 13",
            "B) 12",
            "C) 10",
            "D) 11",
            "E) 9"
          ],
          "correct": 3,
          "solution": "Doğru cevap 11.",
          "id": "e7_q35",
          "no": 35
        },
        {
          "subject": "Matematik",
          "text": "2x + 26 = 30 denkleminde x kaçtır? (SoruID: M185)",
          "options": [
            "A) 2",
            "B) 5",
            "C) 3",
            "D) 1",
            "E) 4"
          ],
          "correct": 0,
          "solution": "Doğru cevap 2.",
          "id": "e7_q36",
          "no": 36
        },
        {
          "subject": "Matematik",
          "text": "120 sayısının %10'si kaçtır? (SoruID: M186)",
          "options": [
            "A) 17",
            "B) 7",
            "C) 12",
            "D) 27",
            "E) 22"
          ],
          "correct": 2,
          "solution": "Doğru cevap 12.",
          "id": "e7_q37",
          "no": 37
        },
        {
          "subject": "Matematik",
          "text": "17, 15 ve 13 sayılarının aritmetik ortalaması kaçtır? (SoruID: M187)",
          "options": [
            "A) 16",
            "B) 13",
            "C) 15",
            "D) 17",
            "E) 14"
          ],
          "correct": 2,
          "solution": "Doğru cevap 15.",
          "id": "e7_q38",
          "no": 38
        },
        {
          "subject": "Matematik",
          "text": "Ali 19, Ayşe 14 yaşındadır. 4 yıl sonra yaşları toplamı kaç olur? (SoruID: M188)",
          "options": [
            "A) 40",
            "B) 37",
            "C) 41",
            "D) 45",
            "E) 42"
          ],
          "correct": 2,
          "solution": "Doğru cevap 41.",
          "id": "e7_q39",
          "no": 39
        },
        {
          "subject": "Matematik",
          "text": "√9 + √9 işleminin sonucu kaçtır? (SoruID: M189)",
          "options": [
            "A) 7",
            "B) 5",
            "C) 6",
            "D) 8",
            "E) 4"
          ],
          "correct": 2,
          "solution": "Doğru cevap 6.",
          "id": "e7_q40",
          "no": 40
        },
        {
          "subject": "Matematik",
          "text": "9x + 40 = 166 denkleminde x kaçtır? (SoruID: M190)",
          "options": [
            "A) 17",
            "B) 16",
            "C) 15",
            "D) 13",
            "E) 14"
          ],
          "correct": 4,
          "solution": "Doğru cevap 14.",
          "id": "e7_q41",
          "no": 41
        },
        {
          "subject": "Matematik",
          "text": "180 sayısının %30'si kaçtır? (SoruID: M191)",
          "options": [
            "A) 49",
            "B) 69",
            "C) 64",
            "D) 59",
            "E) 54"
          ],
          "correct": 4,
          "solution": "Doğru cevap 54.",
          "id": "e7_q42",
          "no": 42
        },
        {
          "subject": "Matematik",
          "text": "18, 30 ve 27 sayılarının aritmetik ortalaması kaçtır? (SoruID: M192)",
          "options": [
            "A) 23",
            "B) 25",
            "C) 24",
            "D) 27",
            "E) 26"
          ],
          "correct": 1,
          "solution": "Doğru cevap 25.",
          "id": "e7_q43",
          "no": 43
        },
        {
          "subject": "Matematik",
          "text": "Ali 12, Ayşe 24 yaşındadır. 9 yıl sonra yaşları toplamı kaç olur? (SoruID: M193)",
          "options": [
            "A) 63",
            "B) 54",
            "C) 45",
            "D) 53",
            "E) 55"
          ],
          "correct": 1,
          "solution": "Doğru cevap 54.",
          "id": "e7_q44",
          "no": 44
        },
        {
          "subject": "Matematik",
          "text": "√4 + √36 işleminin sonucu kaçtır? (SoruID: M194)",
          "options": [
            "A) 7",
            "B) 6",
            "C) 10",
            "D) 9",
            "E) 8"
          ],
          "correct": 4,
          "solution": "Doğru cevap 8.",
          "id": "e7_q45",
          "no": 45
        },
        {
          "subject": "Matematik",
          "text": "6x + 34 = 106 denkleminde x kaçtır? (SoruID: M195)",
          "options": [
            "A) 11",
            "B) 14",
            "C) 12",
            "D) 13",
            "E) 15"
          ],
          "correct": 2,
          "solution": "Doğru cevap 12.",
          "id": "e7_q46",
          "no": 46
        },
        {
          "subject": "Matematik",
          "text": "90 sayısının %40'si kaçtır? (SoruID: M196)",
          "options": [
            "A) 31",
            "B) 46",
            "C) 41",
            "D) 51",
            "E) 36"
          ],
          "correct": 4,
          "solution": "Doğru cevap 36.",
          "id": "e7_q47",
          "no": 47
        },
        {
          "subject": "Matematik",
          "text": "22, 12 ve 23 sayılarının aritmetik ortalaması kaçtır? (SoruID: M197)",
          "options": [
            "A) 18",
            "B) 20",
            "C) 17",
            "D) 19",
            "E) 21"
          ],
          "correct": 3,
          "solution": "Doğru cevap 19.",
          "id": "e7_q48",
          "no": 48
        },
        {
          "subject": "Matematik",
          "text": "Ali 12, Ayşe 18 yaşındadır. 6 yıl sonra yaşları toplamı kaç olur? (SoruID: M198)",
          "options": [
            "A) 43",
            "B) 42",
            "C) 41",
            "D) 36",
            "E) 48"
          ],
          "correct": 1,
          "solution": "Doğru cevap 42.",
          "id": "e7_q49",
          "no": 49
        },
        {
          "subject": "Matematik",
          "text": "√36 + √9 işleminin sonucu kaçtır? (SoruID: M199)",
          "options": [
            "A) 10",
            "B) 11",
            "C) 8",
            "D) 9",
            "E) 7"
          ],
          "correct": 3,
          "solution": "Doğru cevap 9.",
          "id": "e7_q50",
          "no": 50
        },
        {
          "subject": "Matematik",
          "text": "9x + 27 = 108 denkleminde x kaçtır? (SoruID: M200)",
          "options": [
            "A) 11",
            "B) 8",
            "C) 9",
            "D) 12",
            "E) 10"
          ],
          "correct": 2,
          "solution": "Doğru cevap 9.",
          "id": "e7_q51",
          "no": 51
        },
        {
          "subject": "Matematik",
          "text": "120 sayısının %20'si kaçtır? (SoruID: M201)",
          "options": [
            "A) 24",
            "B) 34",
            "C) 39",
            "D) 19",
            "E) 29"
          ],
          "correct": 0,
          "solution": "Doğru cevap 24.",
          "id": "e7_q52",
          "no": 52
        },
        {
          "subject": "Matematik",
          "text": "21, 16 ve 17 sayılarının aritmetik ortalaması kaçtır? (SoruID: M202)",
          "options": [
            "A) 20",
            "B) 18",
            "C) 16",
            "D) 17",
            "E) 19"
          ],
          "correct": 1,
          "solution": "Doğru cevap 18.",
          "id": "e7_q53",
          "no": 53
        },
        {
          "subject": "Matematik",
          "text": "Ali 14, Ayşe 19 yaşındadır. 3 yıl sonra yaşları toplamı kaç olur? (SoruID: M203)",
          "options": [
            "A) 40",
            "B) 42",
            "C) 39",
            "D) 36",
            "E) 38"
          ],
          "correct": 2,
          "solution": "Doğru cevap 39.",
          "id": "e7_q54",
          "no": 54
        },
        {
          "subject": "Matematik",
          "text": "√81 + √4 işleminin sonucu kaçtır? (SoruID: M204)",
          "options": [
            "A) 11",
            "B) 9",
            "C) 13",
            "D) 12",
            "E) 10"
          ],
          "correct": 0,
          "solution": "Doğru cevap 11.",
          "id": "e7_q55",
          "no": 55
        },
        {
          "subject": "Matematik",
          "text": "8x + 50 = 170 denkleminde x kaçtır? (SoruID: M205)",
          "options": [
            "A) 14",
            "B) 18",
            "C) 17",
            "D) 16",
            "E) 15"
          ],
          "correct": 4,
          "solution": "Doğru cevap 15.",
          "id": "e7_q56",
          "no": 56
        },
        {
          "subject": "Matematik",
          "text": "120 sayısının %60'si kaçtır? (SoruID: M206)",
          "options": [
            "A) 87",
            "B) 67",
            "C) 82",
            "D) 77",
            "E) 72"
          ],
          "correct": 4,
          "solution": "Doğru cevap 72.",
          "id": "e7_q57",
          "no": 57
        },
        {
          "subject": "Matematik",
          "text": "19, 14 ve 12 sayılarının aritmetik ortalaması kaçtır? (SoruID: M207)",
          "options": [
            "A) 17",
            "B) 13",
            "C) 16",
            "D) 14",
            "E) 15"
          ],
          "correct": 4,
          "solution": "Doğru cevap 15.",
          "id": "e7_q58",
          "no": 58
        },
        {
          "subject": "Matematik",
          "text": "Ali 16, Ayşe 16 yaşındadır. 3 yıl sonra yaşları toplamı kaç olur? (SoruID: M208)",
          "options": [
            "A) 41",
            "B) 39",
            "C) 37",
            "D) 35",
            "E) 38"
          ],
          "correct": 4,
          "solution": "Doğru cevap 38.",
          "id": "e7_q59",
          "no": 59
        },
        {
          "subject": "Matematik",
          "text": "√49 + √9 işleminin sonucu kaçtır? (SoruID: M209)",
          "options": [
            "A) 10",
            "B) 11",
            "C) 8",
            "D) 12",
            "E) 9"
          ],
          "correct": 0,
          "solution": "Doğru cevap 10.",
          "id": "e7_q60",
          "no": 60
        },
        {
          "subject": "Tarih",
          "text": "Türk siyasi ve askerî tarihinde büyük öneme sahip olan 'Ankara Antlaşması' süreci ile ilgili aşağıdakilerden hangisi söylenebilir? (H-159)",
          "options": [
            "A) Ankara Antlaşması dönemin en kritik gelişmelerinden biridir.",
            "B) Osmanlı'nın kuruluş dönemine aittir.",
            "C) Sadece ekonomik bir olaydır.",
            "D) Hiçbir etkisi olmamıştır.",
            "E) Avrupa'da gerçekleşmiştir."
          ],
          "correct": 0,
          "solution": "Doğru cevap Ankara Antlaşması dönemin en kritik gelişmelerinden biridir..",
          "id": "e7_q61",
          "no": 61
        },
        {
          "subject": "Tarih",
          "text": "Aşağıdaki tarihî gelişmelerden hangisi 'Sivas Kongresi' ile doğrudan veya dolaylı olarak bağlantılıdır? (H-160)",
          "options": [
            "A) Fransız İhtilali",
            "B) Coğrafi Keşifler",
            "C) Sivas Kongresi öncesi ve sonrası yaşanan siyasi krizler.",
            "D) Sanayi İnkılabı",
            "E) Kavimler Göçü"
          ],
          "correct": 2,
          "solution": "Doğru cevap Sivas Kongresi öncesi ve sonrası yaşanan siyasi krizler..",
          "id": "e7_q62",
          "no": 62
        },
        {
          "subject": "Tarih",
          "text": "Millî Mücadele ve inkılaplar tarihi incelendiğinde 'Erzurum Kongresi' olayının temel amacı aşağıdakilerden hangisidir? (H-161)",
          "options": [
            "A) Avrupa'ya göç etmek",
            "B) Yeni sömürgeler elde etmek",
            "C) Saltanatı güçlendirmek",
            "D) Bağımsızlık ve egemenliği pekiştirmek",
            "E) Feodaliteyi kurmak"
          ],
          "correct": 3,
          "solution": "Doğru cevap Bağımsızlık ve egemenliği pekiştirmek.",
          "id": "e7_q63",
          "no": 63
        },
        {
          "subject": "Tarih",
          "text": "Türk siyasi ve askerî tarihinde büyük öneme sahip olan 'Amasya Genelgesi' süreci ile ilgili aşağıdakilerden hangisi söylenebilir? (H-162)",
          "options": [
            "A) Avrupa'da gerçekleşmiştir.",
            "B) Amasya Genelgesi dönemin en kritik gelişmelerinden biridir.",
            "C) Osmanlı'nın kuruluş dönemine aittir.",
            "D) Sadece ekonomik bir olaydır.",
            "E) Hiçbir etkisi olmamıştır."
          ],
          "correct": 1,
          "solution": "Doğru cevap Amasya Genelgesi dönemin en kritik gelişmelerinden biridir..",
          "id": "e7_q64",
          "no": 64
        },
        {
          "subject": "Tarih",
          "text": "Aşağıdaki tarihî gelişmelerden hangisi 'Lozan Antlaşması' ile doğrudan veya dolaylı olarak bağlantılıdır? (H-163)",
          "options": [
            "A) Sanayi İnkılabı",
            "B) Fransız İhtilali",
            "C) Coğrafi Keşifler",
            "D) Lozan Antlaşması öncesi ve sonrası yaşanan siyasi krizler.",
            "E) Kavimler Göçü"
          ],
          "correct": 3,
          "solution": "Doğru cevap Lozan Antlaşması öncesi ve sonrası yaşanan siyasi krizler..",
          "id": "e7_q65",
          "no": 65
        },
        {
          "subject": "Tarih",
          "text": "Millî Mücadele ve inkılaplar tarihi incelendiğinde 'Cumhuriyetin İlanı' olayının temel amacı aşağıdakilerden hangisidir? (H-164)",
          "options": [
            "A) Yeni sömürgeler elde etmek",
            "B) Saltanatı güçlendirmek",
            "C) Avrupa'ya göç etmek",
            "D) Feodaliteyi kurmak",
            "E) Bağımsızlık ve egemenliği pekiştirmek"
          ],
          "correct": 4,
          "solution": "Doğru cevap Bağımsızlık ve egemenliği pekiştirmek.",
          "id": "e7_q66",
          "no": 66
        },
        {
          "subject": "Tarih",
          "text": "Türk siyasi ve askerî tarihinde büyük öneme sahip olan 'TBMM'nin Açılışı' süreci ile ilgili aşağıdakilerden hangisi söylenebilir? (H-165)",
          "options": [
            "A) Hiçbir etkisi olmamıştır.",
            "B) TBMM'nin Açılışı dönemin en kritik gelişmelerinden biridir.",
            "C) Sadece ekonomik bir olaydır.",
            "D) Osmanlı'nın kuruluş dönemine aittir.",
            "E) Avrupa'da gerçekleşmiştir."
          ],
          "correct": 1,
          "solution": "Doğru cevap TBMM'nin Açılışı dönemin en kritik gelişmelerinden biridir..",
          "id": "e7_q67",
          "no": 67
        },
        {
          "subject": "Tarih",
          "text": "Aşağıdaki tarihî gelişmelerden hangisi 'Mudanya Mütarekesi' ile doğrudan veya dolaylı olarak bağlantılıdır? (H-166)",
          "options": [
            "A) Fransız İhtilali",
            "B) Kavimler Göçü",
            "C) Coğrafi Keşifler",
            "D) Mudanya Mütarekesi öncesi ve sonrası yaşanan siyasi krizler.",
            "E) Sanayi İnkılabı"
          ],
          "correct": 3,
          "solution": "Doğru cevap Mudanya Mütarekesi öncesi ve sonrası yaşanan siyasi krizler..",
          "id": "e7_q68",
          "no": 68
        },
        {
          "subject": "Tarih",
          "text": "Millî Mücadele ve inkılaplar tarihi incelendiğinde 'Saltanatın Kaldırılması' olayının temel amacı aşağıdakilerden hangisidir? (H-167)",
          "options": [
            "A) Bağımsızlık ve egemenliği pekiştirmek",
            "B) Saltanatı güçlendirmek",
            "C) Yeni sömürgeler elde etmek",
            "D) Avrupa'ya göç etmek",
            "E) Feodaliteyi kurmak"
          ],
          "correct": 0,
          "solution": "Doğru cevap Bağımsızlık ve egemenliği pekiştirmek.",
          "id": "e7_q69",
          "no": 69
        },
        {
          "subject": "Tarih",
          "text": "Türk siyasi ve askerî tarihinde büyük öneme sahip olan 'Halifeliğin Kaldırılması' süreci ile ilgili aşağıdakilerden hangisi söylenebilir? (H-168)",
          "options": [
            "A) Halifeliğin Kaldırılması dönemin en kritik gelişmelerinden biridir.",
            "B) Avrupa'da gerçekleşmiştir.",
            "C) Sadece ekonomik bir olaydır.",
            "D) Hiçbir etkisi olmamıştır.",
            "E) Osmanlı'nın kuruluş dönemine aittir."
          ],
          "correct": 0,
          "solution": "Doğru cevap Halifeliğin Kaldırılması dönemin en kritik gelişmelerinden biridir..",
          "id": "e7_q70",
          "no": 70
        },
        {
          "subject": "Tarih",
          "text": "Aşağıdaki tarihî gelişmelerden hangisi 'Tevhid-i Tedrisat' ile doğrudan veya dolaylı olarak bağlantılıdır? (H-169)",
          "options": [
            "A) Tevhid-i Tedrisat öncesi ve sonrası yaşanan siyasi krizler.",
            "B) Fransız İhtilali",
            "C) Sanayi İnkılabı",
            "D) Kavimler Göçü",
            "E) Coğrafi Keşifler"
          ],
          "correct": 0,
          "solution": "Doğru cevap Tevhid-i Tedrisat öncesi ve sonrası yaşanan siyasi krizler..",
          "id": "e7_q71",
          "no": 71
        },
        {
          "subject": "Tarih",
          "text": "Millî Mücadele ve inkılaplar tarihi incelendiğinde 'Trablusgarp Savaşı' olayının temel amacı aşağıdakilerden hangisidir? (H-170)",
          "options": [
            "A) Avrupa'ya göç etmek",
            "B) Saltanatı güçlendirmek",
            "C) Yeni sömürgeler elde etmek",
            "D) Bağımsızlık ve egemenliği pekiştirmek",
            "E) Feodaliteyi kurmak"
          ],
          "correct": 3,
          "solution": "Doğru cevap Bağımsızlık ve egemenliği pekiştirmek.",
          "id": "e7_q72",
          "no": 72
        },
        {
          "subject": "Tarih",
          "text": "Türk siyasi ve askerî tarihinde büyük öneme sahip olan 'Balkan Savaşları' süreci ile ilgili aşağıdakilerden hangisi söylenebilir? (H-171)",
          "options": [
            "A) Osmanlı'nın kuruluş dönemine aittir.",
            "B) Sadece ekonomik bir olaydır.",
            "C) Hiçbir etkisi olmamıştır.",
            "D) Balkan Savaşları dönemin en kritik gelişmelerinden biridir.",
            "E) Avrupa'da gerçekleşmiştir."
          ],
          "correct": 3,
          "solution": "Doğru cevap Balkan Savaşları dönemin en kritik gelişmelerinden biridir..",
          "id": "e7_q73",
          "no": 73
        },
        {
          "subject": "Tarih",
          "text": "Aşağıdaki tarihî gelişmelerden hangisi 'I. Dünya Savaşı' ile doğrudan veya dolaylı olarak bağlantılıdır? (H-172)",
          "options": [
            "A) I. Dünya Savaşı öncesi ve sonrası yaşanan siyasi krizler.",
            "B) Fransız İhtilali",
            "C) Sanayi İnkılabı",
            "D) Coğrafi Keşifler",
            "E) Kavimler Göçü"
          ],
          "correct": 0,
          "solution": "Doğru cevap I. Dünya Savaşı öncesi ve sonrası yaşanan siyasi krizler..",
          "id": "e7_q74",
          "no": 74
        },
        {
          "subject": "Tarih",
          "text": "Millî Mücadele ve inkılaplar tarihi incelendiğinde 'Çanakkale Cephesi' olayının temel amacı aşağıdakilerden hangisidir? (H-173)",
          "options": [
            "A) Bağımsızlık ve egemenliği pekiştirmek",
            "B) Yeni sömürgeler elde etmek",
            "C) Saltanatı güçlendirmek",
            "D) Avrupa'ya göç etmek",
            "E) Feodaliteyi kurmak"
          ],
          "correct": 0,
          "solution": "Doğru cevap Bağımsızlık ve egemenliği pekiştirmek.",
          "id": "e7_q75",
          "no": 75
        },
        {
          "subject": "Tarih",
          "text": "Türk siyasi ve askerî tarihinde büyük öneme sahip olan 'Sakarya Meydan Muharebesi' süreci ile ilgili aşağıdakilerden hangisi söylenebilir? (H-174)",
          "options": [
            "A) Osmanlı'nın kuruluş dönemine aittir.",
            "B) Hiçbir etkisi olmamıştır.",
            "C) Avrupa'da gerçekleşmiştir.",
            "D) Sadece ekonomik bir olaydır.",
            "E) Sakarya Meydan Muharebesi dönemin en kritik gelişmelerinden biridir."
          ],
          "correct": 4,
          "solution": "Doğru cevap Sakarya Meydan Muharebesi dönemin en kritik gelişmelerinden biridir..",
          "id": "e7_q76",
          "no": 76
        },
        {
          "subject": "Tarih",
          "text": "Aşağıdaki tarihî gelişmelerden hangisi 'Büyük Taarruz' ile doğrudan veya dolaylı olarak bağlantılıdır? (H-175)",
          "options": [
            "A) Büyük Taarruz öncesi ve sonrası yaşanan siyasi krizler.",
            "B) Coğrafi Keşifler",
            "C) Kavimler Göçü",
            "D) Fransız İhtilali",
            "E) Sanayi İnkılabı"
          ],
          "correct": 0,
          "solution": "Doğru cevap Büyük Taarruz öncesi ve sonrası yaşanan siyasi krizler..",
          "id": "e7_q77",
          "no": 77
        },
        {
          "subject": "Tarih",
          "text": "Millî Mücadele ve inkılaplar tarihi incelendiğinde 'I. İnönü Muharebesi' olayının temel amacı aşağıdakilerden hangisidir? (H-176)",
          "options": [
            "A) Avrupa'ya göç etmek",
            "B) Feodaliteyi kurmak",
            "C) Yeni sömürgeler elde etmek",
            "D) Bağımsızlık ve egemenliği pekiştirmek",
            "E) Saltanatı güçlendirmek"
          ],
          "correct": 3,
          "solution": "Doğru cevap Bağımsızlık ve egemenliği pekiştirmek.",
          "id": "e7_q78",
          "no": 78
        },
        {
          "subject": "Tarih",
          "text": "Türk siyasi ve askerî tarihinde büyük öneme sahip olan 'II. İnönü Muharebesi' süreci ile ilgili aşağıdakilerden hangisi söylenebilir? (H-177)",
          "options": [
            "A) Sadece ekonomik bir olaydır.",
            "B) II. İnönü Muharebesi dönemin en kritik gelişmelerinden biridir.",
            "C) Osmanlı'nın kuruluş dönemine aittir.",
            "D) Hiçbir etkisi olmamıştır.",
            "E) Avrupa'da gerçekleşmiştir."
          ],
          "correct": 1,
          "solution": "Doğru cevap II. İnönü Muharebesi dönemin en kritik gelişmelerinden biridir..",
          "id": "e7_q79",
          "no": 79
        },
        {
          "subject": "Tarih",
          "text": "Aşağıdaki tarihî gelişmelerden hangisi 'Kars Antlaşması' ile doğrudan veya dolaylı olarak bağlantılıdır? (H-178)",
          "options": [
            "A) Kars Antlaşması öncesi ve sonrası yaşanan siyasi krizler.",
            "B) Fransız İhtilali",
            "C) Sanayi İnkılabı",
            "D) Coğrafi Keşifler",
            "E) Kavimler Göçü"
          ],
          "correct": 0,
          "solution": "Doğru cevap Kars Antlaşması öncesi ve sonrası yaşanan siyasi krizler..",
          "id": "e7_q80",
          "no": 80
        },
        {
          "subject": "Tarih",
          "text": "Millî Mücadele ve inkılaplar tarihi incelendiğinde 'Ankara Antlaşması' olayının temel amacı aşağıdakilerden hangisidir? (H-179)",
          "options": [
            "A) Bağımsızlık ve egemenliği pekiştirmek",
            "B) Feodaliteyi kurmak",
            "C) Saltanatı güçlendirmek",
            "D) Avrupa'ya göç etmek",
            "E) Yeni sömürgeler elde etmek"
          ],
          "correct": 0,
          "solution": "Doğru cevap Bağımsızlık ve egemenliği pekiştirmek.",
          "id": "e7_q81",
          "no": 81
        },
        {
          "subject": "Tarih",
          "text": "Türk siyasi ve askerî tarihinde büyük öneme sahip olan 'Sivas Kongresi' süreci ile ilgili aşağıdakilerden hangisi söylenebilir? (H-180)",
          "options": [
            "A) Avrupa'da gerçekleşmiştir.",
            "B) Osmanlı'nın kuruluş dönemine aittir.",
            "C) Hiçbir etkisi olmamıştır.",
            "D) Sivas Kongresi dönemin en kritik gelişmelerinden biridir.",
            "E) Sadece ekonomik bir olaydır."
          ],
          "correct": 3,
          "solution": "Doğru cevap Sivas Kongresi dönemin en kritik gelişmelerinden biridir..",
          "id": "e7_q82",
          "no": 82
        },
        {
          "subject": "Tarih",
          "text": "Aşağıdaki tarihî gelişmelerden hangisi 'Erzurum Kongresi' ile doğrudan veya dolaylı olarak bağlantılıdır? (H-181)",
          "options": [
            "A) Kavimler Göçü",
            "B) Coğrafi Keşifler",
            "C) Fransız İhtilali",
            "D) Erzurum Kongresi öncesi ve sonrası yaşanan siyasi krizler.",
            "E) Sanayi İnkılabı"
          ],
          "correct": 3,
          "solution": "Doğru cevap Erzurum Kongresi öncesi ve sonrası yaşanan siyasi krizler..",
          "id": "e7_q83",
          "no": 83
        },
        {
          "subject": "Tarih",
          "text": "Millî Mücadele ve inkılaplar tarihi incelendiğinde 'Amasya Genelgesi' olayının temel amacı aşağıdakilerden hangisidir? (H-182)",
          "options": [
            "A) Avrupa'ya göç etmek",
            "B) Saltanatı güçlendirmek",
            "C) Feodaliteyi kurmak",
            "D) Yeni sömürgeler elde etmek",
            "E) Bağımsızlık ve egemenliği pekiştirmek"
          ],
          "correct": 4,
          "solution": "Doğru cevap Bağımsızlık ve egemenliği pekiştirmek.",
          "id": "e7_q84",
          "no": 84
        },
        {
          "subject": "Tarih",
          "text": "Türk siyasi ve askerî tarihinde büyük öneme sahip olan 'Lozan Antlaşması' süreci ile ilgili aşağıdakilerden hangisi söylenebilir? (H-183)",
          "options": [
            "A) Osmanlı'nın kuruluş dönemine aittir.",
            "B) Hiçbir etkisi olmamıştır.",
            "C) Lozan Antlaşması dönemin en kritik gelişmelerinden biridir.",
            "D) Sadece ekonomik bir olaydır.",
            "E) Avrupa'da gerçekleşmiştir."
          ],
          "correct": 2,
          "solution": "Doğru cevap Lozan Antlaşması dönemin en kritik gelişmelerinden biridir..",
          "id": "e7_q85",
          "no": 85
        },
        {
          "subject": "Tarih",
          "text": "Aşağıdaki tarihî gelişmelerden hangisi 'Cumhuriyetin İlanı' ile doğrudan veya dolaylı olarak bağlantılıdır? (H-184)",
          "options": [
            "A) Sanayi İnkılabı",
            "B) Kavimler Göçü",
            "C) Coğrafi Keşifler",
            "D) Cumhuriyetin İlanı öncesi ve sonrası yaşanan siyasi krizler.",
            "E) Fransız İhtilali"
          ],
          "correct": 3,
          "solution": "Doğru cevap Cumhuriyetin İlanı öncesi ve sonrası yaşanan siyasi krizler..",
          "id": "e7_q86",
          "no": 86
        },
        {
          "subject": "Tarih",
          "text": "Millî Mücadele ve inkılaplar tarihi incelendiğinde 'TBMM'nin Açılışı' olayının temel amacı aşağıdakilerden hangisidir? (H-185)",
          "options": [
            "A) Saltanatı güçlendirmek",
            "B) Avrupa'ya göç etmek",
            "C) Yeni sömürgeler elde etmek",
            "D) Bağımsızlık ve egemenliği pekiştirmek",
            "E) Feodaliteyi kurmak"
          ],
          "correct": 3,
          "solution": "Doğru cevap Bağımsızlık ve egemenliği pekiştirmek.",
          "id": "e7_q87",
          "no": 87
        },
        {
          "subject": "Coğrafya",
          "text": "Türkiye'nin fiziki coğrafyası düşünüldüğünde 'Ağrı Dağı' için aşağıdakilerden hangisi doğrudur? (C-106)",
          "options": [
            "A) Ağrı Dağı, ülkemizin önemli yeryüzü şekillerinden biridir.",
            "B) Ağrı Dağı tarıma kapalıdır.",
            "C) Ağrı Dağı bir çöldür.",
            "D) Ağrı Dağı Marmara'dadır.",
            "E) Ağrı Dağı yapay bir kanaldır."
          ],
          "correct": 0,
          "solution": "Doğru cevap Ağrı Dağı, ülkemizin önemli yeryüzü şekillerinden biridir..",
          "id": "e7_q88",
          "no": 88
        },
        {
          "subject": "Coğrafya",
          "text": "Coğrafi özellikleri ve turizm potansiyeli göz önüne alındığında 'Kızılırmak' hangi alanda daha çok öne çıkar? (C-107)",
          "options": [
            "A) Doğal güzellikleri ve turizm/coğrafi önemi",
            "B) Sadece madencilik",
            "C) Okyanus balıkçılığı",
            "D) Sadece ağır sanayi",
            "E) Çöl iklimi araştırmaları"
          ],
          "correct": 0,
          "solution": "Doğru cevap Doğal güzellikleri ve turizm/coğrafi önemi.",
          "id": "e7_q89",
          "no": 89
        },
        {
          "subject": "Coğrafya",
          "text": "Türkiye'nin fiziki coğrafyası düşünüldüğünde 'Erciyes Dağı' için aşağıdakilerden hangisi doğrudur? (C-108)",
          "options": [
            "A) Erciyes Dağı, ülkemizin önemli yeryüzü şekillerinden biridir.",
            "B) Erciyes Dağı bir çöldür.",
            "C) Erciyes Dağı yapay bir kanaldır.",
            "D) Erciyes Dağı tarıma kapalıdır.",
            "E) Erciyes Dağı Marmara'dadır."
          ],
          "correct": 0,
          "solution": "Doğru cevap Erciyes Dağı, ülkemizin önemli yeryüzü şekillerinden biridir..",
          "id": "e7_q90",
          "no": 90
        },
        {
          "subject": "Coğrafya",
          "text": "Coğrafi özellikleri ve turizm potansiyeli göz önüne alındığında 'Tuz Gölü' hangi alanda daha çok öne çıkar? (C-109)",
          "options": [
            "A) Sadece madencilik",
            "B) Sadece ağır sanayi",
            "C) Okyanus balıkçılığı",
            "D) Doğal güzellikleri ve turizm/coğrafi önemi",
            "E) Çöl iklimi araştırmaları"
          ],
          "correct": 3,
          "solution": "Doğru cevap Doğal güzellikleri ve turizm/coğrafi önemi.",
          "id": "e7_q91",
          "no": 91
        },
        {
          "subject": "Coğrafya",
          "text": "Türkiye'nin fiziki coğrafyası düşünüldüğünde 'Çukurova' için aşağıdakilerden hangisi doğrudur? (C-110)",
          "options": [
            "A) Çukurova bir çöldür.",
            "B) Çukurova tarıma kapalıdır.",
            "C) Çukurova Marmara'dadır.",
            "D) Çukurova, ülkemizin önemli yeryüzü şekillerinden biridir.",
            "E) Çukurova yapay bir kanaldır."
          ],
          "correct": 3,
          "solution": "Doğru cevap Çukurova, ülkemizin önemli yeryüzü şekillerinden biridir..",
          "id": "e7_q92",
          "no": 92
        },
        {
          "subject": "Coğrafya",
          "text": "Coğrafi özellikleri ve turizm potansiyeli göz önüne alındığında 'Bafra Ovası' hangi alanda daha çok öne çıkar? (C-111)",
          "options": [
            "A) Doğal güzellikleri ve turizm/coğrafi önemi",
            "B) Çöl iklimi araştırmaları",
            "C) Sadece ağır sanayi",
            "D) Okyanus balıkçılığı",
            "E) Sadece madencilik"
          ],
          "correct": 0,
          "solution": "Doğru cevap Doğal güzellikleri ve turizm/coğrafi önemi.",
          "id": "e7_q93",
          "no": 93
        },
        {
          "subject": "Coğrafya",
          "text": "Türkiye'nin fiziki coğrafyası düşünüldüğünde 'Kaçkar Dağları' için aşağıdakilerden hangisi doğrudur? (C-112)",
          "options": [
            "A) Kaçkar Dağları bir çöldür.",
            "B) Kaçkar Dağları, ülkemizin önemli yeryüzü şekillerinden biridir.",
            "C) Kaçkar Dağları yapay bir kanaldır.",
            "D) Kaçkar Dağları tarıma kapalıdır.",
            "E) Kaçkar Dağları Marmara'dadır."
          ],
          "correct": 1,
          "solution": "Doğru cevap Kaçkar Dağları, ülkemizin önemli yeryüzü şekillerinden biridir..",
          "id": "e7_q94",
          "no": 94
        },
        {
          "subject": "Coğrafya",
          "text": "Coğrafi özellikleri ve turizm potansiyeli göz önüne alındığında 'Gediz Nehri' hangi alanda daha çok öne çıkar? (C-113)",
          "options": [
            "A) Sadece ağır sanayi",
            "B) Sadece madencilik",
            "C) Okyanus balıkçılığı",
            "D) Doğal güzellikleri ve turizm/coğrafi önemi",
            "E) Çöl iklimi araştırmaları"
          ],
          "correct": 3,
          "solution": "Doğru cevap Doğal güzellikleri ve turizm/coğrafi önemi.",
          "id": "e7_q95",
          "no": 95
        },
        {
          "subject": "Coğrafya",
          "text": "Türkiye'nin fiziki coğrafyası düşünüldüğünde 'Salda Gölü' için aşağıdakilerden hangisi doğrudur? (C-114)",
          "options": [
            "A) Salda Gölü bir çöldür.",
            "B) Salda Gölü Marmara'dadır.",
            "C) Salda Gölü, ülkemizin önemli yeryüzü şekillerinden biridir.",
            "D) Salda Gölü yapay bir kanaldır.",
            "E) Salda Gölü tarıma kapalıdır."
          ],
          "correct": 2,
          "solution": "Doğru cevap Salda Gölü, ülkemizin önemli yeryüzü şekillerinden biridir..",
          "id": "e7_q96",
          "no": 96
        },
        {
          "subject": "Coğrafya",
          "text": "Coğrafi özellikleri ve turizm potansiyeli göz önüne alındığında 'Kapadokya' hangi alanda daha çok öne çıkar? (C-115)",
          "options": [
            "A) Sadece ağır sanayi",
            "B) Sadece madencilik",
            "C) Okyanus balıkçılığı",
            "D) Çöl iklimi araştırmaları",
            "E) Doğal güzellikleri ve turizm/coğrafi önemi"
          ],
          "correct": 4,
          "solution": "Doğru cevap Doğal güzellikleri ve turizm/coğrafi önemi.",
          "id": "e7_q97",
          "no": 97
        },
        {
          "subject": "Coğrafya",
          "text": "Türkiye'nin fiziki coğrafyası düşünüldüğünde 'Pamukkale' için aşağıdakilerden hangisi doğrudur? (C-116)",
          "options": [
            "A) Pamukkale bir çöldür.",
            "B) Pamukkale, ülkemizin önemli yeryüzü şekillerinden biridir.",
            "C) Pamukkale tarıma kapalıdır.",
            "D) Pamukkale Marmara'dadır.",
            "E) Pamukkale yapay bir kanaldır."
          ],
          "correct": 1,
          "solution": "Doğru cevap Pamukkale, ülkemizin önemli yeryüzü şekillerinden biridir..",
          "id": "e7_q98",
          "no": 98
        },
        {
          "subject": "Coğrafya",
          "text": "Coğrafi özellikleri ve turizm potansiyeli göz önüne alındığında 'Nemrut Dağı' hangi alanda daha çok öne çıkar? (C-117)",
          "options": [
            "A) Sadece madencilik",
            "B) Çöl iklimi araştırmaları",
            "C) Sadece ağır sanayi",
            "D) Okyanus balıkçılığı",
            "E) Doğal güzellikleri ve turizm/coğrafi önemi"
          ],
          "correct": 4,
          "solution": "Doğru cevap Doğal güzellikleri ve turizm/coğrafi önemi.",
          "id": "e7_q99",
          "no": 99
        },
        {
          "subject": "Coğrafya",
          "text": "Türkiye'nin fiziki coğrafyası düşünüldüğünde 'Sümela Manastırı' için aşağıdakilerden hangisi doğrudur? (C-118)",
          "options": [
            "A) Sümela Manastırı tarıma kapalıdır.",
            "B) Sümela Manastırı, ülkemizin önemli yeryüzü şekillerinden biridir.",
            "C) Sümela Manastırı bir çöldür.",
            "D) Sümela Manastırı Marmara'dadır.",
            "E) Sümela Manastırı yapay bir kanaldır."
          ],
          "correct": 1,
          "solution": "Doğru cevap Sümela Manastırı, ülkemizin önemli yeryüzü şekillerinden biridir..",
          "id": "e7_q100",
          "no": 100
        },
        {
          "subject": "Coğrafya",
          "text": "Coğrafi özellikleri ve turizm potansiyeli göz önüne alındığında 'Uludağ' hangi alanda daha çok öne çıkar? (C-119)",
          "options": [
            "A) Sadece madencilik",
            "B) Çöl iklimi araştırmaları",
            "C) Okyanus balıkçılığı",
            "D) Sadece ağır sanayi",
            "E) Doğal güzellikleri ve turizm/coğrafi önemi"
          ],
          "correct": 4,
          "solution": "Doğru cevap Doğal güzellikleri ve turizm/coğrafi önemi.",
          "id": "e7_q101",
          "no": 101
        },
        {
          "subject": "Coğrafya",
          "text": "Türkiye'nin fiziki coğrafyası düşünüldüğünde 'Van Gölü' için aşağıdakilerden hangisi doğrudur? (C-120)",
          "options": [
            "A) Van Gölü yapay bir kanaldır.",
            "B) Van Gölü tarıma kapalıdır.",
            "C) Van Gölü Marmara'dadır.",
            "D) Van Gölü bir çöldür.",
            "E) Van Gölü, ülkemizin önemli yeryüzü şekillerinden biridir."
          ],
          "correct": 4,
          "solution": "Doğru cevap Van Gölü, ülkemizin önemli yeryüzü şekillerinden biridir..",
          "id": "e7_q102",
          "no": 102
        },
        {
          "subject": "Coğrafya",
          "text": "Coğrafi özellikleri ve turizm potansiyeli göz önüne alındığında 'Ağrı Dağı' hangi alanda daha çok öne çıkar? (C-121)",
          "options": [
            "A) Doğal güzellikleri ve turizm/coğrafi önemi",
            "B) Çöl iklimi araştırmaları",
            "C) Sadece ağır sanayi",
            "D) Okyanus balıkçılığı",
            "E) Sadece madencilik"
          ],
          "correct": 0,
          "solution": "Doğru cevap Doğal güzellikleri ve turizm/coğrafi önemi.",
          "id": "e7_q103",
          "no": 103
        },
        {
          "subject": "Coğrafya",
          "text": "Türkiye'nin fiziki coğrafyası düşünüldüğünde 'Kızılırmak' için aşağıdakilerden hangisi doğrudur? (C-122)",
          "options": [
            "A) Kızılırmak bir çöldür.",
            "B) Kızılırmak Marmara'dadır.",
            "C) Kızılırmak, ülkemizin önemli yeryüzü şekillerinden biridir.",
            "D) Kızılırmak tarıma kapalıdır.",
            "E) Kızılırmak yapay bir kanaldır."
          ],
          "correct": 2,
          "solution": "Doğru cevap Kızılırmak, ülkemizin önemli yeryüzü şekillerinden biridir..",
          "id": "e7_q104",
          "no": 104
        },
        {
          "subject": "Coğrafya",
          "text": "Coğrafi özellikleri ve turizm potansiyeli göz önüne alındığında 'Erciyes Dağı' hangi alanda daha çok öne çıkar? (C-123)",
          "options": [
            "A) Çöl iklimi araştırmaları",
            "B) Sadece madencilik",
            "C) Sadece ağır sanayi",
            "D) Okyanus balıkçılığı",
            "E) Doğal güzellikleri ve turizm/coğrafi önemi"
          ],
          "correct": 4,
          "solution": "Doğru cevap Doğal güzellikleri ve turizm/coğrafi önemi.",
          "id": "e7_q105",
          "no": 105
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'Kaymakamlık' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-88)",
          "options": [
            "A) Kaymakamlık yasaklanmıştır.",
            "B) Kaymakamlık, anayasal sistemin önemli bir parçasıdır.",
            "C) Kaymakamlık özel bir şirkettir.",
            "D) Kaymakamlık sadece köylerde bulunur.",
            "E) Kaymakamlık yabancı bir kurumdur."
          ],
          "correct": 1,
          "solution": "Doğru cevap Kaymakamlık, anayasal sistemin önemli bir parçasıdır..",
          "id": "e7_q106",
          "no": 106
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'İl Genel Meclisi' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-89)",
          "options": [
            "A) İl Genel Meclisi, anayasal sistemin önemli bir parçasıdır.",
            "B) İl Genel Meclisi yasaklanmıştır.",
            "C) İl Genel Meclisi yabancı bir kurumdur.",
            "D) İl Genel Meclisi sadece köylerde bulunur.",
            "E) İl Genel Meclisi özel bir şirkettir."
          ],
          "correct": 0,
          "solution": "Doğru cevap İl Genel Meclisi, anayasal sistemin önemli bir parçasıdır..",
          "id": "e7_q107",
          "no": 107
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'Kamu Denetçiliği Kurumu' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-90)",
          "options": [
            "A) Kamu Denetçiliği Kurumu yasaklanmıştır.",
            "B) Kamu Denetçiliği Kurumu yabancı bir kurumdur.",
            "C) Kamu Denetçiliği Kurumu, anayasal sistemin önemli bir parçasıdır.",
            "D) Kamu Denetçiliği Kurumu özel bir şirkettir.",
            "E) Kamu Denetçiliği Kurumu sadece köylerde bulunur."
          ],
          "correct": 2,
          "solution": "Doğru cevap Kamu Denetçiliği Kurumu, anayasal sistemin önemli bir parçasıdır..",
          "id": "e7_q108",
          "no": 108
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'Anayasa Mahkemesi' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-91)",
          "options": [
            "A) Anayasa Mahkemesi yabancı bir kurumdur.",
            "B) Anayasa Mahkemesi sadece köylerde bulunur.",
            "C) Anayasa Mahkemesi yasaklanmıştır.",
            "D) Anayasa Mahkemesi özel bir şirkettir.",
            "E) Anayasa Mahkemesi, anayasal sistemin önemli bir parçasıdır."
          ],
          "correct": 4,
          "solution": "Doğru cevap Anayasa Mahkemesi, anayasal sistemin önemli bir parçasıdır..",
          "id": "e7_q109",
          "no": 109
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'Yargıtay' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-92)",
          "options": [
            "A) Yargıtay özel bir şirkettir.",
            "B) Yargıtay sadece köylerde bulunur.",
            "C) Yargıtay, anayasal sistemin önemli bir parçasıdır.",
            "D) Yargıtay yabancı bir kurumdur.",
            "E) Yargıtay yasaklanmıştır."
          ],
          "correct": 2,
          "solution": "Doğru cevap Yargıtay, anayasal sistemin önemli bir parçasıdır..",
          "id": "e7_q110",
          "no": 110
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'Danıştay' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-93)",
          "options": [
            "A) Danıştay sadece köylerde bulunur.",
            "B) Danıştay, anayasal sistemin önemli bir parçasıdır.",
            "C) Danıştay yabancı bir kurumdur.",
            "D) Danıştay özel bir şirkettir.",
            "E) Danıştay yasaklanmıştır."
          ],
          "correct": 1,
          "solution": "Doğru cevap Danıştay, anayasal sistemin önemli bir parçasıdır..",
          "id": "e7_q111",
          "no": 111
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'TBMM' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-94)",
          "options": [
            "A) TBMM, anayasal sistemin önemli bir parçasıdır.",
            "B) TBMM yasaklanmıştır.",
            "C) TBMM sadece köylerde bulunur.",
            "D) TBMM yabancı bir kurumdur.",
            "E) TBMM özel bir şirkettir."
          ],
          "correct": 0,
          "solution": "Doğru cevap TBMM, anayasal sistemin önemli bir parçasıdır..",
          "id": "e7_q112",
          "no": 112
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'Cumhurbaşkanlığı' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-95)",
          "options": [
            "A) Cumhurbaşkanlığı, anayasal sistemin önemli bir parçasıdır.",
            "B) Cumhurbaşkanlığı sadece köylerde bulunur.",
            "C) Cumhurbaşkanlığı yabancı bir kurumdur.",
            "D) Cumhurbaşkanlığı özel bir şirkettir.",
            "E) Cumhurbaşkanlığı yasaklanmıştır."
          ],
          "correct": 0,
          "solution": "Doğru cevap Cumhurbaşkanlığı, anayasal sistemin önemli bir parçasıdır..",
          "id": "e7_q113",
          "no": 113
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'Sayıştay' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-96)",
          "options": [
            "A) Sayıştay sadece köylerde bulunur.",
            "B) Sayıştay yasaklanmıştır.",
            "C) Sayıştay özel bir şirkettir.",
            "D) Sayıştay, anayasal sistemin önemli bir parçasıdır.",
            "E) Sayıştay yabancı bir kurumdur."
          ],
          "correct": 3,
          "solution": "Doğru cevap Sayıştay, anayasal sistemin önemli bir parçasıdır..",
          "id": "e7_q114",
          "no": 114
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'YSK' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-97)",
          "options": [
            "A) YSK yasaklanmıştır.",
            "B) YSK, anayasal sistemin önemli bir parçasıdır.",
            "C) YSK sadece köylerde bulunur.",
            "D) YSK özel bir şirkettir.",
            "E) YSK yabancı bir kurumdur."
          ],
          "correct": 1,
          "solution": "Doğru cevap YSK, anayasal sistemin önemli bir parçasıdır..",
          "id": "e7_q115",
          "no": 115
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'HSK' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-98)",
          "options": [
            "A) HSK sadece köylerde bulunur.",
            "B) HSK yasaklanmıştır.",
            "C) HSK, anayasal sistemin önemli bir parçasıdır.",
            "D) HSK yabancı bir kurumdur.",
            "E) HSK özel bir şirkettir."
          ],
          "correct": 2,
          "solution": "Doğru cevap HSK, anayasal sistemin önemli bir parçasıdır..",
          "id": "e7_q116",
          "no": 116
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'Belediye' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-99)",
          "options": [
            "A) Belediye sadece köylerde bulunur.",
            "B) Belediye yasaklanmıştır.",
            "C) Belediye yabancı bir kurumdur.",
            "D) Belediye, anayasal sistemin önemli bir parçasıdır.",
            "E) Belediye özel bir şirkettir."
          ],
          "correct": 3,
          "solution": "Doğru cevap Belediye, anayasal sistemin önemli bir parçasıdır..",
          "id": "e7_q117",
          "no": 117
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'Valilik' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-100)",
          "options": [
            "A) Valilik, anayasal sistemin önemli bir parçasıdır.",
            "B) Valilik özel bir şirkettir.",
            "C) Valilik yabancı bir kurumdur.",
            "D) Valilik yasaklanmıştır.",
            "E) Valilik sadece köylerde bulunur."
          ],
          "correct": 0,
          "solution": "Doğru cevap Valilik, anayasal sistemin önemli bir parçasıdır..",
          "id": "e7_q118",
          "no": 118
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'Kaymakamlık' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-101)",
          "options": [
            "A) Kaymakamlık yasaklanmıştır.",
            "B) Kaymakamlık, anayasal sistemin önemli bir parçasıdır.",
            "C) Kaymakamlık sadece köylerde bulunur.",
            "D) Kaymakamlık yabancı bir kurumdur.",
            "E) Kaymakamlık özel bir şirkettir."
          ],
          "correct": 1,
          "solution": "Doğru cevap Kaymakamlık, anayasal sistemin önemli bir parçasıdır..",
          "id": "e7_q119",
          "no": 119
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'İl Genel Meclisi' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-102)",
          "options": [
            "A) İl Genel Meclisi özel bir şirkettir.",
            "B) İl Genel Meclisi sadece köylerde bulunur.",
            "C) İl Genel Meclisi yasaklanmıştır.",
            "D) İl Genel Meclisi, anayasal sistemin önemli bir parçasıdır.",
            "E) İl Genel Meclisi yabancı bir kurumdur."
          ],
          "correct": 3,
          "solution": "Doğru cevap İl Genel Meclisi, anayasal sistemin önemli bir parçasıdır..",
          "id": "e7_q120",
          "no": 120
        }
      ]
    },
    {
      "id": "deneme_8",
      "name": "8. Deneme Sınavı",
      "totalQuestions": 120,
      "duration": 130,
      "distribution": {
        "Türkçe": 30,
        "Matematik": 30,
        "Tarih": 27,
        "Coğrafya": 18,
        "Vatandaşlık": 15
      },
      "questions": [
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde 'bugün' kelimesinin yazımıyla ilgili bir kural hatırlatılmaktadır? (T-205)",
          "options": [
            "A) bugün kelimesi yabancı kökenlidir.",
            "B) bugün cümlede özne olamaz.",
            "C) bugün kelimesi fiildir.",
            "D) 'bugün' kelimesinin doğru yazımına dikkat edilmelidir.",
            "E) bugün kelimesi her zaman ayrı yazılır."
          ],
          "correct": 3,
          "solution": "Doğru cevap 'bugün' kelimesinin doğru yazımına dikkat edilmelidir..",
          "id": "e8_q1",
          "no": 1
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde mecaz anlamlı bir sözcük kullanılmıştır? (T-206)",
          "options": [
            "A) Hava bugün çok soğuk.",
            "B) Buzdolabı soğuk üflüyor.",
            "C) Suyu dolaptan soğuk içti.",
            "D) Olaylara karşı çok 'soğuk' davranıyordu.",
            "E) Kışın havalar soğuk olur."
          ],
          "correct": 3,
          "solution": "Doğru cevap Olaylara karşı çok 'soğuk' davranıyordu..",
          "id": "e8_q2",
          "no": 2
        },
        {
          "subject": "Türkçe",
          "text": "Bilim tarih boyunca insanlığın en büyük rehberlerinden biri olmuştur. Toplumlar Bilim sayesinde sınırlarını aşmış, geleceğe umutla bakabilmiştir. (P-207)\nBu parçanın ana düşüncesi nedir?",
          "options": [
            "A) Bilim sadece geçmişte kalmıştır.",
            "B) Bilim sadece bireyseldir.",
            "C) İnsanlar Bilim ile ilgilenmemelidir.",
            "D) Bilim zaman kaybıdır.",
            "E) Bilim, toplumsal ilerleme ve vizyon için vazgeçilmezdir."
          ],
          "correct": 4,
          "solution": "Doğru cevap Bilim, toplumsal ilerleme ve vizyon için vazgeçilmezdir..",
          "id": "e8_q3",
          "no": 3
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde 'yalnız' kelimesinin yazımıyla ilgili bir kural hatırlatılmaktadır? (T-208)",
          "options": [
            "A) yalnız kelimesi yabancı kökenlidir.",
            "B) yalnız cümlede özne olamaz.",
            "C) 'yalnız' kelimesinin doğru yazımına dikkat edilmelidir.",
            "D) yalnız kelimesi her zaman ayrı yazılır.",
            "E) yalnız kelimesi fiildir."
          ],
          "correct": 2,
          "solution": "Doğru cevap 'yalnız' kelimesinin doğru yazımına dikkat edilmelidir..",
          "id": "e8_q4",
          "no": 4
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde mecaz anlamlı bir sözcük kullanılmıştır? (T-209)",
          "options": [
            "A) Buzdolabı soğuk üflüyor.",
            "B) Olaylara karşı çok 'soğuk' davranıyordu.",
            "C) Hava bugün çok soğuk.",
            "D) Suyu dolaptan soğuk içti.",
            "E) Kışın havalar soğuk olur."
          ],
          "correct": 1,
          "solution": "Doğru cevap Olaylara karşı çok 'soğuk' davranıyordu..",
          "id": "e8_q5",
          "no": 5
        },
        {
          "subject": "Türkçe",
          "text": "Sanat tarih boyunca insanlığın en büyük rehberlerinden biri olmuştur. Toplumlar Sanat sayesinde sınırlarını aşmış, geleceğe umutla bakabilmiştir. (P-210)\nBu parçanın ana düşüncesi nedir?",
          "options": [
            "A) Sanat, toplumsal ilerleme ve vizyon için vazgeçilmezdir.",
            "B) Sanat zaman kaybıdır.",
            "C) İnsanlar Sanat ile ilgilenmemelidir.",
            "D) Sanat sadece geçmişte kalmıştır.",
            "E) Sanat sadece bireyseldir."
          ],
          "correct": 0,
          "solution": "Doğru cevap Sanat, toplumsal ilerleme ve vizyon için vazgeçilmezdir..",
          "id": "e8_q6",
          "no": 6
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde 'hiçbir' kelimesinin yazımıyla ilgili bir kural hatırlatılmaktadır? (T-211)",
          "options": [
            "A) hiçbir cümlede özne olamaz.",
            "B) hiçbir kelimesi fiildir.",
            "C) hiçbir kelimesi her zaman ayrı yazılır.",
            "D) hiçbir kelimesi yabancı kökenlidir.",
            "E) 'hiçbir' kelimesinin doğru yazımına dikkat edilmelidir."
          ],
          "correct": 4,
          "solution": "Doğru cevap 'hiçbir' kelimesinin doğru yazımına dikkat edilmelidir..",
          "id": "e8_q7",
          "no": 7
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde mecaz anlamlı bir sözcük kullanılmıştır? (T-212)",
          "options": [
            "A) Olaylara karşı çok 'soğuk' davranıyordu.",
            "B) Hava bugün çok soğuk.",
            "C) Suyu dolaptan soğuk içti.",
            "D) Buzdolabı soğuk üflüyor.",
            "E) Kışın havalar soğuk olur."
          ],
          "correct": 0,
          "solution": "Doğru cevap Olaylara karşı çok 'soğuk' davranıyordu..",
          "id": "e8_q8",
          "no": 8
        },
        {
          "subject": "Türkçe",
          "text": "Teknoloji tarih boyunca insanlığın en büyük rehberlerinden biri olmuştur. Toplumlar Teknoloji sayesinde sınırlarını aşmış, geleceğe umutla bakabilmiştir. (P-213)\nBu parçanın ana düşüncesi nedir?",
          "options": [
            "A) Teknoloji zaman kaybıdır.",
            "B) Teknoloji, toplumsal ilerleme ve vizyon için vazgeçilmezdir.",
            "C) Teknoloji sadece geçmişte kalmıştır.",
            "D) İnsanlar Teknoloji ile ilgilenmemelidir.",
            "E) Teknoloji sadece bireyseldir."
          ],
          "correct": 1,
          "solution": "Doğru cevap Teknoloji, toplumsal ilerleme ve vizyon için vazgeçilmezdir..",
          "id": "e8_q9",
          "no": 9
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde 'her şey' kelimesinin yazımıyla ilgili bir kural hatırlatılmaktadır? (T-214)",
          "options": [
            "A) 'her şey' kelimesinin doğru yazımına dikkat edilmelidir.",
            "B) her şey cümlede özne olamaz.",
            "C) her şey kelimesi yabancı kökenlidir.",
            "D) her şey kelimesi her zaman ayrı yazılır.",
            "E) her şey kelimesi fiildir."
          ],
          "correct": 0,
          "solution": "Doğru cevap 'her şey' kelimesinin doğru yazımına dikkat edilmelidir..",
          "id": "e8_q10",
          "no": 10
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde mecaz anlamlı bir sözcük kullanılmıştır? (T-215)",
          "options": [
            "A) Olaylara karşı çok 'soğuk' davranıyordu.",
            "B) Buzdolabı soğuk üflüyor.",
            "C) Hava bugün çok soğuk.",
            "D) Kışın havalar soğuk olur.",
            "E) Suyu dolaptan soğuk içti."
          ],
          "correct": 0,
          "solution": "Doğru cevap Olaylara karşı çok 'soğuk' davranıyordu..",
          "id": "e8_q11",
          "no": 11
        },
        {
          "subject": "Türkçe",
          "text": "Doğa tarih boyunca insanlığın en büyük rehberlerinden biri olmuştur. Toplumlar Doğa sayesinde sınırlarını aşmış, geleceğe umutla bakabilmiştir. (P-216)\nBu parçanın ana düşüncesi nedir?",
          "options": [
            "A) Doğa sadece bireyseldir.",
            "B) Doğa sadece geçmişte kalmıştır.",
            "C) İnsanlar Doğa ile ilgilenmemelidir.",
            "D) Doğa zaman kaybıdır.",
            "E) Doğa, toplumsal ilerleme ve vizyon için vazgeçilmezdir."
          ],
          "correct": 4,
          "solution": "Doğru cevap Doğa, toplumsal ilerleme ve vizyon için vazgeçilmezdir..",
          "id": "e8_q12",
          "no": 12
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde 'yanlış' kelimesinin yazımıyla ilgili bir kural hatırlatılmaktadır? (T-217)",
          "options": [
            "A) yanlış kelimesi yabancı kökenlidir.",
            "B) 'yanlış' kelimesinin doğru yazımına dikkat edilmelidir.",
            "C) yanlış kelimesi her zaman ayrı yazılır.",
            "D) yanlış cümlede özne olamaz.",
            "E) yanlış kelimesi fiildir."
          ],
          "correct": 1,
          "solution": "Doğru cevap 'yanlış' kelimesinin doğru yazımına dikkat edilmelidir..",
          "id": "e8_q13",
          "no": 13
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde mecaz anlamlı bir sözcük kullanılmıştır? (T-218)",
          "options": [
            "A) Olaylara karşı çok 'soğuk' davranıyordu.",
            "B) Kışın havalar soğuk olur.",
            "C) Buzdolabı soğuk üflüyor.",
            "D) Hava bugün çok soğuk.",
            "E) Suyu dolaptan soğuk içti."
          ],
          "correct": 0,
          "solution": "Doğru cevap Olaylara karşı çok 'soğuk' davranıyordu..",
          "id": "e8_q14",
          "no": 14
        },
        {
          "subject": "Türkçe",
          "text": "Psikoloji tarih boyunca insanlığın en büyük rehberlerinden biri olmuştur. Toplumlar Psikoloji sayesinde sınırlarını aşmış, geleceğe umutla bakabilmiştir. (P-219)\nBu parçanın ana düşüncesi nedir?",
          "options": [
            "A) Psikoloji sadece bireyseldir.",
            "B) Psikoloji sadece geçmişte kalmıştır.",
            "C) Psikoloji, toplumsal ilerleme ve vizyon için vazgeçilmezdir.",
            "D) Psikoloji zaman kaybıdır.",
            "E) İnsanlar Psikoloji ile ilgilenmemelidir."
          ],
          "correct": 2,
          "solution": "Doğru cevap Psikoloji, toplumsal ilerleme ve vizyon için vazgeçilmezdir..",
          "id": "e8_q15",
          "no": 15
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde 'birkaç' kelimesinin yazımıyla ilgili bir kural hatırlatılmaktadır? (T-220)",
          "options": [
            "A) 'birkaç' kelimesinin doğru yazımına dikkat edilmelidir.",
            "B) birkaç kelimesi her zaman ayrı yazılır.",
            "C) birkaç kelimesi yabancı kökenlidir.",
            "D) birkaç cümlede özne olamaz.",
            "E) birkaç kelimesi fiildir."
          ],
          "correct": 0,
          "solution": "Doğru cevap 'birkaç' kelimesinin doğru yazımına dikkat edilmelidir..",
          "id": "e8_q16",
          "no": 16
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde mecaz anlamlı bir sözcük kullanılmıştır? (T-221)",
          "options": [
            "A) Kışın havalar soğuk olur.",
            "B) Suyu dolaptan soğuk içti.",
            "C) Buzdolabı soğuk üflüyor.",
            "D) Olaylara karşı çok 'soğuk' davranıyordu.",
            "E) Hava bugün çok soğuk."
          ],
          "correct": 3,
          "solution": "Doğru cevap Olaylara karşı çok 'soğuk' davranıyordu..",
          "id": "e8_q17",
          "no": 17
        },
        {
          "subject": "Türkçe",
          "text": "Eğitim tarih boyunca insanlığın en büyük rehberlerinden biri olmuştur. Toplumlar Eğitim sayesinde sınırlarını aşmış, geleceğe umutla bakabilmiştir. (P-222)\nBu parçanın ana düşüncesi nedir?",
          "options": [
            "A) Eğitim zaman kaybıdır.",
            "B) Eğitim sadece geçmişte kalmıştır.",
            "C) Eğitim, toplumsal ilerleme ve vizyon için vazgeçilmezdir.",
            "D) İnsanlar Eğitim ile ilgilenmemelidir.",
            "E) Eğitim sadece bireyseldir."
          ],
          "correct": 2,
          "solution": "Doğru cevap Eğitim, toplumsal ilerleme ve vizyon için vazgeçilmezdir..",
          "id": "e8_q18",
          "no": 18
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde 'hiç kimse' kelimesinin yazımıyla ilgili bir kural hatırlatılmaktadır? (T-223)",
          "options": [
            "A) hiç kimse kelimesi yabancı kökenlidir.",
            "B) hiç kimse kelimesi fiildir.",
            "C) hiç kimse cümlede özne olamaz.",
            "D) hiç kimse kelimesi her zaman ayrı yazılır.",
            "E) 'hiç kimse' kelimesinin doğru yazımına dikkat edilmelidir."
          ],
          "correct": 4,
          "solution": "Doğru cevap 'hiç kimse' kelimesinin doğru yazımına dikkat edilmelidir..",
          "id": "e8_q19",
          "no": 19
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde mecaz anlamlı bir sözcük kullanılmıştır? (T-224)",
          "options": [
            "A) Kışın havalar soğuk olur.",
            "B) Suyu dolaptan soğuk içti.",
            "C) Hava bugün çok soğuk.",
            "D) Olaylara karşı çok 'soğuk' davranıyordu.",
            "E) Buzdolabı soğuk üflüyor."
          ],
          "correct": 3,
          "solution": "Doğru cevap Olaylara karşı çok 'soğuk' davranıyordu..",
          "id": "e8_q20",
          "no": 20
        },
        {
          "subject": "Türkçe",
          "text": "Kültür tarih boyunca insanlığın en büyük rehberlerinden biri olmuştur. Toplumlar Kültür sayesinde sınırlarını aşmış, geleceğe umutla bakabilmiştir. (P-225)\nBu parçanın ana düşüncesi nedir?",
          "options": [
            "A) Kültür sadece geçmişte kalmıştır.",
            "B) Kültür zaman kaybıdır.",
            "C) İnsanlar Kültür ile ilgilenmemelidir.",
            "D) Kültür, toplumsal ilerleme ve vizyon için vazgeçilmezdir.",
            "E) Kültür sadece bireyseldir."
          ],
          "correct": 3,
          "solution": "Doğru cevap Kültür, toplumsal ilerleme ve vizyon için vazgeçilmezdir..",
          "id": "e8_q21",
          "no": 21
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde 'herkes' kelimesinin yazımıyla ilgili bir kural hatırlatılmaktadır? (T-226)",
          "options": [
            "A) herkes kelimesi yabancı kökenlidir.",
            "B) herkes cümlede özne olamaz.",
            "C) 'herkes' kelimesinin doğru yazımına dikkat edilmelidir.",
            "D) herkes kelimesi fiildir.",
            "E) herkes kelimesi her zaman ayrı yazılır."
          ],
          "correct": 2,
          "solution": "Doğru cevap 'herkes' kelimesinin doğru yazımına dikkat edilmelidir..",
          "id": "e8_q22",
          "no": 22
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde mecaz anlamlı bir sözcük kullanılmıştır? (T-227)",
          "options": [
            "A) Kışın havalar soğuk olur.",
            "B) Hava bugün çok soğuk.",
            "C) Buzdolabı soğuk üflüyor.",
            "D) Olaylara karşı çok 'soğuk' davranıyordu.",
            "E) Suyu dolaptan soğuk içti."
          ],
          "correct": 3,
          "solution": "Doğru cevap Olaylara karşı çok 'soğuk' davranıyordu..",
          "id": "e8_q23",
          "no": 23
        },
        {
          "subject": "Türkçe",
          "text": "Felsefe tarih boyunca insanlığın en büyük rehberlerinden biri olmuştur. Toplumlar Felsefe sayesinde sınırlarını aşmış, geleceğe umutla bakabilmiştir. (P-228)\nBu parçanın ana düşüncesi nedir?",
          "options": [
            "A) Felsefe sadece bireyseldir.",
            "B) İnsanlar Felsefe ile ilgilenmemelidir.",
            "C) Felsefe zaman kaybıdır.",
            "D) Felsefe, toplumsal ilerleme ve vizyon için vazgeçilmezdir.",
            "E) Felsefe sadece geçmişte kalmıştır."
          ],
          "correct": 3,
          "solution": "Doğru cevap Felsefe, toplumsal ilerleme ve vizyon için vazgeçilmezdir..",
          "id": "e8_q24",
          "no": 24
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde 'bugün' kelimesinin yazımıyla ilgili bir kural hatırlatılmaktadır? (T-229)",
          "options": [
            "A) bugün cümlede özne olamaz.",
            "B) bugün kelimesi fiildir.",
            "C) bugün kelimesi yabancı kökenlidir.",
            "D) bugün kelimesi her zaman ayrı yazılır.",
            "E) 'bugün' kelimesinin doğru yazımına dikkat edilmelidir."
          ],
          "correct": 4,
          "solution": "Doğru cevap 'bugün' kelimesinin doğru yazımına dikkat edilmelidir..",
          "id": "e8_q25",
          "no": 25
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde mecaz anlamlı bir sözcük kullanılmıştır? (T-230)",
          "options": [
            "A) Olaylara karşı çok 'soğuk' davranıyordu.",
            "B) Suyu dolaptan soğuk içti.",
            "C) Buzdolabı soğuk üflüyor.",
            "D) Hava bugün çok soğuk.",
            "E) Kışın havalar soğuk olur."
          ],
          "correct": 0,
          "solution": "Doğru cevap Olaylara karşı çok 'soğuk' davranıyordu..",
          "id": "e8_q26",
          "no": 26
        },
        {
          "subject": "Türkçe",
          "text": "Edebiyat tarih boyunca insanlığın en büyük rehberlerinden biri olmuştur. Toplumlar Edebiyat sayesinde sınırlarını aşmış, geleceğe umutla bakabilmiştir. (P-231)\nBu parçanın ana düşüncesi nedir?",
          "options": [
            "A) Edebiyat zaman kaybıdır.",
            "B) İnsanlar Edebiyat ile ilgilenmemelidir.",
            "C) Edebiyat sadece bireyseldir.",
            "D) Edebiyat sadece geçmişte kalmıştır.",
            "E) Edebiyat, toplumsal ilerleme ve vizyon için vazgeçilmezdir."
          ],
          "correct": 4,
          "solution": "Doğru cevap Edebiyat, toplumsal ilerleme ve vizyon için vazgeçilmezdir..",
          "id": "e8_q27",
          "no": 27
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde 'yalnız' kelimesinin yazımıyla ilgili bir kural hatırlatılmaktadır? (T-232)",
          "options": [
            "A) 'yalnız' kelimesinin doğru yazımına dikkat edilmelidir.",
            "B) yalnız kelimesi her zaman ayrı yazılır.",
            "C) yalnız cümlede özne olamaz.",
            "D) yalnız kelimesi yabancı kökenlidir.",
            "E) yalnız kelimesi fiildir."
          ],
          "correct": 0,
          "solution": "Doğru cevap 'yalnız' kelimesinin doğru yazımına dikkat edilmelidir..",
          "id": "e8_q28",
          "no": 28
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde mecaz anlamlı bir sözcük kullanılmıştır? (T-233)",
          "options": [
            "A) Buzdolabı soğuk üflüyor.",
            "B) Hava bugün çok soğuk.",
            "C) Olaylara karşı çok 'soğuk' davranıyordu.",
            "D) Kışın havalar soğuk olur.",
            "E) Suyu dolaptan soğuk içti."
          ],
          "correct": 2,
          "solution": "Doğru cevap Olaylara karşı çok 'soğuk' davranıyordu..",
          "id": "e8_q29",
          "no": 29
        },
        {
          "subject": "Türkçe",
          "text": "Tarih tarih boyunca insanlığın en büyük rehberlerinden biri olmuştur. Toplumlar Tarih sayesinde sınırlarını aşmış, geleceğe umutla bakabilmiştir. (P-234)\nBu parçanın ana düşüncesi nedir?",
          "options": [
            "A) Tarih, toplumsal ilerleme ve vizyon için vazgeçilmezdir.",
            "B) İnsanlar Tarih ile ilgilenmemelidir.",
            "C) Tarih zaman kaybıdır.",
            "D) Tarih sadece bireyseldir.",
            "E) Tarih sadece geçmişte kalmıştır."
          ],
          "correct": 0,
          "solution": "Doğru cevap Tarih, toplumsal ilerleme ve vizyon için vazgeçilmezdir..",
          "id": "e8_q30",
          "no": 30
        },
        {
          "subject": "Matematik",
          "text": "7x + 44 = 107 denkleminde x kaçtır? (SoruID: M210)",
          "options": [
            "A) 11",
            "B) 8",
            "C) 12",
            "D) 9",
            "E) 10"
          ],
          "correct": 3,
          "solution": "Doğru cevap 9.",
          "id": "e8_q31",
          "no": 31
        },
        {
          "subject": "Matematik",
          "text": "190 sayısının %60'si kaçtır? (SoruID: M211)",
          "options": [
            "A) 119",
            "B) 129",
            "C) 124",
            "D) 109",
            "E) 114"
          ],
          "correct": 4,
          "solution": "Doğru cevap 114.",
          "id": "e8_q32",
          "no": 32
        },
        {
          "subject": "Matematik",
          "text": "27, 18 ve 27 sayılarının aritmetik ortalaması kaçtır? (SoruID: M212)",
          "options": [
            "A) 26",
            "B) 24",
            "C) 25",
            "D) 23",
            "E) 22"
          ],
          "correct": 1,
          "solution": "Doğru cevap 24.",
          "id": "e8_q33",
          "no": 33
        },
        {
          "subject": "Matematik",
          "text": "Ali 10, Ayşe 23 yaşındadır. 10 yıl sonra yaşları toplamı kaç olur? (SoruID: M213)",
          "options": [
            "A) 43",
            "B) 54",
            "C) 63",
            "D) 52",
            "E) 53"
          ],
          "correct": 4,
          "solution": "Doğru cevap 53.",
          "id": "e8_q34",
          "no": 34
        },
        {
          "subject": "Matematik",
          "text": "√81 + √64 işleminin sonucu kaçtır? (SoruID: M214)",
          "options": [
            "A) 19",
            "B) 18",
            "C) 15",
            "D) 16",
            "E) 17"
          ],
          "correct": 4,
          "solution": "Doğru cevap 17.",
          "id": "e8_q35",
          "no": 35
        },
        {
          "subject": "Matematik",
          "text": "3x + 32 = 44 denkleminde x kaçtır? (SoruID: M215)",
          "options": [
            "A) 3",
            "B) 4",
            "C) 6",
            "D) 7",
            "E) 5"
          ],
          "correct": 1,
          "solution": "Doğru cevap 4.",
          "id": "e8_q36",
          "no": 36
        },
        {
          "subject": "Matematik",
          "text": "180 sayısının %10'si kaçtır? (SoruID: M216)",
          "options": [
            "A) 23",
            "B) 28",
            "C) 13",
            "D) 33",
            "E) 18"
          ],
          "correct": 4,
          "solution": "Doğru cevap 18.",
          "id": "e8_q37",
          "no": 37
        },
        {
          "subject": "Matematik",
          "text": "21, 15 ve 24 sayılarının aritmetik ortalaması kaçtır? (SoruID: M217)",
          "options": [
            "A) 20",
            "B) 22",
            "C) 19",
            "D) 18",
            "E) 21"
          ],
          "correct": 0,
          "solution": "Doğru cevap 20.",
          "id": "e8_q38",
          "no": 38
        },
        {
          "subject": "Matematik",
          "text": "Ali 15, Ayşe 19 yaşındadır. 9 yıl sonra yaşları toplamı kaç olur? (SoruID: M218)",
          "options": [
            "A) 52",
            "B) 51",
            "C) 61",
            "D) 53",
            "E) 43"
          ],
          "correct": 0,
          "solution": "Doğru cevap 52.",
          "id": "e8_q39",
          "no": 39
        },
        {
          "subject": "Matematik",
          "text": "√25 + √9 işleminin sonucu kaçtır? (SoruID: M219)",
          "options": [
            "A) 7",
            "B) 8",
            "C) 9",
            "D) 6",
            "E) 10"
          ],
          "correct": 1,
          "solution": "Doğru cevap 8.",
          "id": "e8_q40",
          "no": 40
        },
        {
          "subject": "Matematik",
          "text": "9x + 25 = 70 denkleminde x kaçtır? (SoruID: M220)",
          "options": [
            "A) 8",
            "B) 5",
            "C) 7",
            "D) 4",
            "E) 6"
          ],
          "correct": 1,
          "solution": "Doğru cevap 5.",
          "id": "e8_q41",
          "no": 41
        },
        {
          "subject": "Matematik",
          "text": "100 sayısının %40'si kaçtır? (SoruID: M221)",
          "options": [
            "A) 35",
            "B) 45",
            "C) 55",
            "D) 40",
            "E) 50"
          ],
          "correct": 3,
          "solution": "Doğru cevap 40.",
          "id": "e8_q42",
          "no": 42
        },
        {
          "subject": "Matematik",
          "text": "17, 17 ve 20 sayılarının aritmetik ortalaması kaçtır? (SoruID: M222)",
          "options": [
            "A) 18",
            "B) 17",
            "C) 19",
            "D) 20",
            "E) 16"
          ],
          "correct": 0,
          "solution": "Doğru cevap 18.",
          "id": "e8_q43",
          "no": 43
        },
        {
          "subject": "Matematik",
          "text": "Ali 11, Ayşe 18 yaşındadır. 7 yıl sonra yaşları toplamı kaç olur? (SoruID: M223)",
          "options": [
            "A) 44",
            "B) 36",
            "C) 50",
            "D) 42",
            "E) 43"
          ],
          "correct": 4,
          "solution": "Doğru cevap 43.",
          "id": "e8_q44",
          "no": 44
        },
        {
          "subject": "Matematik",
          "text": "√49 + √9 işleminin sonucu kaçtır? (SoruID: M224)",
          "options": [
            "A) 10",
            "B) 11",
            "C) 9",
            "D) 8",
            "E) 12"
          ],
          "correct": 0,
          "solution": "Doğru cevap 10.",
          "id": "e8_q45",
          "no": 45
        },
        {
          "subject": "Matematik",
          "text": "8x + 12 = 28 denkleminde x kaçtır? (SoruID: M225)",
          "options": [
            "A) 3",
            "B) 4",
            "C) 5",
            "D) 2",
            "E) 1"
          ],
          "correct": 3,
          "solution": "Doğru cevap 2.",
          "id": "e8_q46",
          "no": 46
        },
        {
          "subject": "Matematik",
          "text": "200 sayısının %25'si kaçtır? (SoruID: M226)",
          "options": [
            "A) 50",
            "B) 65",
            "C) 55",
            "D) 45",
            "E) 60"
          ],
          "correct": 0,
          "solution": "Doğru cevap 50.",
          "id": "e8_q47",
          "no": 47
        },
        {
          "subject": "Matematik",
          "text": "17, 18 ve 31 sayılarının aritmetik ortalaması kaçtır? (SoruID: M227)",
          "options": [
            "A) 24",
            "B) 23",
            "C) 20",
            "D) 22",
            "E) 21"
          ],
          "correct": 3,
          "solution": "Doğru cevap 22.",
          "id": "e8_q48",
          "no": 48
        },
        {
          "subject": "Matematik",
          "text": "Ali 15, Ayşe 18 yaşındadır. 10 yıl sonra yaşları toplamı kaç olur? (SoruID: M228)",
          "options": [
            "A) 63",
            "B) 53",
            "C) 52",
            "D) 54",
            "E) 43"
          ],
          "correct": 1,
          "solution": "Doğru cevap 53.",
          "id": "e8_q49",
          "no": 49
        },
        {
          "subject": "Matematik",
          "text": "√16 + √36 işleminin sonucu kaçtır? (SoruID: M229)",
          "options": [
            "A) 11",
            "B) 8",
            "C) 10",
            "D) 12",
            "E) 9"
          ],
          "correct": 2,
          "solution": "Doğru cevap 10.",
          "id": "e8_q50",
          "no": 50
        },
        {
          "subject": "Matematik",
          "text": "8x + 44 = 60 denkleminde x kaçtır? (SoruID: M230)",
          "options": [
            "A) 3",
            "B) 2",
            "C) 5",
            "D) 4",
            "E) 1"
          ],
          "correct": 1,
          "solution": "Doğru cevap 2.",
          "id": "e8_q51",
          "no": 51
        },
        {
          "subject": "Matematik",
          "text": "40 sayısının %20'si kaçtır? (SoruID: M231)",
          "options": [
            "A) 18",
            "B) 13",
            "C) 3",
            "D) 23",
            "E) 8"
          ],
          "correct": 4,
          "solution": "Doğru cevap 8.",
          "id": "e8_q52",
          "no": 52
        },
        {
          "subject": "Matematik",
          "text": "30, 20 ve 31 sayılarının aritmetik ortalaması kaçtır? (SoruID: M232)",
          "options": [
            "A) 26",
            "B) 25",
            "C) 29",
            "D) 27",
            "E) 28"
          ],
          "correct": 3,
          "solution": "Doğru cevap 27.",
          "id": "e8_q53",
          "no": 53
        },
        {
          "subject": "Matematik",
          "text": "Ali 11, Ayşe 10 yaşındadır. 4 yıl sonra yaşları toplamı kaç olur? (SoruID: M233)",
          "options": [
            "A) 33",
            "B) 25",
            "C) 28",
            "D) 29",
            "E) 30"
          ],
          "correct": 3,
          "solution": "Doğru cevap 29.",
          "id": "e8_q54",
          "no": 54
        },
        {
          "subject": "Matematik",
          "text": "√81 + √25 işleminin sonucu kaçtır? (SoruID: M234)",
          "options": [
            "A) 16",
            "B) 13",
            "C) 12",
            "D) 14",
            "E) 15"
          ],
          "correct": 3,
          "solution": "Doğru cevap 14.",
          "id": "e8_q55",
          "no": 55
        },
        {
          "subject": "Matematik",
          "text": "2x + 7 = 15 denkleminde x kaçtır? (SoruID: M235)",
          "options": [
            "A) 7",
            "B) 4",
            "C) 5",
            "D) 6",
            "E) 3"
          ],
          "correct": 1,
          "solution": "Doğru cevap 4.",
          "id": "e8_q56",
          "no": 56
        },
        {
          "subject": "Matematik",
          "text": "170 sayısının %60'si kaçtır? (SoruID: M236)",
          "options": [
            "A) 107",
            "B) 97",
            "C) 112",
            "D) 117",
            "E) 102"
          ],
          "correct": 4,
          "solution": "Doğru cevap 102.",
          "id": "e8_q57",
          "no": 57
        },
        {
          "subject": "Matematik",
          "text": "17, 21 ve 13 sayılarının aritmetik ortalaması kaçtır? (SoruID: M237)",
          "options": [
            "A) 18",
            "B) 16",
            "C) 19",
            "D) 15",
            "E) 17"
          ],
          "correct": 4,
          "solution": "Doğru cevap 17.",
          "id": "e8_q58",
          "no": 58
        },
        {
          "subject": "Matematik",
          "text": "Ali 17, Ayşe 17 yaşındadır. 3 yıl sonra yaşları toplamı kaç olur? (SoruID: M238)",
          "options": [
            "A) 43",
            "B) 41",
            "C) 39",
            "D) 37",
            "E) 40"
          ],
          "correct": 4,
          "solution": "Doğru cevap 40.",
          "id": "e8_q59",
          "no": 59
        },
        {
          "subject": "Matematik",
          "text": "√4 + √4 işleminin sonucu kaçtır? (SoruID: M239)",
          "options": [
            "A) 2",
            "B) 4",
            "C) 6",
            "D) 5",
            "E) 3"
          ],
          "correct": 1,
          "solution": "Doğru cevap 4.",
          "id": "e8_q60",
          "no": 60
        },
        {
          "subject": "Tarih",
          "text": "Türk siyasi ve askerî tarihinde büyük öneme sahip olan 'Mudanya Mütarekesi' süreci ile ilgili aşağıdakilerden hangisi söylenebilir? (H-186)",
          "options": [
            "A) Avrupa'da gerçekleşmiştir.",
            "B) Osmanlı'nın kuruluş dönemine aittir.",
            "C) Hiçbir etkisi olmamıştır.",
            "D) Mudanya Mütarekesi dönemin en kritik gelişmelerinden biridir.",
            "E) Sadece ekonomik bir olaydır."
          ],
          "correct": 3,
          "solution": "Doğru cevap Mudanya Mütarekesi dönemin en kritik gelişmelerinden biridir..",
          "id": "e8_q61",
          "no": 61
        },
        {
          "subject": "Tarih",
          "text": "Aşağıdaki tarihî gelişmelerden hangisi 'Saltanatın Kaldırılması' ile doğrudan veya dolaylı olarak bağlantılıdır? (H-187)",
          "options": [
            "A) Coğrafi Keşifler",
            "B) Kavimler Göçü",
            "C) Fransız İhtilali",
            "D) Sanayi İnkılabı",
            "E) Saltanatın Kaldırılması öncesi ve sonrası yaşanan siyasi krizler."
          ],
          "correct": 4,
          "solution": "Doğru cevap Saltanatın Kaldırılması öncesi ve sonrası yaşanan siyasi krizler..",
          "id": "e8_q62",
          "no": 62
        },
        {
          "subject": "Tarih",
          "text": "Millî Mücadele ve inkılaplar tarihi incelendiğinde 'Halifeliğin Kaldırılması' olayının temel amacı aşağıdakilerden hangisidir? (H-188)",
          "options": [
            "A) Avrupa'ya göç etmek",
            "B) Bağımsızlık ve egemenliği pekiştirmek",
            "C) Feodaliteyi kurmak",
            "D) Yeni sömürgeler elde etmek",
            "E) Saltanatı güçlendirmek"
          ],
          "correct": 1,
          "solution": "Doğru cevap Bağımsızlık ve egemenliği pekiştirmek.",
          "id": "e8_q63",
          "no": 63
        },
        {
          "subject": "Tarih",
          "text": "Türk siyasi ve askerî tarihinde büyük öneme sahip olan 'Tevhid-i Tedrisat' süreci ile ilgili aşağıdakilerden hangisi söylenebilir? (H-189)",
          "options": [
            "A) Tevhid-i Tedrisat dönemin en kritik gelişmelerinden biridir.",
            "B) Osmanlı'nın kuruluş dönemine aittir.",
            "C) Hiçbir etkisi olmamıştır.",
            "D) Sadece ekonomik bir olaydır.",
            "E) Avrupa'da gerçekleşmiştir."
          ],
          "correct": 0,
          "solution": "Doğru cevap Tevhid-i Tedrisat dönemin en kritik gelişmelerinden biridir..",
          "id": "e8_q64",
          "no": 64
        },
        {
          "subject": "Tarih",
          "text": "Aşağıdaki tarihî gelişmelerden hangisi 'Trablusgarp Savaşı' ile doğrudan veya dolaylı olarak bağlantılıdır? (H-190)",
          "options": [
            "A) Coğrafi Keşifler",
            "B) Kavimler Göçü",
            "C) Sanayi İnkılabı",
            "D) Trablusgarp Savaşı öncesi ve sonrası yaşanan siyasi krizler.",
            "E) Fransız İhtilali"
          ],
          "correct": 3,
          "solution": "Doğru cevap Trablusgarp Savaşı öncesi ve sonrası yaşanan siyasi krizler..",
          "id": "e8_q65",
          "no": 65
        },
        {
          "subject": "Tarih",
          "text": "Millî Mücadele ve inkılaplar tarihi incelendiğinde 'Balkan Savaşları' olayının temel amacı aşağıdakilerden hangisidir? (H-191)",
          "options": [
            "A) Bağımsızlık ve egemenliği pekiştirmek",
            "B) Avrupa'ya göç etmek",
            "C) Feodaliteyi kurmak",
            "D) Saltanatı güçlendirmek",
            "E) Yeni sömürgeler elde etmek"
          ],
          "correct": 0,
          "solution": "Doğru cevap Bağımsızlık ve egemenliği pekiştirmek.",
          "id": "e8_q66",
          "no": 66
        },
        {
          "subject": "Tarih",
          "text": "Türk siyasi ve askerî tarihinde büyük öneme sahip olan 'I. Dünya Savaşı' süreci ile ilgili aşağıdakilerden hangisi söylenebilir? (H-192)",
          "options": [
            "A) Hiçbir etkisi olmamıştır.",
            "B) Sadece ekonomik bir olaydır.",
            "C) I. Dünya Savaşı dönemin en kritik gelişmelerinden biridir.",
            "D) Osmanlı'nın kuruluş dönemine aittir.",
            "E) Avrupa'da gerçekleşmiştir."
          ],
          "correct": 2,
          "solution": "Doğru cevap I. Dünya Savaşı dönemin en kritik gelişmelerinden biridir..",
          "id": "e8_q67",
          "no": 67
        },
        {
          "subject": "Tarih",
          "text": "Aşağıdaki tarihî gelişmelerden hangisi 'Çanakkale Cephesi' ile doğrudan veya dolaylı olarak bağlantılıdır? (H-193)",
          "options": [
            "A) Coğrafi Keşifler",
            "B) Kavimler Göçü",
            "C) Çanakkale Cephesi öncesi ve sonrası yaşanan siyasi krizler.",
            "D) Sanayi İnkılabı",
            "E) Fransız İhtilali"
          ],
          "correct": 2,
          "solution": "Doğru cevap Çanakkale Cephesi öncesi ve sonrası yaşanan siyasi krizler..",
          "id": "e8_q68",
          "no": 68
        },
        {
          "subject": "Tarih",
          "text": "Millî Mücadele ve inkılaplar tarihi incelendiğinde 'Sakarya Meydan Muharebesi' olayının temel amacı aşağıdakilerden hangisidir? (H-194)",
          "options": [
            "A) Yeni sömürgeler elde etmek",
            "B) Saltanatı güçlendirmek",
            "C) Avrupa'ya göç etmek",
            "D) Feodaliteyi kurmak",
            "E) Bağımsızlık ve egemenliği pekiştirmek"
          ],
          "correct": 4,
          "solution": "Doğru cevap Bağımsızlık ve egemenliği pekiştirmek.",
          "id": "e8_q69",
          "no": 69
        },
        {
          "subject": "Tarih",
          "text": "Türk siyasi ve askerî tarihinde büyük öneme sahip olan 'Büyük Taarruz' süreci ile ilgili aşağıdakilerden hangisi söylenebilir? (H-195)",
          "options": [
            "A) Hiçbir etkisi olmamıştır.",
            "B) Osmanlı'nın kuruluş dönemine aittir.",
            "C) Avrupa'da gerçekleşmiştir.",
            "D) Sadece ekonomik bir olaydır.",
            "E) Büyük Taarruz dönemin en kritik gelişmelerinden biridir."
          ],
          "correct": 4,
          "solution": "Doğru cevap Büyük Taarruz dönemin en kritik gelişmelerinden biridir..",
          "id": "e8_q70",
          "no": 70
        },
        {
          "subject": "Tarih",
          "text": "Aşağıdaki tarihî gelişmelerden hangisi 'I. İnönü Muharebesi' ile doğrudan veya dolaylı olarak bağlantılıdır? (H-196)",
          "options": [
            "A) I. İnönü Muharebesi öncesi ve sonrası yaşanan siyasi krizler.",
            "B) Coğrafi Keşifler",
            "C) Fransız İhtilali",
            "D) Sanayi İnkılabı",
            "E) Kavimler Göçü"
          ],
          "correct": 0,
          "solution": "Doğru cevap I. İnönü Muharebesi öncesi ve sonrası yaşanan siyasi krizler..",
          "id": "e8_q71",
          "no": 71
        },
        {
          "subject": "Tarih",
          "text": "Millî Mücadele ve inkılaplar tarihi incelendiğinde 'II. İnönü Muharebesi' olayının temel amacı aşağıdakilerden hangisidir? (H-197)",
          "options": [
            "A) Bağımsızlık ve egemenliği pekiştirmek",
            "B) Saltanatı güçlendirmek",
            "C) Feodaliteyi kurmak",
            "D) Avrupa'ya göç etmek",
            "E) Yeni sömürgeler elde etmek"
          ],
          "correct": 0,
          "solution": "Doğru cevap Bağımsızlık ve egemenliği pekiştirmek.",
          "id": "e8_q72",
          "no": 72
        },
        {
          "subject": "Tarih",
          "text": "Türk siyasi ve askerî tarihinde büyük öneme sahip olan 'Kars Antlaşması' süreci ile ilgili aşağıdakilerden hangisi söylenebilir? (H-198)",
          "options": [
            "A) Kars Antlaşması dönemin en kritik gelişmelerinden biridir.",
            "B) Sadece ekonomik bir olaydır.",
            "C) Osmanlı'nın kuruluş dönemine aittir.",
            "D) Hiçbir etkisi olmamıştır.",
            "E) Avrupa'da gerçekleşmiştir."
          ],
          "correct": 0,
          "solution": "Doğru cevap Kars Antlaşması dönemin en kritik gelişmelerinden biridir..",
          "id": "e8_q73",
          "no": 73
        },
        {
          "subject": "Tarih",
          "text": "Aşağıdaki tarihî gelişmelerden hangisi 'Ankara Antlaşması' ile doğrudan veya dolaylı olarak bağlantılıdır? (H-199)",
          "options": [
            "A) Coğrafi Keşifler",
            "B) Kavimler Göçü",
            "C) Fransız İhtilali",
            "D) Sanayi İnkılabı",
            "E) Ankara Antlaşması öncesi ve sonrası yaşanan siyasi krizler."
          ],
          "correct": 4,
          "solution": "Doğru cevap Ankara Antlaşması öncesi ve sonrası yaşanan siyasi krizler..",
          "id": "e8_q74",
          "no": 74
        },
        {
          "subject": "Tarih",
          "text": "Millî Mücadele ve inkılaplar tarihi incelendiğinde 'Sivas Kongresi' olayının temel amacı aşağıdakilerden hangisidir? (H-200)",
          "options": [
            "A) Avrupa'ya göç etmek",
            "B) Saltanatı güçlendirmek",
            "C) Feodaliteyi kurmak",
            "D) Bağımsızlık ve egemenliği pekiştirmek",
            "E) Yeni sömürgeler elde etmek"
          ],
          "correct": 3,
          "solution": "Doğru cevap Bağımsızlık ve egemenliği pekiştirmek.",
          "id": "e8_q75",
          "no": 75
        },
        {
          "subject": "Tarih",
          "text": "Türk siyasi ve askerî tarihinde büyük öneme sahip olan 'Erzurum Kongresi' süreci ile ilgili aşağıdakilerden hangisi söylenebilir? (H-201)",
          "options": [
            "A) Avrupa'da gerçekleşmiştir.",
            "B) Sadece ekonomik bir olaydır.",
            "C) Osmanlı'nın kuruluş dönemine aittir.",
            "D) Erzurum Kongresi dönemin en kritik gelişmelerinden biridir.",
            "E) Hiçbir etkisi olmamıştır."
          ],
          "correct": 3,
          "solution": "Doğru cevap Erzurum Kongresi dönemin en kritik gelişmelerinden biridir..",
          "id": "e8_q76",
          "no": 76
        },
        {
          "subject": "Tarih",
          "text": "Aşağıdaki tarihî gelişmelerden hangisi 'Amasya Genelgesi' ile doğrudan veya dolaylı olarak bağlantılıdır? (H-202)",
          "options": [
            "A) Coğrafi Keşifler",
            "B) Sanayi İnkılabı",
            "C) Fransız İhtilali",
            "D) Kavimler Göçü",
            "E) Amasya Genelgesi öncesi ve sonrası yaşanan siyasi krizler."
          ],
          "correct": 4,
          "solution": "Doğru cevap Amasya Genelgesi öncesi ve sonrası yaşanan siyasi krizler..",
          "id": "e8_q77",
          "no": 77
        },
        {
          "subject": "Tarih",
          "text": "Millî Mücadele ve inkılaplar tarihi incelendiğinde 'Lozan Antlaşması' olayının temel amacı aşağıdakilerden hangisidir? (H-203)",
          "options": [
            "A) Bağımsızlık ve egemenliği pekiştirmek",
            "B) Saltanatı güçlendirmek",
            "C) Yeni sömürgeler elde etmek",
            "D) Avrupa'ya göç etmek",
            "E) Feodaliteyi kurmak"
          ],
          "correct": 0,
          "solution": "Doğru cevap Bağımsızlık ve egemenliği pekiştirmek.",
          "id": "e8_q78",
          "no": 78
        },
        {
          "subject": "Tarih",
          "text": "Türk siyasi ve askerî tarihinde büyük öneme sahip olan 'Cumhuriyetin İlanı' süreci ile ilgili aşağıdakilerden hangisi söylenebilir? (H-204)",
          "options": [
            "A) Cumhuriyetin İlanı dönemin en kritik gelişmelerinden biridir.",
            "B) Osmanlı'nın kuruluş dönemine aittir.",
            "C) Avrupa'da gerçekleşmiştir.",
            "D) Hiçbir etkisi olmamıştır.",
            "E) Sadece ekonomik bir olaydır."
          ],
          "correct": 0,
          "solution": "Doğru cevap Cumhuriyetin İlanı dönemin en kritik gelişmelerinden biridir..",
          "id": "e8_q79",
          "no": 79
        },
        {
          "subject": "Tarih",
          "text": "Aşağıdaki tarihî gelişmelerden hangisi 'TBMM'nin Açılışı' ile doğrudan veya dolaylı olarak bağlantılıdır? (H-205)",
          "options": [
            "A) Fransız İhtilali",
            "B) Kavimler Göçü",
            "C) Sanayi İnkılabı",
            "D) TBMM'nin Açılışı öncesi ve sonrası yaşanan siyasi krizler.",
            "E) Coğrafi Keşifler"
          ],
          "correct": 3,
          "solution": "Doğru cevap TBMM'nin Açılışı öncesi ve sonrası yaşanan siyasi krizler..",
          "id": "e8_q80",
          "no": 80
        },
        {
          "subject": "Tarih",
          "text": "Millî Mücadele ve inkılaplar tarihi incelendiğinde 'Mudanya Mütarekesi' olayının temel amacı aşağıdakilerden hangisidir? (H-206)",
          "options": [
            "A) Feodaliteyi kurmak",
            "B) Yeni sömürgeler elde etmek",
            "C) Saltanatı güçlendirmek",
            "D) Bağımsızlık ve egemenliği pekiştirmek",
            "E) Avrupa'ya göç etmek"
          ],
          "correct": 3,
          "solution": "Doğru cevap Bağımsızlık ve egemenliği pekiştirmek.",
          "id": "e8_q81",
          "no": 81
        },
        {
          "subject": "Tarih",
          "text": "Türk siyasi ve askerî tarihinde büyük öneme sahip olan 'Saltanatın Kaldırılması' süreci ile ilgili aşağıdakilerden hangisi söylenebilir? (H-207)",
          "options": [
            "A) Osmanlı'nın kuruluş dönemine aittir.",
            "B) Avrupa'da gerçekleşmiştir.",
            "C) Sadece ekonomik bir olaydır.",
            "D) Saltanatın Kaldırılması dönemin en kritik gelişmelerinden biridir.",
            "E) Hiçbir etkisi olmamıştır."
          ],
          "correct": 3,
          "solution": "Doğru cevap Saltanatın Kaldırılması dönemin en kritik gelişmelerinden biridir..",
          "id": "e8_q82",
          "no": 82
        },
        {
          "subject": "Tarih",
          "text": "Aşağıdaki tarihî gelişmelerden hangisi 'Halifeliğin Kaldırılması' ile doğrudan veya dolaylı olarak bağlantılıdır? (H-208)",
          "options": [
            "A) Coğrafi Keşifler",
            "B) Halifeliğin Kaldırılması öncesi ve sonrası yaşanan siyasi krizler.",
            "C) Kavimler Göçü",
            "D) Fransız İhtilali",
            "E) Sanayi İnkılabı"
          ],
          "correct": 1,
          "solution": "Doğru cevap Halifeliğin Kaldırılması öncesi ve sonrası yaşanan siyasi krizler..",
          "id": "e8_q83",
          "no": 83
        },
        {
          "subject": "Tarih",
          "text": "Millî Mücadele ve inkılaplar tarihi incelendiğinde 'Tevhid-i Tedrisat' olayının temel amacı aşağıdakilerden hangisidir? (H-209)",
          "options": [
            "A) Bağımsızlık ve egemenliği pekiştirmek",
            "B) Avrupa'ya göç etmek",
            "C) Feodaliteyi kurmak",
            "D) Yeni sömürgeler elde etmek",
            "E) Saltanatı güçlendirmek"
          ],
          "correct": 0,
          "solution": "Doğru cevap Bağımsızlık ve egemenliği pekiştirmek.",
          "id": "e8_q84",
          "no": 84
        },
        {
          "subject": "Tarih",
          "text": "Türk siyasi ve askerî tarihinde büyük öneme sahip olan 'Trablusgarp Savaşı' süreci ile ilgili aşağıdakilerden hangisi söylenebilir? (H-210)",
          "options": [
            "A) Sadece ekonomik bir olaydır.",
            "B) Avrupa'da gerçekleşmiştir.",
            "C) Trablusgarp Savaşı dönemin en kritik gelişmelerinden biridir.",
            "D) Hiçbir etkisi olmamıştır.",
            "E) Osmanlı'nın kuruluş dönemine aittir."
          ],
          "correct": 2,
          "solution": "Doğru cevap Trablusgarp Savaşı dönemin en kritik gelişmelerinden biridir..",
          "id": "e8_q85",
          "no": 85
        },
        {
          "subject": "Tarih",
          "text": "Aşağıdaki tarihî gelişmelerden hangisi 'Balkan Savaşları' ile doğrudan veya dolaylı olarak bağlantılıdır? (H-211)",
          "options": [
            "A) Coğrafi Keşifler",
            "B) Sanayi İnkılabı",
            "C) Balkan Savaşları öncesi ve sonrası yaşanan siyasi krizler.",
            "D) Kavimler Göçü",
            "E) Fransız İhtilali"
          ],
          "correct": 2,
          "solution": "Doğru cevap Balkan Savaşları öncesi ve sonrası yaşanan siyasi krizler..",
          "id": "e8_q86",
          "no": 86
        },
        {
          "subject": "Tarih",
          "text": "Millî Mücadele ve inkılaplar tarihi incelendiğinde 'I. Dünya Savaşı' olayının temel amacı aşağıdakilerden hangisidir? (H-212)",
          "options": [
            "A) Saltanatı güçlendirmek",
            "B) Feodaliteyi kurmak",
            "C) Yeni sömürgeler elde etmek",
            "D) Avrupa'ya göç etmek",
            "E) Bağımsızlık ve egemenliği pekiştirmek"
          ],
          "correct": 4,
          "solution": "Doğru cevap Bağımsızlık ve egemenliği pekiştirmek.",
          "id": "e8_q87",
          "no": 87
        },
        {
          "subject": "Coğrafya",
          "text": "Türkiye'nin fiziki coğrafyası düşünüldüğünde 'Tuz Gölü' için aşağıdakilerden hangisi doğrudur? (C-124)",
          "options": [
            "A) Tuz Gölü yapay bir kanaldır.",
            "B) Tuz Gölü bir çöldür.",
            "C) Tuz Gölü, ülkemizin önemli yeryüzü şekillerinden biridir.",
            "D) Tuz Gölü Marmara'dadır.",
            "E) Tuz Gölü tarıma kapalıdır."
          ],
          "correct": 2,
          "solution": "Doğru cevap Tuz Gölü, ülkemizin önemli yeryüzü şekillerinden biridir..",
          "id": "e8_q88",
          "no": 88
        },
        {
          "subject": "Coğrafya",
          "text": "Coğrafi özellikleri ve turizm potansiyeli göz önüne alındığında 'Çukurova' hangi alanda daha çok öne çıkar? (C-125)",
          "options": [
            "A) Okyanus balıkçılığı",
            "B) Doğal güzellikleri ve turizm/coğrafi önemi",
            "C) Çöl iklimi araştırmaları",
            "D) Sadece ağır sanayi",
            "E) Sadece madencilik"
          ],
          "correct": 1,
          "solution": "Doğru cevap Doğal güzellikleri ve turizm/coğrafi önemi.",
          "id": "e8_q89",
          "no": 89
        },
        {
          "subject": "Coğrafya",
          "text": "Türkiye'nin fiziki coğrafyası düşünüldüğünde 'Bafra Ovası' için aşağıdakilerden hangisi doğrudur? (C-126)",
          "options": [
            "A) Bafra Ovası Marmara'dadır.",
            "B) Bafra Ovası tarıma kapalıdır.",
            "C) Bafra Ovası, ülkemizin önemli yeryüzü şekillerinden biridir.",
            "D) Bafra Ovası bir çöldür.",
            "E) Bafra Ovası yapay bir kanaldır."
          ],
          "correct": 2,
          "solution": "Doğru cevap Bafra Ovası, ülkemizin önemli yeryüzü şekillerinden biridir..",
          "id": "e8_q90",
          "no": 90
        },
        {
          "subject": "Coğrafya",
          "text": "Coğrafi özellikleri ve turizm potansiyeli göz önüne alındığında 'Kaçkar Dağları' hangi alanda daha çok öne çıkar? (C-127)",
          "options": [
            "A) Doğal güzellikleri ve turizm/coğrafi önemi",
            "B) Okyanus balıkçılığı",
            "C) Çöl iklimi araştırmaları",
            "D) Sadece madencilik",
            "E) Sadece ağır sanayi"
          ],
          "correct": 0,
          "solution": "Doğru cevap Doğal güzellikleri ve turizm/coğrafi önemi.",
          "id": "e8_q91",
          "no": 91
        },
        {
          "subject": "Coğrafya",
          "text": "Türkiye'nin fiziki coğrafyası düşünüldüğünde 'Gediz Nehri' için aşağıdakilerden hangisi doğrudur? (C-128)",
          "options": [
            "A) Gediz Nehri tarıma kapalıdır.",
            "B) Gediz Nehri yapay bir kanaldır.",
            "C) Gediz Nehri bir çöldür.",
            "D) Gediz Nehri Marmara'dadır.",
            "E) Gediz Nehri, ülkemizin önemli yeryüzü şekillerinden biridir."
          ],
          "correct": 4,
          "solution": "Doğru cevap Gediz Nehri, ülkemizin önemli yeryüzü şekillerinden biridir..",
          "id": "e8_q92",
          "no": 92
        },
        {
          "subject": "Coğrafya",
          "text": "Coğrafi özellikleri ve turizm potansiyeli göz önüne alındığında 'Salda Gölü' hangi alanda daha çok öne çıkar? (C-129)",
          "options": [
            "A) Çöl iklimi araştırmaları",
            "B) Sadece ağır sanayi",
            "C) Doğal güzellikleri ve turizm/coğrafi önemi",
            "D) Sadece madencilik",
            "E) Okyanus balıkçılığı"
          ],
          "correct": 2,
          "solution": "Doğru cevap Doğal güzellikleri ve turizm/coğrafi önemi.",
          "id": "e8_q93",
          "no": 93
        },
        {
          "subject": "Coğrafya",
          "text": "Türkiye'nin fiziki coğrafyası düşünüldüğünde 'Kapadokya' için aşağıdakilerden hangisi doğrudur? (C-130)",
          "options": [
            "A) Kapadokya tarıma kapalıdır.",
            "B) Kapadokya, ülkemizin önemli yeryüzü şekillerinden biridir.",
            "C) Kapadokya Marmara'dadır.",
            "D) Kapadokya bir çöldür.",
            "E) Kapadokya yapay bir kanaldır."
          ],
          "correct": 1,
          "solution": "Doğru cevap Kapadokya, ülkemizin önemli yeryüzü şekillerinden biridir..",
          "id": "e8_q94",
          "no": 94
        },
        {
          "subject": "Coğrafya",
          "text": "Coğrafi özellikleri ve turizm potansiyeli göz önüne alındığında 'Pamukkale' hangi alanda daha çok öne çıkar? (C-131)",
          "options": [
            "A) Sadece ağır sanayi",
            "B) Okyanus balıkçılığı",
            "C) Çöl iklimi araştırmaları",
            "D) Sadece madencilik",
            "E) Doğal güzellikleri ve turizm/coğrafi önemi"
          ],
          "correct": 4,
          "solution": "Doğru cevap Doğal güzellikleri ve turizm/coğrafi önemi.",
          "id": "e8_q95",
          "no": 95
        },
        {
          "subject": "Coğrafya",
          "text": "Türkiye'nin fiziki coğrafyası düşünüldüğünde 'Nemrut Dağı' için aşağıdakilerden hangisi doğrudur? (C-132)",
          "options": [
            "A) Nemrut Dağı, ülkemizin önemli yeryüzü şekillerinden biridir.",
            "B) Nemrut Dağı Marmara'dadır.",
            "C) Nemrut Dağı bir çöldür.",
            "D) Nemrut Dağı tarıma kapalıdır.",
            "E) Nemrut Dağı yapay bir kanaldır."
          ],
          "correct": 0,
          "solution": "Doğru cevap Nemrut Dağı, ülkemizin önemli yeryüzü şekillerinden biridir..",
          "id": "e8_q96",
          "no": 96
        },
        {
          "subject": "Coğrafya",
          "text": "Coğrafi özellikleri ve turizm potansiyeli göz önüne alındığında 'Sümela Manastırı' hangi alanda daha çok öne çıkar? (C-133)",
          "options": [
            "A) Sadece ağır sanayi",
            "B) Sadece madencilik",
            "C) Okyanus balıkçılığı",
            "D) Doğal güzellikleri ve turizm/coğrafi önemi",
            "E) Çöl iklimi araştırmaları"
          ],
          "correct": 3,
          "solution": "Doğru cevap Doğal güzellikleri ve turizm/coğrafi önemi.",
          "id": "e8_q97",
          "no": 97
        },
        {
          "subject": "Coğrafya",
          "text": "Türkiye'nin fiziki coğrafyası düşünüldüğünde 'Uludağ' için aşağıdakilerden hangisi doğrudur? (C-134)",
          "options": [
            "A) Uludağ tarıma kapalıdır.",
            "B) Uludağ bir çöldür.",
            "C) Uludağ, ülkemizin önemli yeryüzü şekillerinden biridir.",
            "D) Uludağ yapay bir kanaldır.",
            "E) Uludağ Marmara'dadır."
          ],
          "correct": 2,
          "solution": "Doğru cevap Uludağ, ülkemizin önemli yeryüzü şekillerinden biridir..",
          "id": "e8_q98",
          "no": 98
        },
        {
          "subject": "Coğrafya",
          "text": "Coğrafi özellikleri ve turizm potansiyeli göz önüne alındığında 'Van Gölü' hangi alanda daha çok öne çıkar? (C-135)",
          "options": [
            "A) Doğal güzellikleri ve turizm/coğrafi önemi",
            "B) Sadece ağır sanayi",
            "C) Sadece madencilik",
            "D) Çöl iklimi araştırmaları",
            "E) Okyanus balıkçılığı"
          ],
          "correct": 0,
          "solution": "Doğru cevap Doğal güzellikleri ve turizm/coğrafi önemi.",
          "id": "e8_q99",
          "no": 99
        },
        {
          "subject": "Coğrafya",
          "text": "Türkiye'nin fiziki coğrafyası düşünüldüğünde 'Ağrı Dağı' için aşağıdakilerden hangisi doğrudur? (C-136)",
          "options": [
            "A) Ağrı Dağı yapay bir kanaldır.",
            "B) Ağrı Dağı, ülkemizin önemli yeryüzü şekillerinden biridir.",
            "C) Ağrı Dağı Marmara'dadır.",
            "D) Ağrı Dağı tarıma kapalıdır.",
            "E) Ağrı Dağı bir çöldür."
          ],
          "correct": 1,
          "solution": "Doğru cevap Ağrı Dağı, ülkemizin önemli yeryüzü şekillerinden biridir..",
          "id": "e8_q100",
          "no": 100
        },
        {
          "subject": "Coğrafya",
          "text": "Coğrafi özellikleri ve turizm potansiyeli göz önüne alındığında 'Kızılırmak' hangi alanda daha çok öne çıkar? (C-137)",
          "options": [
            "A) Sadece madencilik",
            "B) Doğal güzellikleri ve turizm/coğrafi önemi",
            "C) Çöl iklimi araştırmaları",
            "D) Okyanus balıkçılığı",
            "E) Sadece ağır sanayi"
          ],
          "correct": 1,
          "solution": "Doğru cevap Doğal güzellikleri ve turizm/coğrafi önemi.",
          "id": "e8_q101",
          "no": 101
        },
        {
          "subject": "Coğrafya",
          "text": "Türkiye'nin fiziki coğrafyası düşünüldüğünde 'Erciyes Dağı' için aşağıdakilerden hangisi doğrudur? (C-138)",
          "options": [
            "A) Erciyes Dağı, ülkemizin önemli yeryüzü şekillerinden biridir.",
            "B) Erciyes Dağı Marmara'dadır.",
            "C) Erciyes Dağı yapay bir kanaldır.",
            "D) Erciyes Dağı tarıma kapalıdır.",
            "E) Erciyes Dağı bir çöldür."
          ],
          "correct": 0,
          "solution": "Doğru cevap Erciyes Dağı, ülkemizin önemli yeryüzü şekillerinden biridir..",
          "id": "e8_q102",
          "no": 102
        },
        {
          "subject": "Coğrafya",
          "text": "Coğrafi özellikleri ve turizm potansiyeli göz önüne alındığında 'Tuz Gölü' hangi alanda daha çok öne çıkar? (C-139)",
          "options": [
            "A) Çöl iklimi araştırmaları",
            "B) Sadece ağır sanayi",
            "C) Sadece madencilik",
            "D) Okyanus balıkçılığı",
            "E) Doğal güzellikleri ve turizm/coğrafi önemi"
          ],
          "correct": 4,
          "solution": "Doğru cevap Doğal güzellikleri ve turizm/coğrafi önemi.",
          "id": "e8_q103",
          "no": 103
        },
        {
          "subject": "Coğrafya",
          "text": "Türkiye'nin fiziki coğrafyası düşünüldüğünde 'Çukurova' için aşağıdakilerden hangisi doğrudur? (C-140)",
          "options": [
            "A) Çukurova Marmara'dadır.",
            "B) Çukurova, ülkemizin önemli yeryüzü şekillerinden biridir.",
            "C) Çukurova yapay bir kanaldır.",
            "D) Çukurova tarıma kapalıdır.",
            "E) Çukurova bir çöldür."
          ],
          "correct": 1,
          "solution": "Doğru cevap Çukurova, ülkemizin önemli yeryüzü şekillerinden biridir..",
          "id": "e8_q104",
          "no": 104
        },
        {
          "subject": "Coğrafya",
          "text": "Coğrafi özellikleri ve turizm potansiyeli göz önüne alındığında 'Bafra Ovası' hangi alanda daha çok öne çıkar? (C-141)",
          "options": [
            "A) Okyanus balıkçılığı",
            "B) Sadece madencilik",
            "C) Çöl iklimi araştırmaları",
            "D) Doğal güzellikleri ve turizm/coğrafi önemi",
            "E) Sadece ağır sanayi"
          ],
          "correct": 3,
          "solution": "Doğru cevap Doğal güzellikleri ve turizm/coğrafi önemi.",
          "id": "e8_q105",
          "no": 105
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'Kamu Denetçiliği Kurumu' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-103)",
          "options": [
            "A) Kamu Denetçiliği Kurumu sadece köylerde bulunur.",
            "B) Kamu Denetçiliği Kurumu özel bir şirkettir.",
            "C) Kamu Denetçiliği Kurumu yabancı bir kurumdur.",
            "D) Kamu Denetçiliği Kurumu, anayasal sistemin önemli bir parçasıdır.",
            "E) Kamu Denetçiliği Kurumu yasaklanmıştır."
          ],
          "correct": 3,
          "solution": "Doğru cevap Kamu Denetçiliği Kurumu, anayasal sistemin önemli bir parçasıdır..",
          "id": "e8_q106",
          "no": 106
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'Anayasa Mahkemesi' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-104)",
          "options": [
            "A) Anayasa Mahkemesi, anayasal sistemin önemli bir parçasıdır.",
            "B) Anayasa Mahkemesi yasaklanmıştır.",
            "C) Anayasa Mahkemesi yabancı bir kurumdur.",
            "D) Anayasa Mahkemesi sadece köylerde bulunur.",
            "E) Anayasa Mahkemesi özel bir şirkettir."
          ],
          "correct": 0,
          "solution": "Doğru cevap Anayasa Mahkemesi, anayasal sistemin önemli bir parçasıdır..",
          "id": "e8_q107",
          "no": 107
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'Yargıtay' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-105)",
          "options": [
            "A) Yargıtay yabancı bir kurumdur.",
            "B) Yargıtay sadece köylerde bulunur.",
            "C) Yargıtay özel bir şirkettir.",
            "D) Yargıtay yasaklanmıştır.",
            "E) Yargıtay, anayasal sistemin önemli bir parçasıdır."
          ],
          "correct": 4,
          "solution": "Doğru cevap Yargıtay, anayasal sistemin önemli bir parçasıdır..",
          "id": "e8_q108",
          "no": 108
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'Danıştay' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-106)",
          "options": [
            "A) Danıştay sadece köylerde bulunur.",
            "B) Danıştay özel bir şirkettir.",
            "C) Danıştay, anayasal sistemin önemli bir parçasıdır.",
            "D) Danıştay yabancı bir kurumdur.",
            "E) Danıştay yasaklanmıştır."
          ],
          "correct": 2,
          "solution": "Doğru cevap Danıştay, anayasal sistemin önemli bir parçasıdır..",
          "id": "e8_q109",
          "no": 109
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'TBMM' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-107)",
          "options": [
            "A) TBMM özel bir şirkettir.",
            "B) TBMM, anayasal sistemin önemli bir parçasıdır.",
            "C) TBMM yasaklanmıştır.",
            "D) TBMM yabancı bir kurumdur.",
            "E) TBMM sadece köylerde bulunur."
          ],
          "correct": 1,
          "solution": "Doğru cevap TBMM, anayasal sistemin önemli bir parçasıdır..",
          "id": "e8_q110",
          "no": 110
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'Cumhurbaşkanlığı' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-108)",
          "options": [
            "A) Cumhurbaşkanlığı, anayasal sistemin önemli bir parçasıdır.",
            "B) Cumhurbaşkanlığı sadece köylerde bulunur.",
            "C) Cumhurbaşkanlığı yasaklanmıştır.",
            "D) Cumhurbaşkanlığı yabancı bir kurumdur.",
            "E) Cumhurbaşkanlığı özel bir şirkettir."
          ],
          "correct": 0,
          "solution": "Doğru cevap Cumhurbaşkanlığı, anayasal sistemin önemli bir parçasıdır..",
          "id": "e8_q111",
          "no": 111
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'Sayıştay' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-109)",
          "options": [
            "A) Sayıştay özel bir şirkettir.",
            "B) Sayıştay yasaklanmıştır.",
            "C) Sayıştay, anayasal sistemin önemli bir parçasıdır.",
            "D) Sayıştay sadece köylerde bulunur.",
            "E) Sayıştay yabancı bir kurumdur."
          ],
          "correct": 2,
          "solution": "Doğru cevap Sayıştay, anayasal sistemin önemli bir parçasıdır..",
          "id": "e8_q112",
          "no": 112
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'YSK' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-110)",
          "options": [
            "A) YSK yabancı bir kurumdur.",
            "B) YSK yasaklanmıştır.",
            "C) YSK, anayasal sistemin önemli bir parçasıdır.",
            "D) YSK özel bir şirkettir.",
            "E) YSK sadece köylerde bulunur."
          ],
          "correct": 2,
          "solution": "Doğru cevap YSK, anayasal sistemin önemli bir parçasıdır..",
          "id": "e8_q113",
          "no": 113
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'HSK' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-111)",
          "options": [
            "A) HSK özel bir şirkettir.",
            "B) HSK, anayasal sistemin önemli bir parçasıdır.",
            "C) HSK sadece köylerde bulunur.",
            "D) HSK yasaklanmıştır.",
            "E) HSK yabancı bir kurumdur."
          ],
          "correct": 1,
          "solution": "Doğru cevap HSK, anayasal sistemin önemli bir parçasıdır..",
          "id": "e8_q114",
          "no": 114
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'Belediye' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-112)",
          "options": [
            "A) Belediye özel bir şirkettir.",
            "B) Belediye yabancı bir kurumdur.",
            "C) Belediye yasaklanmıştır.",
            "D) Belediye, anayasal sistemin önemli bir parçasıdır.",
            "E) Belediye sadece köylerde bulunur."
          ],
          "correct": 3,
          "solution": "Doğru cevap Belediye, anayasal sistemin önemli bir parçasıdır..",
          "id": "e8_q115",
          "no": 115
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'Valilik' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-113)",
          "options": [
            "A) Valilik yasaklanmıştır.",
            "B) Valilik, anayasal sistemin önemli bir parçasıdır.",
            "C) Valilik sadece köylerde bulunur.",
            "D) Valilik yabancı bir kurumdur.",
            "E) Valilik özel bir şirkettir."
          ],
          "correct": 1,
          "solution": "Doğru cevap Valilik, anayasal sistemin önemli bir parçasıdır..",
          "id": "e8_q116",
          "no": 116
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'Kaymakamlık' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-114)",
          "options": [
            "A) Kaymakamlık sadece köylerde bulunur.",
            "B) Kaymakamlık özel bir şirkettir.",
            "C) Kaymakamlık, anayasal sistemin önemli bir parçasıdır.",
            "D) Kaymakamlık yabancı bir kurumdur.",
            "E) Kaymakamlık yasaklanmıştır."
          ],
          "correct": 2,
          "solution": "Doğru cevap Kaymakamlık, anayasal sistemin önemli bir parçasıdır..",
          "id": "e8_q117",
          "no": 117
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'İl Genel Meclisi' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-115)",
          "options": [
            "A) İl Genel Meclisi yasaklanmıştır.",
            "B) İl Genel Meclisi, anayasal sistemin önemli bir parçasıdır.",
            "C) İl Genel Meclisi sadece köylerde bulunur.",
            "D) İl Genel Meclisi yabancı bir kurumdur.",
            "E) İl Genel Meclisi özel bir şirkettir."
          ],
          "correct": 1,
          "solution": "Doğru cevap İl Genel Meclisi, anayasal sistemin önemli bir parçasıdır..",
          "id": "e8_q118",
          "no": 118
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'Kamu Denetçiliği Kurumu' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-116)",
          "options": [
            "A) Kamu Denetçiliği Kurumu, anayasal sistemin önemli bir parçasıdır.",
            "B) Kamu Denetçiliği Kurumu yabancı bir kurumdur.",
            "C) Kamu Denetçiliği Kurumu özel bir şirkettir.",
            "D) Kamu Denetçiliği Kurumu sadece köylerde bulunur.",
            "E) Kamu Denetçiliği Kurumu yasaklanmıştır."
          ],
          "correct": 0,
          "solution": "Doğru cevap Kamu Denetçiliği Kurumu, anayasal sistemin önemli bir parçasıdır..",
          "id": "e8_q119",
          "no": 119
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'Anayasa Mahkemesi' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-117)",
          "options": [
            "A) Anayasa Mahkemesi, anayasal sistemin önemli bir parçasıdır.",
            "B) Anayasa Mahkemesi sadece köylerde bulunur.",
            "C) Anayasa Mahkemesi yasaklanmıştır.",
            "D) Anayasa Mahkemesi özel bir şirkettir.",
            "E) Anayasa Mahkemesi yabancı bir kurumdur."
          ],
          "correct": 0,
          "solution": "Doğru cevap Anayasa Mahkemesi, anayasal sistemin önemli bir parçasıdır..",
          "id": "e8_q120",
          "no": 120
        }
      ]
    },
    {
      "id": "deneme_9",
      "name": "9. Deneme Sınavı",
      "totalQuestions": 120,
      "duration": 130,
      "distribution": {
        "Türkçe": 30,
        "Matematik": 30,
        "Tarih": 27,
        "Coğrafya": 18,
        "Vatandaşlık": 15
      },
      "questions": [
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde 'hiçbir' kelimesinin yazımıyla ilgili bir kural hatırlatılmaktadır? (T-235)",
          "options": [
            "A) 'hiçbir' kelimesinin doğru yazımına dikkat edilmelidir.",
            "B) hiçbir kelimesi fiildir.",
            "C) hiçbir cümlede özne olamaz.",
            "D) hiçbir kelimesi her zaman ayrı yazılır.",
            "E) hiçbir kelimesi yabancı kökenlidir."
          ],
          "correct": 0,
          "solution": "Doğru cevap 'hiçbir' kelimesinin doğru yazımına dikkat edilmelidir..",
          "id": "e9_q1",
          "no": 1
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde mecaz anlamlı bir sözcük kullanılmıştır? (T-236)",
          "options": [
            "A) Suyu dolaptan soğuk içti.",
            "B) Olaylara karşı çok 'soğuk' davranıyordu.",
            "C) Buzdolabı soğuk üflüyor.",
            "D) Hava bugün çok soğuk.",
            "E) Kışın havalar soğuk olur."
          ],
          "correct": 1,
          "solution": "Doğru cevap Olaylara karşı çok 'soğuk' davranıyordu..",
          "id": "e9_q2",
          "no": 2
        },
        {
          "subject": "Türkçe",
          "text": "Bilim tarih boyunca insanlığın en büyük rehberlerinden biri olmuştur. Toplumlar Bilim sayesinde sınırlarını aşmış, geleceğe umutla bakabilmiştir. (P-237)\nBu parçanın ana düşüncesi nedir?",
          "options": [
            "A) Bilim sadece bireyseldir.",
            "B) İnsanlar Bilim ile ilgilenmemelidir.",
            "C) Bilim zaman kaybıdır.",
            "D) Bilim sadece geçmişte kalmıştır.",
            "E) Bilim, toplumsal ilerleme ve vizyon için vazgeçilmezdir."
          ],
          "correct": 4,
          "solution": "Doğru cevap Bilim, toplumsal ilerleme ve vizyon için vazgeçilmezdir..",
          "id": "e9_q3",
          "no": 3
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde 'her şey' kelimesinin yazımıyla ilgili bir kural hatırlatılmaktadır? (T-238)",
          "options": [
            "A) her şey kelimesi yabancı kökenlidir.",
            "B) her şey kelimesi her zaman ayrı yazılır.",
            "C) 'her şey' kelimesinin doğru yazımına dikkat edilmelidir.",
            "D) her şey kelimesi fiildir.",
            "E) her şey cümlede özne olamaz."
          ],
          "correct": 2,
          "solution": "Doğru cevap 'her şey' kelimesinin doğru yazımına dikkat edilmelidir..",
          "id": "e9_q4",
          "no": 4
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde mecaz anlamlı bir sözcük kullanılmıştır? (T-239)",
          "options": [
            "A) Olaylara karşı çok 'soğuk' davranıyordu.",
            "B) Suyu dolaptan soğuk içti.",
            "C) Buzdolabı soğuk üflüyor.",
            "D) Kışın havalar soğuk olur.",
            "E) Hava bugün çok soğuk."
          ],
          "correct": 0,
          "solution": "Doğru cevap Olaylara karşı çok 'soğuk' davranıyordu..",
          "id": "e9_q5",
          "no": 5
        },
        {
          "subject": "Türkçe",
          "text": "Sanat tarih boyunca insanlığın en büyük rehberlerinden biri olmuştur. Toplumlar Sanat sayesinde sınırlarını aşmış, geleceğe umutla bakabilmiştir. (P-240)\nBu parçanın ana düşüncesi nedir?",
          "options": [
            "A) Sanat sadece geçmişte kalmıştır.",
            "B) Sanat zaman kaybıdır.",
            "C) Sanat sadece bireyseldir.",
            "D) Sanat, toplumsal ilerleme ve vizyon için vazgeçilmezdir.",
            "E) İnsanlar Sanat ile ilgilenmemelidir."
          ],
          "correct": 3,
          "solution": "Doğru cevap Sanat, toplumsal ilerleme ve vizyon için vazgeçilmezdir..",
          "id": "e9_q6",
          "no": 6
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde 'yanlış' kelimesinin yazımıyla ilgili bir kural hatırlatılmaktadır? (T-241)",
          "options": [
            "A) yanlış kelimesi her zaman ayrı yazılır.",
            "B) yanlış cümlede özne olamaz.",
            "C) yanlış kelimesi fiildir.",
            "D) 'yanlış' kelimesinin doğru yazımına dikkat edilmelidir.",
            "E) yanlış kelimesi yabancı kökenlidir."
          ],
          "correct": 3,
          "solution": "Doğru cevap 'yanlış' kelimesinin doğru yazımına dikkat edilmelidir..",
          "id": "e9_q7",
          "no": 7
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde mecaz anlamlı bir sözcük kullanılmıştır? (T-242)",
          "options": [
            "A) Kışın havalar soğuk olur.",
            "B) Olaylara karşı çok 'soğuk' davranıyordu.",
            "C) Buzdolabı soğuk üflüyor.",
            "D) Hava bugün çok soğuk.",
            "E) Suyu dolaptan soğuk içti."
          ],
          "correct": 1,
          "solution": "Doğru cevap Olaylara karşı çok 'soğuk' davranıyordu..",
          "id": "e9_q8",
          "no": 8
        },
        {
          "subject": "Türkçe",
          "text": "Teknoloji tarih boyunca insanlığın en büyük rehberlerinden biri olmuştur. Toplumlar Teknoloji sayesinde sınırlarını aşmış, geleceğe umutla bakabilmiştir. (P-243)\nBu parçanın ana düşüncesi nedir?",
          "options": [
            "A) Teknoloji sadece bireyseldir.",
            "B) Teknoloji zaman kaybıdır.",
            "C) Teknoloji, toplumsal ilerleme ve vizyon için vazgeçilmezdir.",
            "D) Teknoloji sadece geçmişte kalmıştır.",
            "E) İnsanlar Teknoloji ile ilgilenmemelidir."
          ],
          "correct": 2,
          "solution": "Doğru cevap Teknoloji, toplumsal ilerleme ve vizyon için vazgeçilmezdir..",
          "id": "e9_q9",
          "no": 9
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde 'birkaç' kelimesinin yazımıyla ilgili bir kural hatırlatılmaktadır? (T-244)",
          "options": [
            "A) birkaç kelimesi fiildir.",
            "B) birkaç kelimesi yabancı kökenlidir.",
            "C) 'birkaç' kelimesinin doğru yazımına dikkat edilmelidir.",
            "D) birkaç cümlede özne olamaz.",
            "E) birkaç kelimesi her zaman ayrı yazılır."
          ],
          "correct": 2,
          "solution": "Doğru cevap 'birkaç' kelimesinin doğru yazımına dikkat edilmelidir..",
          "id": "e9_q10",
          "no": 10
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde mecaz anlamlı bir sözcük kullanılmıştır? (T-245)",
          "options": [
            "A) Olaylara karşı çok 'soğuk' davranıyordu.",
            "B) Kışın havalar soğuk olur.",
            "C) Hava bugün çok soğuk.",
            "D) Buzdolabı soğuk üflüyor.",
            "E) Suyu dolaptan soğuk içti."
          ],
          "correct": 0,
          "solution": "Doğru cevap Olaylara karşı çok 'soğuk' davranıyordu..",
          "id": "e9_q11",
          "no": 11
        },
        {
          "subject": "Türkçe",
          "text": "Doğa tarih boyunca insanlığın en büyük rehberlerinden biri olmuştur. Toplumlar Doğa sayesinde sınırlarını aşmış, geleceğe umutla bakabilmiştir. (P-246)\nBu parçanın ana düşüncesi nedir?",
          "options": [
            "A) Doğa zaman kaybıdır.",
            "B) Doğa sadece geçmişte kalmıştır.",
            "C) Doğa sadece bireyseldir.",
            "D) İnsanlar Doğa ile ilgilenmemelidir.",
            "E) Doğa, toplumsal ilerleme ve vizyon için vazgeçilmezdir."
          ],
          "correct": 4,
          "solution": "Doğru cevap Doğa, toplumsal ilerleme ve vizyon için vazgeçilmezdir..",
          "id": "e9_q12",
          "no": 12
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde 'hiç kimse' kelimesinin yazımıyla ilgili bir kural hatırlatılmaktadır? (T-247)",
          "options": [
            "A) hiç kimse cümlede özne olamaz.",
            "B) hiç kimse kelimesi fiildir.",
            "C) hiç kimse kelimesi her zaman ayrı yazılır.",
            "D) 'hiç kimse' kelimesinin doğru yazımına dikkat edilmelidir.",
            "E) hiç kimse kelimesi yabancı kökenlidir."
          ],
          "correct": 3,
          "solution": "Doğru cevap 'hiç kimse' kelimesinin doğru yazımına dikkat edilmelidir..",
          "id": "e9_q13",
          "no": 13
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde mecaz anlamlı bir sözcük kullanılmıştır? (T-248)",
          "options": [
            "A) Olaylara karşı çok 'soğuk' davranıyordu.",
            "B) Kışın havalar soğuk olur.",
            "C) Suyu dolaptan soğuk içti.",
            "D) Buzdolabı soğuk üflüyor.",
            "E) Hava bugün çok soğuk."
          ],
          "correct": 0,
          "solution": "Doğru cevap Olaylara karşı çok 'soğuk' davranıyordu..",
          "id": "e9_q14",
          "no": 14
        },
        {
          "subject": "Türkçe",
          "text": "Psikoloji tarih boyunca insanlığın en büyük rehberlerinden biri olmuştur. Toplumlar Psikoloji sayesinde sınırlarını aşmış, geleceğe umutla bakabilmiştir. (P-249)\nBu parçanın ana düşüncesi nedir?",
          "options": [
            "A) Psikoloji zaman kaybıdır.",
            "B) İnsanlar Psikoloji ile ilgilenmemelidir.",
            "C) Psikoloji sadece bireyseldir.",
            "D) Psikoloji sadece geçmişte kalmıştır.",
            "E) Psikoloji, toplumsal ilerleme ve vizyon için vazgeçilmezdir."
          ],
          "correct": 4,
          "solution": "Doğru cevap Psikoloji, toplumsal ilerleme ve vizyon için vazgeçilmezdir..",
          "id": "e9_q15",
          "no": 15
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde 'herkes' kelimesinin yazımıyla ilgili bir kural hatırlatılmaktadır? (T-250)",
          "options": [
            "A) herkes kelimesi fiildir.",
            "B) herkes kelimesi her zaman ayrı yazılır.",
            "C) herkes cümlede özne olamaz.",
            "D) herkes kelimesi yabancı kökenlidir.",
            "E) 'herkes' kelimesinin doğru yazımına dikkat edilmelidir."
          ],
          "correct": 4,
          "solution": "Doğru cevap 'herkes' kelimesinin doğru yazımına dikkat edilmelidir..",
          "id": "e9_q16",
          "no": 16
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde mecaz anlamlı bir sözcük kullanılmıştır? (T-251)",
          "options": [
            "A) Kışın havalar soğuk olur.",
            "B) Suyu dolaptan soğuk içti.",
            "C) Hava bugün çok soğuk.",
            "D) Olaylara karşı çok 'soğuk' davranıyordu.",
            "E) Buzdolabı soğuk üflüyor."
          ],
          "correct": 3,
          "solution": "Doğru cevap Olaylara karşı çok 'soğuk' davranıyordu..",
          "id": "e9_q17",
          "no": 17
        },
        {
          "subject": "Türkçe",
          "text": "Eğitim tarih boyunca insanlığın en büyük rehberlerinden biri olmuştur. Toplumlar Eğitim sayesinde sınırlarını aşmış, geleceğe umutla bakabilmiştir. (P-252)\nBu parçanın ana düşüncesi nedir?",
          "options": [
            "A) Eğitim sadece bireyseldir.",
            "B) Eğitim sadece geçmişte kalmıştır.",
            "C) İnsanlar Eğitim ile ilgilenmemelidir.",
            "D) Eğitim zaman kaybıdır.",
            "E) Eğitim, toplumsal ilerleme ve vizyon için vazgeçilmezdir."
          ],
          "correct": 4,
          "solution": "Doğru cevap Eğitim, toplumsal ilerleme ve vizyon için vazgeçilmezdir..",
          "id": "e9_q18",
          "no": 18
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde 'bugün' kelimesinin yazımıyla ilgili bir kural hatırlatılmaktadır? (T-253)",
          "options": [
            "A) bugün cümlede özne olamaz.",
            "B) bugün kelimesi her zaman ayrı yazılır.",
            "C) bugün kelimesi yabancı kökenlidir.",
            "D) 'bugün' kelimesinin doğru yazımına dikkat edilmelidir.",
            "E) bugün kelimesi fiildir."
          ],
          "correct": 3,
          "solution": "Doğru cevap 'bugün' kelimesinin doğru yazımına dikkat edilmelidir..",
          "id": "e9_q19",
          "no": 19
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde mecaz anlamlı bir sözcük kullanılmıştır? (T-254)",
          "options": [
            "A) Buzdolabı soğuk üflüyor.",
            "B) Olaylara karşı çok 'soğuk' davranıyordu.",
            "C) Suyu dolaptan soğuk içti.",
            "D) Kışın havalar soğuk olur.",
            "E) Hava bugün çok soğuk."
          ],
          "correct": 1,
          "solution": "Doğru cevap Olaylara karşı çok 'soğuk' davranıyordu..",
          "id": "e9_q20",
          "no": 20
        },
        {
          "subject": "Türkçe",
          "text": "Kültür tarih boyunca insanlığın en büyük rehberlerinden biri olmuştur. Toplumlar Kültür sayesinde sınırlarını aşmış, geleceğe umutla bakabilmiştir. (P-255)\nBu parçanın ana düşüncesi nedir?",
          "options": [
            "A) Kültür, toplumsal ilerleme ve vizyon için vazgeçilmezdir.",
            "B) Kültür sadece bireyseldir.",
            "C) İnsanlar Kültür ile ilgilenmemelidir.",
            "D) Kültür zaman kaybıdır.",
            "E) Kültür sadece geçmişte kalmıştır."
          ],
          "correct": 0,
          "solution": "Doğru cevap Kültür, toplumsal ilerleme ve vizyon için vazgeçilmezdir..",
          "id": "e9_q21",
          "no": 21
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde 'yalnız' kelimesinin yazımıyla ilgili bir kural hatırlatılmaktadır? (T-256)",
          "options": [
            "A) yalnız cümlede özne olamaz.",
            "B) yalnız kelimesi her zaman ayrı yazılır.",
            "C) yalnız kelimesi fiildir.",
            "D) yalnız kelimesi yabancı kökenlidir.",
            "E) 'yalnız' kelimesinin doğru yazımına dikkat edilmelidir."
          ],
          "correct": 4,
          "solution": "Doğru cevap 'yalnız' kelimesinin doğru yazımına dikkat edilmelidir..",
          "id": "e9_q22",
          "no": 22
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde mecaz anlamlı bir sözcük kullanılmıştır? (T-257)",
          "options": [
            "A) Suyu dolaptan soğuk içti.",
            "B) Kışın havalar soğuk olur.",
            "C) Buzdolabı soğuk üflüyor.",
            "D) Olaylara karşı çok 'soğuk' davranıyordu.",
            "E) Hava bugün çok soğuk."
          ],
          "correct": 3,
          "solution": "Doğru cevap Olaylara karşı çok 'soğuk' davranıyordu..",
          "id": "e9_q23",
          "no": 23
        },
        {
          "subject": "Türkçe",
          "text": "Felsefe tarih boyunca insanlığın en büyük rehberlerinden biri olmuştur. Toplumlar Felsefe sayesinde sınırlarını aşmış, geleceğe umutla bakabilmiştir. (P-258)\nBu parçanın ana düşüncesi nedir?",
          "options": [
            "A) Felsefe zaman kaybıdır.",
            "B) Felsefe, toplumsal ilerleme ve vizyon için vazgeçilmezdir.",
            "C) Felsefe sadece geçmişte kalmıştır.",
            "D) İnsanlar Felsefe ile ilgilenmemelidir.",
            "E) Felsefe sadece bireyseldir."
          ],
          "correct": 1,
          "solution": "Doğru cevap Felsefe, toplumsal ilerleme ve vizyon için vazgeçilmezdir..",
          "id": "e9_q24",
          "no": 24
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde 'hiçbir' kelimesinin yazımıyla ilgili bir kural hatırlatılmaktadır? (T-259)",
          "options": [
            "A) hiçbir kelimesi her zaman ayrı yazılır.",
            "B) hiçbir kelimesi yabancı kökenlidir.",
            "C) 'hiçbir' kelimesinin doğru yazımına dikkat edilmelidir.",
            "D) hiçbir cümlede özne olamaz.",
            "E) hiçbir kelimesi fiildir."
          ],
          "correct": 2,
          "solution": "Doğru cevap 'hiçbir' kelimesinin doğru yazımına dikkat edilmelidir..",
          "id": "e9_q25",
          "no": 25
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde mecaz anlamlı bir sözcük kullanılmıştır? (T-260)",
          "options": [
            "A) Hava bugün çok soğuk.",
            "B) Kışın havalar soğuk olur.",
            "C) Olaylara karşı çok 'soğuk' davranıyordu.",
            "D) Buzdolabı soğuk üflüyor.",
            "E) Suyu dolaptan soğuk içti."
          ],
          "correct": 2,
          "solution": "Doğru cevap Olaylara karşı çok 'soğuk' davranıyordu..",
          "id": "e9_q26",
          "no": 26
        },
        {
          "subject": "Türkçe",
          "text": "Edebiyat tarih boyunca insanlığın en büyük rehberlerinden biri olmuştur. Toplumlar Edebiyat sayesinde sınırlarını aşmış, geleceğe umutla bakabilmiştir. (P-261)\nBu parçanın ana düşüncesi nedir?",
          "options": [
            "A) Edebiyat, toplumsal ilerleme ve vizyon için vazgeçilmezdir.",
            "B) Edebiyat sadece bireyseldir.",
            "C) İnsanlar Edebiyat ile ilgilenmemelidir.",
            "D) Edebiyat sadece geçmişte kalmıştır.",
            "E) Edebiyat zaman kaybıdır."
          ],
          "correct": 0,
          "solution": "Doğru cevap Edebiyat, toplumsal ilerleme ve vizyon için vazgeçilmezdir..",
          "id": "e9_q27",
          "no": 27
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde 'her şey' kelimesinin yazımıyla ilgili bir kural hatırlatılmaktadır? (T-262)",
          "options": [
            "A) her şey kelimesi fiildir.",
            "B) her şey cümlede özne olamaz.",
            "C) her şey kelimesi yabancı kökenlidir.",
            "D) her şey kelimesi her zaman ayrı yazılır.",
            "E) 'her şey' kelimesinin doğru yazımına dikkat edilmelidir."
          ],
          "correct": 4,
          "solution": "Doğru cevap 'her şey' kelimesinin doğru yazımına dikkat edilmelidir..",
          "id": "e9_q28",
          "no": 28
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde mecaz anlamlı bir sözcük kullanılmıştır? (T-263)",
          "options": [
            "A) Hava bugün çok soğuk.",
            "B) Kışın havalar soğuk olur.",
            "C) Buzdolabı soğuk üflüyor.",
            "D) Olaylara karşı çok 'soğuk' davranıyordu.",
            "E) Suyu dolaptan soğuk içti."
          ],
          "correct": 3,
          "solution": "Doğru cevap Olaylara karşı çok 'soğuk' davranıyordu..",
          "id": "e9_q29",
          "no": 29
        },
        {
          "subject": "Türkçe",
          "text": "Tarih tarih boyunca insanlığın en büyük rehberlerinden biri olmuştur. Toplumlar Tarih sayesinde sınırlarını aşmış, geleceğe umutla bakabilmiştir. (P-264)\nBu parçanın ana düşüncesi nedir?",
          "options": [
            "A) İnsanlar Tarih ile ilgilenmemelidir.",
            "B) Tarih zaman kaybıdır.",
            "C) Tarih sadece geçmişte kalmıştır.",
            "D) Tarih sadece bireyseldir.",
            "E) Tarih, toplumsal ilerleme ve vizyon için vazgeçilmezdir."
          ],
          "correct": 4,
          "solution": "Doğru cevap Tarih, toplumsal ilerleme ve vizyon için vazgeçilmezdir..",
          "id": "e9_q30",
          "no": 30
        },
        {
          "subject": "Matematik",
          "text": "9x + 32 = 50 denkleminde x kaçtır? (SoruID: M240)",
          "options": [
            "A) 5",
            "B) 1",
            "C) 3",
            "D) 2",
            "E) 4"
          ],
          "correct": 3,
          "solution": "Doğru cevap 2.",
          "id": "e9_q31",
          "no": 31
        },
        {
          "subject": "Matematik",
          "text": "90 sayısının %30'si kaçtır? (SoruID: M241)",
          "options": [
            "A) 22",
            "B) 37",
            "C) 32",
            "D) 42",
            "E) 27"
          ],
          "correct": 4,
          "solution": "Doğru cevap 27.",
          "id": "e9_q32",
          "no": 32
        },
        {
          "subject": "Matematik",
          "text": "24, 11 ve 28 sayılarının aritmetik ortalaması kaçtır? (SoruID: M242)",
          "options": [
            "A) 19",
            "B) 23",
            "C) 20",
            "D) 22",
            "E) 21"
          ],
          "correct": 4,
          "solution": "Doğru cevap 21.",
          "id": "e9_q33",
          "no": 33
        },
        {
          "subject": "Matematik",
          "text": "Ali 25, Ayşe 10 yaşındadır. 8 yıl sonra yaşları toplamı kaç olur? (SoruID: M243)",
          "options": [
            "A) 50",
            "B) 51",
            "C) 43",
            "D) 59",
            "E) 52"
          ],
          "correct": 1,
          "solution": "Doğru cevap 51.",
          "id": "e9_q34",
          "no": 34
        },
        {
          "subject": "Matematik",
          "text": "√25 + √9 işleminin sonucu kaçtır? (SoruID: M244)",
          "options": [
            "A) 7",
            "B) 8",
            "C) 10",
            "D) 6",
            "E) 9"
          ],
          "correct": 1,
          "solution": "Doğru cevap 8.",
          "id": "e9_q35",
          "no": 35
        },
        {
          "subject": "Matematik",
          "text": "4x + 48 = 80 denkleminde x kaçtır? (SoruID: M245)",
          "options": [
            "A) 7",
            "B) 9",
            "C) 11",
            "D) 10",
            "E) 8"
          ],
          "correct": 4,
          "solution": "Doğru cevap 8.",
          "id": "e9_q36",
          "no": 36
        },
        {
          "subject": "Matematik",
          "text": "70 sayısının %25'si kaçtır? (SoruID: M246)",
          "options": [
            "A) 22",
            "B) 12",
            "C) 27",
            "D) 17",
            "E) 32"
          ],
          "correct": 3,
          "solution": "Doğru cevap 17.",
          "id": "e9_q37",
          "no": 37
        },
        {
          "subject": "Matematik",
          "text": "10, 22 ve 25 sayılarının aritmetik ortalaması kaçtır? (SoruID: M247)",
          "options": [
            "A) 19",
            "B) 21",
            "C) 20",
            "D) 17",
            "E) 18"
          ],
          "correct": 0,
          "solution": "Doğru cevap 19.",
          "id": "e9_q38",
          "no": 38
        },
        {
          "subject": "Matematik",
          "text": "Ali 11, Ayşe 23 yaşındadır. 9 yıl sonra yaşları toplamı kaç olur? (SoruID: M248)",
          "options": [
            "A) 53",
            "B) 51",
            "C) 52",
            "D) 43",
            "E) 61"
          ],
          "correct": 2,
          "solution": "Doğru cevap 52.",
          "id": "e9_q39",
          "no": 39
        },
        {
          "subject": "Matematik",
          "text": "√81 + √64 işleminin sonucu kaçtır? (SoruID: M249)",
          "options": [
            "A) 17",
            "B) 16",
            "C) 19",
            "D) 18",
            "E) 15"
          ],
          "correct": 0,
          "solution": "Doğru cevap 17.",
          "id": "e9_q40",
          "no": 40
        },
        {
          "subject": "Matematik",
          "text": "5x + 40 = 65 denkleminde x kaçtır? (SoruID: M250)",
          "options": [
            "A) 4",
            "B) 8",
            "C) 7",
            "D) 6",
            "E) 5"
          ],
          "correct": 4,
          "solution": "Doğru cevap 5.",
          "id": "e9_q41",
          "no": 41
        },
        {
          "subject": "Matematik",
          "text": "180 sayısının %25'si kaçtır? (SoruID: M251)",
          "options": [
            "A) 60",
            "B) 55",
            "C) 45",
            "D) 40",
            "E) 50"
          ],
          "correct": 2,
          "solution": "Doğru cevap 45.",
          "id": "e9_q42",
          "no": 42
        },
        {
          "subject": "Matematik",
          "text": "22, 14 ve 27 sayılarının aritmetik ortalaması kaçtır? (SoruID: M252)",
          "options": [
            "A) 19",
            "B) 23",
            "C) 20",
            "D) 21",
            "E) 22"
          ],
          "correct": 3,
          "solution": "Doğru cevap 21.",
          "id": "e9_q43",
          "no": 43
        },
        {
          "subject": "Matematik",
          "text": "Ali 10, Ayşe 14 yaşındadır. 7 yıl sonra yaşları toplamı kaç olur? (SoruID: M253)",
          "options": [
            "A) 31",
            "B) 39",
            "C) 38",
            "D) 37",
            "E) 45"
          ],
          "correct": 2,
          "solution": "Doğru cevap 38.",
          "id": "e9_q44",
          "no": 44
        },
        {
          "subject": "Matematik",
          "text": "√16 + √64 işleminin sonucu kaçtır? (SoruID: M254)",
          "options": [
            "A) 11",
            "B) 12",
            "C) 14",
            "D) 10",
            "E) 13"
          ],
          "correct": 1,
          "solution": "Doğru cevap 12.",
          "id": "e9_q45",
          "no": 45
        },
        {
          "subject": "Matematik",
          "text": "7x + 29 = 36 denkleminde x kaçtır? (SoruID: M255)",
          "options": [
            "A) 3",
            "B) 2",
            "C) 0",
            "D) 4",
            "E) 1"
          ],
          "correct": 4,
          "solution": "Doğru cevap 1.",
          "id": "e9_q46",
          "no": 46
        },
        {
          "subject": "Matematik",
          "text": "40 sayısının %40'si kaçtır? (SoruID: M256)",
          "options": [
            "A) 21",
            "B) 26",
            "C) 31",
            "D) 11",
            "E) 16"
          ],
          "correct": 4,
          "solution": "Doğru cevap 16.",
          "id": "e9_q47",
          "no": 47
        },
        {
          "subject": "Matematik",
          "text": "27, 11 ve 13 sayılarının aritmetik ortalaması kaçtır? (SoruID: M257)",
          "options": [
            "A) 19",
            "B) 17",
            "C) 16",
            "D) 15",
            "E) 18"
          ],
          "correct": 1,
          "solution": "Doğru cevap 17.",
          "id": "e9_q48",
          "no": 48
        },
        {
          "subject": "Matematik",
          "text": "Ali 20, Ayşe 15 yaşındadır. 9 yıl sonra yaşları toplamı kaç olur? (SoruID: M258)",
          "options": [
            "A) 53",
            "B) 62",
            "C) 54",
            "D) 44",
            "E) 52"
          ],
          "correct": 0,
          "solution": "Doğru cevap 53.",
          "id": "e9_q49",
          "no": 49
        },
        {
          "subject": "Matematik",
          "text": "√25 + √81 işleminin sonucu kaçtır? (SoruID: M259)",
          "options": [
            "A) 14",
            "B) 13",
            "C) 16",
            "D) 15",
            "E) 12"
          ],
          "correct": 0,
          "solution": "Doğru cevap 14.",
          "id": "e9_q50",
          "no": 50
        },
        {
          "subject": "Matematik",
          "text": "2x + 37 = 59 denkleminde x kaçtır? (SoruID: M260)",
          "options": [
            "A) 13",
            "B) 14",
            "C) 10",
            "D) 11",
            "E) 12"
          ],
          "correct": 3,
          "solution": "Doğru cevap 11.",
          "id": "e9_q51",
          "no": 51
        },
        {
          "subject": "Matematik",
          "text": "70 sayısının %25'si kaçtır? (SoruID: M261)",
          "options": [
            "A) 32",
            "B) 22",
            "C) 12",
            "D) 27",
            "E) 17"
          ],
          "correct": 4,
          "solution": "Doğru cevap 17.",
          "id": "e9_q52",
          "no": 52
        },
        {
          "subject": "Matematik",
          "text": "22, 11 ve 24 sayılarının aritmetik ortalaması kaçtır? (SoruID: M262)",
          "options": [
            "A) 20",
            "B) 18",
            "C) 21",
            "D) 17",
            "E) 19"
          ],
          "correct": 4,
          "solution": "Doğru cevap 19.",
          "id": "e9_q53",
          "no": 53
        },
        {
          "subject": "Matematik",
          "text": "Ali 16, Ayşe 22 yaşındadır. 9 yıl sonra yaşları toplamı kaç olur? (SoruID: M263)",
          "options": [
            "A) 57",
            "B) 65",
            "C) 56",
            "D) 47",
            "E) 55"
          ],
          "correct": 2,
          "solution": "Doğru cevap 56.",
          "id": "e9_q54",
          "no": 54
        },
        {
          "subject": "Matematik",
          "text": "√25 + √16 işleminin sonucu kaçtır? (SoruID: M264)",
          "options": [
            "A) 9",
            "B) 7",
            "C) 10",
            "D) 8",
            "E) 11"
          ],
          "correct": 0,
          "solution": "Doğru cevap 9.",
          "id": "e9_q55",
          "no": 55
        },
        {
          "subject": "Matematik",
          "text": "7x + 9 = 16 denkleminde x kaçtır? (SoruID: M265)",
          "options": [
            "A) 4",
            "B) 3",
            "C) 1",
            "D) 0",
            "E) 2"
          ],
          "correct": 2,
          "solution": "Doğru cevap 1.",
          "id": "e9_q56",
          "no": 56
        },
        {
          "subject": "Matematik",
          "text": "50 sayısının %60'si kaçtır? (SoruID: M266)",
          "options": [
            "A) 25",
            "B) 45",
            "C) 30",
            "D) 35",
            "E) 40"
          ],
          "correct": 2,
          "solution": "Doğru cevap 30.",
          "id": "e9_q57",
          "no": 57
        },
        {
          "subject": "Matematik",
          "text": "12, 30 ve 15 sayılarının aritmetik ortalaması kaçtır? (SoruID: M267)",
          "options": [
            "A) 17",
            "B) 21",
            "C) 19",
            "D) 18",
            "E) 20"
          ],
          "correct": 2,
          "solution": "Doğru cevap 19.",
          "id": "e9_q58",
          "no": 58
        },
        {
          "subject": "Matematik",
          "text": "Ali 21, Ayşe 12 yaşındadır. 9 yıl sonra yaşları toplamı kaç olur? (SoruID: M268)",
          "options": [
            "A) 52",
            "B) 60",
            "C) 51",
            "D) 50",
            "E) 42"
          ],
          "correct": 2,
          "solution": "Doğru cevap 51.",
          "id": "e9_q59",
          "no": 59
        },
        {
          "subject": "Matematik",
          "text": "√4 + √9 işleminin sonucu kaçtır? (SoruID: M269)",
          "options": [
            "A) 6",
            "B) 7",
            "C) 5",
            "D) 3",
            "E) 4"
          ],
          "correct": 2,
          "solution": "Doğru cevap 5.",
          "id": "e9_q60",
          "no": 60
        },
        {
          "subject": "Tarih",
          "text": "Türk siyasi ve askerî tarihinde büyük öneme sahip olan 'Çanakkale Cephesi' süreci ile ilgili aşağıdakilerden hangisi söylenebilir? (H-213)",
          "options": [
            "A) Osmanlı'nın kuruluş dönemine aittir.",
            "B) Çanakkale Cephesi dönemin en kritik gelişmelerinden biridir.",
            "C) Sadece ekonomik bir olaydır.",
            "D) Avrupa'da gerçekleşmiştir.",
            "E) Hiçbir etkisi olmamıştır."
          ],
          "correct": 1,
          "solution": "Doğru cevap Çanakkale Cephesi dönemin en kritik gelişmelerinden biridir..",
          "id": "e9_q61",
          "no": 61
        },
        {
          "subject": "Tarih",
          "text": "Aşağıdaki tarihî gelişmelerden hangisi 'Sakarya Meydan Muharebesi' ile doğrudan veya dolaylı olarak bağlantılıdır? (H-214)",
          "options": [
            "A) Kavimler Göçü",
            "B) Sanayi İnkılabı",
            "C) Coğrafi Keşifler",
            "D) Sakarya Meydan Muharebesi öncesi ve sonrası yaşanan siyasi krizler.",
            "E) Fransız İhtilali"
          ],
          "correct": 3,
          "solution": "Doğru cevap Sakarya Meydan Muharebesi öncesi ve sonrası yaşanan siyasi krizler..",
          "id": "e9_q62",
          "no": 62
        },
        {
          "subject": "Tarih",
          "text": "Millî Mücadele ve inkılaplar tarihi incelendiğinde 'Büyük Taarruz' olayının temel amacı aşağıdakilerden hangisidir? (H-215)",
          "options": [
            "A) Feodaliteyi kurmak",
            "B) Yeni sömürgeler elde etmek",
            "C) Bağımsızlık ve egemenliği pekiştirmek",
            "D) Avrupa'ya göç etmek",
            "E) Saltanatı güçlendirmek"
          ],
          "correct": 2,
          "solution": "Doğru cevap Bağımsızlık ve egemenliği pekiştirmek.",
          "id": "e9_q63",
          "no": 63
        },
        {
          "subject": "Tarih",
          "text": "Türk siyasi ve askerî tarihinde büyük öneme sahip olan 'I. İnönü Muharebesi' süreci ile ilgili aşağıdakilerden hangisi söylenebilir? (H-216)",
          "options": [
            "A) Sadece ekonomik bir olaydır.",
            "B) Hiçbir etkisi olmamıştır.",
            "C) Osmanlı'nın kuruluş dönemine aittir.",
            "D) I. İnönü Muharebesi dönemin en kritik gelişmelerinden biridir.",
            "E) Avrupa'da gerçekleşmiştir."
          ],
          "correct": 3,
          "solution": "Doğru cevap I. İnönü Muharebesi dönemin en kritik gelişmelerinden biridir..",
          "id": "e9_q64",
          "no": 64
        },
        {
          "subject": "Tarih",
          "text": "Aşağıdaki tarihî gelişmelerden hangisi 'II. İnönü Muharebesi' ile doğrudan veya dolaylı olarak bağlantılıdır? (H-217)",
          "options": [
            "A) Coğrafi Keşifler",
            "B) Kavimler Göçü",
            "C) II. İnönü Muharebesi öncesi ve sonrası yaşanan siyasi krizler.",
            "D) Fransız İhtilali",
            "E) Sanayi İnkılabı"
          ],
          "correct": 2,
          "solution": "Doğru cevap II. İnönü Muharebesi öncesi ve sonrası yaşanan siyasi krizler..",
          "id": "e9_q65",
          "no": 65
        },
        {
          "subject": "Tarih",
          "text": "Millî Mücadele ve inkılaplar tarihi incelendiğinde 'Kars Antlaşması' olayının temel amacı aşağıdakilerden hangisidir? (H-218)",
          "options": [
            "A) Yeni sömürgeler elde etmek",
            "B) Bağımsızlık ve egemenliği pekiştirmek",
            "C) Saltanatı güçlendirmek",
            "D) Avrupa'ya göç etmek",
            "E) Feodaliteyi kurmak"
          ],
          "correct": 1,
          "solution": "Doğru cevap Bağımsızlık ve egemenliği pekiştirmek.",
          "id": "e9_q66",
          "no": 66
        },
        {
          "subject": "Tarih",
          "text": "Türk siyasi ve askerî tarihinde büyük öneme sahip olan 'Ankara Antlaşması' süreci ile ilgili aşağıdakilerden hangisi söylenebilir? (H-219)",
          "options": [
            "A) Hiçbir etkisi olmamıştır.",
            "B) Ankara Antlaşması dönemin en kritik gelişmelerinden biridir.",
            "C) Osmanlı'nın kuruluş dönemine aittir.",
            "D) Sadece ekonomik bir olaydır.",
            "E) Avrupa'da gerçekleşmiştir."
          ],
          "correct": 1,
          "solution": "Doğru cevap Ankara Antlaşması dönemin en kritik gelişmelerinden biridir..",
          "id": "e9_q67",
          "no": 67
        },
        {
          "subject": "Tarih",
          "text": "Aşağıdaki tarihî gelişmelerden hangisi 'Sivas Kongresi' ile doğrudan veya dolaylı olarak bağlantılıdır? (H-220)",
          "options": [
            "A) Fransız İhtilali",
            "B) Sivas Kongresi öncesi ve sonrası yaşanan siyasi krizler.",
            "C) Coğrafi Keşifler",
            "D) Kavimler Göçü",
            "E) Sanayi İnkılabı"
          ],
          "correct": 1,
          "solution": "Doğru cevap Sivas Kongresi öncesi ve sonrası yaşanan siyasi krizler..",
          "id": "e9_q68",
          "no": 68
        },
        {
          "subject": "Tarih",
          "text": "Millî Mücadele ve inkılaplar tarihi incelendiğinde 'Erzurum Kongresi' olayının temel amacı aşağıdakilerden hangisidir? (H-221)",
          "options": [
            "A) Yeni sömürgeler elde etmek",
            "B) Feodaliteyi kurmak",
            "C) Saltanatı güçlendirmek",
            "D) Avrupa'ya göç etmek",
            "E) Bağımsızlık ve egemenliği pekiştirmek"
          ],
          "correct": 4,
          "solution": "Doğru cevap Bağımsızlık ve egemenliği pekiştirmek.",
          "id": "e9_q69",
          "no": 69
        },
        {
          "subject": "Tarih",
          "text": "Türk siyasi ve askerî tarihinde büyük öneme sahip olan 'Amasya Genelgesi' süreci ile ilgili aşağıdakilerden hangisi söylenebilir? (H-222)",
          "options": [
            "A) Amasya Genelgesi dönemin en kritik gelişmelerinden biridir.",
            "B) Osmanlı'nın kuruluş dönemine aittir.",
            "C) Sadece ekonomik bir olaydır.",
            "D) Hiçbir etkisi olmamıştır.",
            "E) Avrupa'da gerçekleşmiştir."
          ],
          "correct": 0,
          "solution": "Doğru cevap Amasya Genelgesi dönemin en kritik gelişmelerinden biridir..",
          "id": "e9_q70",
          "no": 70
        },
        {
          "subject": "Tarih",
          "text": "Aşağıdaki tarihî gelişmelerden hangisi 'Lozan Antlaşması' ile doğrudan veya dolaylı olarak bağlantılıdır? (H-223)",
          "options": [
            "A) Lozan Antlaşması öncesi ve sonrası yaşanan siyasi krizler.",
            "B) Sanayi İnkılabı",
            "C) Coğrafi Keşifler",
            "D) Kavimler Göçü",
            "E) Fransız İhtilali"
          ],
          "correct": 0,
          "solution": "Doğru cevap Lozan Antlaşması öncesi ve sonrası yaşanan siyasi krizler..",
          "id": "e9_q71",
          "no": 71
        },
        {
          "subject": "Tarih",
          "text": "Millî Mücadele ve inkılaplar tarihi incelendiğinde 'Cumhuriyetin İlanı' olayının temel amacı aşağıdakilerden hangisidir? (H-224)",
          "options": [
            "A) Avrupa'ya göç etmek",
            "B) Feodaliteyi kurmak",
            "C) Bağımsızlık ve egemenliği pekiştirmek",
            "D) Yeni sömürgeler elde etmek",
            "E) Saltanatı güçlendirmek"
          ],
          "correct": 2,
          "solution": "Doğru cevap Bağımsızlık ve egemenliği pekiştirmek.",
          "id": "e9_q72",
          "no": 72
        },
        {
          "subject": "Tarih",
          "text": "Türk siyasi ve askerî tarihinde büyük öneme sahip olan 'TBMM'nin Açılışı' süreci ile ilgili aşağıdakilerden hangisi söylenebilir? (H-225)",
          "options": [
            "A) Avrupa'da gerçekleşmiştir.",
            "B) Sadece ekonomik bir olaydır.",
            "C) Hiçbir etkisi olmamıştır.",
            "D) TBMM'nin Açılışı dönemin en kritik gelişmelerinden biridir.",
            "E) Osmanlı'nın kuruluş dönemine aittir."
          ],
          "correct": 3,
          "solution": "Doğru cevap TBMM'nin Açılışı dönemin en kritik gelişmelerinden biridir..",
          "id": "e9_q73",
          "no": 73
        },
        {
          "subject": "Tarih",
          "text": "Aşağıdaki tarihî gelişmelerden hangisi 'Mudanya Mütarekesi' ile doğrudan veya dolaylı olarak bağlantılıdır? (H-226)",
          "options": [
            "A) Sanayi İnkılabı",
            "B) Coğrafi Keşifler",
            "C) Mudanya Mütarekesi öncesi ve sonrası yaşanan siyasi krizler.",
            "D) Fransız İhtilali",
            "E) Kavimler Göçü"
          ],
          "correct": 2,
          "solution": "Doğru cevap Mudanya Mütarekesi öncesi ve sonrası yaşanan siyasi krizler..",
          "id": "e9_q74",
          "no": 74
        },
        {
          "subject": "Tarih",
          "text": "Millî Mücadele ve inkılaplar tarihi incelendiğinde 'Saltanatın Kaldırılması' olayının temel amacı aşağıdakilerden hangisidir? (H-227)",
          "options": [
            "A) Saltanatı güçlendirmek",
            "B) Feodaliteyi kurmak",
            "C) Yeni sömürgeler elde etmek",
            "D) Bağımsızlık ve egemenliği pekiştirmek",
            "E) Avrupa'ya göç etmek"
          ],
          "correct": 3,
          "solution": "Doğru cevap Bağımsızlık ve egemenliği pekiştirmek.",
          "id": "e9_q75",
          "no": 75
        },
        {
          "subject": "Tarih",
          "text": "Türk siyasi ve askerî tarihinde büyük öneme sahip olan 'Halifeliğin Kaldırılması' süreci ile ilgili aşağıdakilerden hangisi söylenebilir? (H-228)",
          "options": [
            "A) Avrupa'da gerçekleşmiştir.",
            "B) Halifeliğin Kaldırılması dönemin en kritik gelişmelerinden biridir.",
            "C) Hiçbir etkisi olmamıştır.",
            "D) Sadece ekonomik bir olaydır.",
            "E) Osmanlı'nın kuruluş dönemine aittir."
          ],
          "correct": 1,
          "solution": "Doğru cevap Halifeliğin Kaldırılması dönemin en kritik gelişmelerinden biridir..",
          "id": "e9_q76",
          "no": 76
        },
        {
          "subject": "Tarih",
          "text": "Aşağıdaki tarihî gelişmelerden hangisi 'Tevhid-i Tedrisat' ile doğrudan veya dolaylı olarak bağlantılıdır? (H-229)",
          "options": [
            "A) Fransız İhtilali",
            "B) Coğrafi Keşifler",
            "C) Tevhid-i Tedrisat öncesi ve sonrası yaşanan siyasi krizler.",
            "D) Kavimler Göçü",
            "E) Sanayi İnkılabı"
          ],
          "correct": 2,
          "solution": "Doğru cevap Tevhid-i Tedrisat öncesi ve sonrası yaşanan siyasi krizler..",
          "id": "e9_q77",
          "no": 77
        },
        {
          "subject": "Tarih",
          "text": "Millî Mücadele ve inkılaplar tarihi incelendiğinde 'Trablusgarp Savaşı' olayının temel amacı aşağıdakilerden hangisidir? (H-230)",
          "options": [
            "A) Bağımsızlık ve egemenliği pekiştirmek",
            "B) Avrupa'ya göç etmek",
            "C) Saltanatı güçlendirmek",
            "D) Yeni sömürgeler elde etmek",
            "E) Feodaliteyi kurmak"
          ],
          "correct": 0,
          "solution": "Doğru cevap Bağımsızlık ve egemenliği pekiştirmek.",
          "id": "e9_q78",
          "no": 78
        },
        {
          "subject": "Tarih",
          "text": "Türk siyasi ve askerî tarihinde büyük öneme sahip olan 'Balkan Savaşları' süreci ile ilgili aşağıdakilerden hangisi söylenebilir? (H-231)",
          "options": [
            "A) Hiçbir etkisi olmamıştır.",
            "B) Sadece ekonomik bir olaydır.",
            "C) Osmanlı'nın kuruluş dönemine aittir.",
            "D) Balkan Savaşları dönemin en kritik gelişmelerinden biridir.",
            "E) Avrupa'da gerçekleşmiştir."
          ],
          "correct": 3,
          "solution": "Doğru cevap Balkan Savaşları dönemin en kritik gelişmelerinden biridir..",
          "id": "e9_q79",
          "no": 79
        },
        {
          "subject": "Tarih",
          "text": "Aşağıdaki tarihî gelişmelerden hangisi 'I. Dünya Savaşı' ile doğrudan veya dolaylı olarak bağlantılıdır? (H-232)",
          "options": [
            "A) Fransız İhtilali",
            "B) Coğrafi Keşifler",
            "C) Sanayi İnkılabı",
            "D) I. Dünya Savaşı öncesi ve sonrası yaşanan siyasi krizler.",
            "E) Kavimler Göçü"
          ],
          "correct": 3,
          "solution": "Doğru cevap I. Dünya Savaşı öncesi ve sonrası yaşanan siyasi krizler..",
          "id": "e9_q80",
          "no": 80
        },
        {
          "subject": "Tarih",
          "text": "Millî Mücadele ve inkılaplar tarihi incelendiğinde 'Çanakkale Cephesi' olayının temel amacı aşağıdakilerden hangisidir? (H-233)",
          "options": [
            "A) Yeni sömürgeler elde etmek",
            "B) Saltanatı güçlendirmek",
            "C) Avrupa'ya göç etmek",
            "D) Bağımsızlık ve egemenliği pekiştirmek",
            "E) Feodaliteyi kurmak"
          ],
          "correct": 3,
          "solution": "Doğru cevap Bağımsızlık ve egemenliği pekiştirmek.",
          "id": "e9_q81",
          "no": 81
        },
        {
          "subject": "Tarih",
          "text": "Türk siyasi ve askerî tarihinde büyük öneme sahip olan 'Sakarya Meydan Muharebesi' süreci ile ilgili aşağıdakilerden hangisi söylenebilir? (H-234)",
          "options": [
            "A) Sakarya Meydan Muharebesi dönemin en kritik gelişmelerinden biridir.",
            "B) Hiçbir etkisi olmamıştır.",
            "C) Avrupa'da gerçekleşmiştir.",
            "D) Sadece ekonomik bir olaydır.",
            "E) Osmanlı'nın kuruluş dönemine aittir."
          ],
          "correct": 0,
          "solution": "Doğru cevap Sakarya Meydan Muharebesi dönemin en kritik gelişmelerinden biridir..",
          "id": "e9_q82",
          "no": 82
        },
        {
          "subject": "Tarih",
          "text": "Aşağıdaki tarihî gelişmelerden hangisi 'Büyük Taarruz' ile doğrudan veya dolaylı olarak bağlantılıdır? (H-235)",
          "options": [
            "A) Fransız İhtilali",
            "B) Büyük Taarruz öncesi ve sonrası yaşanan siyasi krizler.",
            "C) Kavimler Göçü",
            "D) Sanayi İnkılabı",
            "E) Coğrafi Keşifler"
          ],
          "correct": 1,
          "solution": "Doğru cevap Büyük Taarruz öncesi ve sonrası yaşanan siyasi krizler..",
          "id": "e9_q83",
          "no": 83
        },
        {
          "subject": "Tarih",
          "text": "Millî Mücadele ve inkılaplar tarihi incelendiğinde 'I. İnönü Muharebesi' olayının temel amacı aşağıdakilerden hangisidir? (H-236)",
          "options": [
            "A) Saltanatı güçlendirmek",
            "B) Avrupa'ya göç etmek",
            "C) Yeni sömürgeler elde etmek",
            "D) Feodaliteyi kurmak",
            "E) Bağımsızlık ve egemenliği pekiştirmek"
          ],
          "correct": 4,
          "solution": "Doğru cevap Bağımsızlık ve egemenliği pekiştirmek.",
          "id": "e9_q84",
          "no": 84
        },
        {
          "subject": "Tarih",
          "text": "Türk siyasi ve askerî tarihinde büyük öneme sahip olan 'II. İnönü Muharebesi' süreci ile ilgili aşağıdakilerden hangisi söylenebilir? (H-237)",
          "options": [
            "A) II. İnönü Muharebesi dönemin en kritik gelişmelerinden biridir.",
            "B) Hiçbir etkisi olmamıştır.",
            "C) Osmanlı'nın kuruluş dönemine aittir.",
            "D) Avrupa'da gerçekleşmiştir.",
            "E) Sadece ekonomik bir olaydır."
          ],
          "correct": 0,
          "solution": "Doğru cevap II. İnönü Muharebesi dönemin en kritik gelişmelerinden biridir..",
          "id": "e9_q85",
          "no": 85
        },
        {
          "subject": "Tarih",
          "text": "Aşağıdaki tarihî gelişmelerden hangisi 'Kars Antlaşması' ile doğrudan veya dolaylı olarak bağlantılıdır? (H-238)",
          "options": [
            "A) Kars Antlaşması öncesi ve sonrası yaşanan siyasi krizler.",
            "B) Coğrafi Keşifler",
            "C) Kavimler Göçü",
            "D) Sanayi İnkılabı",
            "E) Fransız İhtilali"
          ],
          "correct": 0,
          "solution": "Doğru cevap Kars Antlaşması öncesi ve sonrası yaşanan siyasi krizler..",
          "id": "e9_q86",
          "no": 86
        },
        {
          "subject": "Tarih",
          "text": "Millî Mücadele ve inkılaplar tarihi incelendiğinde 'Ankara Antlaşması' olayının temel amacı aşağıdakilerden hangisidir? (H-239)",
          "options": [
            "A) Yeni sömürgeler elde etmek",
            "B) Saltanatı güçlendirmek",
            "C) Avrupa'ya göç etmek",
            "D) Bağımsızlık ve egemenliği pekiştirmek",
            "E) Feodaliteyi kurmak"
          ],
          "correct": 3,
          "solution": "Doğru cevap Bağımsızlık ve egemenliği pekiştirmek.",
          "id": "e9_q87",
          "no": 87
        },
        {
          "subject": "Coğrafya",
          "text": "Türkiye'nin fiziki coğrafyası düşünüldüğünde 'Kaçkar Dağları' için aşağıdakilerden hangisi doğrudur? (C-142)",
          "options": [
            "A) Kaçkar Dağları tarıma kapalıdır.",
            "B) Kaçkar Dağları Marmara'dadır.",
            "C) Kaçkar Dağları yapay bir kanaldır.",
            "D) Kaçkar Dağları, ülkemizin önemli yeryüzü şekillerinden biridir.",
            "E) Kaçkar Dağları bir çöldür."
          ],
          "correct": 3,
          "solution": "Doğru cevap Kaçkar Dağları, ülkemizin önemli yeryüzü şekillerinden biridir..",
          "id": "e9_q88",
          "no": 88
        },
        {
          "subject": "Coğrafya",
          "text": "Coğrafi özellikleri ve turizm potansiyeli göz önüne alındığında 'Gediz Nehri' hangi alanda daha çok öne çıkar? (C-143)",
          "options": [
            "A) Sadece ağır sanayi",
            "B) Okyanus balıkçılığı",
            "C) Doğal güzellikleri ve turizm/coğrafi önemi",
            "D) Sadece madencilik",
            "E) Çöl iklimi araştırmaları"
          ],
          "correct": 2,
          "solution": "Doğru cevap Doğal güzellikleri ve turizm/coğrafi önemi.",
          "id": "e9_q89",
          "no": 89
        },
        {
          "subject": "Coğrafya",
          "text": "Türkiye'nin fiziki coğrafyası düşünüldüğünde 'Salda Gölü' için aşağıdakilerden hangisi doğrudur? (C-144)",
          "options": [
            "A) Salda Gölü bir çöldür.",
            "B) Salda Gölü tarıma kapalıdır.",
            "C) Salda Gölü Marmara'dadır.",
            "D) Salda Gölü yapay bir kanaldır.",
            "E) Salda Gölü, ülkemizin önemli yeryüzü şekillerinden biridir."
          ],
          "correct": 4,
          "solution": "Doğru cevap Salda Gölü, ülkemizin önemli yeryüzü şekillerinden biridir..",
          "id": "e9_q90",
          "no": 90
        },
        {
          "subject": "Coğrafya",
          "text": "Coğrafi özellikleri ve turizm potansiyeli göz önüne alındığında 'Kapadokya' hangi alanda daha çok öne çıkar? (C-145)",
          "options": [
            "A) Doğal güzellikleri ve turizm/coğrafi önemi",
            "B) Çöl iklimi araştırmaları",
            "C) Sadece ağır sanayi",
            "D) Okyanus balıkçılığı",
            "E) Sadece madencilik"
          ],
          "correct": 0,
          "solution": "Doğru cevap Doğal güzellikleri ve turizm/coğrafi önemi.",
          "id": "e9_q91",
          "no": 91
        },
        {
          "subject": "Coğrafya",
          "text": "Türkiye'nin fiziki coğrafyası düşünüldüğünde 'Pamukkale' için aşağıdakilerden hangisi doğrudur? (C-146)",
          "options": [
            "A) Pamukkale bir çöldür.",
            "B) Pamukkale Marmara'dadır.",
            "C) Pamukkale yapay bir kanaldır.",
            "D) Pamukkale, ülkemizin önemli yeryüzü şekillerinden biridir.",
            "E) Pamukkale tarıma kapalıdır."
          ],
          "correct": 3,
          "solution": "Doğru cevap Pamukkale, ülkemizin önemli yeryüzü şekillerinden biridir..",
          "id": "e9_q92",
          "no": 92
        },
        {
          "subject": "Coğrafya",
          "text": "Coğrafi özellikleri ve turizm potansiyeli göz önüne alındığında 'Nemrut Dağı' hangi alanda daha çok öne çıkar? (C-147)",
          "options": [
            "A) Sadece madencilik",
            "B) Doğal güzellikleri ve turizm/coğrafi önemi",
            "C) Çöl iklimi araştırmaları",
            "D) Sadece ağır sanayi",
            "E) Okyanus balıkçılığı"
          ],
          "correct": 1,
          "solution": "Doğru cevap Doğal güzellikleri ve turizm/coğrafi önemi.",
          "id": "e9_q93",
          "no": 93
        },
        {
          "subject": "Coğrafya",
          "text": "Türkiye'nin fiziki coğrafyası düşünüldüğünde 'Sümela Manastırı' için aşağıdakilerden hangisi doğrudur? (C-148)",
          "options": [
            "A) Sümela Manastırı, ülkemizin önemli yeryüzü şekillerinden biridir.",
            "B) Sümela Manastırı yapay bir kanaldır.",
            "C) Sümela Manastırı tarıma kapalıdır.",
            "D) Sümela Manastırı bir çöldür.",
            "E) Sümela Manastırı Marmara'dadır."
          ],
          "correct": 0,
          "solution": "Doğru cevap Sümela Manastırı, ülkemizin önemli yeryüzü şekillerinden biridir..",
          "id": "e9_q94",
          "no": 94
        },
        {
          "subject": "Coğrafya",
          "text": "Coğrafi özellikleri ve turizm potansiyeli göz önüne alındığında 'Uludağ' hangi alanda daha çok öne çıkar? (C-149)",
          "options": [
            "A) Sadece madencilik",
            "B) Çöl iklimi araştırmaları",
            "C) Okyanus balıkçılığı",
            "D) Doğal güzellikleri ve turizm/coğrafi önemi",
            "E) Sadece ağır sanayi"
          ],
          "correct": 3,
          "solution": "Doğru cevap Doğal güzellikleri ve turizm/coğrafi önemi.",
          "id": "e9_q95",
          "no": 95
        },
        {
          "subject": "Coğrafya",
          "text": "Türkiye'nin fiziki coğrafyası düşünüldüğünde 'Van Gölü' için aşağıdakilerden hangisi doğrudur? (C-150)",
          "options": [
            "A) Van Gölü, ülkemizin önemli yeryüzü şekillerinden biridir.",
            "B) Van Gölü tarıma kapalıdır.",
            "C) Van Gölü bir çöldür.",
            "D) Van Gölü yapay bir kanaldır.",
            "E) Van Gölü Marmara'dadır."
          ],
          "correct": 0,
          "solution": "Doğru cevap Van Gölü, ülkemizin önemli yeryüzü şekillerinden biridir..",
          "id": "e9_q96",
          "no": 96
        },
        {
          "subject": "Coğrafya",
          "text": "Coğrafi özellikleri ve turizm potansiyeli göz önüne alındığında 'Ağrı Dağı' hangi alanda daha çok öne çıkar? (C-151)",
          "options": [
            "A) Sadece madencilik",
            "B) Sadece ağır sanayi",
            "C) Doğal güzellikleri ve turizm/coğrafi önemi",
            "D) Okyanus balıkçılığı",
            "E) Çöl iklimi araştırmaları"
          ],
          "correct": 2,
          "solution": "Doğru cevap Doğal güzellikleri ve turizm/coğrafi önemi.",
          "id": "e9_q97",
          "no": 97
        },
        {
          "subject": "Coğrafya",
          "text": "Türkiye'nin fiziki coğrafyası düşünüldüğünde 'Kızılırmak' için aşağıdakilerden hangisi doğrudur? (C-152)",
          "options": [
            "A) Kızılırmak tarıma kapalıdır.",
            "B) Kızılırmak yapay bir kanaldır.",
            "C) Kızılırmak Marmara'dadır.",
            "D) Kızılırmak bir çöldür.",
            "E) Kızılırmak, ülkemizin önemli yeryüzü şekillerinden biridir."
          ],
          "correct": 4,
          "solution": "Doğru cevap Kızılırmak, ülkemizin önemli yeryüzü şekillerinden biridir..",
          "id": "e9_q98",
          "no": 98
        },
        {
          "subject": "Coğrafya",
          "text": "Coğrafi özellikleri ve turizm potansiyeli göz önüne alındığında 'Erciyes Dağı' hangi alanda daha çok öne çıkar? (C-153)",
          "options": [
            "A) Sadece madencilik",
            "B) Çöl iklimi araştırmaları",
            "C) Okyanus balıkçılığı",
            "D) Sadece ağır sanayi",
            "E) Doğal güzellikleri ve turizm/coğrafi önemi"
          ],
          "correct": 4,
          "solution": "Doğru cevap Doğal güzellikleri ve turizm/coğrafi önemi.",
          "id": "e9_q99",
          "no": 99
        },
        {
          "subject": "Coğrafya",
          "text": "Türkiye'nin fiziki coğrafyası düşünüldüğünde 'Tuz Gölü' için aşağıdakilerden hangisi doğrudur? (C-154)",
          "options": [
            "A) Tuz Gölü bir çöldür.",
            "B) Tuz Gölü, ülkemizin önemli yeryüzü şekillerinden biridir.",
            "C) Tuz Gölü Marmara'dadır.",
            "D) Tuz Gölü tarıma kapalıdır.",
            "E) Tuz Gölü yapay bir kanaldır."
          ],
          "correct": 1,
          "solution": "Doğru cevap Tuz Gölü, ülkemizin önemli yeryüzü şekillerinden biridir..",
          "id": "e9_q100",
          "no": 100
        },
        {
          "subject": "Coğrafya",
          "text": "Coğrafi özellikleri ve turizm potansiyeli göz önüne alındığında 'Çukurova' hangi alanda daha çok öne çıkar? (C-155)",
          "options": [
            "A) Sadece ağır sanayi",
            "B) Sadece madencilik",
            "C) Okyanus balıkçılığı",
            "D) Doğal güzellikleri ve turizm/coğrafi önemi",
            "E) Çöl iklimi araştırmaları"
          ],
          "correct": 3,
          "solution": "Doğru cevap Doğal güzellikleri ve turizm/coğrafi önemi.",
          "id": "e9_q101",
          "no": 101
        },
        {
          "subject": "Coğrafya",
          "text": "Türkiye'nin fiziki coğrafyası düşünüldüğünde 'Bafra Ovası' için aşağıdakilerden hangisi doğrudur? (C-156)",
          "options": [
            "A) Bafra Ovası yapay bir kanaldır.",
            "B) Bafra Ovası bir çöldür.",
            "C) Bafra Ovası Marmara'dadır.",
            "D) Bafra Ovası, ülkemizin önemli yeryüzü şekillerinden biridir.",
            "E) Bafra Ovası tarıma kapalıdır."
          ],
          "correct": 3,
          "solution": "Doğru cevap Bafra Ovası, ülkemizin önemli yeryüzü şekillerinden biridir..",
          "id": "e9_q102",
          "no": 102
        },
        {
          "subject": "Coğrafya",
          "text": "Coğrafi özellikleri ve turizm potansiyeli göz önüne alındığında 'Kaçkar Dağları' hangi alanda daha çok öne çıkar? (C-157)",
          "options": [
            "A) Sadece ağır sanayi",
            "B) Okyanus balıkçılığı",
            "C) Çöl iklimi araştırmaları",
            "D) Doğal güzellikleri ve turizm/coğrafi önemi",
            "E) Sadece madencilik"
          ],
          "correct": 3,
          "solution": "Doğru cevap Doğal güzellikleri ve turizm/coğrafi önemi.",
          "id": "e9_q103",
          "no": 103
        },
        {
          "subject": "Coğrafya",
          "text": "Türkiye'nin fiziki coğrafyası düşünüldüğünde 'Gediz Nehri' için aşağıdakilerden hangisi doğrudur? (C-158)",
          "options": [
            "A) Gediz Nehri yapay bir kanaldır.",
            "B) Gediz Nehri, ülkemizin önemli yeryüzü şekillerinden biridir.",
            "C) Gediz Nehri tarıma kapalıdır.",
            "D) Gediz Nehri bir çöldür.",
            "E) Gediz Nehri Marmara'dadır."
          ],
          "correct": 1,
          "solution": "Doğru cevap Gediz Nehri, ülkemizin önemli yeryüzü şekillerinden biridir..",
          "id": "e9_q104",
          "no": 104
        },
        {
          "subject": "Coğrafya",
          "text": "Coğrafi özellikleri ve turizm potansiyeli göz önüne alındığında 'Salda Gölü' hangi alanda daha çok öne çıkar? (C-159)",
          "options": [
            "A) Sadece madencilik",
            "B) Doğal güzellikleri ve turizm/coğrafi önemi",
            "C) Okyanus balıkçılığı",
            "D) Sadece ağır sanayi",
            "E) Çöl iklimi araştırmaları"
          ],
          "correct": 1,
          "solution": "Doğru cevap Doğal güzellikleri ve turizm/coğrafi önemi.",
          "id": "e9_q105",
          "no": 105
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'Yargıtay' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-118)",
          "options": [
            "A) Yargıtay yasaklanmıştır.",
            "B) Yargıtay yabancı bir kurumdur.",
            "C) Yargıtay, anayasal sistemin önemli bir parçasıdır.",
            "D) Yargıtay sadece köylerde bulunur.",
            "E) Yargıtay özel bir şirkettir."
          ],
          "correct": 2,
          "solution": "Doğru cevap Yargıtay, anayasal sistemin önemli bir parçasıdır..",
          "id": "e9_q106",
          "no": 106
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'Danıştay' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-119)",
          "options": [
            "A) Danıştay, anayasal sistemin önemli bir parçasıdır.",
            "B) Danıştay yabancı bir kurumdur.",
            "C) Danıştay sadece köylerde bulunur.",
            "D) Danıştay özel bir şirkettir.",
            "E) Danıştay yasaklanmıştır."
          ],
          "correct": 0,
          "solution": "Doğru cevap Danıştay, anayasal sistemin önemli bir parçasıdır..",
          "id": "e9_q107",
          "no": 107
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'TBMM' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-120)",
          "options": [
            "A) TBMM yasaklanmıştır.",
            "B) TBMM yabancı bir kurumdur.",
            "C) TBMM sadece köylerde bulunur.",
            "D) TBMM, anayasal sistemin önemli bir parçasıdır.",
            "E) TBMM özel bir şirkettir."
          ],
          "correct": 3,
          "solution": "Doğru cevap TBMM, anayasal sistemin önemli bir parçasıdır..",
          "id": "e9_q108",
          "no": 108
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'Cumhurbaşkanlığı' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-121)",
          "options": [
            "A) Cumhurbaşkanlığı sadece köylerde bulunur.",
            "B) Cumhurbaşkanlığı, anayasal sistemin önemli bir parçasıdır.",
            "C) Cumhurbaşkanlığı yabancı bir kurumdur.",
            "D) Cumhurbaşkanlığı özel bir şirkettir.",
            "E) Cumhurbaşkanlığı yasaklanmıştır."
          ],
          "correct": 1,
          "solution": "Doğru cevap Cumhurbaşkanlığı, anayasal sistemin önemli bir parçasıdır..",
          "id": "e9_q109",
          "no": 109
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'Sayıştay' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-122)",
          "options": [
            "A) Sayıştay yasaklanmıştır.",
            "B) Sayıştay sadece köylerde bulunur.",
            "C) Sayıştay yabancı bir kurumdur.",
            "D) Sayıştay özel bir şirkettir.",
            "E) Sayıştay, anayasal sistemin önemli bir parçasıdır."
          ],
          "correct": 4,
          "solution": "Doğru cevap Sayıştay, anayasal sistemin önemli bir parçasıdır..",
          "id": "e9_q110",
          "no": 110
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'YSK' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-123)",
          "options": [
            "A) YSK sadece köylerde bulunur.",
            "B) YSK yabancı bir kurumdur.",
            "C) YSK özel bir şirkettir.",
            "D) YSK, anayasal sistemin önemli bir parçasıdır.",
            "E) YSK yasaklanmıştır."
          ],
          "correct": 3,
          "solution": "Doğru cevap YSK, anayasal sistemin önemli bir parçasıdır..",
          "id": "e9_q111",
          "no": 111
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'HSK' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-124)",
          "options": [
            "A) HSK yasaklanmıştır.",
            "B) HSK özel bir şirkettir.",
            "C) HSK, anayasal sistemin önemli bir parçasıdır.",
            "D) HSK yabancı bir kurumdur.",
            "E) HSK sadece köylerde bulunur."
          ],
          "correct": 2,
          "solution": "Doğru cevap HSK, anayasal sistemin önemli bir parçasıdır..",
          "id": "e9_q112",
          "no": 112
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'Belediye' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-125)",
          "options": [
            "A) Belediye yasaklanmıştır.",
            "B) Belediye yabancı bir kurumdur.",
            "C) Belediye sadece köylerde bulunur.",
            "D) Belediye, anayasal sistemin önemli bir parçasıdır.",
            "E) Belediye özel bir şirkettir."
          ],
          "correct": 3,
          "solution": "Doğru cevap Belediye, anayasal sistemin önemli bir parçasıdır..",
          "id": "e9_q113",
          "no": 113
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'Valilik' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-126)",
          "options": [
            "A) Valilik, anayasal sistemin önemli bir parçasıdır.",
            "B) Valilik özel bir şirkettir.",
            "C) Valilik yabancı bir kurumdur.",
            "D) Valilik yasaklanmıştır.",
            "E) Valilik sadece köylerde bulunur."
          ],
          "correct": 0,
          "solution": "Doğru cevap Valilik, anayasal sistemin önemli bir parçasıdır..",
          "id": "e9_q114",
          "no": 114
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'Kaymakamlık' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-127)",
          "options": [
            "A) Kaymakamlık özel bir şirkettir.",
            "B) Kaymakamlık yabancı bir kurumdur.",
            "C) Kaymakamlık, anayasal sistemin önemli bir parçasıdır.",
            "D) Kaymakamlık sadece köylerde bulunur.",
            "E) Kaymakamlık yasaklanmıştır."
          ],
          "correct": 2,
          "solution": "Doğru cevap Kaymakamlık, anayasal sistemin önemli bir parçasıdır..",
          "id": "e9_q115",
          "no": 115
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'İl Genel Meclisi' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-128)",
          "options": [
            "A) İl Genel Meclisi özel bir şirkettir.",
            "B) İl Genel Meclisi yabancı bir kurumdur.",
            "C) İl Genel Meclisi yasaklanmıştır.",
            "D) İl Genel Meclisi, anayasal sistemin önemli bir parçasıdır.",
            "E) İl Genel Meclisi sadece köylerde bulunur."
          ],
          "correct": 3,
          "solution": "Doğru cevap İl Genel Meclisi, anayasal sistemin önemli bir parçasıdır..",
          "id": "e9_q116",
          "no": 116
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'Kamu Denetçiliği Kurumu' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-129)",
          "options": [
            "A) Kamu Denetçiliği Kurumu yabancı bir kurumdur.",
            "B) Kamu Denetçiliği Kurumu özel bir şirkettir.",
            "C) Kamu Denetçiliği Kurumu yasaklanmıştır.",
            "D) Kamu Denetçiliği Kurumu sadece köylerde bulunur.",
            "E) Kamu Denetçiliği Kurumu, anayasal sistemin önemli bir parçasıdır."
          ],
          "correct": 4,
          "solution": "Doğru cevap Kamu Denetçiliği Kurumu, anayasal sistemin önemli bir parçasıdır..",
          "id": "e9_q117",
          "no": 117
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'Anayasa Mahkemesi' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-130)",
          "options": [
            "A) Anayasa Mahkemesi, anayasal sistemin önemli bir parçasıdır.",
            "B) Anayasa Mahkemesi özel bir şirkettir.",
            "C) Anayasa Mahkemesi sadece köylerde bulunur.",
            "D) Anayasa Mahkemesi yabancı bir kurumdur.",
            "E) Anayasa Mahkemesi yasaklanmıştır."
          ],
          "correct": 0,
          "solution": "Doğru cevap Anayasa Mahkemesi, anayasal sistemin önemli bir parçasıdır..",
          "id": "e9_q118",
          "no": 118
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'Yargıtay' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-131)",
          "options": [
            "A) Yargıtay yabancı bir kurumdur.",
            "B) Yargıtay, anayasal sistemin önemli bir parçasıdır.",
            "C) Yargıtay sadece köylerde bulunur.",
            "D) Yargıtay özel bir şirkettir.",
            "E) Yargıtay yasaklanmıştır."
          ],
          "correct": 1,
          "solution": "Doğru cevap Yargıtay, anayasal sistemin önemli bir parçasıdır..",
          "id": "e9_q119",
          "no": 119
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'Danıştay' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-132)",
          "options": [
            "A) Danıştay sadece köylerde bulunur.",
            "B) Danıştay özel bir şirkettir.",
            "C) Danıştay yasaklanmıştır.",
            "D) Danıştay, anayasal sistemin önemli bir parçasıdır.",
            "E) Danıştay yabancı bir kurumdur."
          ],
          "correct": 3,
          "solution": "Doğru cevap Danıştay, anayasal sistemin önemli bir parçasıdır..",
          "id": "e9_q120",
          "no": 120
        }
      ]
    },
    {
      "id": "deneme_10",
      "name": "10. Deneme Sınavı",
      "totalQuestions": 120,
      "duration": 130,
      "distribution": {
        "Türkçe": 30,
        "Matematik": 30,
        "Tarih": 27,
        "Coğrafya": 18,
        "Vatandaşlık": 15
      },
      "questions": [
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde 'yanlış' kelimesinin yazımıyla ilgili bir kural hatırlatılmaktadır? (T-265)",
          "options": [
            "A) yanlış cümlede özne olamaz.",
            "B) yanlış kelimesi her zaman ayrı yazılır.",
            "C) yanlış kelimesi fiildir.",
            "D) 'yanlış' kelimesinin doğru yazımına dikkat edilmelidir.",
            "E) yanlış kelimesi yabancı kökenlidir."
          ],
          "correct": 3,
          "solution": "Doğru cevap 'yanlış' kelimesinin doğru yazımına dikkat edilmelidir..",
          "id": "e10_q1",
          "no": 1
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde mecaz anlamlı bir sözcük kullanılmıştır? (T-266)",
          "options": [
            "A) Buzdolabı soğuk üflüyor.",
            "B) Suyu dolaptan soğuk içti.",
            "C) Olaylara karşı çok 'soğuk' davranıyordu.",
            "D) Kışın havalar soğuk olur.",
            "E) Hava bugün çok soğuk."
          ],
          "correct": 2,
          "solution": "Doğru cevap Olaylara karşı çok 'soğuk' davranıyordu..",
          "id": "e10_q2",
          "no": 2
        },
        {
          "subject": "Türkçe",
          "text": "Bilim tarih boyunca insanlığın en büyük rehberlerinden biri olmuştur. Toplumlar Bilim sayesinde sınırlarını aşmış, geleceğe umutla bakabilmiştir. (P-267)\nBu parçanın ana düşüncesi nedir?",
          "options": [
            "A) İnsanlar Bilim ile ilgilenmemelidir.",
            "B) Bilim, toplumsal ilerleme ve vizyon için vazgeçilmezdir.",
            "C) Bilim zaman kaybıdır.",
            "D) Bilim sadece geçmişte kalmıştır.",
            "E) Bilim sadece bireyseldir."
          ],
          "correct": 1,
          "solution": "Doğru cevap Bilim, toplumsal ilerleme ve vizyon için vazgeçilmezdir..",
          "id": "e10_q3",
          "no": 3
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde 'birkaç' kelimesinin yazımıyla ilgili bir kural hatırlatılmaktadır? (T-268)",
          "options": [
            "A) 'birkaç' kelimesinin doğru yazımına dikkat edilmelidir.",
            "B) birkaç kelimesi fiildir.",
            "C) birkaç kelimesi her zaman ayrı yazılır.",
            "D) birkaç cümlede özne olamaz.",
            "E) birkaç kelimesi yabancı kökenlidir."
          ],
          "correct": 0,
          "solution": "Doğru cevap 'birkaç' kelimesinin doğru yazımına dikkat edilmelidir..",
          "id": "e10_q4",
          "no": 4
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde mecaz anlamlı bir sözcük kullanılmıştır? (T-269)",
          "options": [
            "A) Suyu dolaptan soğuk içti.",
            "B) Hava bugün çok soğuk.",
            "C) Kışın havalar soğuk olur.",
            "D) Buzdolabı soğuk üflüyor.",
            "E) Olaylara karşı çok 'soğuk' davranıyordu."
          ],
          "correct": 4,
          "solution": "Doğru cevap Olaylara karşı çok 'soğuk' davranıyordu..",
          "id": "e10_q5",
          "no": 5
        },
        {
          "subject": "Türkçe",
          "text": "Sanat tarih boyunca insanlığın en büyük rehberlerinden biri olmuştur. Toplumlar Sanat sayesinde sınırlarını aşmış, geleceğe umutla bakabilmiştir. (P-270)\nBu parçanın ana düşüncesi nedir?",
          "options": [
            "A) Sanat zaman kaybıdır.",
            "B) Sanat sadece bireyseldir.",
            "C) Sanat sadece geçmişte kalmıştır.",
            "D) İnsanlar Sanat ile ilgilenmemelidir.",
            "E) Sanat, toplumsal ilerleme ve vizyon için vazgeçilmezdir."
          ],
          "correct": 4,
          "solution": "Doğru cevap Sanat, toplumsal ilerleme ve vizyon için vazgeçilmezdir..",
          "id": "e10_q6",
          "no": 6
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde 'hiç kimse' kelimesinin yazımıyla ilgili bir kural hatırlatılmaktadır? (T-271)",
          "options": [
            "A) hiç kimse kelimesi yabancı kökenlidir.",
            "B) hiç kimse kelimesi her zaman ayrı yazılır.",
            "C) hiç kimse kelimesi fiildir.",
            "D) 'hiç kimse' kelimesinin doğru yazımına dikkat edilmelidir.",
            "E) hiç kimse cümlede özne olamaz."
          ],
          "correct": 3,
          "solution": "Doğru cevap 'hiç kimse' kelimesinin doğru yazımına dikkat edilmelidir..",
          "id": "e10_q7",
          "no": 7
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde mecaz anlamlı bir sözcük kullanılmıştır? (T-272)",
          "options": [
            "A) Olaylara karşı çok 'soğuk' davranıyordu.",
            "B) Kışın havalar soğuk olur.",
            "C) Hava bugün çok soğuk.",
            "D) Buzdolabı soğuk üflüyor.",
            "E) Suyu dolaptan soğuk içti."
          ],
          "correct": 0,
          "solution": "Doğru cevap Olaylara karşı çok 'soğuk' davranıyordu..",
          "id": "e10_q8",
          "no": 8
        },
        {
          "subject": "Türkçe",
          "text": "Teknoloji tarih boyunca insanlığın en büyük rehberlerinden biri olmuştur. Toplumlar Teknoloji sayesinde sınırlarını aşmış, geleceğe umutla bakabilmiştir. (P-273)\nBu parçanın ana düşüncesi nedir?",
          "options": [
            "A) İnsanlar Teknoloji ile ilgilenmemelidir.",
            "B) Teknoloji zaman kaybıdır.",
            "C) Teknoloji, toplumsal ilerleme ve vizyon için vazgeçilmezdir.",
            "D) Teknoloji sadece geçmişte kalmıştır.",
            "E) Teknoloji sadece bireyseldir."
          ],
          "correct": 2,
          "solution": "Doğru cevap Teknoloji, toplumsal ilerleme ve vizyon için vazgeçilmezdir..",
          "id": "e10_q9",
          "no": 9
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde 'herkes' kelimesinin yazımıyla ilgili bir kural hatırlatılmaktadır? (T-274)",
          "options": [
            "A) herkes kelimesi yabancı kökenlidir.",
            "B) herkes cümlede özne olamaz.",
            "C) herkes kelimesi fiildir.",
            "D) herkes kelimesi her zaman ayrı yazılır.",
            "E) 'herkes' kelimesinin doğru yazımına dikkat edilmelidir."
          ],
          "correct": 4,
          "solution": "Doğru cevap 'herkes' kelimesinin doğru yazımına dikkat edilmelidir..",
          "id": "e10_q10",
          "no": 10
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde mecaz anlamlı bir sözcük kullanılmıştır? (T-275)",
          "options": [
            "A) Buzdolabı soğuk üflüyor.",
            "B) Hava bugün çok soğuk.",
            "C) Suyu dolaptan soğuk içti.",
            "D) Olaylara karşı çok 'soğuk' davranıyordu.",
            "E) Kışın havalar soğuk olur."
          ],
          "correct": 3,
          "solution": "Doğru cevap Olaylara karşı çok 'soğuk' davranıyordu..",
          "id": "e10_q11",
          "no": 11
        },
        {
          "subject": "Türkçe",
          "text": "Doğa tarih boyunca insanlığın en büyük rehberlerinden biri olmuştur. Toplumlar Doğa sayesinde sınırlarını aşmış, geleceğe umutla bakabilmiştir. (P-276)\nBu parçanın ana düşüncesi nedir?",
          "options": [
            "A) Doğa sadece geçmişte kalmıştır.",
            "B) İnsanlar Doğa ile ilgilenmemelidir.",
            "C) Doğa, toplumsal ilerleme ve vizyon için vazgeçilmezdir.",
            "D) Doğa sadece bireyseldir.",
            "E) Doğa zaman kaybıdır."
          ],
          "correct": 2,
          "solution": "Doğru cevap Doğa, toplumsal ilerleme ve vizyon için vazgeçilmezdir..",
          "id": "e10_q12",
          "no": 12
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde 'bugün' kelimesinin yazımıyla ilgili bir kural hatırlatılmaktadır? (T-277)",
          "options": [
            "A) bugün cümlede özne olamaz.",
            "B) bugün kelimesi yabancı kökenlidir.",
            "C) 'bugün' kelimesinin doğru yazımına dikkat edilmelidir.",
            "D) bugün kelimesi her zaman ayrı yazılır.",
            "E) bugün kelimesi fiildir."
          ],
          "correct": 2,
          "solution": "Doğru cevap 'bugün' kelimesinin doğru yazımına dikkat edilmelidir..",
          "id": "e10_q13",
          "no": 13
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde mecaz anlamlı bir sözcük kullanılmıştır? (T-278)",
          "options": [
            "A) Buzdolabı soğuk üflüyor.",
            "B) Kışın havalar soğuk olur.",
            "C) Suyu dolaptan soğuk içti.",
            "D) Hava bugün çok soğuk.",
            "E) Olaylara karşı çok 'soğuk' davranıyordu."
          ],
          "correct": 4,
          "solution": "Doğru cevap Olaylara karşı çok 'soğuk' davranıyordu..",
          "id": "e10_q14",
          "no": 14
        },
        {
          "subject": "Türkçe",
          "text": "Psikoloji tarih boyunca insanlığın en büyük rehberlerinden biri olmuştur. Toplumlar Psikoloji sayesinde sınırlarını aşmış, geleceğe umutla bakabilmiştir. (P-279)\nBu parçanın ana düşüncesi nedir?",
          "options": [
            "A) Psikoloji, toplumsal ilerleme ve vizyon için vazgeçilmezdir.",
            "B) Psikoloji sadece bireyseldir.",
            "C) Psikoloji zaman kaybıdır.",
            "D) Psikoloji sadece geçmişte kalmıştır.",
            "E) İnsanlar Psikoloji ile ilgilenmemelidir."
          ],
          "correct": 0,
          "solution": "Doğru cevap Psikoloji, toplumsal ilerleme ve vizyon için vazgeçilmezdir..",
          "id": "e10_q15",
          "no": 15
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde 'yalnız' kelimesinin yazımıyla ilgili bir kural hatırlatılmaktadır? (T-280)",
          "options": [
            "A) yalnız cümlede özne olamaz.",
            "B) yalnız kelimesi yabancı kökenlidir.",
            "C) 'yalnız' kelimesinin doğru yazımına dikkat edilmelidir.",
            "D) yalnız kelimesi fiildir.",
            "E) yalnız kelimesi her zaman ayrı yazılır."
          ],
          "correct": 2,
          "solution": "Doğru cevap 'yalnız' kelimesinin doğru yazımına dikkat edilmelidir..",
          "id": "e10_q16",
          "no": 16
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde mecaz anlamlı bir sözcük kullanılmıştır? (T-281)",
          "options": [
            "A) Kışın havalar soğuk olur.",
            "B) Buzdolabı soğuk üflüyor.",
            "C) Hava bugün çok soğuk.",
            "D) Olaylara karşı çok 'soğuk' davranıyordu.",
            "E) Suyu dolaptan soğuk içti."
          ],
          "correct": 3,
          "solution": "Doğru cevap Olaylara karşı çok 'soğuk' davranıyordu..",
          "id": "e10_q17",
          "no": 17
        },
        {
          "subject": "Türkçe",
          "text": "Eğitim tarih boyunca insanlığın en büyük rehberlerinden biri olmuştur. Toplumlar Eğitim sayesinde sınırlarını aşmış, geleceğe umutla bakabilmiştir. (P-282)\nBu parçanın ana düşüncesi nedir?",
          "options": [
            "A) Eğitim zaman kaybıdır.",
            "B) Eğitim sadece bireyseldir.",
            "C) Eğitim, toplumsal ilerleme ve vizyon için vazgeçilmezdir.",
            "D) İnsanlar Eğitim ile ilgilenmemelidir.",
            "E) Eğitim sadece geçmişte kalmıştır."
          ],
          "correct": 2,
          "solution": "Doğru cevap Eğitim, toplumsal ilerleme ve vizyon için vazgeçilmezdir..",
          "id": "e10_q18",
          "no": 18
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde 'hiçbir' kelimesinin yazımıyla ilgili bir kural hatırlatılmaktadır? (T-283)",
          "options": [
            "A) hiçbir kelimesi fiildir.",
            "B) hiçbir kelimesi yabancı kökenlidir.",
            "C) hiçbir kelimesi her zaman ayrı yazılır.",
            "D) hiçbir cümlede özne olamaz.",
            "E) 'hiçbir' kelimesinin doğru yazımına dikkat edilmelidir."
          ],
          "correct": 4,
          "solution": "Doğru cevap 'hiçbir' kelimesinin doğru yazımına dikkat edilmelidir..",
          "id": "e10_q19",
          "no": 19
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde mecaz anlamlı bir sözcük kullanılmıştır? (T-284)",
          "options": [
            "A) Olaylara karşı çok 'soğuk' davranıyordu.",
            "B) Kışın havalar soğuk olur.",
            "C) Suyu dolaptan soğuk içti.",
            "D) Buzdolabı soğuk üflüyor.",
            "E) Hava bugün çok soğuk."
          ],
          "correct": 0,
          "solution": "Doğru cevap Olaylara karşı çok 'soğuk' davranıyordu..",
          "id": "e10_q20",
          "no": 20
        },
        {
          "subject": "Türkçe",
          "text": "Kültür tarih boyunca insanlığın en büyük rehberlerinden biri olmuştur. Toplumlar Kültür sayesinde sınırlarını aşmış, geleceğe umutla bakabilmiştir. (P-285)\nBu parçanın ana düşüncesi nedir?",
          "options": [
            "A) Kültür zaman kaybıdır.",
            "B) İnsanlar Kültür ile ilgilenmemelidir.",
            "C) Kültür sadece geçmişte kalmıştır.",
            "D) Kültür sadece bireyseldir.",
            "E) Kültür, toplumsal ilerleme ve vizyon için vazgeçilmezdir."
          ],
          "correct": 4,
          "solution": "Doğru cevap Kültür, toplumsal ilerleme ve vizyon için vazgeçilmezdir..",
          "id": "e10_q21",
          "no": 21
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde 'her şey' kelimesinin yazımıyla ilgili bir kural hatırlatılmaktadır? (T-286)",
          "options": [
            "A) 'her şey' kelimesinin doğru yazımına dikkat edilmelidir.",
            "B) her şey kelimesi her zaman ayrı yazılır.",
            "C) her şey kelimesi fiildir.",
            "D) her şey kelimesi yabancı kökenlidir.",
            "E) her şey cümlede özne olamaz."
          ],
          "correct": 0,
          "solution": "Doğru cevap 'her şey' kelimesinin doğru yazımına dikkat edilmelidir..",
          "id": "e10_q22",
          "no": 22
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde mecaz anlamlı bir sözcük kullanılmıştır? (T-287)",
          "options": [
            "A) Hava bugün çok soğuk.",
            "B) Kışın havalar soğuk olur.",
            "C) Suyu dolaptan soğuk içti.",
            "D) Buzdolabı soğuk üflüyor.",
            "E) Olaylara karşı çok 'soğuk' davranıyordu."
          ],
          "correct": 4,
          "solution": "Doğru cevap Olaylara karşı çok 'soğuk' davranıyordu..",
          "id": "e10_q23",
          "no": 23
        },
        {
          "subject": "Türkçe",
          "text": "Felsefe tarih boyunca insanlığın en büyük rehberlerinden biri olmuştur. Toplumlar Felsefe sayesinde sınırlarını aşmış, geleceğe umutla bakabilmiştir. (P-288)\nBu parçanın ana düşüncesi nedir?",
          "options": [
            "A) Felsefe, toplumsal ilerleme ve vizyon için vazgeçilmezdir.",
            "B) Felsefe zaman kaybıdır.",
            "C) Felsefe sadece bireyseldir.",
            "D) Felsefe sadece geçmişte kalmıştır.",
            "E) İnsanlar Felsefe ile ilgilenmemelidir."
          ],
          "correct": 0,
          "solution": "Doğru cevap Felsefe, toplumsal ilerleme ve vizyon için vazgeçilmezdir..",
          "id": "e10_q24",
          "no": 24
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde 'yanlış' kelimesinin yazımıyla ilgili bir kural hatırlatılmaktadır? (T-289)",
          "options": [
            "A) yanlış kelimesi fiildir.",
            "B) yanlış kelimesi yabancı kökenlidir.",
            "C) 'yanlış' kelimesinin doğru yazımına dikkat edilmelidir.",
            "D) yanlış cümlede özne olamaz.",
            "E) yanlış kelimesi her zaman ayrı yazılır."
          ],
          "correct": 2,
          "solution": "Doğru cevap 'yanlış' kelimesinin doğru yazımına dikkat edilmelidir..",
          "id": "e10_q25",
          "no": 25
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde mecaz anlamlı bir sözcük kullanılmıştır? (T-290)",
          "options": [
            "A) Buzdolabı soğuk üflüyor.",
            "B) Kışın havalar soğuk olur.",
            "C) Hava bugün çok soğuk.",
            "D) Suyu dolaptan soğuk içti.",
            "E) Olaylara karşı çok 'soğuk' davranıyordu."
          ],
          "correct": 4,
          "solution": "Doğru cevap Olaylara karşı çok 'soğuk' davranıyordu..",
          "id": "e10_q26",
          "no": 26
        },
        {
          "subject": "Türkçe",
          "text": "Edebiyat tarih boyunca insanlığın en büyük rehberlerinden biri olmuştur. Toplumlar Edebiyat sayesinde sınırlarını aşmış, geleceğe umutla bakabilmiştir. (P-291)\nBu parçanın ana düşüncesi nedir?",
          "options": [
            "A) Edebiyat zaman kaybıdır.",
            "B) İnsanlar Edebiyat ile ilgilenmemelidir.",
            "C) Edebiyat sadece bireyseldir.",
            "D) Edebiyat, toplumsal ilerleme ve vizyon için vazgeçilmezdir.",
            "E) Edebiyat sadece geçmişte kalmıştır."
          ],
          "correct": 3,
          "solution": "Doğru cevap Edebiyat, toplumsal ilerleme ve vizyon için vazgeçilmezdir..",
          "id": "e10_q27",
          "no": 27
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde 'birkaç' kelimesinin yazımıyla ilgili bir kural hatırlatılmaktadır? (T-292)",
          "options": [
            "A) birkaç kelimesi her zaman ayrı yazılır.",
            "B) birkaç cümlede özne olamaz.",
            "C) 'birkaç' kelimesinin doğru yazımına dikkat edilmelidir.",
            "D) birkaç kelimesi yabancı kökenlidir.",
            "E) birkaç kelimesi fiildir."
          ],
          "correct": 2,
          "solution": "Doğru cevap 'birkaç' kelimesinin doğru yazımına dikkat edilmelidir..",
          "id": "e10_q28",
          "no": 28
        },
        {
          "subject": "Türkçe",
          "text": "Aşağıdaki cümlelerin hangisinde mecaz anlamlı bir sözcük kullanılmıştır? (T-293)",
          "options": [
            "A) Suyu dolaptan soğuk içti.",
            "B) Olaylara karşı çok 'soğuk' davranıyordu.",
            "C) Kışın havalar soğuk olur.",
            "D) Buzdolabı soğuk üflüyor.",
            "E) Hava bugün çok soğuk."
          ],
          "correct": 1,
          "solution": "Doğru cevap Olaylara karşı çok 'soğuk' davranıyordu..",
          "id": "e10_q29",
          "no": 29
        },
        {
          "subject": "Türkçe",
          "text": "Tarih tarih boyunca insanlığın en büyük rehberlerinden biri olmuştur. Toplumlar Tarih sayesinde sınırlarını aşmış, geleceğe umutla bakabilmiştir. (P-294)\nBu parçanın ana düşüncesi nedir?",
          "options": [
            "A) Tarih, toplumsal ilerleme ve vizyon için vazgeçilmezdir.",
            "B) Tarih zaman kaybıdır.",
            "C) Tarih sadece bireyseldir.",
            "D) Tarih sadece geçmişte kalmıştır.",
            "E) İnsanlar Tarih ile ilgilenmemelidir."
          ],
          "correct": 0,
          "solution": "Doğru cevap Tarih, toplumsal ilerleme ve vizyon için vazgeçilmezdir..",
          "id": "e10_q30",
          "no": 30
        },
        {
          "subject": "Matematik",
          "text": "8x + 7 = 23 denkleminde x kaçtır? (SoruID: M270)",
          "options": [
            "A) 5",
            "B) 1",
            "C) 4",
            "D) 2",
            "E) 3"
          ],
          "correct": 3,
          "solution": "Doğru cevap 2.",
          "id": "e10_q31",
          "no": 31
        },
        {
          "subject": "Matematik",
          "text": "150 sayısının %10'si kaçtır? (SoruID: M271)",
          "options": [
            "A) 10",
            "B) 20",
            "C) 30",
            "D) 15",
            "E) 25"
          ],
          "correct": 3,
          "solution": "Doğru cevap 15.",
          "id": "e10_q32",
          "no": 32
        },
        {
          "subject": "Matematik",
          "text": "10, 21 ve 14 sayılarının aritmetik ortalaması kaçtır? (SoruID: M272)",
          "options": [
            "A) 16",
            "B) 13",
            "C) 17",
            "D) 14",
            "E) 15"
          ],
          "correct": 4,
          "solution": "Doğru cevap 15.",
          "id": "e10_q33",
          "no": 33
        },
        {
          "subject": "Matematik",
          "text": "Ali 18, Ayşe 13 yaşındadır. 6 yıl sonra yaşları toplamı kaç olur? (SoruID: M273)",
          "options": [
            "A) 49",
            "B) 44",
            "C) 42",
            "D) 43",
            "E) 37"
          ],
          "correct": 3,
          "solution": "Doğru cevap 43.",
          "id": "e10_q34",
          "no": 34
        },
        {
          "subject": "Matematik",
          "text": "√16 + √25 işleminin sonucu kaçtır? (SoruID: M274)",
          "options": [
            "A) 10",
            "B) 9",
            "C) 8",
            "D) 11",
            "E) 7"
          ],
          "correct": 1,
          "solution": "Doğru cevap 9.",
          "id": "e10_q35",
          "no": 35
        },
        {
          "subject": "Matematik",
          "text": "5x + 13 = 43 denkleminde x kaçtır? (SoruID: M275)",
          "options": [
            "A) 8",
            "B) 5",
            "C) 9",
            "D) 7",
            "E) 6"
          ],
          "correct": 4,
          "solution": "Doğru cevap 6.",
          "id": "e10_q36",
          "no": 36
        },
        {
          "subject": "Matematik",
          "text": "100 sayısının %60'si kaçtır? (SoruID: M276)",
          "options": [
            "A) 60",
            "B) 75",
            "C) 55",
            "D) 65",
            "E) 70"
          ],
          "correct": 0,
          "solution": "Doğru cevap 60.",
          "id": "e10_q37",
          "no": 37
        },
        {
          "subject": "Matematik",
          "text": "25, 22 ve 13 sayılarının aritmetik ortalaması kaçtır? (SoruID: M277)",
          "options": [
            "A) 22",
            "B) 18",
            "C) 21",
            "D) 20",
            "E) 19"
          ],
          "correct": 3,
          "solution": "Doğru cevap 20.",
          "id": "e10_q38",
          "no": 38
        },
        {
          "subject": "Matematik",
          "text": "Ali 15, Ayşe 19 yaşındadır. 9 yıl sonra yaşları toplamı kaç olur? (SoruID: M278)",
          "options": [
            "A) 53",
            "B) 52",
            "C) 61",
            "D) 43",
            "E) 51"
          ],
          "correct": 1,
          "solution": "Doğru cevap 52.",
          "id": "e10_q39",
          "no": 39
        },
        {
          "subject": "Matematik",
          "text": "√36 + √16 işleminin sonucu kaçtır? (SoruID: M279)",
          "options": [
            "A) 9",
            "B) 10",
            "C) 11",
            "D) 8",
            "E) 12"
          ],
          "correct": 1,
          "solution": "Doğru cevap 10.",
          "id": "e10_q40",
          "no": 40
        },
        {
          "subject": "Matematik",
          "text": "4x + 45 = 85 denkleminde x kaçtır? (SoruID: M280)",
          "options": [
            "A) 10",
            "B) 13",
            "C) 11",
            "D) 9",
            "E) 12"
          ],
          "correct": 0,
          "solution": "Doğru cevap 10.",
          "id": "e10_q41",
          "no": 41
        },
        {
          "subject": "Matematik",
          "text": "160 sayısının %60'si kaçtır? (SoruID: M281)",
          "options": [
            "A) 111",
            "B) 106",
            "C) 101",
            "D) 91",
            "E) 96"
          ],
          "correct": 4,
          "solution": "Doğru cevap 96.",
          "id": "e10_q42",
          "no": 42
        },
        {
          "subject": "Matematik",
          "text": "12, 17 ve 31 sayılarının aritmetik ortalaması kaçtır? (SoruID: M282)",
          "options": [
            "A) 18",
            "B) 20",
            "C) 19",
            "D) 22",
            "E) 21"
          ],
          "correct": 1,
          "solution": "Doğru cevap 20.",
          "id": "e10_q43",
          "no": 43
        },
        {
          "subject": "Matematik",
          "text": "Ali 21, Ayşe 20 yaşındadır. 3 yıl sonra yaşları toplamı kaç olur? (SoruID: M283)",
          "options": [
            "A) 47",
            "B) 46",
            "C) 50",
            "D) 48",
            "E) 44"
          ],
          "correct": 0,
          "solution": "Doğru cevap 47.",
          "id": "e10_q44",
          "no": 44
        },
        {
          "subject": "Matematik",
          "text": "√4 + √64 işleminin sonucu kaçtır? (SoruID: M284)",
          "options": [
            "A) 8",
            "B) 12",
            "C) 11",
            "D) 9",
            "E) 10"
          ],
          "correct": 4,
          "solution": "Doğru cevap 10.",
          "id": "e10_q45",
          "no": 45
        },
        {
          "subject": "Matematik",
          "text": "5x + 18 = 38 denkleminde x kaçtır? (SoruID: M285)",
          "options": [
            "A) 5",
            "B) 4",
            "C) 3",
            "D) 6",
            "E) 7"
          ],
          "correct": 1,
          "solution": "Doğru cevap 4.",
          "id": "e10_q46",
          "no": 46
        },
        {
          "subject": "Matematik",
          "text": "160 sayısının %75'si kaçtır? (SoruID: M286)",
          "options": [
            "A) 115",
            "B) 130",
            "C) 135",
            "D) 120",
            "E) 125"
          ],
          "correct": 3,
          "solution": "Doğru cevap 120.",
          "id": "e10_q47",
          "no": 47
        },
        {
          "subject": "Matematik",
          "text": "19, 18 ve 20 sayılarının aritmetik ortalaması kaçtır? (SoruID: M287)",
          "options": [
            "A) 20",
            "B) 17",
            "C) 19",
            "D) 18",
            "E) 21"
          ],
          "correct": 2,
          "solution": "Doğru cevap 19.",
          "id": "e10_q48",
          "no": 48
        },
        {
          "subject": "Matematik",
          "text": "Ali 24, Ayşe 15 yaşındadır. 3 yıl sonra yaşları toplamı kaç olur? (SoruID: M288)",
          "options": [
            "A) 48",
            "B) 45",
            "C) 44",
            "D) 46",
            "E) 42"
          ],
          "correct": 1,
          "solution": "Doğru cevap 45.",
          "id": "e10_q49",
          "no": 49
        },
        {
          "subject": "Matematik",
          "text": "√16 + √64 işleminin sonucu kaçtır? (SoruID: M289)",
          "options": [
            "A) 10",
            "B) 11",
            "C) 13",
            "D) 12",
            "E) 14"
          ],
          "correct": 3,
          "solution": "Doğru cevap 12.",
          "id": "e10_q50",
          "no": 50
        },
        {
          "subject": "Matematik",
          "text": "8x + 42 = 114 denkleminde x kaçtır? (SoruID: M290)",
          "options": [
            "A) 12",
            "B) 10",
            "C) 9",
            "D) 8",
            "E) 11"
          ],
          "correct": 2,
          "solution": "Doğru cevap 9.",
          "id": "e10_q51",
          "no": 51
        },
        {
          "subject": "Matematik",
          "text": "130 sayısının %10'si kaçtır? (SoruID: M291)",
          "options": [
            "A) 28",
            "B) 8",
            "C) 13",
            "D) 23",
            "E) 18"
          ],
          "correct": 2,
          "solution": "Doğru cevap 13.",
          "id": "e10_q52",
          "no": 52
        },
        {
          "subject": "Matematik",
          "text": "28, 23 ve 15 sayılarının aritmetik ortalaması kaçtır? (SoruID: M292)",
          "options": [
            "A) 24",
            "B) 20",
            "C) 21",
            "D) 22",
            "E) 23"
          ],
          "correct": 3,
          "solution": "Doğru cevap 22.",
          "id": "e10_q53",
          "no": 53
        },
        {
          "subject": "Matematik",
          "text": "Ali 23, Ayşe 20 yaşındadır. 6 yıl sonra yaşları toplamı kaç olur? (SoruID: M293)",
          "options": [
            "A) 61",
            "B) 49",
            "C) 55",
            "D) 56",
            "E) 54"
          ],
          "correct": 2,
          "solution": "Doğru cevap 55.",
          "id": "e10_q54",
          "no": 54
        },
        {
          "subject": "Matematik",
          "text": "√4 + √4 işleminin sonucu kaçtır? (SoruID: M294)",
          "options": [
            "A) 3",
            "B) 4",
            "C) 5",
            "D) 6",
            "E) 2"
          ],
          "correct": 1,
          "solution": "Doğru cevap 4.",
          "id": "e10_q55",
          "no": 55
        },
        {
          "subject": "Matematik",
          "text": "2x + 37 = 43 denkleminde x kaçtır? (SoruID: M295)",
          "options": [
            "A) 2",
            "B) 5",
            "C) 3",
            "D) 6",
            "E) 4"
          ],
          "correct": 2,
          "solution": "Doğru cevap 3.",
          "id": "e10_q56",
          "no": 56
        },
        {
          "subject": "Matematik",
          "text": "40 sayısının %20'si kaçtır? (SoruID: M296)",
          "options": [
            "A) 8",
            "B) 23",
            "C) 3",
            "D) 18",
            "E) 13"
          ],
          "correct": 0,
          "solution": "Doğru cevap 8.",
          "id": "e10_q57",
          "no": 57
        },
        {
          "subject": "Matematik",
          "text": "19, 15 ve 26 sayılarının aritmetik ortalaması kaçtır? (SoruID: M297)",
          "options": [
            "A) 19",
            "B) 22",
            "C) 20",
            "D) 21",
            "E) 18"
          ],
          "correct": 2,
          "solution": "Doğru cevap 20.",
          "id": "e10_q58",
          "no": 58
        },
        {
          "subject": "Matematik",
          "text": "Ali 14, Ayşe 18 yaşındadır. 7 yıl sonra yaşları toplamı kaç olur? (SoruID: M298)",
          "options": [
            "A) 47",
            "B) 39",
            "C) 45",
            "D) 46",
            "E) 53"
          ],
          "correct": 3,
          "solution": "Doğru cevap 46.",
          "id": "e10_q59",
          "no": 59
        },
        {
          "subject": "Matematik",
          "text": "√36 + √64 işleminin sonucu kaçtır? (SoruID: M299)",
          "options": [
            "A) 15",
            "B) 12",
            "C) 14",
            "D) 13",
            "E) 16"
          ],
          "correct": 2,
          "solution": "Doğru cevap 14.",
          "id": "e10_q60",
          "no": 60
        },
        {
          "subject": "Tarih",
          "text": "Türk siyasi ve askerî tarihinde büyük öneme sahip olan 'Sivas Kongresi' süreci ile ilgili aşağıdakilerden hangisi söylenebilir? (H-240)",
          "options": [
            "A) Sadece ekonomik bir olaydır.",
            "B) Osmanlı'nın kuruluş dönemine aittir.",
            "C) Avrupa'da gerçekleşmiştir.",
            "D) Hiçbir etkisi olmamıştır.",
            "E) Sivas Kongresi dönemin en kritik gelişmelerinden biridir."
          ],
          "correct": 4,
          "solution": "Doğru cevap Sivas Kongresi dönemin en kritik gelişmelerinden biridir..",
          "id": "e10_q61",
          "no": 61
        },
        {
          "subject": "Tarih",
          "text": "Aşağıdaki tarihî gelişmelerden hangisi 'Erzurum Kongresi' ile doğrudan veya dolaylı olarak bağlantılıdır? (H-241)",
          "options": [
            "A) Sanayi İnkılabı",
            "B) Fransız İhtilali",
            "C) Erzurum Kongresi öncesi ve sonrası yaşanan siyasi krizler.",
            "D) Coğrafi Keşifler",
            "E) Kavimler Göçü"
          ],
          "correct": 2,
          "solution": "Doğru cevap Erzurum Kongresi öncesi ve sonrası yaşanan siyasi krizler..",
          "id": "e10_q62",
          "no": 62
        },
        {
          "subject": "Tarih",
          "text": "Millî Mücadele ve inkılaplar tarihi incelendiğinde 'Amasya Genelgesi' olayının temel amacı aşağıdakilerden hangisidir? (H-242)",
          "options": [
            "A) Feodaliteyi kurmak",
            "B) Saltanatı güçlendirmek",
            "C) Yeni sömürgeler elde etmek",
            "D) Avrupa'ya göç etmek",
            "E) Bağımsızlık ve egemenliği pekiştirmek"
          ],
          "correct": 4,
          "solution": "Doğru cevap Bağımsızlık ve egemenliği pekiştirmek.",
          "id": "e10_q63",
          "no": 63
        },
        {
          "subject": "Tarih",
          "text": "Türk siyasi ve askerî tarihinde büyük öneme sahip olan 'Lozan Antlaşması' süreci ile ilgili aşağıdakilerden hangisi söylenebilir? (H-243)",
          "options": [
            "A) Sadece ekonomik bir olaydır.",
            "B) Osmanlı'nın kuruluş dönemine aittir.",
            "C) Lozan Antlaşması dönemin en kritik gelişmelerinden biridir.",
            "D) Hiçbir etkisi olmamıştır.",
            "E) Avrupa'da gerçekleşmiştir."
          ],
          "correct": 2,
          "solution": "Doğru cevap Lozan Antlaşması dönemin en kritik gelişmelerinden biridir..",
          "id": "e10_q64",
          "no": 64
        },
        {
          "subject": "Tarih",
          "text": "Aşağıdaki tarihî gelişmelerden hangisi 'Cumhuriyetin İlanı' ile doğrudan veya dolaylı olarak bağlantılıdır? (H-244)",
          "options": [
            "A) Fransız İhtilali",
            "B) Cumhuriyetin İlanı öncesi ve sonrası yaşanan siyasi krizler.",
            "C) Coğrafi Keşifler",
            "D) Sanayi İnkılabı",
            "E) Kavimler Göçü"
          ],
          "correct": 1,
          "solution": "Doğru cevap Cumhuriyetin İlanı öncesi ve sonrası yaşanan siyasi krizler..",
          "id": "e10_q65",
          "no": 65
        },
        {
          "subject": "Tarih",
          "text": "Millî Mücadele ve inkılaplar tarihi incelendiğinde 'TBMM'nin Açılışı' olayının temel amacı aşağıdakilerden hangisidir? (H-245)",
          "options": [
            "A) Yeni sömürgeler elde etmek",
            "B) Bağımsızlık ve egemenliği pekiştirmek",
            "C) Saltanatı güçlendirmek",
            "D) Avrupa'ya göç etmek",
            "E) Feodaliteyi kurmak"
          ],
          "correct": 1,
          "solution": "Doğru cevap Bağımsızlık ve egemenliği pekiştirmek.",
          "id": "e10_q66",
          "no": 66
        },
        {
          "subject": "Tarih",
          "text": "Türk siyasi ve askerî tarihinde büyük öneme sahip olan 'Mudanya Mütarekesi' süreci ile ilgili aşağıdakilerden hangisi söylenebilir? (H-246)",
          "options": [
            "A) Avrupa'da gerçekleşmiştir.",
            "B) Hiçbir etkisi olmamıştır.",
            "C) Sadece ekonomik bir olaydır.",
            "D) Osmanlı'nın kuruluş dönemine aittir.",
            "E) Mudanya Mütarekesi dönemin en kritik gelişmelerinden biridir."
          ],
          "correct": 4,
          "solution": "Doğru cevap Mudanya Mütarekesi dönemin en kritik gelişmelerinden biridir..",
          "id": "e10_q67",
          "no": 67
        },
        {
          "subject": "Tarih",
          "text": "Aşağıdaki tarihî gelişmelerden hangisi 'Saltanatın Kaldırılması' ile doğrudan veya dolaylı olarak bağlantılıdır? (H-247)",
          "options": [
            "A) Fransız İhtilali",
            "B) Sanayi İnkılabı",
            "C) Coğrafi Keşifler",
            "D) Saltanatın Kaldırılması öncesi ve sonrası yaşanan siyasi krizler.",
            "E) Kavimler Göçü"
          ],
          "correct": 3,
          "solution": "Doğru cevap Saltanatın Kaldırılması öncesi ve sonrası yaşanan siyasi krizler..",
          "id": "e10_q68",
          "no": 68
        },
        {
          "subject": "Tarih",
          "text": "Millî Mücadele ve inkılaplar tarihi incelendiğinde 'Halifeliğin Kaldırılması' olayının temel amacı aşağıdakilerden hangisidir? (H-248)",
          "options": [
            "A) Avrupa'ya göç etmek",
            "B) Saltanatı güçlendirmek",
            "C) Yeni sömürgeler elde etmek",
            "D) Bağımsızlık ve egemenliği pekiştirmek",
            "E) Feodaliteyi kurmak"
          ],
          "correct": 3,
          "solution": "Doğru cevap Bağımsızlık ve egemenliği pekiştirmek.",
          "id": "e10_q69",
          "no": 69
        },
        {
          "subject": "Tarih",
          "text": "Türk siyasi ve askerî tarihinde büyük öneme sahip olan 'Tevhid-i Tedrisat' süreci ile ilgili aşağıdakilerden hangisi söylenebilir? (H-249)",
          "options": [
            "A) Tevhid-i Tedrisat dönemin en kritik gelişmelerinden biridir.",
            "B) Osmanlı'nın kuruluş dönemine aittir.",
            "C) Avrupa'da gerçekleşmiştir.",
            "D) Hiçbir etkisi olmamıştır.",
            "E) Sadece ekonomik bir olaydır."
          ],
          "correct": 0,
          "solution": "Doğru cevap Tevhid-i Tedrisat dönemin en kritik gelişmelerinden biridir..",
          "id": "e10_q70",
          "no": 70
        },
        {
          "subject": "Tarih",
          "text": "Aşağıdaki tarihî gelişmelerden hangisi 'Trablusgarp Savaşı' ile doğrudan veya dolaylı olarak bağlantılıdır? (H-250)",
          "options": [
            "A) Kavimler Göçü",
            "B) Fransız İhtilali",
            "C) Sanayi İnkılabı",
            "D) Coğrafi Keşifler",
            "E) Trablusgarp Savaşı öncesi ve sonrası yaşanan siyasi krizler."
          ],
          "correct": 4,
          "solution": "Doğru cevap Trablusgarp Savaşı öncesi ve sonrası yaşanan siyasi krizler..",
          "id": "e10_q71",
          "no": 71
        },
        {
          "subject": "Tarih",
          "text": "Millî Mücadele ve inkılaplar tarihi incelendiğinde 'Balkan Savaşları' olayının temel amacı aşağıdakilerden hangisidir? (H-251)",
          "options": [
            "A) Avrupa'ya göç etmek",
            "B) Feodaliteyi kurmak",
            "C) Saltanatı güçlendirmek",
            "D) Yeni sömürgeler elde etmek",
            "E) Bağımsızlık ve egemenliği pekiştirmek"
          ],
          "correct": 4,
          "solution": "Doğru cevap Bağımsızlık ve egemenliği pekiştirmek.",
          "id": "e10_q72",
          "no": 72
        },
        {
          "subject": "Tarih",
          "text": "Türk siyasi ve askerî tarihinde büyük öneme sahip olan 'I. Dünya Savaşı' süreci ile ilgili aşağıdakilerden hangisi söylenebilir? (H-252)",
          "options": [
            "A) Osmanlı'nın kuruluş dönemine aittir.",
            "B) I. Dünya Savaşı dönemin en kritik gelişmelerinden biridir.",
            "C) Sadece ekonomik bir olaydır.",
            "D) Hiçbir etkisi olmamıştır.",
            "E) Avrupa'da gerçekleşmiştir."
          ],
          "correct": 1,
          "solution": "Doğru cevap I. Dünya Savaşı dönemin en kritik gelişmelerinden biridir..",
          "id": "e10_q73",
          "no": 73
        },
        {
          "subject": "Tarih",
          "text": "Aşağıdaki tarihî gelişmelerden hangisi 'Çanakkale Cephesi' ile doğrudan veya dolaylı olarak bağlantılıdır? (H-253)",
          "options": [
            "A) Sanayi İnkılabı",
            "B) Coğrafi Keşifler",
            "C) Fransız İhtilali",
            "D) Çanakkale Cephesi öncesi ve sonrası yaşanan siyasi krizler.",
            "E) Kavimler Göçü"
          ],
          "correct": 3,
          "solution": "Doğru cevap Çanakkale Cephesi öncesi ve sonrası yaşanan siyasi krizler..",
          "id": "e10_q74",
          "no": 74
        },
        {
          "subject": "Tarih",
          "text": "Millî Mücadele ve inkılaplar tarihi incelendiğinde 'Sakarya Meydan Muharebesi' olayının temel amacı aşağıdakilerden hangisidir? (H-254)",
          "options": [
            "A) Avrupa'ya göç etmek",
            "B) Bağımsızlık ve egemenliği pekiştirmek",
            "C) Feodaliteyi kurmak",
            "D) Yeni sömürgeler elde etmek",
            "E) Saltanatı güçlendirmek"
          ],
          "correct": 1,
          "solution": "Doğru cevap Bağımsızlık ve egemenliği pekiştirmek.",
          "id": "e10_q75",
          "no": 75
        },
        {
          "subject": "Tarih",
          "text": "Türk siyasi ve askerî tarihinde büyük öneme sahip olan 'Büyük Taarruz' süreci ile ilgili aşağıdakilerden hangisi söylenebilir? (H-255)",
          "options": [
            "A) Osmanlı'nın kuruluş dönemine aittir.",
            "B) Büyük Taarruz dönemin en kritik gelişmelerinden biridir.",
            "C) Avrupa'da gerçekleşmiştir.",
            "D) Sadece ekonomik bir olaydır.",
            "E) Hiçbir etkisi olmamıştır."
          ],
          "correct": 1,
          "solution": "Doğru cevap Büyük Taarruz dönemin en kritik gelişmelerinden biridir..",
          "id": "e10_q76",
          "no": 76
        },
        {
          "subject": "Tarih",
          "text": "Aşağıdaki tarihî gelişmelerden hangisi 'I. İnönü Muharebesi' ile doğrudan veya dolaylı olarak bağlantılıdır? (H-256)",
          "options": [
            "A) Fransız İhtilali",
            "B) Kavimler Göçü",
            "C) Coğrafi Keşifler",
            "D) I. İnönü Muharebesi öncesi ve sonrası yaşanan siyasi krizler.",
            "E) Sanayi İnkılabı"
          ],
          "correct": 3,
          "solution": "Doğru cevap I. İnönü Muharebesi öncesi ve sonrası yaşanan siyasi krizler..",
          "id": "e10_q77",
          "no": 77
        },
        {
          "subject": "Tarih",
          "text": "Millî Mücadele ve inkılaplar tarihi incelendiğinde 'II. İnönü Muharebesi' olayının temel amacı aşağıdakilerden hangisidir? (H-257)",
          "options": [
            "A) Bağımsızlık ve egemenliği pekiştirmek",
            "B) Feodaliteyi kurmak",
            "C) Yeni sömürgeler elde etmek",
            "D) Saltanatı güçlendirmek",
            "E) Avrupa'ya göç etmek"
          ],
          "correct": 0,
          "solution": "Doğru cevap Bağımsızlık ve egemenliği pekiştirmek.",
          "id": "e10_q78",
          "no": 78
        },
        {
          "subject": "Tarih",
          "text": "Türk siyasi ve askerî tarihinde büyük öneme sahip olan 'Kars Antlaşması' süreci ile ilgili aşağıdakilerden hangisi söylenebilir? (H-258)",
          "options": [
            "A) Hiçbir etkisi olmamıştır.",
            "B) Osmanlı'nın kuruluş dönemine aittir.",
            "C) Avrupa'da gerçekleşmiştir.",
            "D) Sadece ekonomik bir olaydır.",
            "E) Kars Antlaşması dönemin en kritik gelişmelerinden biridir."
          ],
          "correct": 4,
          "solution": "Doğru cevap Kars Antlaşması dönemin en kritik gelişmelerinden biridir..",
          "id": "e10_q79",
          "no": 79
        },
        {
          "subject": "Tarih",
          "text": "Aşağıdaki tarihî gelişmelerden hangisi 'Ankara Antlaşması' ile doğrudan veya dolaylı olarak bağlantılıdır? (H-259)",
          "options": [
            "A) Coğrafi Keşifler",
            "B) Ankara Antlaşması öncesi ve sonrası yaşanan siyasi krizler.",
            "C) Sanayi İnkılabı",
            "D) Fransız İhtilali",
            "E) Kavimler Göçü"
          ],
          "correct": 1,
          "solution": "Doğru cevap Ankara Antlaşması öncesi ve sonrası yaşanan siyasi krizler..",
          "id": "e10_q80",
          "no": 80
        },
        {
          "subject": "Tarih",
          "text": "Millî Mücadele ve inkılaplar tarihi incelendiğinde 'Sivas Kongresi' olayının temel amacı aşağıdakilerden hangisidir? (H-260)",
          "options": [
            "A) Saltanatı güçlendirmek",
            "B) Feodaliteyi kurmak",
            "C) Avrupa'ya göç etmek",
            "D) Bağımsızlık ve egemenliği pekiştirmek",
            "E) Yeni sömürgeler elde etmek"
          ],
          "correct": 3,
          "solution": "Doğru cevap Bağımsızlık ve egemenliği pekiştirmek.",
          "id": "e10_q81",
          "no": 81
        },
        {
          "subject": "Tarih",
          "text": "Türk siyasi ve askerî tarihinde büyük öneme sahip olan 'Erzurum Kongresi' süreci ile ilgili aşağıdakilerden hangisi söylenebilir? (H-261)",
          "options": [
            "A) Hiçbir etkisi olmamıştır.",
            "B) Osmanlı'nın kuruluş dönemine aittir.",
            "C) Erzurum Kongresi dönemin en kritik gelişmelerinden biridir.",
            "D) Sadece ekonomik bir olaydır.",
            "E) Avrupa'da gerçekleşmiştir."
          ],
          "correct": 2,
          "solution": "Doğru cevap Erzurum Kongresi dönemin en kritik gelişmelerinden biridir..",
          "id": "e10_q82",
          "no": 82
        },
        {
          "subject": "Tarih",
          "text": "Aşağıdaki tarihî gelişmelerden hangisi 'Amasya Genelgesi' ile doğrudan veya dolaylı olarak bağlantılıdır? (H-262)",
          "options": [
            "A) Coğrafi Keşifler",
            "B) Amasya Genelgesi öncesi ve sonrası yaşanan siyasi krizler.",
            "C) Sanayi İnkılabı",
            "D) Fransız İhtilali",
            "E) Kavimler Göçü"
          ],
          "correct": 1,
          "solution": "Doğru cevap Amasya Genelgesi öncesi ve sonrası yaşanan siyasi krizler..",
          "id": "e10_q83",
          "no": 83
        },
        {
          "subject": "Tarih",
          "text": "Millî Mücadele ve inkılaplar tarihi incelendiğinde 'Lozan Antlaşması' olayının temel amacı aşağıdakilerden hangisidir? (H-263)",
          "options": [
            "A) Saltanatı güçlendirmek",
            "B) Feodaliteyi kurmak",
            "C) Bağımsızlık ve egemenliği pekiştirmek",
            "D) Avrupa'ya göç etmek",
            "E) Yeni sömürgeler elde etmek"
          ],
          "correct": 2,
          "solution": "Doğru cevap Bağımsızlık ve egemenliği pekiştirmek.",
          "id": "e10_q84",
          "no": 84
        },
        {
          "subject": "Tarih",
          "text": "Türk siyasi ve askerî tarihinde büyük öneme sahip olan 'Cumhuriyetin İlanı' süreci ile ilgili aşağıdakilerden hangisi söylenebilir? (H-264)",
          "options": [
            "A) Avrupa'da gerçekleşmiştir.",
            "B) Cumhuriyetin İlanı dönemin en kritik gelişmelerinden biridir.",
            "C) Osmanlı'nın kuruluş dönemine aittir.",
            "D) Hiçbir etkisi olmamıştır.",
            "E) Sadece ekonomik bir olaydır."
          ],
          "correct": 1,
          "solution": "Doğru cevap Cumhuriyetin İlanı dönemin en kritik gelişmelerinden biridir..",
          "id": "e10_q85",
          "no": 85
        },
        {
          "subject": "Tarih",
          "text": "Aşağıdaki tarihî gelişmelerden hangisi 'TBMM'nin Açılışı' ile doğrudan veya dolaylı olarak bağlantılıdır? (H-265)",
          "options": [
            "A) Kavimler Göçü",
            "B) Sanayi İnkılabı",
            "C) TBMM'nin Açılışı öncesi ve sonrası yaşanan siyasi krizler.",
            "D) Fransız İhtilali",
            "E) Coğrafi Keşifler"
          ],
          "correct": 2,
          "solution": "Doğru cevap TBMM'nin Açılışı öncesi ve sonrası yaşanan siyasi krizler..",
          "id": "e10_q86",
          "no": 86
        },
        {
          "subject": "Tarih",
          "text": "Millî Mücadele ve inkılaplar tarihi incelendiğinde 'Mudanya Mütarekesi' olayının temel amacı aşağıdakilerden hangisidir? (H-266)",
          "options": [
            "A) Feodaliteyi kurmak",
            "B) Avrupa'ya göç etmek",
            "C) Saltanatı güçlendirmek",
            "D) Yeni sömürgeler elde etmek",
            "E) Bağımsızlık ve egemenliği pekiştirmek"
          ],
          "correct": 4,
          "solution": "Doğru cevap Bağımsızlık ve egemenliği pekiştirmek.",
          "id": "e10_q87",
          "no": 87
        },
        {
          "subject": "Coğrafya",
          "text": "Türkiye'nin fiziki coğrafyası düşünüldüğünde 'Kapadokya' için aşağıdakilerden hangisi doğrudur? (C-160)",
          "options": [
            "A) Kapadokya tarıma kapalıdır.",
            "B) Kapadokya, ülkemizin önemli yeryüzü şekillerinden biridir.",
            "C) Kapadokya bir çöldür.",
            "D) Kapadokya Marmara'dadır.",
            "E) Kapadokya yapay bir kanaldır."
          ],
          "correct": 1,
          "solution": "Doğru cevap Kapadokya, ülkemizin önemli yeryüzü şekillerinden biridir..",
          "id": "e10_q88",
          "no": 88
        },
        {
          "subject": "Coğrafya",
          "text": "Coğrafi özellikleri ve turizm potansiyeli göz önüne alındığında 'Pamukkale' hangi alanda daha çok öne çıkar? (C-161)",
          "options": [
            "A) Doğal güzellikleri ve turizm/coğrafi önemi",
            "B) Sadece ağır sanayi",
            "C) Sadece madencilik",
            "D) Okyanus balıkçılığı",
            "E) Çöl iklimi araştırmaları"
          ],
          "correct": 0,
          "solution": "Doğru cevap Doğal güzellikleri ve turizm/coğrafi önemi.",
          "id": "e10_q89",
          "no": 89
        },
        {
          "subject": "Coğrafya",
          "text": "Türkiye'nin fiziki coğrafyası düşünüldüğünde 'Nemrut Dağı' için aşağıdakilerden hangisi doğrudur? (C-162)",
          "options": [
            "A) Nemrut Dağı yapay bir kanaldır.",
            "B) Nemrut Dağı Marmara'dadır.",
            "C) Nemrut Dağı bir çöldür.",
            "D) Nemrut Dağı, ülkemizin önemli yeryüzü şekillerinden biridir.",
            "E) Nemrut Dağı tarıma kapalıdır."
          ],
          "correct": 3,
          "solution": "Doğru cevap Nemrut Dağı, ülkemizin önemli yeryüzü şekillerinden biridir..",
          "id": "e10_q90",
          "no": 90
        },
        {
          "subject": "Coğrafya",
          "text": "Coğrafi özellikleri ve turizm potansiyeli göz önüne alındığında 'Sümela Manastırı' hangi alanda daha çok öne çıkar? (C-163)",
          "options": [
            "A) Doğal güzellikleri ve turizm/coğrafi önemi",
            "B) Okyanus balıkçılığı",
            "C) Çöl iklimi araştırmaları",
            "D) Sadece ağır sanayi",
            "E) Sadece madencilik"
          ],
          "correct": 0,
          "solution": "Doğru cevap Doğal güzellikleri ve turizm/coğrafi önemi.",
          "id": "e10_q91",
          "no": 91
        },
        {
          "subject": "Coğrafya",
          "text": "Türkiye'nin fiziki coğrafyası düşünüldüğünde 'Uludağ' için aşağıdakilerden hangisi doğrudur? (C-164)",
          "options": [
            "A) Uludağ bir çöldür.",
            "B) Uludağ tarıma kapalıdır.",
            "C) Uludağ Marmara'dadır.",
            "D) Uludağ yapay bir kanaldır.",
            "E) Uludağ, ülkemizin önemli yeryüzü şekillerinden biridir."
          ],
          "correct": 4,
          "solution": "Doğru cevap Uludağ, ülkemizin önemli yeryüzü şekillerinden biridir..",
          "id": "e10_q92",
          "no": 92
        },
        {
          "subject": "Coğrafya",
          "text": "Coğrafi özellikleri ve turizm potansiyeli göz önüne alındığında 'Van Gölü' hangi alanda daha çok öne çıkar? (C-165)",
          "options": [
            "A) Sadece ağır sanayi",
            "B) Okyanus balıkçılığı",
            "C) Doğal güzellikleri ve turizm/coğrafi önemi",
            "D) Çöl iklimi araştırmaları",
            "E) Sadece madencilik"
          ],
          "correct": 2,
          "solution": "Doğru cevap Doğal güzellikleri ve turizm/coğrafi önemi.",
          "id": "e10_q93",
          "no": 93
        },
        {
          "subject": "Coğrafya",
          "text": "Türkiye'nin fiziki coğrafyası düşünüldüğünde 'Ağrı Dağı' için aşağıdakilerden hangisi doğrudur? (C-166)",
          "options": [
            "A) Ağrı Dağı tarıma kapalıdır.",
            "B) Ağrı Dağı Marmara'dadır.",
            "C) Ağrı Dağı, ülkemizin önemli yeryüzü şekillerinden biridir.",
            "D) Ağrı Dağı yapay bir kanaldır.",
            "E) Ağrı Dağı bir çöldür."
          ],
          "correct": 2,
          "solution": "Doğru cevap Ağrı Dağı, ülkemizin önemli yeryüzü şekillerinden biridir..",
          "id": "e10_q94",
          "no": 94
        },
        {
          "subject": "Coğrafya",
          "text": "Coğrafi özellikleri ve turizm potansiyeli göz önüne alındığında 'Kızılırmak' hangi alanda daha çok öne çıkar? (C-167)",
          "options": [
            "A) Okyanus balıkçılığı",
            "B) Doğal güzellikleri ve turizm/coğrafi önemi",
            "C) Sadece madencilik",
            "D) Çöl iklimi araştırmaları",
            "E) Sadece ağır sanayi"
          ],
          "correct": 1,
          "solution": "Doğru cevap Doğal güzellikleri ve turizm/coğrafi önemi.",
          "id": "e10_q95",
          "no": 95
        },
        {
          "subject": "Coğrafya",
          "text": "Türkiye'nin fiziki coğrafyası düşünüldüğünde 'Erciyes Dağı' için aşağıdakilerden hangisi doğrudur? (C-168)",
          "options": [
            "A) Erciyes Dağı bir çöldür.",
            "B) Erciyes Dağı yapay bir kanaldır.",
            "C) Erciyes Dağı tarıma kapalıdır.",
            "D) Erciyes Dağı, ülkemizin önemli yeryüzü şekillerinden biridir.",
            "E) Erciyes Dağı Marmara'dadır."
          ],
          "correct": 3,
          "solution": "Doğru cevap Erciyes Dağı, ülkemizin önemli yeryüzü şekillerinden biridir..",
          "id": "e10_q96",
          "no": 96
        },
        {
          "subject": "Coğrafya",
          "text": "Coğrafi özellikleri ve turizm potansiyeli göz önüne alındığında 'Tuz Gölü' hangi alanda daha çok öne çıkar? (C-169)",
          "options": [
            "A) Sadece ağır sanayi",
            "B) Sadece madencilik",
            "C) Çöl iklimi araştırmaları",
            "D) Okyanus balıkçılığı",
            "E) Doğal güzellikleri ve turizm/coğrafi önemi"
          ],
          "correct": 4,
          "solution": "Doğru cevap Doğal güzellikleri ve turizm/coğrafi önemi.",
          "id": "e10_q97",
          "no": 97
        },
        {
          "subject": "Coğrafya",
          "text": "Türkiye'nin fiziki coğrafyası düşünüldüğünde 'Çukurova' için aşağıdakilerden hangisi doğrudur? (C-170)",
          "options": [
            "A) Çukurova, ülkemizin önemli yeryüzü şekillerinden biridir.",
            "B) Çukurova bir çöldür.",
            "C) Çukurova Marmara'dadır.",
            "D) Çukurova tarıma kapalıdır.",
            "E) Çukurova yapay bir kanaldır."
          ],
          "correct": 0,
          "solution": "Doğru cevap Çukurova, ülkemizin önemli yeryüzü şekillerinden biridir..",
          "id": "e10_q98",
          "no": 98
        },
        {
          "subject": "Coğrafya",
          "text": "Coğrafi özellikleri ve turizm potansiyeli göz önüne alındığında 'Bafra Ovası' hangi alanda daha çok öne çıkar? (C-171)",
          "options": [
            "A) Çöl iklimi araştırmaları",
            "B) Sadece ağır sanayi",
            "C) Sadece madencilik",
            "D) Okyanus balıkçılığı",
            "E) Doğal güzellikleri ve turizm/coğrafi önemi"
          ],
          "correct": 4,
          "solution": "Doğru cevap Doğal güzellikleri ve turizm/coğrafi önemi.",
          "id": "e10_q99",
          "no": 99
        },
        {
          "subject": "Coğrafya",
          "text": "Türkiye'nin fiziki coğrafyası düşünüldüğünde 'Kaçkar Dağları' için aşağıdakilerden hangisi doğrudur? (C-172)",
          "options": [
            "A) Kaçkar Dağları yapay bir kanaldır.",
            "B) Kaçkar Dağları tarıma kapalıdır.",
            "C) Kaçkar Dağları, ülkemizin önemli yeryüzü şekillerinden biridir.",
            "D) Kaçkar Dağları Marmara'dadır.",
            "E) Kaçkar Dağları bir çöldür."
          ],
          "correct": 2,
          "solution": "Doğru cevap Kaçkar Dağları, ülkemizin önemli yeryüzü şekillerinden biridir..",
          "id": "e10_q100",
          "no": 100
        },
        {
          "subject": "Coğrafya",
          "text": "Coğrafi özellikleri ve turizm potansiyeli göz önüne alındığında 'Gediz Nehri' hangi alanda daha çok öne çıkar? (C-173)",
          "options": [
            "A) Sadece ağır sanayi",
            "B) Okyanus balıkçılığı",
            "C) Doğal güzellikleri ve turizm/coğrafi önemi",
            "D) Sadece madencilik",
            "E) Çöl iklimi araştırmaları"
          ],
          "correct": 2,
          "solution": "Doğru cevap Doğal güzellikleri ve turizm/coğrafi önemi.",
          "id": "e10_q101",
          "no": 101
        },
        {
          "subject": "Coğrafya",
          "text": "Türkiye'nin fiziki coğrafyası düşünüldüğünde 'Salda Gölü' için aşağıdakilerden hangisi doğrudur? (C-174)",
          "options": [
            "A) Salda Gölü tarıma kapalıdır.",
            "B) Salda Gölü bir çöldür.",
            "C) Salda Gölü, ülkemizin önemli yeryüzü şekillerinden biridir.",
            "D) Salda Gölü Marmara'dadır.",
            "E) Salda Gölü yapay bir kanaldır."
          ],
          "correct": 2,
          "solution": "Doğru cevap Salda Gölü, ülkemizin önemli yeryüzü şekillerinden biridir..",
          "id": "e10_q102",
          "no": 102
        },
        {
          "subject": "Coğrafya",
          "text": "Coğrafi özellikleri ve turizm potansiyeli göz önüne alındığında 'Kapadokya' hangi alanda daha çok öne çıkar? (C-175)",
          "options": [
            "A) Okyanus balıkçılığı",
            "B) Çöl iklimi araştırmaları",
            "C) Sadece ağır sanayi",
            "D) Doğal güzellikleri ve turizm/coğrafi önemi",
            "E) Sadece madencilik"
          ],
          "correct": 3,
          "solution": "Doğru cevap Doğal güzellikleri ve turizm/coğrafi önemi.",
          "id": "e10_q103",
          "no": 103
        },
        {
          "subject": "Coğrafya",
          "text": "Türkiye'nin fiziki coğrafyası düşünüldüğünde 'Pamukkale' için aşağıdakilerden hangisi doğrudur? (C-176)",
          "options": [
            "A) Pamukkale Marmara'dadır.",
            "B) Pamukkale bir çöldür.",
            "C) Pamukkale yapay bir kanaldır.",
            "D) Pamukkale tarıma kapalıdır.",
            "E) Pamukkale, ülkemizin önemli yeryüzü şekillerinden biridir."
          ],
          "correct": 4,
          "solution": "Doğru cevap Pamukkale, ülkemizin önemli yeryüzü şekillerinden biridir..",
          "id": "e10_q104",
          "no": 104
        },
        {
          "subject": "Coğrafya",
          "text": "Coğrafi özellikleri ve turizm potansiyeli göz önüne alındığında 'Nemrut Dağı' hangi alanda daha çok öne çıkar? (C-177)",
          "options": [
            "A) Doğal güzellikleri ve turizm/coğrafi önemi",
            "B) Okyanus balıkçılığı",
            "C) Çöl iklimi araştırmaları",
            "D) Sadece ağır sanayi",
            "E) Sadece madencilik"
          ],
          "correct": 0,
          "solution": "Doğru cevap Doğal güzellikleri ve turizm/coğrafi önemi.",
          "id": "e10_q105",
          "no": 105
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'TBMM' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-133)",
          "options": [
            "A) TBMM yabancı bir kurumdur.",
            "B) TBMM özel bir şirkettir.",
            "C) TBMM yasaklanmıştır.",
            "D) TBMM sadece köylerde bulunur.",
            "E) TBMM, anayasal sistemin önemli bir parçasıdır."
          ],
          "correct": 4,
          "solution": "Doğru cevap TBMM, anayasal sistemin önemli bir parçasıdır..",
          "id": "e10_q106",
          "no": 106
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'Cumhurbaşkanlığı' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-134)",
          "options": [
            "A) Cumhurbaşkanlığı sadece köylerde bulunur.",
            "B) Cumhurbaşkanlığı yasaklanmıştır.",
            "C) Cumhurbaşkanlığı, anayasal sistemin önemli bir parçasıdır.",
            "D) Cumhurbaşkanlığı yabancı bir kurumdur.",
            "E) Cumhurbaşkanlığı özel bir şirkettir."
          ],
          "correct": 2,
          "solution": "Doğru cevap Cumhurbaşkanlığı, anayasal sistemin önemli bir parçasıdır..",
          "id": "e10_q107",
          "no": 107
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'Sayıştay' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-135)",
          "options": [
            "A) Sayıştay özel bir şirkettir.",
            "B) Sayıştay yabancı bir kurumdur.",
            "C) Sayıştay, anayasal sistemin önemli bir parçasıdır.",
            "D) Sayıştay sadece köylerde bulunur.",
            "E) Sayıştay yasaklanmıştır."
          ],
          "correct": 2,
          "solution": "Doğru cevap Sayıştay, anayasal sistemin önemli bir parçasıdır..",
          "id": "e10_q108",
          "no": 108
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'YSK' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-136)",
          "options": [
            "A) YSK, anayasal sistemin önemli bir parçasıdır.",
            "B) YSK yabancı bir kurumdur.",
            "C) YSK yasaklanmıştır.",
            "D) YSK sadece köylerde bulunur.",
            "E) YSK özel bir şirkettir."
          ],
          "correct": 0,
          "solution": "Doğru cevap YSK, anayasal sistemin önemli bir parçasıdır..",
          "id": "e10_q109",
          "no": 109
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'HSK' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-137)",
          "options": [
            "A) HSK sadece köylerde bulunur.",
            "B) HSK, anayasal sistemin önemli bir parçasıdır.",
            "C) HSK yasaklanmıştır.",
            "D) HSK özel bir şirkettir.",
            "E) HSK yabancı bir kurumdur."
          ],
          "correct": 1,
          "solution": "Doğru cevap HSK, anayasal sistemin önemli bir parçasıdır..",
          "id": "e10_q110",
          "no": 110
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'Belediye' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-138)",
          "options": [
            "A) Belediye özel bir şirkettir.",
            "B) Belediye yasaklanmıştır.",
            "C) Belediye sadece köylerde bulunur.",
            "D) Belediye yabancı bir kurumdur.",
            "E) Belediye, anayasal sistemin önemli bir parçasıdır."
          ],
          "correct": 4,
          "solution": "Doğru cevap Belediye, anayasal sistemin önemli bir parçasıdır..",
          "id": "e10_q111",
          "no": 111
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'Valilik' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-139)",
          "options": [
            "A) Valilik sadece köylerde bulunur.",
            "B) Valilik yasaklanmıştır.",
            "C) Valilik, anayasal sistemin önemli bir parçasıdır.",
            "D) Valilik yabancı bir kurumdur.",
            "E) Valilik özel bir şirkettir."
          ],
          "correct": 2,
          "solution": "Doğru cevap Valilik, anayasal sistemin önemli bir parçasıdır..",
          "id": "e10_q112",
          "no": 112
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'Kaymakamlık' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-140)",
          "options": [
            "A) Kaymakamlık sadece köylerde bulunur.",
            "B) Kaymakamlık yabancı bir kurumdur.",
            "C) Kaymakamlık yasaklanmıştır.",
            "D) Kaymakamlık özel bir şirkettir.",
            "E) Kaymakamlık, anayasal sistemin önemli bir parçasıdır."
          ],
          "correct": 4,
          "solution": "Doğru cevap Kaymakamlık, anayasal sistemin önemli bir parçasıdır..",
          "id": "e10_q113",
          "no": 113
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'İl Genel Meclisi' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-141)",
          "options": [
            "A) İl Genel Meclisi yabancı bir kurumdur.",
            "B) İl Genel Meclisi, anayasal sistemin önemli bir parçasıdır.",
            "C) İl Genel Meclisi yasaklanmıştır.",
            "D) İl Genel Meclisi özel bir şirkettir.",
            "E) İl Genel Meclisi sadece köylerde bulunur."
          ],
          "correct": 1,
          "solution": "Doğru cevap İl Genel Meclisi, anayasal sistemin önemli bir parçasıdır..",
          "id": "e10_q114",
          "no": 114
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'Kamu Denetçiliği Kurumu' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-142)",
          "options": [
            "A) Kamu Denetçiliği Kurumu, anayasal sistemin önemli bir parçasıdır.",
            "B) Kamu Denetçiliği Kurumu yasaklanmıştır.",
            "C) Kamu Denetçiliği Kurumu yabancı bir kurumdur.",
            "D) Kamu Denetçiliği Kurumu sadece köylerde bulunur.",
            "E) Kamu Denetçiliği Kurumu özel bir şirkettir."
          ],
          "correct": 0,
          "solution": "Doğru cevap Kamu Denetçiliği Kurumu, anayasal sistemin önemli bir parçasıdır..",
          "id": "e10_q115",
          "no": 115
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'Anayasa Mahkemesi' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-143)",
          "options": [
            "A) Anayasa Mahkemesi yabancı bir kurumdur.",
            "B) Anayasa Mahkemesi sadece köylerde bulunur.",
            "C) Anayasa Mahkemesi yasaklanmıştır.",
            "D) Anayasa Mahkemesi özel bir şirkettir.",
            "E) Anayasa Mahkemesi, anayasal sistemin önemli bir parçasıdır."
          ],
          "correct": 4,
          "solution": "Doğru cevap Anayasa Mahkemesi, anayasal sistemin önemli bir parçasıdır..",
          "id": "e10_q116",
          "no": 116
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'Yargıtay' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-144)",
          "options": [
            "A) Yargıtay özel bir şirkettir.",
            "B) Yargıtay yabancı bir kurumdur.",
            "C) Yargıtay, anayasal sistemin önemli bir parçasıdır.",
            "D) Yargıtay yasaklanmıştır.",
            "E) Yargıtay sadece köylerde bulunur."
          ],
          "correct": 2,
          "solution": "Doğru cevap Yargıtay, anayasal sistemin önemli bir parçasıdır..",
          "id": "e10_q117",
          "no": 117
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'Danıştay' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-145)",
          "options": [
            "A) Danıştay, anayasal sistemin önemli bir parçasıdır.",
            "B) Danıştay yasaklanmıştır.",
            "C) Danıştay özel bir şirkettir.",
            "D) Danıştay yabancı bir kurumdur.",
            "E) Danıştay sadece köylerde bulunur."
          ],
          "correct": 0,
          "solution": "Doğru cevap Danıştay, anayasal sistemin önemli bir parçasıdır..",
          "id": "e10_q118",
          "no": 118
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'TBMM' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-146)",
          "options": [
            "A) TBMM özel bir şirkettir.",
            "B) TBMM yabancı bir kurumdur.",
            "C) TBMM, anayasal sistemin önemli bir parçasıdır.",
            "D) TBMM sadece köylerde bulunur.",
            "E) TBMM yasaklanmıştır."
          ],
          "correct": 2,
          "solution": "Doğru cevap TBMM, anayasal sistemin önemli bir parçasıdır..",
          "id": "e10_q119",
          "no": 119
        },
        {
          "subject": "Vatandaşlık",
          "text": "Türkiye Cumhuriyeti 1982 Anayasası'na göre 'Cumhurbaşkanlığı' kurumunun yapısı veya görevleriyle ilgili hangisi söylenebilir? (V-147)",
          "options": [
            "A) Cumhurbaşkanlığı özel bir şirkettir.",
            "B) Cumhurbaşkanlığı, anayasal sistemin önemli bir parçasıdır.",
            "C) Cumhurbaşkanlığı sadece köylerde bulunur.",
            "D) Cumhurbaşkanlığı yabancı bir kurumdur.",
            "E) Cumhurbaşkanlığı yasaklanmıştır."
          ],
          "correct": 1,
          "solution": "Doğru cevap Cumhurbaşkanlığı, anayasal sistemin önemli bir parçasıdır..",
          "id": "e10_q120",
          "no": 120
        }
      ]
    }
  ],
  "correct": 1,
  "solution": "Seçenekteki 'açık' kelimesi mecazi olarak 'gizliliği olmayan, herkesçe bilinen' anlamında kullanılmıştır."
};
