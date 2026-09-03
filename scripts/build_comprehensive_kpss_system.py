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
    {
      "id": "deneme_2",
      "title": "KPSS 2026 Ortaöğretim - 2. Deneme Sınavı (120 Soru)",
      "totalDurationMinutes": 130,
      "questions": [
        {
          "id": "e2_q1",
          "subject": "Türkçe",
          "number": 1,
          "text": "1. Aşağıdaki cümlelerin hangisinde <u>'ağır'</u> sözcüğü 'ciddi, kırıcı veya derin tesir bırakan' anlamında kullanılmıştır?",
          "options": [
            "A) Pencerenin kenarındaki nesne yere düştü.",
            "B) Yolun karşısındaki durağa doğru hızlıca koştu.",
            "C) Söylediği <u>ağır</u> sözler arkadaşını derinden yaraladı.",
            "D) Bahçedeki ağaçların gölgesinde dinlenmeyi seçti.",
            "E) Kitaplarını çantasına özenle yerleştirdi."
          ],
          "correct": 2,
          "solution": "Seçenekteki 'ağır' kelimesi mecazi olarak 'ciddi, kırıcı veya derin tesir bırakan' anlamında kullanılmıştır."
        },
        {
          "id": "e2_q2",
          "subject": "Türkçe",
          "number": 2,
          "text": "2. Aşağıdaki cümlelerin hangisinde <u>'çam devirmek'</u> deyimi 'farkında olmadan kırıcı söz söylemek' anlamında kullanılmıştır?",
          "options": [
            "A) Sabah erkenden kalkıp iş yerine gitti.",
            "B) Toplantıda yaptığı konuşmada farkında olmadan <u>çam devirdi</u>.",
            "C) Tren vaktinde istasyona yanaşarak yolcularını aldı.",
            "D) Bahçede rengarenk çiçekler açmıştı.",
            "E) Raporun son halini inceleyip imzaladı."
          ],
          "correct": 1,
          "solution": "Deyim cümlede 'farkında olmadan kırıcı söz söylemek' anlamını karşılayacak şekilde yer almıştır."
        },
        {
          "id": "e2_q3",
          "subject": "Türkçe",
          "number": 3,
          "text": "3. (I) Şairin 23 yılında yayımlanan bu eseri yoğun bir ilgi gördü. (II) Kitapta yer alan imgeler okurun hayal dünyasını zenginleştiriyor. (III) Eser toplam 120 sayfadan ve 45 şiirden oluşmaktadır. (IV) Bence dönemin en başarılı şiir kitabı budur. (V) Kitabın ikinci baskısı geçen ay yapıldı.\n\nBu parçadaki numaralanmış cümlelerden hangisi <u>öznel</u> bir yargı içermektedir?",
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
          "id": "e2_q4",
          "subject": "Türkçe",
          "number": 4,
          "text": "4. (I) Şairin 24 yılında yayımlanan bu eseri yoğun bir ilgi gördü. (II) Kitapta yer alan imgeler okurun hayal dünyasını zenginleştiriyor. (III) Eser toplam 120 sayfadan ve 45 şiirden oluşmaktadır. (IV) Bence dönemin en başarılı şiir kitabı budur. (V) Kitabın ikinci baskısı geçen ay yapıldı.\n\nBu parçadaki numaralanmış cümlelerden hangisi <u>öznel</u> bir yargı içermektedir?",
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
          "id": "e2_q5",
          "subject": "Türkçe",
          "number": 5,
          "text": "5. (I) Şairin 25 yılında yayımlanan bu eseri yoğun bir ilgi gördü. (II) Kitapta yer alan imgeler okurun hayal dünyasını zenginleştiriyor. (III) Eser toplam 120 sayfadan ve 45 şiirden oluşmaktadır. (IV) Bence dönemin en başarılı şiir kitabı budur. (V) Kitabın ikinci baskısı geçen ay yapıldı.\n\nBu parçadaki numaralanmış cümlelerden hangisi <u>öznel</u> bir yargı içermektedir?",
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
          "id": "e2_q6",
          "subject": "Türkçe",
          "number": 6,
          "text": "6. (I) Şairin 26 yılında yayımlanan bu eseri yoğun bir ilgi gördü. (II) Kitapta yer alan imgeler okurun hayal dünyasını zenginleştiriyor. (III) Eser toplam 120 sayfadan ve 45 şiirden oluşmaktadır. (IV) Bence dönemin en başarılı şiir kitabı budur. (V) Kitabın ikinci baskısı geçen ay yapıldı.\n\nBu parçadaki numaralanmış cümlelerden hangisi <u>öznel</u> bir yargı içermektedir?",
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
          "id": "e2_q7",
          "subject": "Türkçe",
          "number": 7,
          "text": "7. (I) Şairin 27 yılında yayımlanan bu eseri yoğun bir ilgi gördü. (II) Kitapta yer alan imgeler okurun hayal dünyasını zenginleştiriyor. (III) Eser toplam 120 sayfadan ve 45 şiirden oluşmaktadır. (IV) Bence dönemin en başarılı şiir kitabı budur. (V) Kitabın ikinci baskısı geçen ay yapıldı.\n\nBu parçadaki numaralanmış cümlelerden hangisi <u>öznel</u> bir yargı içermektedir?",
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
          "id": "e2_q8",
          "subject": "Türkçe",
          "number": 8,
          "text": "8. (I) Şairin 28 yılında yayımlanan bu eseri yoğun bir ilgi gördü. (II) Kitapta yer alan imgeler okurun hayal dünyasını zenginleştiriyor. (III) Eser toplam 120 sayfadan ve 45 şiirden oluşmaktadır. (IV) Bence dönemin en başarılı şiir kitabı budur. (V) Kitabın ikinci baskısı geçen ay yapıldı.\n\nBu parçadaki numaralanmış cümlelerden hangisi <u>öznel</u> bir yargı içermektedir?",
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
          "id": "e2_q9",
          "subject": "Türkçe",
          "number": 9,
          "text": "9. (I) Şairin 29 yılında yayımlanan bu eseri yoğun bir ilgi gördü. (II) Kitapta yer alan imgeler okurun hayal dünyasını zenginleştiriyor. (III) Eser toplam 120 sayfadan ve 45 şiirden oluşmaktadır. (IV) Bence dönemin en başarılı şiir kitabı budur. (V) Kitabın ikinci baskısı geçen ay yapıldı.\n\nBu parçadaki numaralanmış cümlelerden hangisi <u>öznel</u> bir yargı içermektedir?",
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
          "id": "e2_q10",
          "subject": "Türkçe",
          "number": 10,
          "text": "10. (I) Şairin 30 yılında yayımlanan bu eseri yoğun bir ilgi gördü. (II) Kitapta yer alan imgeler okurun hayal dünyasını zenginleştiriyor. (III) Eser toplam 120 sayfadan ve 45 şiirden oluşmaktadır. (IV) Bence dönemin en başarılı şiir kitabı budur. (V) Kitabın ikinci baskısı geçen ay yapıldı.\n\nBu parçadaki numaralanmış cümlelerden hangisi <u>öznel</u> bir yargı içermektedir?",
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
          "id": "e2_q11",
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
          "id": "e2_q12",
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
          "id": "e2_q13",
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
          "id": "e2_q14",
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
          "id": "e2_q15",
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
          "id": "e2_q16",
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
          "id": "e2_q17",
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
          "id": "e2_q18",
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
          "id": "e2_q19",
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
          "id": "e2_q20",
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
          "id": "e2_q21",
          "subject": "Türkçe",
          "number": 21,
          "text": "21. Aşağıdaki cümlelerin hangisinde bir <u>yazım yanlışı</u> yapılmıştır?",
          "options": [
            "A) Türk Dil Kurumu yeni kılavuzunu yayımladı.",
            "B) 2. yüzyılda pek çok önemli gelişme yaşandı.",
            "C) Bu konuda <u>herşey</u> planlandığı gibi gidiyor.",
            "D) TBMM'nin aldığı tarihi karar Resmi Gazete'de duyuruldu.",
            "E) Yanı sıra pek çok yabancı konuk da törene katıldı."
          ],
          "correct": 2,
          "solution": "'Herşey' sözcüğü 'Her şey' şeklinde ayrı yazılmalıdır. Şey sözcüğü daima ayrı yazılır."
        },
        {
          "id": "e2_q22",
          "subject": "Türkçe",
          "number": 22,
          "text": "22. Aşağıdaki cümlelerin hangisinde bir <u>yazım yanlışı</u> yapılmıştır?",
          "options": [
            "A) Türk Dil Kurumu yeni kılavuzunu yayımladı.",
            "B) 2. yüzyılda pek çok önemli gelişme yaşandı.",
            "C) Bu konuda <u>herşey</u> planlandığı gibi gidiyor.",
            "D) TBMM'nin aldığı tarihi karar Resmi Gazete'de duyuruldu.",
            "E) Yanı sıra pek çok yabancı konuk da törene katıldı."
          ],
          "correct": 2,
          "solution": "'Herşey' sözcüğü 'Her şey' şeklinde ayrı yazılmalıdır. Şey sözcüğü daima ayrı yazılır."
        },
        {
          "id": "e2_q23",
          "subject": "Türkçe",
          "number": 23,
          "text": "23. Aşağıdaki cümlelerin hangisinde bir <u>yazım yanlışı</u> yapılmıştır?",
          "options": [
            "A) Türk Dil Kurumu yeni kılavuzunu yayımladı.",
            "B) 2. yüzyılda pek çok önemli gelişme yaşandı.",
            "C) Bu konuda <u>herşey</u> planlandığı gibi gidiyor.",
            "D) TBMM'nin aldığı tarihi karar Resmi Gazete'de duyuruldu.",
            "E) Yanı sıra pek çok yabancı konuk da törene katıldı."
          ],
          "correct": 2,
          "solution": "'Herşey' sözcüğü 'Her şey' şeklinde ayrı yazılmalıdır. Şey sözcüğü daima ayrı yazılır."
        },
        {
          "id": "e2_q24",
          "subject": "Türkçe",
          "number": 24,
          "text": "24. Aşağıdaki cümlelerin hangisinde bir <u>yazım yanlışı</u> yapılmıştır?",
          "options": [
            "A) Türk Dil Kurumu yeni kılavuzunu yayımladı.",
            "B) 2. yüzyılda pek çok önemli gelişme yaşandı.",
            "C) Bu konuda <u>herşey</u> planlandığı gibi gidiyor.",
            "D) TBMM'nin aldığı tarihi karar Resmi Gazete'de duyuruldu.",
            "E) Yanı sıra pek çok yabancı konuk da törene katıldı."
          ],
          "correct": 2,
          "solution": "'Herşey' sözcüğü 'Her şey' şeklinde ayrı yazılmalıdır. Şey sözcüğü daima ayrı yazılır."
        },
        {
          "id": "e2_q25",
          "subject": "Türkçe",
          "number": 25,
          "text": "25. Aşağıdaki cümlelerin hangisinde bir <u>yazım yanlışı</u> yapılmıştır?",
          "options": [
            "A) Türk Dil Kurumu yeni kılavuzunu yayımladı.",
            "B) 2. yüzyılda pek çok önemli gelişme yaşandı.",
            "C) Bu konuda <u>herşey</u> planlandığı gibi gidiyor.",
            "D) TBMM'nin aldığı tarihi karar Resmi Gazete'de duyuruldu.",
            "E) Yanı sıra pek çok yabancı konuk da törene katıldı."
          ],
          "correct": 2,
          "solution": "'Herşey' sözcüğü 'Her şey' şeklinde ayrı yazılmalıdır. Şey sözcüğü daima ayrı yazılır."
        },
        {
          "id": "e2_q26",
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
          "id": "e2_q27",
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
          "id": "e2_q28",
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
          "id": "e2_q29",
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
          "id": "e2_q30",
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
          "id": "e2_q31",
          "subject": "Matematik",
          "number": 31,
          "text": "31. a ve b birer pozitif tam sayı olmak üzere,\n<code>3a + 5b = 47</code>\neşitliğini sağlayan en küçük b değeri için a kaçtır?",
          "options": [
            "A) 2",
            "B) 4",
            "C) 6",
            "D) 8",
            "E) 10"
          ],
          "correct": 1,
          "solution": "Denklemde b yerine en küçük pozitif tam sayı değerleri verilerek a = 4 olarak bulunur."
        },
        {
          "id": "e2_q32",
          "subject": "Matematik",
          "number": 32,
          "text": "32. a ve b birer pozitif tam sayı olmak üzere,\n<code>3a + 5b = 47</code>\neşitliğini sağlayan en küçük b değeri için a kaçtır?",
          "options": [
            "A) 2",
            "B) 4",
            "C) 6",
            "D) 8",
            "E) 10"
          ],
          "correct": 1,
          "solution": "Denklemde b yerine en küçük pozitif tam sayı değerleri verilerek a = 4 olarak bulunur."
        },
        {
          "id": "e2_q33",
          "subject": "Matematik",
          "number": 33,
          "text": "33. a ve b birer pozitif tam sayı olmak üzere,\n<code>3a + 5b = 47</code>\neşitliğini sağlayan en küçük b değeri için a kaçtır?",
          "options": [
            "A) 2",
            "B) 4",
            "C) 6",
            "D) 8",
            "E) 10"
          ],
          "correct": 1,
          "solution": "Denklemde b yerine en küçük pozitif tam sayı değerleri verilerek a = 4 olarak bulunur."
        },
        {
          "id": "e2_q34",
          "subject": "Matematik",
          "number": 34,
          "text": "34. a ve b birer pozitif tam sayı olmak üzere,\n<code>3a + 5b = 47</code>\neşitliğini sağlayan en küçük b değeri için a kaçtır?",
          "options": [
            "A) 2",
            "B) 4",
            "C) 6",
            "D) 8",
            "E) 10"
          ],
          "correct": 1,
          "solution": "Denklemde b yerine en küçük pozitif tam sayı değerleri verilerek a = 4 olarak bulunur."
        },
        {
          "id": "e2_q35",
          "subject": "Matematik",
          "number": 35,
          "text": "35. a ve b birer pozitif tam sayı olmak üzere,\n<code>3a + 5b = 47</code>\neşitliğini sağlayan en küçük b değeri için a kaçtır?",
          "options": [
            "A) 2",
            "B) 4",
            "C) 6",
            "D) 8",
            "E) 10"
          ],
          "correct": 1,
          "solution": "Denklemde b yerine en küçük pozitif tam sayı değerleri verilerek a = 4 olarak bulunur."
        },
        {
          "id": "e2_q36",
          "subject": "Matematik",
          "number": 36,
          "text": "36. <code>(1/2 + 1/3) : (5/6) + 2^3 = x</code>\nişleminin sonucu kaçtır?",
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
          "id": "e2_q37",
          "subject": "Matematik",
          "number": 37,
          "text": "37. <code>(1/2 + 1/3) : (5/6) + 2^4 = x</code>\nişleminin sonucu kaçtır?",
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
          "id": "e2_q38",
          "subject": "Matematik",
          "number": 38,
          "text": "38. <code>(1/2 + 1/3) : (5/6) + 2^5 = x</code>\nişleminin sonucu kaçtır?",
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
          "id": "e2_q39",
          "subject": "Matematik",
          "number": 39,
          "text": "39. <code>(1/2 + 1/3) : (5/6) + 2^6 = x</code>\nişleminin sonucu kaçtır?",
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
          "id": "e2_q40",
          "subject": "Matematik",
          "number": 40,
          "text": "40. <code>(1/2 + 1/3) : (5/6) + 2^7 = x</code>\nişleminin sonucu kaçtır?",
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
          "id": "e2_q41",
          "subject": "Matematik",
          "number": 41,
          "text": "41. <code>(1/2 + 1/3) : (5/6) + 2^8 = x</code>\nişleminin sonucu kaçtır?",
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
          "id": "e2_q42",
          "subject": "Matematik",
          "number": 42,
          "text": "42. <code>(1/2 + 1/3) : (5/6) + 2^9 = x</code>\nişleminin sonucu kaçtır?",
          "options": [
            "A) 513",
            "B) 514",
            "C) 512",
            "D) 257",
            "E) 515"
          ],
          "correct": 0,
          "solution": "(1/2 + 1/3) = 5/6. (5/6) : (5/6) = 1. Sonuç = 1 + 2^9 = 513."
        },
        {
          "id": "e2_q43",
          "subject": "Matematik",
          "number": 43,
          "text": "43. Bir babanın bugünkü yaşı 40, oğlunun bugünkü yaşı ise 8'dır.\nBuna göre kaç yıl sonra babanın yaşı oğlunun yaşının 3 katı olur?",
          "options": [
            "A) 6",
            "B) 7",
            "C) 8",
            "D) 9",
            "E) 10"
          ],
          "correct": 2,
          "solution": "40 + t = 3(8 + t) => 40 + t = 24 + 3t => 2t = 16 => t = 8 yıl sonra."
        },
        {
          "id": "e2_q44",
          "subject": "Matematik",
          "number": 44,
          "text": "44. Bir babanın bugünkü yaşı 40, oğlunun bugünkü yaşı ise 8'dır.\nBuna göre kaç yıl sonra babanın yaşı oğlunun yaşının 3 katı olur?",
          "options": [
            "A) 6",
            "B) 7",
            "C) 8",
            "D) 9",
            "E) 10"
          ],
          "correct": 2,
          "solution": "40 + t = 3(8 + t) => 40 + t = 24 + 3t => 2t = 16 => t = 8 yıl sonra."
        },
        {
          "id": "e2_q45",
          "subject": "Matematik",
          "number": 45,
          "text": "45. Bir babanın bugünkü yaşı 40, oğlunun bugünkü yaşı ise 8'dır.\nBuna göre kaç yıl sonra babanın yaşı oğlunun yaşının 3 katı olur?",
          "options": [
            "A) 6",
            "B) 7",
            "C) 8",
            "D) 9",
            "E) 10"
          ],
          "correct": 2,
          "solution": "40 + t = 3(8 + t) => 40 + t = 24 + 3t => 2t = 16 => t = 8 yıl sonra."
        },
        {
          "id": "e2_q46",
          "subject": "Matematik",
          "number": 46,
          "text": "46. Bir babanın bugünkü yaşı 40, oğlunun bugünkü yaşı ise 8'dır.\nBuna göre kaç yıl sonra babanın yaşı oğlunun yaşının 3 katı olur?",
          "options": [
            "A) 6",
            "B) 7",
            "C) 8",
            "D) 9",
            "E) 10"
          ],
          "correct": 2,
          "solution": "40 + t = 3(8 + t) => 40 + t = 24 + 3t => 2t = 16 => t = 8 yıl sonra."
        },
        {
          "id": "e2_q47",
          "subject": "Matematik",
          "number": 47,
          "text": "47. Bir babanın bugünkü yaşı 40, oğlunun bugünkü yaşı ise 8'dır.\nBuna göre kaç yıl sonra babanın yaşı oğlunun yaşının 3 katı olur?",
          "options": [
            "A) 6",
            "B) 7",
            "C) 8",
            "D) 9",
            "E) 10"
          ],
          "correct": 2,
          "solution": "40 + t = 3(8 + t) => 40 + t = 24 + 3t => 2t = 16 => t = 8 yıl sonra."
        },
        {
          "id": "e2_q48",
          "subject": "Matematik",
          "number": 48,
          "text": "48. Bir babanın bugünkü yaşı 40, oğlunun bugünkü yaşı ise 8'dır.\nBuna göre kaç yıl sonra babanın yaşı oğlunun yaşının 3 katı olur?",
          "options": [
            "A) 6",
            "B) 7",
            "C) 8",
            "D) 9",
            "E) 10"
          ],
          "correct": 2,
          "solution": "40 + t = 3(8 + t) => 40 + t = 24 + 3t => 2t = 16 => t = 8 yıl sonra."
        },
        {
          "id": "e2_q49",
          "subject": "Matematik",
          "number": 49,
          "text": "49. Bir babanın bugünkü yaşı 40, oğlunun bugünkü yaşı ise 8'dır.\nBuna göre kaç yıl sonra babanın yaşı oğlunun yaşının 3 katı olur?",
          "options": [
            "A) 6",
            "B) 7",
            "C) 8",
            "D) 9",
            "E) 10"
          ],
          "correct": 2,
          "solution": "40 + t = 3(8 + t) => 40 + t = 24 + 3t => 2t = 16 => t = 8 yıl sonra."
        },
        {
          "id": "e2_q50",
          "subject": "Matematik",
          "number": 50,
          "text": "50. Bir babanın bugünkü yaşı 40, oğlunun bugünkü yaşı ise 8'dır.\nBuna göre kaç yıl sonra babanın yaşı oğlunun yaşının 3 katı olur?",
          "options": [
            "A) 6",
            "B) 7",
            "C) 8",
            "D) 9",
            "E) 10"
          ],
          "correct": 2,
          "solution": "40 + t = 3(8 + t) => 40 + t = 24 + 3t => 2t = 16 => t = 8 yıl sonra."
        },
        {
          "id": "e2_q51",
          "subject": "Matematik",
          "number": 51,
          "text": "51. Bir babanın bugünkü yaşı 40, oğlunun bugünkü yaşı ise 8'dır.\nBuna göre kaç yıl sonra babanın yaşı oğlunun yaşının 3 katı olur?",
          "options": [
            "A) 6",
            "B) 7",
            "C) 8",
            "D) 9",
            "E) 10"
          ],
          "correct": 2,
          "solution": "40 + t = 3(8 + t) => 40 + t = 24 + 3t => 2t = 16 => t = 8 yıl sonra."
        },
        {
          "id": "e2_q52",
          "subject": "Matematik",
          "number": 52,
          "text": "52. Bir babanın bugünkü yaşı 40, oğlunun bugünkü yaşı ise 8'dır.\nBuna göre kaç yıl sonra babanın yaşı oğlunun yaşının 3 katı olur?",
          "options": [
            "A) 6",
            "B) 7",
            "C) 8",
            "D) 9",
            "E) 10"
          ],
          "correct": 2,
          "solution": "40 + t = 3(8 + t) => 40 + t = 24 + 3t => 2t = 16 => t = 8 yıl sonra."
        },
        {
          "id": "e2_q53",
          "subject": "Matematik",
          "number": 53,
          "text": "53. Bir babanın bugünkü yaşı 40, oğlunun bugünkü yaşı ise 8'dır.\nBuna göre kaç yıl sonra babanın yaşı oğlunun yaşının 3 katı olur?",
          "options": [
            "A) 6",
            "B) 7",
            "C) 8",
            "D) 9",
            "E) 10"
          ],
          "correct": 2,
          "solution": "40 + t = 3(8 + t) => 40 + t = 24 + 3t => 2t = 16 => t = 8 yıl sonra."
        },
        {
          "id": "e2_q54",
          "subject": "Matematik",
          "number": 54,
          "text": "54. Bir babanın bugünkü yaşı 40, oğlunun bugünkü yaşı ise 8'dır.\nBuna göre kaç yıl sonra babanın yaşı oğlunun yaşının 3 katı olur?",
          "options": [
            "A) 6",
            "B) 7",
            "C) 8",
            "D) 9",
            "E) 10"
          ],
          "correct": 2,
          "solution": "40 + t = 3(8 + t) => 40 + t = 24 + 3t => 2t = 16 => t = 8 yıl sonra."
        },
        {
          "id": "e2_q55",
          "subject": "Matematik",
          "number": 55,
          "text": "55. A ve B iki küme olmak üzere,\n<code>s(A) = 14</code>, <code>s(B) = 12</code> ve <code>s(A ∩ B) = 5</code>\nolduğuna göre <code>s(A ∪ B)</code> kaçtır?",
          "options": [
            "A) 19",
            "B) 21",
            "C) 23",
            "D) 25",
            "E) 27"
          ],
          "correct": 1,
          "solution": "s(A ∪ B) = s(A) + s(B) - s(A ∩ B) = 14 + 12 - 5 = 21."
        },
        {
          "id": "e2_q56",
          "subject": "Matematik",
          "number": 56,
          "text": "56. A ve B iki küme olmak üzere,\n<code>s(A) = 14</code>, <code>s(B) = 12</code> ve <code>s(A ∩ B) = 5</code>\nolduğuna göre <code>s(A ∪ B)</code> kaçtır?",
          "options": [
            "A) 19",
            "B) 21",
            "C) 23",
            "D) 25",
            "E) 27"
          ],
          "correct": 1,
          "solution": "s(A ∪ B) = s(A) + s(B) - s(A ∩ B) = 14 + 12 - 5 = 21."
        },
        {
          "id": "e2_q57",
          "subject": "Matematik",
          "number": 57,
          "text": "57. A ve B iki küme olmak üzere,\n<code>s(A) = 14</code>, <code>s(B) = 12</code> ve <code>s(A ∩ B) = 5</code>\nolduğuna göre <code>s(A ∪ B)</code> kaçtır?",
          "options": [
            "A) 19",
            "B) 21",
            "C) 23",
            "D) 25",
            "E) 27"
          ],
          "correct": 1,
          "solution": "s(A ∪ B) = s(A) + s(B) - s(A ∩ B) = 14 + 12 - 5 = 21."
        },
        {
          "id": "e2_q58",
          "subject": "Matematik",
          "number": 58,
          "text": "58. A ve B iki küme olmak üzere,\n<code>s(A) = 14</code>, <code>s(B) = 12</code> ve <code>s(A ∩ B) = 5</code>\nolduğuna göre <code>s(A ∪ B)</code> kaçtır?",
          "options": [
            "A) 19",
            "B) 21",
            "C) 23",
            "D) 25",
            "E) 27"
          ],
          "correct": 1,
          "solution": "s(A ∪ B) = s(A) + s(B) - s(A ∩ B) = 14 + 12 - 5 = 21."
        },
        {
          "id": "e2_q59",
          "subject": "Matematik",
          "number": 59,
          "text": "59. Dik kenar uzunlukları 9 cm ve 12 cm olan bir dik üçgenin hipotenüs uzunluğu kaç cm'dir?",
          "options": [
            "A) 14",
            "B) 15",
            "C) 16",
            "D) 17",
            "E) 18"
          ],
          "correct": 1,
          "solution": "Pisagor bağıntısı: a² + b² = c² => 9² + 12² = 225 = 15² => Hipotenüs = 15 cm (3-4-5 katı)."
        },
        {
          "id": "e2_q60",
          "subject": "Matematik",
          "number": 60,
          "text": "60. Dik kenar uzunlukları 9 cm ve 12 cm olan bir dik üçgenin hipotenüs uzunluğu kaç cm'dir?",
          "options": [
            "A) 14",
            "B) 15",
            "C) 16",
            "D) 17",
            "E) 18"
          ],
          "correct": 1,
          "solution": "Pisagor bağıntısı: a² + b² = c² => 9² + 12² = 225 = 15² => Hipotenüs = 15 cm (3-4-5 katı)."
        },
        {
          "id": "e2_q61",
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
          "id": "e2_q62",
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
          "id": "e2_q63",
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
          "id": "e2_q64",
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
          "id": "e2_q65",
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
          "id": "e2_q66",
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
          "id": "e2_q67",
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
          "id": "e2_q68",
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
          "id": "e2_q69",
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
          "id": "e2_q70",
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
          "id": "e2_q71",
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
          "id": "e2_q72",
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
          "id": "e2_q73",
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
          "id": "e2_q74",
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
          "id": "e2_q75",
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
          "id": "e2_q76",
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
          "id": "e2_q77",
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
          "id": "e2_q78",
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
          "id": "e2_q79",
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
          "id": "e2_q80",
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
          "id": "e2_q81",
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
          "id": "e2_q82",
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
          "id": "e2_q83",
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
          "id": "e2_q84",
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
          "id": "e2_q85",
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
          "id": "e2_q86",
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
          "id": "e2_q87",
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
          "id": "e2_q88",
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
          "id": "e2_q89",
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
          "id": "e2_q90",
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
          "id": "e2_q91",
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
          "id": "e2_q92",
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
          "id": "e2_q93",
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
          "id": "e2_q94",
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
          "id": "e2_q95",
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
          "id": "e2_q96",
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
          "id": "e2_q97",
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
          "id": "e2_q98",
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
          "id": "e2_q99",
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
          "id": "e2_q100",
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
          "id": "e2_q101",
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
          "id": "e2_q102",
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
          "id": "e2_q103",
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
          "id": "e2_q104",
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
          "id": "e2_q105",
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
          "id": "e2_q106",
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
          "id": "e2_q107",
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
          "id": "e2_q108",
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
          "id": "e2_q109",
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
          "id": "e2_q110",
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
          "id": "e2_q111",
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
          "id": "e2_q112",
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
          "id": "e2_q113",
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
          "id": "e2_q114",
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
          "id": "e2_q115",
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
          "id": "e2_q116",
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
          "id": "e2_q117",
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
          "id": "e2_q118",
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
          "id": "e2_q119",
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
          "id": "e2_q120",
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
    {
      "id": "deneme_3",
      "title": "KPSS 2026 Ortaöğretim - 3. Deneme Sınavı (120 Soru)",
      "totalDurationMinutes": 130,
      "questions": [
        {
          "id": "e3_q1",
          "subject": "Türkçe",
          "number": 1,
          "text": "1. Aşağıdaki cümlelerin hangisinde <u>'kuru'</u> sözcüğü 'etkisi ve çekiciliği olmayan, tekdüze' anlamında kullanılmıştır?",
          "options": [
            "A) Yazarın <u>kuru</u> bir anlatımı tercih etmesi eseri sıkıcı kılmış.",
            "B) Yolun karşısındaki durağa doğru hızlıca koştu.",
            "C) Günün ilk saatlerinde dışarıda serin bir hava vardı.",
            "D) Bahçedeki ağaçların gölgesinde dinlenmeyi seçti.",
            "E) Kitaplarını çantasına özenle yerleştirdi."
          ],
          "correct": 0,
          "solution": "Seçenekteki 'kuru' kelimesi mecazi olarak 'etkisi ve çekiciliği olmayan, tekdüze' anlamında kullanılmıştır."
        },
        {
          "id": "e3_q2",
          "subject": "Türkçe",
          "number": 2,
          "text": "2. Aşağıdaki cümlelerin hangisinde <u>'kulak kabartmak'</u> deyimi 'belli etmeden dinlemek' anlamında kullanılmıştır?",
          "options": [
            "A) Sabah erkenden kalkıp iş yerine gitti.",
            "B) Kütüphanedeki sessizliği kimse bozmak istemiyordu.",
            "C) Yan masadaki konuşmalara istemeden de olsa <u>kulak kabarttı</u>.",
            "D) Bahçede rengarenk çiçekler açmıştı.",
            "E) Raporun son halini inceleyip imzaladı."
          ],
          "correct": 2,
          "solution": "Deyim cümlede 'belli etmeden dinlemek' anlamını karşılayacak şekilde yer almıştır."
        },
        {
          "id": "e3_q3",
          "subject": "Türkçe",
          "number": 3,
          "text": "3. (I) Şairin 33 yılında yayımlanan bu eseri yoğun bir ilgi gördü. (II) Kitapta yer alan imgeler okurun hayal dünyasını zenginleştiriyor. (III) Eser toplam 120 sayfadan ve 45 şiirden oluşmaktadır. (IV) Bence dönemin en başarılı şiir kitabı budur. (V) Kitabın ikinci baskısı geçen ay yapıldı.\n\nBu parçadaki numaralanmış cümlelerden hangisi <u>öznel</u> bir yargı içermektedir?",
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
          "id": "e3_q4",
          "subject": "Türkçe",
          "number": 4,
          "text": "4. (I) Şairin 34 yılında yayımlanan bu eseri yoğun bir ilgi gördü. (II) Kitapta yer alan imgeler okurun hayal dünyasını zenginleştiriyor. (III) Eser toplam 120 sayfadan ve 45 şiirden oluşmaktadır. (IV) Bence dönemin en başarılı şiir kitabı budur. (V) Kitabın ikinci baskısı geçen ay yapıldı.\n\nBu parçadaki numaralanmış cümlelerden hangisi <u>öznel</u> bir yargı içermektedir?",
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
          "id": "e3_q5",
          "subject": "Türkçe",
          "number": 5,
          "text": "5. (I) Şairin 35 yılında yayımlanan bu eseri yoğun bir ilgi gördü. (II) Kitapta yer alan imgeler okurun hayal dünyasını zenginleştiriyor. (III) Eser toplam 120 sayfadan ve 45 şiirden oluşmaktadır. (IV) Bence dönemin en başarılı şiir kitabı budur. (V) Kitabın ikinci baskısı geçen ay yapıldı.\n\nBu parçadaki numaralanmış cümlelerden hangisi <u>öznel</u> bir yargı içermektedir?",
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
          "id": "e3_q6",
          "subject": "Türkçe",
          "number": 6,
          "text": "6. (I) Şairin 36 yılında yayımlanan bu eseri yoğun bir ilgi gördü. (II) Kitapta yer alan imgeler okurun hayal dünyasını zenginleştiriyor. (III) Eser toplam 120 sayfadan ve 45 şiirden oluşmaktadır. (IV) Bence dönemin en başarılı şiir kitabı budur. (V) Kitabın ikinci baskısı geçen ay yapıldı.\n\nBu parçadaki numaralanmış cümlelerden hangisi <u>öznel</u> bir yargı içermektedir?",
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
          "id": "e3_q7",
          "subject": "Türkçe",
          "number": 7,
          "text": "7. (I) Şairin 37 yılında yayımlanan bu eseri yoğun bir ilgi gördü. (II) Kitapta yer alan imgeler okurun hayal dünyasını zenginleştiriyor. (III) Eser toplam 120 sayfadan ve 45 şiirden oluşmaktadır. (IV) Bence dönemin en başarılı şiir kitabı budur. (V) Kitabın ikinci baskısı geçen ay yapıldı.\n\nBu parçadaki numaralanmış cümlelerden hangisi <u>öznel</u> bir yargı içermektedir?",
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
          "id": "e3_q8",
          "subject": "Türkçe",
          "number": 8,
          "text": "8. (I) Şairin 38 yılında yayımlanan bu eseri yoğun bir ilgi gördü. (II) Kitapta yer alan imgeler okurun hayal dünyasını zenginleştiriyor. (III) Eser toplam 120 sayfadan ve 45 şiirden oluşmaktadır. (IV) Bence dönemin en başarılı şiir kitabı budur. (V) Kitabın ikinci baskısı geçen ay yapıldı.\n\nBu parçadaki numaralanmış cümlelerden hangisi <u>öznel</u> bir yargı içermektedir?",
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
          "id": "e3_q9",
          "subject": "Türkçe",
          "number": 9,
          "text": "9. (I) Şairin 39 yılında yayımlanan bu eseri yoğun bir ilgi gördü. (II) Kitapta yer alan imgeler okurun hayal dünyasını zenginleştiriyor. (III) Eser toplam 120 sayfadan ve 45 şiirden oluşmaktadır. (IV) Bence dönemin en başarılı şiir kitabı budur. (V) Kitabın ikinci baskısı geçen ay yapıldı.\n\nBu parçadaki numaralanmış cümlelerden hangisi <u>öznel</u> bir yargı içermektedir?",
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
          "id": "e3_q10",
          "subject": "Türkçe",
          "number": 10,
          "text": "10. (I) Şairin 40 yılında yayımlanan bu eseri yoğun bir ilgi gördü. (II) Kitapta yer alan imgeler okurun hayal dünyasını zenginleştiriyor. (III) Eser toplam 120 sayfadan ve 45 şiirden oluşmaktadır. (IV) Bence dönemin en başarılı şiir kitabı budur. (V) Kitabın ikinci baskısı geçen ay yapıldı.\n\nBu parçadaki numaralanmış cümlelerden hangisi <u>öznel</u> bir yargı içermektedir?",
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
          "id": "e3_q11",
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
          "id": "e3_q12",
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
          "id": "e3_q13",
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
          "id": "e3_q14",
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
          "id": "e3_q15",
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
          "id": "e3_q16",
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
          "id": "e3_q17",
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
          "id": "e3_q18",
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
          "id": "e3_q19",
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
          "id": "e3_q20",
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
          "id": "e3_q21",
          "subject": "Türkçe",
          "number": 21,
          "text": "21. Aşağıdaki cümlelerin hangisinde bir <u>yazım yanlışı</u> yapılmıştır?",
          "options": [
            "A) Türk Dil Kurumu yeni kılavuzunu yayımladı.",
            "B) 3. yüzyılda pek çok önemli gelişme yaşandı.",
            "C) Bu konuda <u>herşey</u> planlandığı gibi gidiyor.",
            "D) TBMM'nin aldığı tarihi karar Resmi Gazete'de duyuruldu.",
            "E) Yanı sıra pek çok yabancı konuk da törene katıldı."
          ],
          "correct": 2,
          "solution": "'Herşey' sözcüğü 'Her şey' şeklinde ayrı yazılmalıdır. Şey sözcüğü daima ayrı yazılır."
        },
        {
          "id": "e3_q22",
          "subject": "Türkçe",
          "number": 22,
          "text": "22. Aşağıdaki cümlelerin hangisinde bir <u>yazım yanlışı</u> yapılmıştır?",
          "options": [
            "A) Türk Dil Kurumu yeni kılavuzunu yayımladı.",
            "B) 3. yüzyılda pek çok önemli gelişme yaşandı.",
            "C) Bu konuda <u>herşey</u> planlandığı gibi gidiyor.",
            "D) TBMM'nin aldığı tarihi karar Resmi Gazete'de duyuruldu.",
            "E) Yanı sıra pek çok yabancı konuk da törene katıldı."
          ],
          "correct": 2,
          "solution": "'Herşey' sözcüğü 'Her şey' şeklinde ayrı yazılmalıdır. Şey sözcüğü daima ayrı yazılır."
        },
        {
          "id": "e3_q23",
          "subject": "Türkçe",
          "number": 23,
          "text": "23. Aşağıdaki cümlelerin hangisinde bir <u>yazım yanlışı</u> yapılmıştır?",
          "options": [
            "A) Türk Dil Kurumu yeni kılavuzunu yayımladı.",
            "B) 3. yüzyılda pek çok önemli gelişme yaşandı.",
            "C) Bu konuda <u>herşey</u> planlandığı gibi gidiyor.",
            "D) TBMM'nin aldığı tarihi karar Resmi Gazete'de duyuruldu.",
            "E) Yanı sıra pek çok yabancı konuk da törene katıldı."
          ],
          "correct": 2,
          "solution": "'Herşey' sözcüğü 'Her şey' şeklinde ayrı yazılmalıdır. Şey sözcüğü daima ayrı yazılır."
        },
        {
          "id": "e3_q24",
          "subject": "Türkçe",
          "number": 24,
          "text": "24. Aşağıdaki cümlelerin hangisinde bir <u>yazım yanlışı</u> yapılmıştır?",
          "options": [
            "A) Türk Dil Kurumu yeni kılavuzunu yayımladı.",
            "B) 3. yüzyılda pek çok önemli gelişme yaşandı.",
            "C) Bu konuda <u>herşey</u> planlandığı gibi gidiyor.",
            "D) TBMM'nin aldığı tarihi karar Resmi Gazete'de duyuruldu.",
            "E) Yanı sıra pek çok yabancı konuk da törene katıldı."
          ],
          "correct": 2,
          "solution": "'Herşey' sözcüğü 'Her şey' şeklinde ayrı yazılmalıdır. Şey sözcüğü daima ayrı yazılır."
        },
        {
          "id": "e3_q25",
          "subject": "Türkçe",
          "number": 25,
          "text": "25. Aşağıdaki cümlelerin hangisinde bir <u>yazım yanlışı</u> yapılmıştır?",
          "options": [
            "A) Türk Dil Kurumu yeni kılavuzunu yayımladı.",
            "B) 3. yüzyılda pek çok önemli gelişme yaşandı.",
            "C) Bu konuda <u>herşey</u> planlandığı gibi gidiyor.",
            "D) TBMM'nin aldığı tarihi karar Resmi Gazete'de duyuruldu.",
            "E) Yanı sıra pek çok yabancı konuk da törene katıldı."
          ],
          "correct": 2,
          "solution": "'Herşey' sözcüğü 'Her şey' şeklinde ayrı yazılmalıdır. Şey sözcüğü daima ayrı yazılır."
        },
        {
          "id": "e3_q26",
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
          "id": "e3_q27",
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
          "id": "e3_q28",
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
          "id": "e3_q29",
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
          "id": "e3_q30",
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
          "id": "e3_q31",
          "subject": "Matematik",
          "number": 31,
          "text": "31. a ve b birer pozitif tam sayı olmak üzere,\n<code>3a + 5b = 65</code>\neşitliğini sağlayan en küçük b değeri için a kaçtır?",
          "options": [
            "A) 3",
            "B) 5",
            "C) 7",
            "D) 9",
            "E) 11"
          ],
          "correct": 1,
          "solution": "Denklemde b yerine en küçük pozitif tam sayı değerleri verilerek a = 5 olarak bulunur."
        },
        {
          "id": "e3_q32",
          "subject": "Matematik",
          "number": 32,
          "text": "32. a ve b birer pozitif tam sayı olmak üzere,\n<code>3a + 5b = 65</code>\neşitliğini sağlayan en küçük b değeri için a kaçtır?",
          "options": [
            "A) 3",
            "B) 5",
            "C) 7",
            "D) 9",
            "E) 11"
          ],
          "correct": 1,
          "solution": "Denklemde b yerine en küçük pozitif tam sayı değerleri verilerek a = 5 olarak bulunur."
        },
        {
          "id": "e3_q33",
          "subject": "Matematik",
          "number": 33,
          "text": "33. a ve b birer pozitif tam sayı olmak üzere,\n<code>3a + 5b = 65</code>\neşitliğini sağlayan en küçük b değeri için a kaçtır?",
          "options": [
            "A) 3",
            "B) 5",
            "C) 7",
            "D) 9",
            "E) 11"
          ],
          "correct": 1,
          "solution": "Denklemde b yerine en küçük pozitif tam sayı değerleri verilerek a = 5 olarak bulunur."
        },
        {
          "id": "e3_q34",
          "subject": "Matematik",
          "number": 34,
          "text": "34. a ve b birer pozitif tam sayı olmak üzere,\n<code>3a + 5b = 65</code>\neşitliğini sağlayan en küçük b değeri için a kaçtır?",
          "options": [
            "A) 3",
            "B) 5",
            "C) 7",
            "D) 9",
            "E) 11"
          ],
          "correct": 1,
          "solution": "Denklemde b yerine en küçük pozitif tam sayı değerleri verilerek a = 5 olarak bulunur."
        },
        {
          "id": "e3_q35",
          "subject": "Matematik",
          "number": 35,
          "text": "35. a ve b birer pozitif tam sayı olmak üzere,\n<code>3a + 5b = 65</code>\neşitliğini sağlayan en küçük b değeri için a kaçtır?",
          "options": [
            "A) 3",
            "B) 5",
            "C) 7",
            "D) 9",
            "E) 11"
          ],
          "correct": 1,
          "solution": "Denklemde b yerine en küçük pozitif tam sayı değerleri verilerek a = 5 olarak bulunur."
        },
        {
          "id": "e3_q36",
          "subject": "Matematik",
          "number": 36,
          "text": "36. <code>(1/2 + 1/3) : (5/6) + 2^4 = x</code>\nişleminin sonucu kaçtır?",
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
          "id": "e3_q37",
          "subject": "Matematik",
          "number": 37,
          "text": "37. <code>(1/2 + 1/3) : (5/6) + 2^5 = x</code>\nişleminin sonucu kaçtır?",
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
          "id": "e3_q38",
          "subject": "Matematik",
          "number": 38,
          "text": "38. <code>(1/2 + 1/3) : (5/6) + 2^6 = x</code>\nişleminin sonucu kaçtır?",
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
          "id": "e3_q39",
          "subject": "Matematik",
          "number": 39,
          "text": "39. <code>(1/2 + 1/3) : (5/6) + 2^7 = x</code>\nişleminin sonucu kaçtır?",
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
          "id": "e3_q40",
          "subject": "Matematik",
          "number": 40,
          "text": "40. <code>(1/2 + 1/3) : (5/6) + 2^8 = x</code>\nişleminin sonucu kaçtır?",
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
          "id": "e3_q41",
          "subject": "Matematik",
          "number": 41,
          "text": "41. <code>(1/2 + 1/3) : (5/6) + 2^9 = x</code>\nişleminin sonucu kaçtır?",
          "options": [
            "A) 513",
            "B) 514",
            "C) 512",
            "D) 257",
            "E) 515"
          ],
          "correct": 0,
          "solution": "(1/2 + 1/3) = 5/6. (5/6) : (5/6) = 1. Sonuç = 1 + 2^9 = 513."
        },
        {
          "id": "e3_q42",
          "subject": "Matematik",
          "number": 42,
          "text": "42. <code>(1/2 + 1/3) : (5/6) + 2^10 = x</code>\nişleminin sonucu kaçtır?",
          "options": [
            "A) 1025",
            "B) 1026",
            "C) 1024",
            "D) 513",
            "E) 1027"
          ],
          "correct": 0,
          "solution": "(1/2 + 1/3) = 5/6. (5/6) : (5/6) = 1. Sonuç = 1 + 2^10 = 1025."
        },
        {
          "id": "e3_q43",
          "subject": "Matematik",
          "number": 43,
          "text": "43. Bir babanın bugünkü yaşı 42, oğlunun bugünkü yaşı ise 9'dır.\nBuna göre kaç yıl sonra babanın yaşı oğlunun yaşının 3 katı olur?",
          "options": [
            "A) 5",
            "B) 6",
            "C) 7",
            "D) 8",
            "E) 9"
          ],
          "correct": 2,
          "solution": "42 + t = 3(9 + t) => 42 + t = 27 + 3t => 2t = 15 => t = 7 yıl sonra."
        },
        {
          "id": "e3_q44",
          "subject": "Matematik",
          "number": 44,
          "text": "44. Bir babanın bugünkü yaşı 42, oğlunun bugünkü yaşı ise 9'dır.\nBuna göre kaç yıl sonra babanın yaşı oğlunun yaşının 3 katı olur?",
          "options": [
            "A) 5",
            "B) 6",
            "C) 7",
            "D) 8",
            "E) 9"
          ],
          "correct": 2,
          "solution": "42 + t = 3(9 + t) => 42 + t = 27 + 3t => 2t = 15 => t = 7 yıl sonra."
        },
        {
          "id": "e3_q45",
          "subject": "Matematik",
          "number": 45,
          "text": "45. Bir babanın bugünkü yaşı 42, oğlunun bugünkü yaşı ise 9'dır.\nBuna göre kaç yıl sonra babanın yaşı oğlunun yaşının 3 katı olur?",
          "options": [
            "A) 5",
            "B) 6",
            "C) 7",
            "D) 8",
            "E) 9"
          ],
          "correct": 2,
          "solution": "42 + t = 3(9 + t) => 42 + t = 27 + 3t => 2t = 15 => t = 7 yıl sonra."
        },
        {
          "id": "e3_q46",
          "subject": "Matematik",
          "number": 46,
          "text": "46. Bir babanın bugünkü yaşı 42, oğlunun bugünkü yaşı ise 9'dır.\nBuna göre kaç yıl sonra babanın yaşı oğlunun yaşının 3 katı olur?",
          "options": [
            "A) 5",
            "B) 6",
            "C) 7",
            "D) 8",
            "E) 9"
          ],
          "correct": 2,
          "solution": "42 + t = 3(9 + t) => 42 + t = 27 + 3t => 2t = 15 => t = 7 yıl sonra."
        },
        {
          "id": "e3_q47",
          "subject": "Matematik",
          "number": 47,
          "text": "47. Bir babanın bugünkü yaşı 42, oğlunun bugünkü yaşı ise 9'dır.\nBuna göre kaç yıl sonra babanın yaşı oğlunun yaşının 3 katı olur?",
          "options": [
            "A) 5",
            "B) 6",
            "C) 7",
            "D) 8",
            "E) 9"
          ],
          "correct": 2,
          "solution": "42 + t = 3(9 + t) => 42 + t = 27 + 3t => 2t = 15 => t = 7 yıl sonra."
        },
        {
          "id": "e3_q48",
          "subject": "Matematik",
          "number": 48,
          "text": "48. Bir babanın bugünkü yaşı 42, oğlunun bugünkü yaşı ise 9'dır.\nBuna göre kaç yıl sonra babanın yaşı oğlunun yaşının 3 katı olur?",
          "options": [
            "A) 5",
            "B) 6",
            "C) 7",
            "D) 8",
            "E) 9"
          ],
          "correct": 2,
          "solution": "42 + t = 3(9 + t) => 42 + t = 27 + 3t => 2t = 15 => t = 7 yıl sonra."
        },
        {
          "id": "e3_q49",
          "subject": "Matematik",
          "number": 49,
          "text": "49. Bir babanın bugünkü yaşı 42, oğlunun bugünkü yaşı ise 9'dır.\nBuna göre kaç yıl sonra babanın yaşı oğlunun yaşının 3 katı olur?",
          "options": [
            "A) 5",
            "B) 6",
            "C) 7",
            "D) 8",
            "E) 9"
          ],
          "correct": 2,
          "solution": "42 + t = 3(9 + t) => 42 + t = 27 + 3t => 2t = 15 => t = 7 yıl sonra."
        },
        {
          "id": "e3_q50",
          "subject": "Matematik",
          "number": 50,
          "text": "50. Bir babanın bugünkü yaşı 42, oğlunun bugünkü yaşı ise 9'dır.\nBuna göre kaç yıl sonra babanın yaşı oğlunun yaşının 3 katı olur?",
          "options": [
            "A) 5",
            "B) 6",
            "C) 7",
            "D) 8",
            "E) 9"
          ],
          "correct": 2,
          "solution": "42 + t = 3(9 + t) => 42 + t = 27 + 3t => 2t = 15 => t = 7 yıl sonra."
        },
        {
          "id": "e3_q51",
          "subject": "Matematik",
          "number": 51,
          "text": "51. Bir babanın bugünkü yaşı 42, oğlunun bugünkü yaşı ise 9'dır.\nBuna göre kaç yıl sonra babanın yaşı oğlunun yaşının 3 katı olur?",
          "options": [
            "A) 5",
            "B) 6",
            "C) 7",
            "D) 8",
            "E) 9"
          ],
          "correct": 2,
          "solution": "42 + t = 3(9 + t) => 42 + t = 27 + 3t => 2t = 15 => t = 7 yıl sonra."
        },
        {
          "id": "e3_q52",
          "subject": "Matematik",
          "number": 52,
          "text": "52. Bir babanın bugünkü yaşı 42, oğlunun bugünkü yaşı ise 9'dır.\nBuna göre kaç yıl sonra babanın yaşı oğlunun yaşının 3 katı olur?",
          "options": [
            "A) 5",
            "B) 6",
            "C) 7",
            "D) 8",
            "E) 9"
          ],
          "correct": 2,
          "solution": "42 + t = 3(9 + t) => 42 + t = 27 + 3t => 2t = 15 => t = 7 yıl sonra."
        },
        {
          "id": "e3_q53",
          "subject": "Matematik",
          "number": 53,
          "text": "53. Bir babanın bugünkü yaşı 42, oğlunun bugünkü yaşı ise 9'dır.\nBuna göre kaç yıl sonra babanın yaşı oğlunun yaşının 3 katı olur?",
          "options": [
            "A) 5",
            "B) 6",
            "C) 7",
            "D) 8",
            "E) 9"
          ],
          "correct": 2,
          "solution": "42 + t = 3(9 + t) => 42 + t = 27 + 3t => 2t = 15 => t = 7 yıl sonra."
        },
        {
          "id": "e3_q54",
          "subject": "Matematik",
          "number": 54,
          "text": "54. Bir babanın bugünkü yaşı 42, oğlunun bugünkü yaşı ise 9'dır.\nBuna göre kaç yıl sonra babanın yaşı oğlunun yaşının 3 katı olur?",
          "options": [
            "A) 5",
            "B) 6",
            "C) 7",
            "D) 8",
            "E) 9"
          ],
          "correct": 2,
          "solution": "42 + t = 3(9 + t) => 42 + t = 27 + 3t => 2t = 15 => t = 7 yıl sonra."
        },
        {
          "id": "e3_q55",
          "subject": "Matematik",
          "number": 55,
          "text": "55. A ve B iki küme olmak üzere,\n<code>s(A) = 15</code>, <code>s(B) = 13</code> ve <code>s(A ∩ B) = 5</code>\nolduğuna göre <code>s(A ∪ B)</code> kaçtır?",
          "options": [
            "A) 21",
            "B) 23",
            "C) 25",
            "D) 27",
            "E) 29"
          ],
          "correct": 1,
          "solution": "s(A ∪ B) = s(A) + s(B) - s(A ∩ B) = 15 + 13 - 5 = 23."
        },
        {
          "id": "e3_q56",
          "subject": "Matematik",
          "number": 56,
          "text": "56. A ve B iki küme olmak üzere,\n<code>s(A) = 15</code>, <code>s(B) = 13</code> ve <code>s(A ∩ B) = 5</code>\nolduğuna göre <code>s(A ∪ B)</code> kaçtır?",
          "options": [
            "A) 21",
            "B) 23",
            "C) 25",
            "D) 27",
            "E) 29"
          ],
          "correct": 1,
          "solution": "s(A ∪ B) = s(A) + s(B) - s(A ∩ B) = 15 + 13 - 5 = 23."
        },
        {
          "id": "e3_q57",
          "subject": "Matematik",
          "number": 57,
          "text": "57. A ve B iki küme olmak üzere,\n<code>s(A) = 15</code>, <code>s(B) = 13</code> ve <code>s(A ∩ B) = 5</code>\nolduğuna göre <code>s(A ∪ B)</code> kaçtır?",
          "options": [
            "A) 21",
            "B) 23",
            "C) 25",
            "D) 27",
            "E) 29"
          ],
          "correct": 1,
          "solution": "s(A ∪ B) = s(A) + s(B) - s(A ∩ B) = 15 + 13 - 5 = 23."
        },
        {
          "id": "e3_q58",
          "subject": "Matematik",
          "number": 58,
          "text": "58. A ve B iki küme olmak üzere,\n<code>s(A) = 15</code>, <code>s(B) = 13</code> ve <code>s(A ∩ B) = 5</code>\nolduğuna göre <code>s(A ∪ B)</code> kaçtır?",
          "options": [
            "A) 21",
            "B) 23",
            "C) 25",
            "D) 27",
            "E) 29"
          ],
          "correct": 1,
          "solution": "s(A ∪ B) = s(A) + s(B) - s(A ∩ B) = 15 + 13 - 5 = 23."
        },
        {
          "id": "e3_q59",
          "subject": "Matematik",
          "number": 59,
          "text": "59. Dik kenar uzunlukları 3 cm ve 4 cm olan bir dik üçgenin hipotenüs uzunluğu kaç cm'dir?",
          "options": [
            "A) 4",
            "B) 5",
            "C) 6",
            "D) 7",
            "E) 8"
          ],
          "correct": 1,
          "solution": "Pisagor bağıntısı: a² + b² = c² => 3² + 4² = 25 = 5² => Hipotenüs = 5 cm (3-4-5 katı)."
        },
        {
          "id": "e3_q60",
          "subject": "Matematik",
          "number": 60,
          "text": "60. Dik kenar uzunlukları 3 cm ve 4 cm olan bir dik üçgenin hipotenüs uzunluğu kaç cm'dir?",
          "options": [
            "A) 4",
            "B) 5",
            "C) 6",
            "D) 7",
            "E) 8"
          ],
          "correct": 1,
          "solution": "Pisagor bağıntısı: a² + b² = c² => 3² + 4² = 25 = 5² => Hipotenüs = 5 cm (3-4-5 katı)."
        },
        {
          "id": "e3_q61",
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
          "id": "e3_q62",
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
          "id": "e3_q63",
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
          "id": "e3_q64",
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
          "id": "e3_q65",
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
          "id": "e3_q66",
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
          "id": "e3_q67",
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
          "id": "e3_q68",
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
          "id": "e3_q69",
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
          "id": "e3_q70",
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
          "id": "e3_q71",
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
          "id": "e3_q72",
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
          "id": "e3_q73",
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
          "id": "e3_q74",
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
          "id": "e3_q75",
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
          "id": "e3_q76",
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
          "id": "e3_q77",
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
          "id": "e3_q78",
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
          "id": "e3_q79",
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
          "id": "e3_q80",
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
          "id": "e3_q81",
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
          "id": "e3_q82",
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
          "id": "e3_q83",
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
          "id": "e3_q84",
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
          "id": "e3_q85",
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
          "id": "e3_q86",
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
          "id": "e3_q87",
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
          "id": "e3_q88",
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
          "id": "e3_q89",
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
          "id": "e3_q90",
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
          "id": "e3_q91",
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
          "id": "e3_q92",
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
          "id": "e3_q93",
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
          "id": "e3_q94",
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
          "id": "e3_q95",
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
          "id": "e3_q96",
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
          "id": "e3_q97",
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
          "id": "e3_q98",
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
          "id": "e3_q99",
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
          "id": "e3_q100",
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
          "id": "e3_q101",
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
          "id": "e3_q102",
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
          "id": "e3_q103",
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
          "id": "e3_q104",
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
          "id": "e3_q105",
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
          "id": "e3_q106",
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
          "id": "e3_q107",
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
          "id": "e3_q108",
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
          "id": "e3_q109",
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
          "id": "e3_q110",
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
          "id": "e3_q111",
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
          "id": "e3_q112",
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
          "id": "e3_q113",
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
          "id": "e3_q114",
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
          "id": "e3_q115",
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
          "id": "e3_q116",
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
          "id": "e3_q117",
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
          "id": "e3_q118",
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
          "id": "e3_q119",
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
          "id": "e3_q120",
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
    {
      "id": "deneme_4",
      "title": "KPSS 2026 Ortaöğretim - 4. Deneme Sınavı (120 Soru)",
      "totalDurationMinutes": 130,
      "questions": [
        {
          "id": "e4_q1",
          "subject": "Türkçe",
          "number": 1,
          "text": "1. Aşağıdaki cümlelerin hangisinde <u>'ince'</u> sözcüğü 'nazik, kibar ve duygulu' anlamında kullanılmıştır?",
          "options": [
            "A) Pencerenin kenarındaki nesne yere düştü.",
            "B) Yolun karşısındaki durağa doğru hızlıca koştu.",
            "C) Günün ilk saatlerinde dışarıda serin bir hava vardı.",
            "D) Misafirlerine karşı son derece <u>ince</u> bir davranış sergiledi.",
            "E) Kitaplarını çantasına özenle yerleştirdi."
          ],
          "correct": 3,
          "solution": "Seçenekteki 'ince' kelimesi mecazi olarak 'nazik, kibar ve duygulu' anlamında kullanılmıştır."
        },
        {
          "id": "e4_q2",
          "subject": "Türkçe",
          "number": 2,
          "text": "2. Aşağıdaki cümlelerin hangisinde <u>'etekleri zil çalmak'</u> deyimi 'çok sevinmek' anlamında kullanılmıştır?",
          "options": [
            "A) Sabah erkenden kalkıp iş yerine gitti.",
            "B) Kütüphanedeki sessizliği kimse bozmak istemiyordu.",
            "C) Tren vaktinde istasyona yanaşarak yolcularını aldı.",
            "D) Sınav sonucunun iyi geldiğini öğrenince <u>etekleri zil çaldı</u>.",
            "E) Raporun son halini inceleyip imzaladı."
          ],
          "correct": 3,
          "solution": "Deyim cümlede 'çok sevinmek' anlamını karşılayacak şekilde yer almıştır."
        },
        {
          "id": "e4_q3",
          "subject": "Türkçe",
          "number": 3,
          "text": "3. (I) Şairin 43 yılında yayımlanan bu eseri yoğun bir ilgi gördü. (II) Kitapta yer alan imgeler okurun hayal dünyasını zenginleştiriyor. (III) Eser toplam 120 sayfadan ve 45 şiirden oluşmaktadır. (IV) Bence dönemin en başarılı şiir kitabı budur. (V) Kitabın ikinci baskısı geçen ay yapıldı.\n\nBu parçadaki numaralanmış cümlelerden hangisi <u>öznel</u> bir yargı içermektedir?",
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
          "id": "e4_q4",
          "subject": "Türkçe",
          "number": 4,
          "text": "4. (I) Şairin 44 yılında yayımlanan bu eseri yoğun bir ilgi gördü. (II) Kitapta yer alan imgeler okurun hayal dünyasını zenginleştiriyor. (III) Eser toplam 120 sayfadan ve 45 şiirden oluşmaktadır. (IV) Bence dönemin en başarılı şiir kitabı budur. (V) Kitabın ikinci baskısı geçen ay yapıldı.\n\nBu parçadaki numaralanmış cümlelerden hangisi <u>öznel</u> bir yargı içermektedir?",
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
          "id": "e4_q5",
          "subject": "Türkçe",
          "number": 5,
          "text": "5. (I) Şairin 45 yılında yayımlanan bu eseri yoğun bir ilgi gördü. (II) Kitapta yer alan imgeler okurun hayal dünyasını zenginleştiriyor. (III) Eser toplam 120 sayfadan ve 45 şiirden oluşmaktadır. (IV) Bence dönemin en başarılı şiir kitabı budur. (V) Kitabın ikinci baskısı geçen ay yapıldı.\n\nBu parçadaki numaralanmış cümlelerden hangisi <u>öznel</u> bir yargı içermektedir?",
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
          "id": "e4_q6",
          "subject": "Türkçe",
          "number": 6,
          "text": "6. (I) Şairin 46 yılında yayımlanan bu eseri yoğun bir ilgi gördü. (II) Kitapta yer alan imgeler okurun hayal dünyasını zenginleştiriyor. (III) Eser toplam 120 sayfadan ve 45 şiirden oluşmaktadır. (IV) Bence dönemin en başarılı şiir kitabı budur. (V) Kitabın ikinci baskısı geçen ay yapıldı.\n\nBu parçadaki numaralanmış cümlelerden hangisi <u>öznel</u> bir yargı içermektedir?",
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
          "id": "e4_q7",
          "subject": "Türkçe",
          "number": 7,
          "text": "7. (I) Şairin 47 yılında yayımlanan bu eseri yoğun bir ilgi gördü. (II) Kitapta yer alan imgeler okurun hayal dünyasını zenginleştiriyor. (III) Eser toplam 120 sayfadan ve 45 şiirden oluşmaktadır. (IV) Bence dönemin en başarılı şiir kitabı budur. (V) Kitabın ikinci baskısı geçen ay yapıldı.\n\nBu parçadaki numaralanmış cümlelerden hangisi <u>öznel</u> bir yargı içermektedir?",
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
          "id": "e4_q8",
          "subject": "Türkçe",
          "number": 8,
          "text": "8. (I) Şairin 48 yılında yayımlanan bu eseri yoğun bir ilgi gördü. (II) Kitapta yer alan imgeler okurun hayal dünyasını zenginleştiriyor. (III) Eser toplam 120 sayfadan ve 45 şiirden oluşmaktadır. (IV) Bence dönemin en başarılı şiir kitabı budur. (V) Kitabın ikinci baskısı geçen ay yapıldı.\n\nBu parçadaki numaralanmış cümlelerden hangisi <u>öznel</u> bir yargı içermektedir?",
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
          "id": "e4_q9",
          "subject": "Türkçe",
          "number": 9,
          "text": "9. (I) Şairin 49 yılında yayımlanan bu eseri yoğun bir ilgi gördü. (II) Kitapta yer alan imgeler okurun hayal dünyasını zenginleştiriyor. (III) Eser toplam 120 sayfadan ve 45 şiirden oluşmaktadır. (IV) Bence dönemin en başarılı şiir kitabı budur. (V) Kitabın ikinci baskısı geçen ay yapıldı.\n\nBu parçadaki numaralanmış cümlelerden hangisi <u>öznel</u> bir yargı içermektedir?",
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
          "id": "e4_q10",
          "subject": "Türkçe",
          "number": 10,
          "text": "10. (I) Şairin 50 yılında yayımlanan bu eseri yoğun bir ilgi gördü. (II) Kitapta yer alan imgeler okurun hayal dünyasını zenginleştiriyor. (III) Eser toplam 120 sayfadan ve 45 şiirden oluşmaktadır. (IV) Bence dönemin en başarılı şiir kitabı budur. (V) Kitabın ikinci baskısı geçen ay yapıldı.\n\nBu parçadaki numaralanmış cümlelerden hangisi <u>öznel</u> bir yargı içermektedir?",
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
          "id": "e4_q11",
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
          "id": "e4_q12",
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
          "id": "e4_q13",
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
          "id": "e4_q14",
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
          "id": "e4_q15",
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
          "id": "e4_q16",
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
          "id": "e4_q17",
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
          "id": "e4_q18",
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
          "id": "e4_q19",
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
          "id": "e4_q20",
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
          "id": "e4_q21",
          "subject": "Türkçe",
          "number": 21,
          "text": "21. Aşağıdaki cümlelerin hangisinde bir <u>yazım yanlışı</u> yapılmıştır?",
          "options": [
            "A) Türk Dil Kurumu yeni kılavuzunu yayımladı.",
            "B) 4. yüzyılda pek çok önemli gelişme yaşandı.",
            "C) Bu konuda <u>herşey</u> planlandığı gibi gidiyor.",
            "D) TBMM'nin aldığı tarihi karar Resmi Gazete'de duyuruldu.",
            "E) Yanı sıra pek çok yabancı konuk da törene katıldı."
          ],
          "correct": 2,
          "solution": "'Herşey' sözcüğü 'Her şey' şeklinde ayrı yazılmalıdır. Şey sözcüğü daima ayrı yazılır."
        },
        {
          "id": "e4_q22",
          "subject": "Türkçe",
          "number": 22,
          "text": "22. Aşağıdaki cümlelerin hangisinde bir <u>yazım yanlışı</u> yapılmıştır?",
          "options": [
            "A) Türk Dil Kurumu yeni kılavuzunu yayımladı.",
            "B) 4. yüzyılda pek çok önemli gelişme yaşandı.",
            "C) Bu konuda <u>herşey</u> planlandığı gibi gidiyor.",
            "D) TBMM'nin aldığı tarihi karar Resmi Gazete'de duyuruldu.",
            "E) Yanı sıra pek çok yabancı konuk da törene katıldı."
          ],
          "correct": 2,
          "solution": "'Herşey' sözcüğü 'Her şey' şeklinde ayrı yazılmalıdır. Şey sözcüğü daima ayrı yazılır."
        },
        {
          "id": "e4_q23",
          "subject": "Türkçe",
          "number": 23,
          "text": "23. Aşağıdaki cümlelerin hangisinde bir <u>yazım yanlışı</u> yapılmıştır?",
          "options": [
            "A) Türk Dil Kurumu yeni kılavuzunu yayımladı.",
            "B) 4. yüzyılda pek çok önemli gelişme yaşandı.",
            "C) Bu konuda <u>herşey</u> planlandığı gibi gidiyor.",
            "D) TBMM'nin aldığı tarihi karar Resmi Gazete'de duyuruldu.",
            "E) Yanı sıra pek çok yabancı konuk da törene katıldı."
          ],
          "correct": 2,
          "solution": "'Herşey' sözcüğü 'Her şey' şeklinde ayrı yazılmalıdır. Şey sözcüğü daima ayrı yazılır."
        },
        {
          "id": "e4_q24",
          "subject": "Türkçe",
          "number": 24,
          "text": "24. Aşağıdaki cümlelerin hangisinde bir <u>yazım yanlışı</u> yapılmıştır?",
          "options": [
            "A) Türk Dil Kurumu yeni kılavuzunu yayımladı.",
            "B) 4. yüzyılda pek çok önemli gelişme yaşandı.",
            "C) Bu konuda <u>herşey</u> planlandığı gibi gidiyor.",
            "D) TBMM'nin aldığı tarihi karar Resmi Gazete'de duyuruldu.",
            "E) Yanı sıra pek çok yabancı konuk da törene katıldı."
          ],
          "correct": 2,
          "solution": "'Herşey' sözcüğü 'Her şey' şeklinde ayrı yazılmalıdır. Şey sözcüğü daima ayrı yazılır."
        },
        {
          "id": "e4_q25",
          "subject": "Türkçe",
          "number": 25,
          "text": "25. Aşağıdaki cümlelerin hangisinde bir <u>yazım yanlışı</u> yapılmıştır?",
          "options": [
            "A) Türk Dil Kurumu yeni kılavuzunu yayımladı.",
            "B) 4. yüzyılda pek çok önemli gelişme yaşandı.",
            "C) Bu konuda <u>herşey</u> planlandığı gibi gidiyor.",
            "D) TBMM'nin aldığı tarihi karar Resmi Gazete'de duyuruldu.",
            "E) Yanı sıra pek çok yabancı konuk da törene katıldı."
          ],
          "correct": 2,
          "solution": "'Herşey' sözcüğü 'Her şey' şeklinde ayrı yazılmalıdır. Şey sözcüğü daima ayrı yazılır."
        },
        {
          "id": "e4_q26",
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
          "id": "e4_q27",
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
          "id": "e4_q28",
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
          "id": "e4_q29",
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
          "id": "e4_q30",
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
          "id": "e4_q31",
          "subject": "Matematik",
          "number": 31,
          "text": "31. a ve b birer pozitif tam sayı olmak üzere,\n<code>3a + 5b = 83</code>\neşitliğini sağlayan en küçük b değeri için a kaçtır?",
          "options": [
            "A) 4",
            "B) 6",
            "C) 8",
            "D) 10",
            "E) 12"
          ],
          "correct": 1,
          "solution": "Denklemde b yerine en küçük pozitif tam sayı değerleri verilerek a = 6 olarak bulunur."
        },
        {
          "id": "e4_q32",
          "subject": "Matematik",
          "number": 32,
          "text": "32. a ve b birer pozitif tam sayı olmak üzere,\n<code>3a + 5b = 83</code>\neşitliğini sağlayan en küçük b değeri için a kaçtır?",
          "options": [
            "A) 4",
            "B) 6",
            "C) 8",
            "D) 10",
            "E) 12"
          ],
          "correct": 1,
          "solution": "Denklemde b yerine en küçük pozitif tam sayı değerleri verilerek a = 6 olarak bulunur."
        },
        {
          "id": "e4_q33",
          "subject": "Matematik",
          "number": 33,
          "text": "33. a ve b birer pozitif tam sayı olmak üzere,\n<code>3a + 5b = 83</code>\neşitliğini sağlayan en küçük b değeri için a kaçtır?",
          "options": [
            "A) 4",
            "B) 6",
            "C) 8",
            "D) 10",
            "E) 12"
          ],
          "correct": 1,
          "solution": "Denklemde b yerine en küçük pozitif tam sayı değerleri verilerek a = 6 olarak bulunur."
        },
        {
          "id": "e4_q34",
          "subject": "Matematik",
          "number": 34,
          "text": "34. a ve b birer pozitif tam sayı olmak üzere,\n<code>3a + 5b = 83</code>\neşitliğini sağlayan en küçük b değeri için a kaçtır?",
          "options": [
            "A) 4",
            "B) 6",
            "C) 8",
            "D) 10",
            "E) 12"
          ],
          "correct": 1,
          "solution": "Denklemde b yerine en küçük pozitif tam sayı değerleri verilerek a = 6 olarak bulunur."
        },
        {
          "id": "e4_q35",
          "subject": "Matematik",
          "number": 35,
          "text": "35. a ve b birer pozitif tam sayı olmak üzere,\n<code>3a + 5b = 83</code>\neşitliğini sağlayan en küçük b değeri için a kaçtır?",
          "options": [
            "A) 4",
            "B) 6",
            "C) 8",
            "D) 10",
            "E) 12"
          ],
          "correct": 1,
          "solution": "Denklemde b yerine en küçük pozitif tam sayı değerleri verilerek a = 6 olarak bulunur."
        },
        {
          "id": "e4_q36",
          "subject": "Matematik",
          "number": 36,
          "text": "36. <code>(1/2 + 1/3) : (5/6) + 2^5 = x</code>\nişleminin sonucu kaçtır?",
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
          "id": "e4_q37",
          "subject": "Matematik",
          "number": 37,
          "text": "37. <code>(1/2 + 1/3) : (5/6) + 2^6 = x</code>\nişleminin sonucu kaçtır?",
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
          "id": "e4_q38",
          "subject": "Matematik",
          "number": 38,
          "text": "38. <code>(1/2 + 1/3) : (5/6) + 2^7 = x</code>\nişleminin sonucu kaçtır?",
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
          "id": "e4_q39",
          "subject": "Matematik",
          "number": 39,
          "text": "39. <code>(1/2 + 1/3) : (5/6) + 2^8 = x</code>\nişleminin sonucu kaçtır?",
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
          "id": "e4_q40",
          "subject": "Matematik",
          "number": 40,
          "text": "40. <code>(1/2 + 1/3) : (5/6) + 2^9 = x</code>\nişleminin sonucu kaçtır?",
          "options": [
            "A) 513",
            "B) 514",
            "C) 512",
            "D) 257",
            "E) 515"
          ],
          "correct": 0,
          "solution": "(1/2 + 1/3) = 5/6. (5/6) : (5/6) = 1. Sonuç = 1 + 2^9 = 513."
        },
        {
          "id": "e4_q41",
          "subject": "Matematik",
          "number": 41,
          "text": "41. <code>(1/2 + 1/3) : (5/6) + 2^10 = x</code>\nişleminin sonucu kaçtır?",
          "options": [
            "A) 1025",
            "B) 1026",
            "C) 1024",
            "D) 513",
            "E) 1027"
          ],
          "correct": 0,
          "solution": "(1/2 + 1/3) = 5/6. (5/6) : (5/6) = 1. Sonuç = 1 + 2^10 = 1025."
        },
        {
          "id": "e4_q42",
          "subject": "Matematik",
          "number": 42,
          "text": "42. <code>(1/2 + 1/3) : (5/6) + 2^11 = x</code>\nişleminin sonucu kaçtır?",
          "options": [
            "A) 2049",
            "B) 2050",
            "C) 2048",
            "D) 1025",
            "E) 2051"
          ],
          "correct": 0,
          "solution": "(1/2 + 1/3) = 5/6. (5/6) : (5/6) = 1. Sonuç = 1 + 2^11 = 2049."
        },
        {
          "id": "e4_q43",
          "subject": "Matematik",
          "number": 43,
          "text": "43. Bir babanın bugünkü yaşı 44, oğlunun bugünkü yaşı ise 10'dır.\nBuna göre kaç yıl sonra babanın yaşı oğlunun yaşının 3 katı olur?",
          "options": [
            "A) 5",
            "B) 6",
            "C) 7",
            "D) 8",
            "E) 9"
          ],
          "correct": 2,
          "solution": "44 + t = 3(10 + t) => 44 + t = 30 + 3t => 2t = 14 => t = 7 yıl sonra."
        },
        {
          "id": "e4_q44",
          "subject": "Matematik",
          "number": 44,
          "text": "44. Bir babanın bugünkü yaşı 44, oğlunun bugünkü yaşı ise 10'dır.\nBuna göre kaç yıl sonra babanın yaşı oğlunun yaşının 3 katı olur?",
          "options": [
            "A) 5",
            "B) 6",
            "C) 7",
            "D) 8",
            "E) 9"
          ],
          "correct": 2,
          "solution": "44 + t = 3(10 + t) => 44 + t = 30 + 3t => 2t = 14 => t = 7 yıl sonra."
        },
        {
          "id": "e4_q45",
          "subject": "Matematik",
          "number": 45,
          "text": "45. Bir babanın bugünkü yaşı 44, oğlunun bugünkü yaşı ise 10'dır.\nBuna göre kaç yıl sonra babanın yaşı oğlunun yaşının 3 katı olur?",
          "options": [
            "A) 5",
            "B) 6",
            "C) 7",
            "D) 8",
            "E) 9"
          ],
          "correct": 2,
          "solution": "44 + t = 3(10 + t) => 44 + t = 30 + 3t => 2t = 14 => t = 7 yıl sonra."
        },
        {
          "id": "e4_q46",
          "subject": "Matematik",
          "number": 46,
          "text": "46. Bir babanın bugünkü yaşı 44, oğlunun bugünkü yaşı ise 10'dır.\nBuna göre kaç yıl sonra babanın yaşı oğlunun yaşının 3 katı olur?",
          "options": [
            "A) 5",
            "B) 6",
            "C) 7",
            "D) 8",
            "E) 9"
          ],
          "correct": 2,
          "solution": "44 + t = 3(10 + t) => 44 + t = 30 + 3t => 2t = 14 => t = 7 yıl sonra."
        },
        {
          "id": "e4_q47",
          "subject": "Matematik",
          "number": 47,
          "text": "47. Bir babanın bugünkü yaşı 44, oğlunun bugünkü yaşı ise 10'dır.\nBuna göre kaç yıl sonra babanın yaşı oğlunun yaşının 3 katı olur?",
          "options": [
            "A) 5",
            "B) 6",
            "C) 7",
            "D) 8",
            "E) 9"
          ],
          "correct": 2,
          "solution": "44 + t = 3(10 + t) => 44 + t = 30 + 3t => 2t = 14 => t = 7 yıl sonra."
        },
        {
          "id": "e4_q48",
          "subject": "Matematik",
          "number": 48,
          "text": "48. Bir babanın bugünkü yaşı 44, oğlunun bugünkü yaşı ise 10'dır.\nBuna göre kaç yıl sonra babanın yaşı oğlunun yaşının 3 katı olur?",
          "options": [
            "A) 5",
            "B) 6",
            "C) 7",
            "D) 8",
            "E) 9"
          ],
          "correct": 2,
          "solution": "44 + t = 3(10 + t) => 44 + t = 30 + 3t => 2t = 14 => t = 7 yıl sonra."
        },
        {
          "id": "e4_q49",
          "subject": "Matematik",
          "number": 49,
          "text": "49. Bir babanın bugünkü yaşı 44, oğlunun bugünkü yaşı ise 10'dır.\nBuna göre kaç yıl sonra babanın yaşı oğlunun yaşının 3 katı olur?",
          "options": [
            "A) 5",
            "B) 6",
            "C) 7",
            "D) 8",
            "E) 9"
          ],
          "correct": 2,
          "solution": "44 + t = 3(10 + t) => 44 + t = 30 + 3t => 2t = 14 => t = 7 yıl sonra."
        },
        {
          "id": "e4_q50",
          "subject": "Matematik",
          "number": 50,
          "text": "50. Bir babanın bugünkü yaşı 44, oğlunun bugünkü yaşı ise 10'dır.\nBuna göre kaç yıl sonra babanın yaşı oğlunun yaşının 3 katı olur?",
          "options": [
            "A) 5",
            "B) 6",
            "C) 7",
            "D) 8",
            "E) 9"
          ],
          "correct": 2,
          "solution": "44 + t = 3(10 + t) => 44 + t = 30 + 3t => 2t = 14 => t = 7 yıl sonra."
        },
        {
          "id": "e4_q51",
          "subject": "Matematik",
          "number": 51,
          "text": "51. Bir babanın bugünkü yaşı 44, oğlunun bugünkü yaşı ise 10'dır.\nBuna göre kaç yıl sonra babanın yaşı oğlunun yaşının 3 katı olur?",
          "options": [
            "A) 5",
            "B) 6",
            "C) 7",
            "D) 8",
            "E) 9"
          ],
          "correct": 2,
          "solution": "44 + t = 3(10 + t) => 44 + t = 30 + 3t => 2t = 14 => t = 7 yıl sonra."
        },
        {
          "id": "e4_q52",
          "subject": "Matematik",
          "number": 52,
          "text": "52. Bir babanın bugünkü yaşı 44, oğlunun bugünkü yaşı ise 10'dır.\nBuna göre kaç yıl sonra babanın yaşı oğlunun yaşının 3 katı olur?",
          "options": [
            "A) 5",
            "B) 6",
            "C) 7",
            "D) 8",
            "E) 9"
          ],
          "correct": 2,
          "solution": "44 + t = 3(10 + t) => 44 + t = 30 + 3t => 2t = 14 => t = 7 yıl sonra."
        },
        {
          "id": "e4_q53",
          "subject": "Matematik",
          "number": 53,
          "text": "53. Bir babanın bugünkü yaşı 44, oğlunun bugünkü yaşı ise 10'dır.\nBuna göre kaç yıl sonra babanın yaşı oğlunun yaşının 3 katı olur?",
          "options": [
            "A) 5",
            "B) 6",
            "C) 7",
            "D) 8",
            "E) 9"
          ],
          "correct": 2,
          "solution": "44 + t = 3(10 + t) => 44 + t = 30 + 3t => 2t = 14 => t = 7 yıl sonra."
        },
        {
          "id": "e4_q54",
          "subject": "Matematik",
          "number": 54,
          "text": "54. Bir babanın bugünkü yaşı 44, oğlunun bugünkü yaşı ise 10'dır.\nBuna göre kaç yıl sonra babanın yaşı oğlunun yaşının 3 katı olur?",
          "options": [
            "A) 5",
            "B) 6",
            "C) 7",
            "D) 8",
            "E) 9"
          ],
          "correct": 2,
          "solution": "44 + t = 3(10 + t) => 44 + t = 30 + 3t => 2t = 14 => t = 7 yıl sonra."
        },
        {
          "id": "e4_q55",
          "subject": "Matematik",
          "number": 55,
          "text": "55. A ve B iki küme olmak üzere,\n<code>s(A) = 16</code>, <code>s(B) = 14</code> ve <code>s(A ∩ B) = 6</code>\nolduğuna göre <code>s(A ∪ B)</code> kaçtır?",
          "options": [
            "A) 22",
            "B) 24",
            "C) 26",
            "D) 28",
            "E) 30"
          ],
          "correct": 1,
          "solution": "s(A ∪ B) = s(A) + s(B) - s(A ∩ B) = 16 + 14 - 6 = 24."
        },
        {
          "id": "e4_q56",
          "subject": "Matematik",
          "number": 56,
          "text": "56. A ve B iki küme olmak üzere,\n<code>s(A) = 16</code>, <code>s(B) = 14</code> ve <code>s(A ∩ B) = 6</code>\nolduğuna göre <code>s(A ∪ B)</code> kaçtır?",
          "options": [
            "A) 22",
            "B) 24",
            "C) 26",
            "D) 28",
            "E) 30"
          ],
          "correct": 1,
          "solution": "s(A ∪ B) = s(A) + s(B) - s(A ∩ B) = 16 + 14 - 6 = 24."
        },
        {
          "id": "e4_q57",
          "subject": "Matematik",
          "number": 57,
          "text": "57. A ve B iki küme olmak üzere,\n<code>s(A) = 16</code>, <code>s(B) = 14</code> ve <code>s(A ∩ B) = 6</code>\nolduğuna göre <code>s(A ∪ B)</code> kaçtır?",
          "options": [
            "A) 22",
            "B) 24",
            "C) 26",
            "D) 28",
            "E) 30"
          ],
          "correct": 1,
          "solution": "s(A ∪ B) = s(A) + s(B) - s(A ∩ B) = 16 + 14 - 6 = 24."
        },
        {
          "id": "e4_q58",
          "subject": "Matematik",
          "number": 58,
          "text": "58. A ve B iki küme olmak üzere,\n<code>s(A) = 16</code>, <code>s(B) = 14</code> ve <code>s(A ∩ B) = 6</code>\nolduğuna göre <code>s(A ∪ B)</code> kaçtır?",
          "options": [
            "A) 22",
            "B) 24",
            "C) 26",
            "D) 28",
            "E) 30"
          ],
          "correct": 1,
          "solution": "s(A ∪ B) = s(A) + s(B) - s(A ∩ B) = 16 + 14 - 6 = 24."
        },
        {
          "id": "e4_q59",
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
          "id": "e4_q60",
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
          "id": "e4_q61",
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
          "id": "e4_q62",
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
          "id": "e4_q63",
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
          "id": "e4_q64",
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
          "id": "e4_q65",
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
          "id": "e4_q66",
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
          "id": "e4_q67",
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
          "id": "e4_q68",
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
          "id": "e4_q69",
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
          "id": "e4_q70",
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
          "id": "e4_q71",
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
          "id": "e4_q72",
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
          "id": "e4_q73",
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
          "id": "e4_q74",
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
          "id": "e4_q75",
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
          "id": "e4_q76",
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
          "id": "e4_q77",
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
          "id": "e4_q78",
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
          "id": "e4_q79",
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
          "id": "e4_q80",
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
          "id": "e4_q81",
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
          "id": "e4_q82",
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
          "id": "e4_q83",
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
          "id": "e4_q84",
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
          "id": "e4_q85",
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
          "id": "e4_q86",
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
          "id": "e4_q87",
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
          "id": "e4_q88",
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
          "id": "e4_q89",
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
          "id": "e4_q90",
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
          "id": "e4_q91",
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
          "id": "e4_q92",
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
          "id": "e4_q93",
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
          "id": "e4_q94",
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
          "id": "e4_q95",
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
          "id": "e4_q96",
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
          "id": "e4_q97",
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
          "id": "e4_q98",
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
          "id": "e4_q99",
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
          "id": "e4_q100",
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
          "id": "e4_q101",
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
          "id": "e4_q102",
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
          "id": "e4_q103",
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
          "id": "e4_q104",
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
          "id": "e4_q105",
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
          "id": "e4_q106",
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
          "id": "e4_q107",
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
          "id": "e4_q108",
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
          "id": "e4_q109",
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
          "id": "e4_q110",
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
          "id": "e4_q111",
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
          "id": "e4_q112",
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
          "id": "e4_q113",
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
          "id": "e4_q114",
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
          "id": "e4_q115",
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
          "id": "e4_q116",
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
          "id": "e4_q117",
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
          "id": "e4_q118",
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
          "id": "e4_q119",
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
          "id": "e4_q120",
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
    {
      "id": "deneme_5",
      "title": "KPSS 2026 Ortaöğretim - 5. Deneme Sınavı (120 Soru)",
      "totalDurationMinutes": 130,
      "questions": [
        {
          "id": "e5_q1",
          "subject": "Türkçe",
          "number": 1,
          "text": "1. Aşağıdaki cümlelerin hangisinde <u>'keskin'</u> sözcüğü 'kesici olmayan, etkileyici ve sert' anlamında kullanılmıştır?",
          "options": [
            "A) Pencerenin kenarındaki nesne yere düştü.",
            "B) Olaylar karşısında <u>keskin</u> bir zekaya sahip olduğunu gösterdi.",
            "C) Günün ilk saatlerinde dışarıda serin bir hava vardı.",
            "D) Bahçedeki ağaçların gölgesinde dinlenmeyi seçti.",
            "E) Kitaplarını çantasına özenle yerleştirdi."
          ],
          "correct": 1,
          "solution": "Seçenekteki 'keskin' kelimesi mecazi olarak 'kesici olmayan, etkileyici ve sert' anlamında kullanılmıştır."
        },
        {
          "id": "e5_q2",
          "subject": "Türkçe",
          "number": 2,
          "text": "2. Aşağıdaki cümlelerin hangisinde <u>'burun kıvırmak'</u> deyimi 'küçümsemek, beğenmemek' anlamında kullanılmıştır?",
          "options": [
            "A) Sabah erkenden kalkıp iş yerine gitti.",
            "B) Kendisine sunulan cazip tekliflere nedense <u>burun kıvırdı</u>.",
            "C) Tren vaktinde istasyona yanaşarak yolcularını aldı.",
            "D) Bahçede rengarenk çiçekler açmıştı.",
            "E) Raporun son halini inceleyip imzaladı."
          ],
          "correct": 1,
          "solution": "Deyim cümlede 'küçümsemek, beğenmemek' anlamını karşılayacak şekilde yer almıştır."
        },
        {
          "id": "e5_q3",
          "subject": "Türkçe",
          "number": 3,
          "text": "3. (I) Şairin 53 yılında yayımlanan bu eseri yoğun bir ilgi gördü. (II) Kitapta yer alan imgeler okurun hayal dünyasını zenginleştiriyor. (III) Eser toplam 120 sayfadan ve 45 şiirden oluşmaktadır. (IV) Bence dönemin en başarılı şiir kitabı budur. (V) Kitabın ikinci baskısı geçen ay yapıldı.\n\nBu parçadaki numaralanmış cümlelerden hangisi <u>öznel</u> bir yargı içermektedir?",
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
          "id": "e5_q4",
          "subject": "Türkçe",
          "number": 4,
          "text": "4. (I) Şairin 54 yılında yayımlanan bu eseri yoğun bir ilgi gördü. (II) Kitapta yer alan imgeler okurun hayal dünyasını zenginleştiriyor. (III) Eser toplam 120 sayfadan ve 45 şiirden oluşmaktadır. (IV) Bence dönemin en başarılı şiir kitabı budur. (V) Kitabın ikinci baskısı geçen ay yapıldı.\n\nBu parçadaki numaralanmış cümlelerden hangisi <u>öznel</u> bir yargı içermektedir?",
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
          "id": "e5_q5",
          "subject": "Türkçe",
          "number": 5,
          "text": "5. (I) Şairin 55 yılında yayımlanan bu eseri yoğun bir ilgi gördü. (II) Kitapta yer alan imgeler okurun hayal dünyasını zenginleştiriyor. (III) Eser toplam 120 sayfadan ve 45 şiirden oluşmaktadır. (IV) Bence dönemin en başarılı şiir kitabı budur. (V) Kitabın ikinci baskısı geçen ay yapıldı.\n\nBu parçadaki numaralanmış cümlelerden hangisi <u>öznel</u> bir yargı içermektedir?",
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
          "id": "e5_q6",
          "subject": "Türkçe",
          "number": 6,
          "text": "6. (I) Şairin 56 yılında yayımlanan bu eseri yoğun bir ilgi gördü. (II) Kitapta yer alan imgeler okurun hayal dünyasını zenginleştiriyor. (III) Eser toplam 120 sayfadan ve 45 şiirden oluşmaktadır. (IV) Bence dönemin en başarılı şiir kitabı budur. (V) Kitabın ikinci baskısı geçen ay yapıldı.\n\nBu parçadaki numaralanmış cümlelerden hangisi <u>öznel</u> bir yargı içermektedir?",
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
          "id": "e5_q7",
          "subject": "Türkçe",
          "number": 7,
          "text": "7. (I) Şairin 57 yılında yayımlanan bu eseri yoğun bir ilgi gördü. (II) Kitapta yer alan imgeler okurun hayal dünyasını zenginleştiriyor. (III) Eser toplam 120 sayfadan ve 45 şiirden oluşmaktadır. (IV) Bence dönemin en başarılı şiir kitabı budur. (V) Kitabın ikinci baskısı geçen ay yapıldı.\n\nBu parçadaki numaralanmış cümlelerden hangisi <u>öznel</u> bir yargı içermektedir?",
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
          "id": "e5_q8",
          "subject": "Türkçe",
          "number": 8,
          "text": "8. (I) Şairin 58 yılında yayımlanan bu eseri yoğun bir ilgi gördü. (II) Kitapta yer alan imgeler okurun hayal dünyasını zenginleştiriyor. (III) Eser toplam 120 sayfadan ve 45 şiirden oluşmaktadır. (IV) Bence dönemin en başarılı şiir kitabı budur. (V) Kitabın ikinci baskısı geçen ay yapıldı.\n\nBu parçadaki numaralanmış cümlelerden hangisi <u>öznel</u> bir yargı içermektedir?",
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
          "id": "e5_q9",
          "subject": "Türkçe",
          "number": 9,
          "text": "9. (I) Şairin 59 yılında yayımlanan bu eseri yoğun bir ilgi gördü. (II) Kitapta yer alan imgeler okurun hayal dünyasını zenginleştiriyor. (III) Eser toplam 120 sayfadan ve 45 şiirden oluşmaktadır. (IV) Bence dönemin en başarılı şiir kitabı budur. (V) Kitabın ikinci baskısı geçen ay yapıldı.\n\nBu parçadaki numaralanmış cümlelerden hangisi <u>öznel</u> bir yargı içermektedir?",
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
          "id": "e5_q10",
          "subject": "Türkçe",
          "number": 10,
          "text": "10. (I) Şairin 60 yılında yayımlanan bu eseri yoğun bir ilgi gördü. (II) Kitapta yer alan imgeler okurun hayal dünyasını zenginleştiriyor. (III) Eser toplam 120 sayfadan ve 45 şiirden oluşmaktadır. (IV) Bence dönemin en başarılı şiir kitabı budur. (V) Kitabın ikinci baskısı geçen ay yapıldı.\n\nBu parçadaki numaralanmış cümlelerden hangisi <u>öznel</u> bir yargı içermektedir?",
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
          "id": "e5_q11",
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
          "id": "e5_q12",
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
          "id": "e5_q13",
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
          "id": "e5_q14",
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
          "id": "e5_q15",
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
          "id": "e5_q16",
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
          "id": "e5_q17",
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
          "id": "e5_q18",
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
          "id": "e5_q19",
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
          "id": "e5_q20",
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
          "id": "e5_q21",
          "subject": "Türkçe",
          "number": 21,
          "text": "21. Aşağıdaki cümlelerin hangisinde bir <u>yazım yanlışı</u> yapılmıştır?",
          "options": [
            "A) Türk Dil Kurumu yeni kılavuzunu yayımladı.",
            "B) 5. yüzyılda pek çok önemli gelişme yaşandı.",
            "C) Bu konuda <u>herşey</u> planlandığı gibi gidiyor.",
            "D) TBMM'nin aldığı tarihi karar Resmi Gazete'de duyuruldu.",
            "E) Yanı sıra pek çok yabancı konuk da törene katıldı."
          ],
          "correct": 2,
          "solution": "'Herşey' sözcüğü 'Her şey' şeklinde ayrı yazılmalıdır. Şey sözcüğü daima ayrı yazılır."
        },
        {
          "id": "e5_q22",
          "subject": "Türkçe",
          "number": 22,
          "text": "22. Aşağıdaki cümlelerin hangisinde bir <u>yazım yanlışı</u> yapılmıştır?",
          "options": [
            "A) Türk Dil Kurumu yeni kılavuzunu yayımladı.",
            "B) 5. yüzyılda pek çok önemli gelişme yaşandı.",
            "C) Bu konuda <u>herşey</u> planlandığı gibi gidiyor.",
            "D) TBMM'nin aldığı tarihi karar Resmi Gazete'de duyuruldu.",
            "E) Yanı sıra pek çok yabancı konuk da törene katıldı."
          ],
          "correct": 2,
          "solution": "'Herşey' sözcüğü 'Her şey' şeklinde ayrı yazılmalıdır. Şey sözcüğü daima ayrı yazılır."
        },
        {
          "id": "e5_q23",
          "subject": "Türkçe",
          "number": 23,
          "text": "23. Aşağıdaki cümlelerin hangisinde bir <u>yazım yanlışı</u> yapılmıştır?",
          "options": [
            "A) Türk Dil Kurumu yeni kılavuzunu yayımladı.",
            "B) 5. yüzyılda pek çok önemli gelişme yaşandı.",
            "C) Bu konuda <u>herşey</u> planlandığı gibi gidiyor.",
            "D) TBMM'nin aldığı tarihi karar Resmi Gazete'de duyuruldu.",
            "E) Yanı sıra pek çok yabancı konuk da törene katıldı."
          ],
          "correct": 2,
          "solution": "'Herşey' sözcüğü 'Her şey' şeklinde ayrı yazılmalıdır. Şey sözcüğü daima ayrı yazılır."
        },
        {
          "id": "e5_q24",
          "subject": "Türkçe",
          "number": 24,
          "text": "24. Aşağıdaki cümlelerin hangisinde bir <u>yazım yanlışı</u> yapılmıştır?",
          "options": [
            "A) Türk Dil Kurumu yeni kılavuzunu yayımladı.",
            "B) 5. yüzyılda pek çok önemli gelişme yaşandı.",
            "C) Bu konuda <u>herşey</u> planlandığı gibi gidiyor.",
            "D) TBMM'nin aldığı tarihi karar Resmi Gazete'de duyuruldu.",
            "E) Yanı sıra pek çok yabancı konuk da törene katıldı."
          ],
          "correct": 2,
          "solution": "'Herşey' sözcüğü 'Her şey' şeklinde ayrı yazılmalıdır. Şey sözcüğü daima ayrı yazılır."
        },
        {
          "id": "e5_q25",
          "subject": "Türkçe",
          "number": 25,
          "text": "25. Aşağıdaki cümlelerin hangisinde bir <u>yazım yanlışı</u> yapılmıştır?",
          "options": [
            "A) Türk Dil Kurumu yeni kılavuzunu yayımladı.",
            "B) 5. yüzyılda pek çok önemli gelişme yaşandı.",
            "C) Bu konuda <u>herşey</u> planlandığı gibi gidiyor.",
            "D) TBMM'nin aldığı tarihi karar Resmi Gazete'de duyuruldu.",
            "E) Yanı sıra pek çok yabancı konuk da törene katıldı."
          ],
          "correct": 2,
          "solution": "'Herşey' sözcüğü 'Her şey' şeklinde ayrı yazılmalıdır. Şey sözcüğü daima ayrı yazılır."
        },
        {
          "id": "e5_q26",
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
          "id": "e5_q27",
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
          "id": "e5_q28",
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
          "id": "e5_q29",
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
          "id": "e5_q30",
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
          "id": "e5_q31",
          "subject": "Matematik",
          "number": 31,
          "text": "31. a ve b birer pozitif tam sayı olmak üzere,\n<code>3a + 5b = 101</code>\neşitliğini sağlayan en küçük b değeri için a kaçtır?",
          "options": [
            "A) 5",
            "B) 7",
            "C) 9",
            "D) 11",
            "E) 13"
          ],
          "correct": 1,
          "solution": "Denklemde b yerine en küçük pozitif tam sayı değerleri verilerek a = 7 olarak bulunur."
        },
        {
          "id": "e5_q32",
          "subject": "Matematik",
          "number": 32,
          "text": "32. a ve b birer pozitif tam sayı olmak üzere,\n<code>3a + 5b = 101</code>\neşitliğini sağlayan en küçük b değeri için a kaçtır?",
          "options": [
            "A) 5",
            "B) 7",
            "C) 9",
            "D) 11",
            "E) 13"
          ],
          "correct": 1,
          "solution": "Denklemde b yerine en küçük pozitif tam sayı değerleri verilerek a = 7 olarak bulunur."
        },
        {
          "id": "e5_q33",
          "subject": "Matematik",
          "number": 33,
          "text": "33. a ve b birer pozitif tam sayı olmak üzere,\n<code>3a + 5b = 101</code>\neşitliğini sağlayan en küçük b değeri için a kaçtır?",
          "options": [
            "A) 5",
            "B) 7",
            "C) 9",
            "D) 11",
            "E) 13"
          ],
          "correct": 1,
          "solution": "Denklemde b yerine en küçük pozitif tam sayı değerleri verilerek a = 7 olarak bulunur."
        },
        {
          "id": "e5_q34",
          "subject": "Matematik",
          "number": 34,
          "text": "34. a ve b birer pozitif tam sayı olmak üzere,\n<code>3a + 5b = 101</code>\neşitliğini sağlayan en küçük b değeri için a kaçtır?",
          "options": [
            "A) 5",
            "B) 7",
            "C) 9",
            "D) 11",
            "E) 13"
          ],
          "correct": 1,
          "solution": "Denklemde b yerine en küçük pozitif tam sayı değerleri verilerek a = 7 olarak bulunur."
        },
        {
          "id": "e5_q35",
          "subject": "Matematik",
          "number": 35,
          "text": "35. a ve b birer pozitif tam sayı olmak üzere,\n<code>3a + 5b = 101</code>\neşitliğini sağlayan en küçük b değeri için a kaçtır?",
          "options": [
            "A) 5",
            "B) 7",
            "C) 9",
            "D) 11",
            "E) 13"
          ],
          "correct": 1,
          "solution": "Denklemde b yerine en küçük pozitif tam sayı değerleri verilerek a = 7 olarak bulunur."
        },
        {
          "id": "e5_q36",
          "subject": "Matematik",
          "number": 36,
          "text": "36. <code>(1/2 + 1/3) : (5/6) + 2^6 = x</code>\nişleminin sonucu kaçtır?",
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
          "id": "e5_q37",
          "subject": "Matematik",
          "number": 37,
          "text": "37. <code>(1/2 + 1/3) : (5/6) + 2^7 = x</code>\nişleminin sonucu kaçtır?",
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
          "id": "e5_q38",
          "subject": "Matematik",
          "number": 38,
          "text": "38. <code>(1/2 + 1/3) : (5/6) + 2^8 = x</code>\nişleminin sonucu kaçtır?",
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
          "id": "e5_q39",
          "subject": "Matematik",
          "number": 39,
          "text": "39. <code>(1/2 + 1/3) : (5/6) + 2^9 = x</code>\nişleminin sonucu kaçtır?",
          "options": [
            "A) 513",
            "B) 514",
            "C) 512",
            "D) 257",
            "E) 515"
          ],
          "correct": 0,
          "solution": "(1/2 + 1/3) = 5/6. (5/6) : (5/6) = 1. Sonuç = 1 + 2^9 = 513."
        },
        {
          "id": "e5_q40",
          "subject": "Matematik",
          "number": 40,
          "text": "40. <code>(1/2 + 1/3) : (5/6) + 2^10 = x</code>\nişleminin sonucu kaçtır?",
          "options": [
            "A) 1025",
            "B) 1026",
            "C) 1024",
            "D) 513",
            "E) 1027"
          ],
          "correct": 0,
          "solution": "(1/2 + 1/3) = 5/6. (5/6) : (5/6) = 1. Sonuç = 1 + 2^10 = 1025."
        },
        {
          "id": "e5_q41",
          "subject": "Matematik",
          "number": 41,
          "text": "41. <code>(1/2 + 1/3) : (5/6) + 2^11 = x</code>\nişleminin sonucu kaçtır?",
          "options": [
            "A) 2049",
            "B) 2050",
            "C) 2048",
            "D) 1025",
            "E) 2051"
          ],
          "correct": 0,
          "solution": "(1/2 + 1/3) = 5/6. (5/6) : (5/6) = 1. Sonuç = 1 + 2^11 = 2049."
        },
        {
          "id": "e5_q42",
          "subject": "Matematik",
          "number": 42,
          "text": "42. <code>(1/2 + 1/3) : (5/6) + 2^12 = x</code>\nişleminin sonucu kaçtır?",
          "options": [
            "A) 4097",
            "B) 4098",
            "C) 4096",
            "D) 2049",
            "E) 4099"
          ],
          "correct": 0,
          "solution": "(1/2 + 1/3) = 5/6. (5/6) : (5/6) = 1. Sonuç = 1 + 2^12 = 4097."
        },
        {
          "id": "e5_q43",
          "subject": "Matematik",
          "number": 43,
          "text": "43. Bir babanın bugünkü yaşı 46, oğlunun bugünkü yaşı ise 11'dır.\nBuna göre kaç yıl sonra babanın yaşı oğlunun yaşının 3 katı olur?",
          "options": [
            "A) 4",
            "B) 5",
            "C) 6",
            "D) 7",
            "E) 8"
          ],
          "correct": 2,
          "solution": "46 + t = 3(11 + t) => 46 + t = 33 + 3t => 2t = 13 => t = 6 yıl sonra."
        },
        {
          "id": "e5_q44",
          "subject": "Matematik",
          "number": 44,
          "text": "44. Bir babanın bugünkü yaşı 46, oğlunun bugünkü yaşı ise 11'dır.\nBuna göre kaç yıl sonra babanın yaşı oğlunun yaşının 3 katı olur?",
          "options": [
            "A) 4",
            "B) 5",
            "C) 6",
            "D) 7",
            "E) 8"
          ],
          "correct": 2,
          "solution": "46 + t = 3(11 + t) => 46 + t = 33 + 3t => 2t = 13 => t = 6 yıl sonra."
        },
        {
          "id": "e5_q45",
          "subject": "Matematik",
          "number": 45,
          "text": "45. Bir babanın bugünkü yaşı 46, oğlunun bugünkü yaşı ise 11'dır.\nBuna göre kaç yıl sonra babanın yaşı oğlunun yaşının 3 katı olur?",
          "options": [
            "A) 4",
            "B) 5",
            "C) 6",
            "D) 7",
            "E) 8"
          ],
          "correct": 2,
          "solution": "46 + t = 3(11 + t) => 46 + t = 33 + 3t => 2t = 13 => t = 6 yıl sonra."
        },
        {
          "id": "e5_q46",
          "subject": "Matematik",
          "number": 46,
          "text": "46. Bir babanın bugünkü yaşı 46, oğlunun bugünkü yaşı ise 11'dır.\nBuna göre kaç yıl sonra babanın yaşı oğlunun yaşının 3 katı olur?",
          "options": [
            "A) 4",
            "B) 5",
            "C) 6",
            "D) 7",
            "E) 8"
          ],
          "correct": 2,
          "solution": "46 + t = 3(11 + t) => 46 + t = 33 + 3t => 2t = 13 => t = 6 yıl sonra."
        },
        {
          "id": "e5_q47",
          "subject": "Matematik",
          "number": 47,
          "text": "47. Bir babanın bugünkü yaşı 46, oğlunun bugünkü yaşı ise 11'dır.\nBuna göre kaç yıl sonra babanın yaşı oğlunun yaşının 3 katı olur?",
          "options": [
            "A) 4",
            "B) 5",
            "C) 6",
            "D) 7",
            "E) 8"
          ],
          "correct": 2,
          "solution": "46 + t = 3(11 + t) => 46 + t = 33 + 3t => 2t = 13 => t = 6 yıl sonra."
        },
        {
          "id": "e5_q48",
          "subject": "Matematik",
          "number": 48,
          "text": "48. Bir babanın bugünkü yaşı 46, oğlunun bugünkü yaşı ise 11'dır.\nBuna göre kaç yıl sonra babanın yaşı oğlunun yaşının 3 katı olur?",
          "options": [
            "A) 4",
            "B) 5",
            "C) 6",
            "D) 7",
            "E) 8"
          ],
          "correct": 2,
          "solution": "46 + t = 3(11 + t) => 46 + t = 33 + 3t => 2t = 13 => t = 6 yıl sonra."
        },
        {
          "id": "e5_q49",
          "subject": "Matematik",
          "number": 49,
          "text": "49. Bir babanın bugünkü yaşı 46, oğlunun bugünkü yaşı ise 11'dır.\nBuna göre kaç yıl sonra babanın yaşı oğlunun yaşının 3 katı olur?",
          "options": [
            "A) 4",
            "B) 5",
            "C) 6",
            "D) 7",
            "E) 8"
          ],
          "correct": 2,
          "solution": "46 + t = 3(11 + t) => 46 + t = 33 + 3t => 2t = 13 => t = 6 yıl sonra."
        },
        {
          "id": "e5_q50",
          "subject": "Matematik",
          "number": 50,
          "text": "50. Bir babanın bugünkü yaşı 46, oğlunun bugünkü yaşı ise 11'dır.\nBuna göre kaç yıl sonra babanın yaşı oğlunun yaşının 3 katı olur?",
          "options": [
            "A) 4",
            "B) 5",
            "C) 6",
            "D) 7",
            "E) 8"
          ],
          "correct": 2,
          "solution": "46 + t = 3(11 + t) => 46 + t = 33 + 3t => 2t = 13 => t = 6 yıl sonra."
        },
        {
          "id": "e5_q51",
          "subject": "Matematik",
          "number": 51,
          "text": "51. Bir babanın bugünkü yaşı 46, oğlunun bugünkü yaşı ise 11'dır.\nBuna göre kaç yıl sonra babanın yaşı oğlunun yaşının 3 katı olur?",
          "options": [
            "A) 4",
            "B) 5",
            "C) 6",
            "D) 7",
            "E) 8"
          ],
          "correct": 2,
          "solution": "46 + t = 3(11 + t) => 46 + t = 33 + 3t => 2t = 13 => t = 6 yıl sonra."
        },
        {
          "id": "e5_q52",
          "subject": "Matematik",
          "number": 52,
          "text": "52. Bir babanın bugünkü yaşı 46, oğlunun bugünkü yaşı ise 11'dır.\nBuna göre kaç yıl sonra babanın yaşı oğlunun yaşının 3 katı olur?",
          "options": [
            "A) 4",
            "B) 5",
            "C) 6",
            "D) 7",
            "E) 8"
          ],
          "correct": 2,
          "solution": "46 + t = 3(11 + t) => 46 + t = 33 + 3t => 2t = 13 => t = 6 yıl sonra."
        },
        {
          "id": "e5_q53",
          "subject": "Matematik",
          "number": 53,
          "text": "53. Bir babanın bugünkü yaşı 46, oğlunun bugünkü yaşı ise 11'dır.\nBuna göre kaç yıl sonra babanın yaşı oğlunun yaşının 3 katı olur?",
          "options": [
            "A) 4",
            "B) 5",
            "C) 6",
            "D) 7",
            "E) 8"
          ],
          "correct": 2,
          "solution": "46 + t = 3(11 + t) => 46 + t = 33 + 3t => 2t = 13 => t = 6 yıl sonra."
        },
        {
          "id": "e5_q54",
          "subject": "Matematik",
          "number": 54,
          "text": "54. Bir babanın bugünkü yaşı 46, oğlunun bugünkü yaşı ise 11'dır.\nBuna göre kaç yıl sonra babanın yaşı oğlunun yaşının 3 katı olur?",
          "options": [
            "A) 4",
            "B) 5",
            "C) 6",
            "D) 7",
            "E) 8"
          ],
          "correct": 2,
          "solution": "46 + t = 3(11 + t) => 46 + t = 33 + 3t => 2t = 13 => t = 6 yıl sonra."
        },
        {
          "id": "e5_q55",
          "subject": "Matematik",
          "number": 55,
          "text": "55. A ve B iki küme olmak üzere,\n<code>s(A) = 17</code>, <code>s(B) = 15</code> ve <code>s(A ∩ B) = 6</code>\nolduğuna göre <code>s(A ∪ B)</code> kaçtır?",
          "options": [
            "A) 24",
            "B) 26",
            "C) 28",
            "D) 30",
            "E) 32"
          ],
          "correct": 1,
          "solution": "s(A ∪ B) = s(A) + s(B) - s(A ∩ B) = 17 + 15 - 6 = 26."
        },
        {
          "id": "e5_q56",
          "subject": "Matematik",
          "number": 56,
          "text": "56. A ve B iki küme olmak üzere,\n<code>s(A) = 17</code>, <code>s(B) = 15</code> ve <code>s(A ∩ B) = 6</code>\nolduğuna göre <code>s(A ∪ B)</code> kaçtır?",
          "options": [
            "A) 24",
            "B) 26",
            "C) 28",
            "D) 30",
            "E) 32"
          ],
          "correct": 1,
          "solution": "s(A ∪ B) = s(A) + s(B) - s(A ∩ B) = 17 + 15 - 6 = 26."
        },
        {
          "id": "e5_q57",
          "subject": "Matematik",
          "number": 57,
          "text": "57. A ve B iki küme olmak üzere,\n<code>s(A) = 17</code>, <code>s(B) = 15</code> ve <code>s(A ∩ B) = 6</code>\nolduğuna göre <code>s(A ∪ B)</code> kaçtır?",
          "options": [
            "A) 24",
            "B) 26",
            "C) 28",
            "D) 30",
            "E) 32"
          ],
          "correct": 1,
          "solution": "s(A ∪ B) = s(A) + s(B) - s(A ∩ B) = 17 + 15 - 6 = 26."
        },
        {
          "id": "e5_q58",
          "subject": "Matematik",
          "number": 58,
          "text": "58. A ve B iki küme olmak üzere,\n<code>s(A) = 17</code>, <code>s(B) = 15</code> ve <code>s(A ∩ B) = 6</code>\nolduğuna göre <code>s(A ∪ B)</code> kaçtır?",
          "options": [
            "A) 24",
            "B) 26",
            "C) 28",
            "D) 30",
            "E) 32"
          ],
          "correct": 1,
          "solution": "s(A ∪ B) = s(A) + s(B) - s(A ∩ B) = 17 + 15 - 6 = 26."
        },
        {
          "id": "e5_q59",
          "subject": "Matematik",
          "number": 59,
          "text": "59. Dik kenar uzunlukları 9 cm ve 12 cm olan bir dik üçgenin hipotenüs uzunluğu kaç cm'dir?",
          "options": [
            "A) 14",
            "B) 15",
            "C) 16",
            "D) 17",
            "E) 18"
          ],
          "correct": 1,
          "solution": "Pisagor bağıntısı: a² + b² = c² => 9² + 12² = 225 = 15² => Hipotenüs = 15 cm (3-4-5 katı)."
        },
        {
          "id": "e5_q60",
          "subject": "Matematik",
          "number": 60,
          "text": "60. Dik kenar uzunlukları 9 cm ve 12 cm olan bir dik üçgenin hipotenüs uzunluğu kaç cm'dir?",
          "options": [
            "A) 14",
            "B) 15",
            "C) 16",
            "D) 17",
            "E) 18"
          ],
          "correct": 1,
          "solution": "Pisagor bağıntısı: a² + b² = c² => 9² + 12² = 225 = 15² => Hipotenüs = 15 cm (3-4-5 katı)."
        },
        {
          "id": "e5_q61",
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
          "id": "e5_q62",
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
          "id": "e5_q63",
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
          "id": "e5_q64",
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
          "id": "e5_q65",
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
          "id": "e5_q66",
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
          "id": "e5_q67",
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
          "id": "e5_q68",
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
          "id": "e5_q69",
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
          "id": "e5_q70",
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
          "id": "e5_q71",
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
          "id": "e5_q72",
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
          "id": "e5_q73",
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
          "id": "e5_q74",
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
          "id": "e5_q75",
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
          "id": "e5_q76",
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
          "id": "e5_q77",
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
          "id": "e5_q78",
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
          "id": "e5_q79",
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
          "id": "e5_q80",
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
          "id": "e5_q81",
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
          "id": "e5_q82",
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
          "id": "e5_q83",
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
          "id": "e5_q84",
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
          "id": "e5_q85",
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
          "id": "e5_q86",
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
          "id": "e5_q87",
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
          "id": "e5_q88",
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
          "id": "e5_q89",
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
          "id": "e5_q90",
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
          "id": "e5_q91",
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
          "id": "e5_q92",
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
          "id": "e5_q93",
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
          "id": "e5_q94",
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
          "id": "e5_q95",
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
          "id": "e5_q96",
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
          "id": "e5_q97",
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
          "id": "e5_q98",
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
          "id": "e5_q99",
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
          "id": "e5_q100",
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
          "id": "e5_q101",
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
          "id": "e5_q102",
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
          "id": "e5_q103",
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
          "id": "e5_q104",
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
          "id": "e5_q105",
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
          "id": "e5_q106",
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
          "id": "e5_q107",
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
          "id": "e5_q108",
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
          "id": "e5_q109",
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
          "id": "e5_q110",
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
          "id": "e5_q111",
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
          "id": "e5_q112",
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
          "id": "e5_q113",
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
          "id": "e5_q114",
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
          "id": "e5_q115",
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
          "id": "e5_q116",
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
          "id": "e5_q117",
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
          "id": "e5_q118",
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
          "id": "e5_q119",
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
          "id": "e5_q120",
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
    {
      "id": "deneme_6",
      "title": "KPSS 2026 Ortaöğretim - 6. Deneme Sınavı (120 Soru)",
      "totalDurationMinutes": 130,
      "questions": [
        {
          "id": "e6_q1",
          "subject": "Türkçe",
          "number": 1,
          "text": "1. Aşağıdaki cümlelerin hangisinde <u>'parlak'</u> sözcüğü 'geleceği umut vadeden, başarılı' anlamında kullanılmıştır?",
          "options": [
            "A) Pencerenin kenarındaki nesne yere düştü.",
            "B) Yolun karşısındaki durağa doğru hızlıca koştu.",
            "C) Genç sporcunun çok <u>parlak</u> bir kariyeri olacağı anlaşılıyor.",
            "D) Bahçedeki ağaçların gölgesinde dinlenmeyi seçti.",
            "E) Kitaplarını çantasına özenle yerleştirdi."
          ],
          "correct": 2,
          "solution": "Seçenekteki 'parlak' kelimesi mecazi olarak 'geleceği umut vadeden, başarılı' anlamında kullanılmıştır."
        },
        {
          "id": "e6_q2",
          "subject": "Türkçe",
          "number": 2,
          "text": "2. Aşağıdaki cümlelerin hangisinde <u>'can kulağıyla dinlemek'</u> deyimi 'büyük dikkatle dinlemek' anlamında kullanılmıştır?",
          "options": [
            "A) Öğretmenin anlattığı dersi <u>can kulağıyla dinledi</u>.",
            "B) Kütüphanedeki sessizliği kimse bozmak istemiyordu.",
            "C) Tren vaktinde istasyona yanaşarak yolcularını aldı.",
            "D) Bahçede rengarenk çiçekler açmıştı.",
            "E) Raporun son halini inceleyip imzaladı."
          ],
          "correct": 0,
          "solution": "Deyim cümlede 'büyük dikkatle dinlemek' anlamını karşılayacak şekilde yer almıştır."
        },
        {
          "id": "e6_q3",
          "subject": "Türkçe",
          "number": 3,
          "text": "3. (I) Şairin 63 yılında yayımlanan bu eseri yoğun bir ilgi gördü. (II) Kitapta yer alan imgeler okurun hayal dünyasını zenginleştiriyor. (III) Eser toplam 120 sayfadan ve 45 şiirden oluşmaktadır. (IV) Bence dönemin en başarılı şiir kitabı budur. (V) Kitabın ikinci baskısı geçen ay yapıldı.\n\nBu parçadaki numaralanmış cümlelerden hangisi <u>öznel</u> bir yargı içermektedir?",
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
          "id": "e6_q4",
          "subject": "Türkçe",
          "number": 4,
          "text": "4. (I) Şairin 64 yılında yayımlanan bu eseri yoğun bir ilgi gördü. (II) Kitapta yer alan imgeler okurun hayal dünyasını zenginleştiriyor. (III) Eser toplam 120 sayfadan ve 45 şiirden oluşmaktadır. (IV) Bence dönemin en başarılı şiir kitabı budur. (V) Kitabın ikinci baskısı geçen ay yapıldı.\n\nBu parçadaki numaralanmış cümlelerden hangisi <u>öznel</u> bir yargı içermektedir?",
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
          "id": "e6_q5",
          "subject": "Türkçe",
          "number": 5,
          "text": "5. (I) Şairin 65 yılında yayımlanan bu eseri yoğun bir ilgi gördü. (II) Kitapta yer alan imgeler okurun hayal dünyasını zenginleştiriyor. (III) Eser toplam 120 sayfadan ve 45 şiirden oluşmaktadır. (IV) Bence dönemin en başarılı şiir kitabı budur. (V) Kitabın ikinci baskısı geçen ay yapıldı.\n\nBu parçadaki numaralanmış cümlelerden hangisi <u>öznel</u> bir yargı içermektedir?",
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
          "id": "e6_q6",
          "subject": "Türkçe",
          "number": 6,
          "text": "6. (I) Şairin 66 yılında yayımlanan bu eseri yoğun bir ilgi gördü. (II) Kitapta yer alan imgeler okurun hayal dünyasını zenginleştiriyor. (III) Eser toplam 120 sayfadan ve 45 şiirden oluşmaktadır. (IV) Bence dönemin en başarılı şiir kitabı budur. (V) Kitabın ikinci baskısı geçen ay yapıldı.\n\nBu parçadaki numaralanmış cümlelerden hangisi <u>öznel</u> bir yargı içermektedir?",
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
          "id": "e6_q7",
          "subject": "Türkçe",
          "number": 7,
          "text": "7. (I) Şairin 67 yılında yayımlanan bu eseri yoğun bir ilgi gördü. (II) Kitapta yer alan imgeler okurun hayal dünyasını zenginleştiriyor. (III) Eser toplam 120 sayfadan ve 45 şiirden oluşmaktadır. (IV) Bence dönemin en başarılı şiir kitabı budur. (V) Kitabın ikinci baskısı geçen ay yapıldı.\n\nBu parçadaki numaralanmış cümlelerden hangisi <u>öznel</u> bir yargı içermektedir?",
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
          "id": "e6_q8",
          "subject": "Türkçe",
          "number": 8,
          "text": "8. (I) Şairin 68 yılında yayımlanan bu eseri yoğun bir ilgi gördü. (II) Kitapta yer alan imgeler okurun hayal dünyasını zenginleştiriyor. (III) Eser toplam 120 sayfadan ve 45 şiirden oluşmaktadır. (IV) Bence dönemin en başarılı şiir kitabı budur. (V) Kitabın ikinci baskısı geçen ay yapıldı.\n\nBu parçadaki numaralanmış cümlelerden hangisi <u>öznel</u> bir yargı içermektedir?",
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
          "id": "e6_q9",
          "subject": "Türkçe",
          "number": 9,
          "text": "9. (I) Şairin 69 yılında yayımlanan bu eseri yoğun bir ilgi gördü. (II) Kitapta yer alan imgeler okurun hayal dünyasını zenginleştiriyor. (III) Eser toplam 120 sayfadan ve 45 şiirden oluşmaktadır. (IV) Bence dönemin en başarılı şiir kitabı budur. (V) Kitabın ikinci baskısı geçen ay yapıldı.\n\nBu parçadaki numaralanmış cümlelerden hangisi <u>öznel</u> bir yargı içermektedir?",
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
          "id": "e6_q10",
          "subject": "Türkçe",
          "number": 10,
          "text": "10. (I) Şairin 70 yılında yayımlanan bu eseri yoğun bir ilgi gördü. (II) Kitapta yer alan imgeler okurun hayal dünyasını zenginleştiriyor. (III) Eser toplam 120 sayfadan ve 45 şiirden oluşmaktadır. (IV) Bence dönemin en başarılı şiir kitabı budur. (V) Kitabın ikinci baskısı geçen ay yapıldı.\n\nBu parçadaki numaralanmış cümlelerden hangisi <u>öznel</u> bir yargı içermektedir?",
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
          "id": "e6_q11",
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
          "id": "e6_q12",
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
          "id": "e6_q13",
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
          "id": "e6_q14",
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
          "id": "e6_q15",
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
          "id": "e6_q16",
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
          "id": "e6_q17",
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
          "id": "e6_q18",
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
          "id": "e6_q19",
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
          "id": "e6_q20",
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
          "id": "e6_q21",
          "subject": "Türkçe",
          "number": 21,
          "text": "21. Aşağıdaki cümlelerin hangisinde bir <u>yazım yanlışı</u> yapılmıştır?",
          "options": [
            "A) Türk Dil Kurumu yeni kılavuzunu yayımladı.",
            "B) 6. yüzyılda pek çok önemli gelişme yaşandı.",
            "C) Bu konuda <u>herşey</u> planlandığı gibi gidiyor.",
            "D) TBMM'nin aldığı tarihi karar Resmi Gazete'de duyuruldu.",
            "E) Yanı sıra pek çok yabancı konuk da törene katıldı."
          ],
          "correct": 2,
          "solution": "'Herşey' sözcüğü 'Her şey' şeklinde ayrı yazılmalıdır. Şey sözcüğü daima ayrı yazılır."
        },
        {
          "id": "e6_q22",
          "subject": "Türkçe",
          "number": 22,
          "text": "22. Aşağıdaki cümlelerin hangisinde bir <u>yazım yanlışı</u> yapılmıştır?",
          "options": [
            "A) Türk Dil Kurumu yeni kılavuzunu yayımladı.",
            "B) 6. yüzyılda pek çok önemli gelişme yaşandı.",
            "C) Bu konuda <u>herşey</u> planlandığı gibi gidiyor.",
            "D) TBMM'nin aldığı tarihi karar Resmi Gazete'de duyuruldu.",
            "E) Yanı sıra pek çok yabancı konuk da törene katıldı."
          ],
          "correct": 2,
          "solution": "'Herşey' sözcüğü 'Her şey' şeklinde ayrı yazılmalıdır. Şey sözcüğü daima ayrı yazılır."
        },
        {
          "id": "e6_q23",
          "subject": "Türkçe",
          "number": 23,
          "text": "23. Aşağıdaki cümlelerin hangisinde bir <u>yazım yanlışı</u> yapılmıştır?",
          "options": [
            "A) Türk Dil Kurumu yeni kılavuzunu yayımladı.",
            "B) 6. yüzyılda pek çok önemli gelişme yaşandı.",
            "C) Bu konuda <u>herşey</u> planlandığı gibi gidiyor.",
            "D) TBMM'nin aldığı tarihi karar Resmi Gazete'de duyuruldu.",
            "E) Yanı sıra pek çok yabancı konuk da törene katıldı."
          ],
          "correct": 2,
          "solution": "'Herşey' sözcüğü 'Her şey' şeklinde ayrı yazılmalıdır. Şey sözcüğü daima ayrı yazılır."
        },
        {
          "id": "e6_q24",
          "subject": "Türkçe",
          "number": 24,
          "text": "24. Aşağıdaki cümlelerin hangisinde bir <u>yazım yanlışı</u> yapılmıştır?",
          "options": [
            "A) Türk Dil Kurumu yeni kılavuzunu yayımladı.",
            "B) 6. yüzyılda pek çok önemli gelişme yaşandı.",
            "C) Bu konuda <u>herşey</u> planlandığı gibi gidiyor.",
            "D) TBMM'nin aldığı tarihi karar Resmi Gazete'de duyuruldu.",
            "E) Yanı sıra pek çok yabancı konuk da törene katıldı."
          ],
          "correct": 2,
          "solution": "'Herşey' sözcüğü 'Her şey' şeklinde ayrı yazılmalıdır. Şey sözcüğü daima ayrı yazılır."
        },
        {
          "id": "e6_q25",
          "subject": "Türkçe",
          "number": 25,
          "text": "25. Aşağıdaki cümlelerin hangisinde bir <u>yazım yanlışı</u> yapılmıştır?",
          "options": [
            "A) Türk Dil Kurumu yeni kılavuzunu yayımladı.",
            "B) 6. yüzyılda pek çok önemli gelişme yaşandı.",
            "C) Bu konuda <u>herşey</u> planlandığı gibi gidiyor.",
            "D) TBMM'nin aldığı tarihi karar Resmi Gazete'de duyuruldu.",
            "E) Yanı sıra pek çok yabancı konuk da törene katıldı."
          ],
          "correct": 2,
          "solution": "'Herşey' sözcüğü 'Her şey' şeklinde ayrı yazılmalıdır. Şey sözcüğü daima ayrı yazılır."
        },
        {
          "id": "e6_q26",
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
          "id": "e6_q27",
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
          "id": "e6_q28",
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
          "id": "e6_q29",
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
          "id": "e6_q30",
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
          "id": "e6_q31",
          "subject": "Matematik",
          "number": 31,
          "text": "31. a ve b birer pozitif tam sayı olmak üzere,\n<code>3a + 5b = 119</code>\neşitliğini sağlayan en küçük b değeri için a kaçtır?",
          "options": [
            "A) 6",
            "B) 8",
            "C) 10",
            "D) 12",
            "E) 14"
          ],
          "correct": 1,
          "solution": "Denklemde b yerine en küçük pozitif tam sayı değerleri verilerek a = 8 olarak bulunur."
        },
        {
          "id": "e6_q32",
          "subject": "Matematik",
          "number": 32,
          "text": "32. a ve b birer pozitif tam sayı olmak üzere,\n<code>3a + 5b = 119</code>\neşitliğini sağlayan en küçük b değeri için a kaçtır?",
          "options": [
            "A) 6",
            "B) 8",
            "C) 10",
            "D) 12",
            "E) 14"
          ],
          "correct": 1,
          "solution": "Denklemde b yerine en küçük pozitif tam sayı değerleri verilerek a = 8 olarak bulunur."
        },
        {
          "id": "e6_q33",
          "subject": "Matematik",
          "number": 33,
          "text": "33. a ve b birer pozitif tam sayı olmak üzere,\n<code>3a + 5b = 119</code>\neşitliğini sağlayan en küçük b değeri için a kaçtır?",
          "options": [
            "A) 6",
            "B) 8",
            "C) 10",
            "D) 12",
            "E) 14"
          ],
          "correct": 1,
          "solution": "Denklemde b yerine en küçük pozitif tam sayı değerleri verilerek a = 8 olarak bulunur."
        },
        {
          "id": "e6_q34",
          "subject": "Matematik",
          "number": 34,
          "text": "34. a ve b birer pozitif tam sayı olmak üzere,\n<code>3a + 5b = 119</code>\neşitliğini sağlayan en küçük b değeri için a kaçtır?",
          "options": [
            "A) 6",
            "B) 8",
            "C) 10",
            "D) 12",
            "E) 14"
          ],
          "correct": 1,
          "solution": "Denklemde b yerine en küçük pozitif tam sayı değerleri verilerek a = 8 olarak bulunur."
        },
        {
          "id": "e6_q35",
          "subject": "Matematik",
          "number": 35,
          "text": "35. a ve b birer pozitif tam sayı olmak üzere,\n<code>3a + 5b = 119</code>\neşitliğini sağlayan en küçük b değeri için a kaçtır?",
          "options": [
            "A) 6",
            "B) 8",
            "C) 10",
            "D) 12",
            "E) 14"
          ],
          "correct": 1,
          "solution": "Denklemde b yerine en küçük pozitif tam sayı değerleri verilerek a = 8 olarak bulunur."
        },
        {
          "id": "e6_q36",
          "subject": "Matematik",
          "number": 36,
          "text": "36. <code>(1/2 + 1/3) : (5/6) + 2^7 = x</code>\nişleminin sonucu kaçtır?",
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
          "id": "e6_q37",
          "subject": "Matematik",
          "number": 37,
          "text": "37. <code>(1/2 + 1/3) : (5/6) + 2^8 = x</code>\nişleminin sonucu kaçtır?",
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
          "id": "e6_q38",
          "subject": "Matematik",
          "number": 38,
          "text": "38. <code>(1/2 + 1/3) : (5/6) + 2^9 = x</code>\nişleminin sonucu kaçtır?",
          "options": [
            "A) 513",
            "B) 514",
            "C) 512",
            "D) 257",
            "E) 515"
          ],
          "correct": 0,
          "solution": "(1/2 + 1/3) = 5/6. (5/6) : (5/6) = 1. Sonuç = 1 + 2^9 = 513."
        },
        {
          "id": "e6_q39",
          "subject": "Matematik",
          "number": 39,
          "text": "39. <code>(1/2 + 1/3) : (5/6) + 2^10 = x</code>\nişleminin sonucu kaçtır?",
          "options": [
            "A) 1025",
            "B) 1026",
            "C) 1024",
            "D) 513",
            "E) 1027"
          ],
          "correct": 0,
          "solution": "(1/2 + 1/3) = 5/6. (5/6) : (5/6) = 1. Sonuç = 1 + 2^10 = 1025."
        },
        {
          "id": "e6_q40",
          "subject": "Matematik",
          "number": 40,
          "text": "40. <code>(1/2 + 1/3) : (5/6) + 2^11 = x</code>\nişleminin sonucu kaçtır?",
          "options": [
            "A) 2049",
            "B) 2050",
            "C) 2048",
            "D) 1025",
            "E) 2051"
          ],
          "correct": 0,
          "solution": "(1/2 + 1/3) = 5/6. (5/6) : (5/6) = 1. Sonuç = 1 + 2^11 = 2049."
        },
        {
          "id": "e6_q41",
          "subject": "Matematik",
          "number": 41,
          "text": "41. <code>(1/2 + 1/3) : (5/6) + 2^12 = x</code>\nişleminin sonucu kaçtır?",
          "options": [
            "A) 4097",
            "B) 4098",
            "C) 4096",
            "D) 2049",
            "E) 4099"
          ],
          "correct": 0,
          "solution": "(1/2 + 1/3) = 5/6. (5/6) : (5/6) = 1. Sonuç = 1 + 2^12 = 4097."
        },
        {
          "id": "e6_q42",
          "subject": "Matematik",
          "number": 42,
          "text": "42. <code>(1/2 + 1/3) : (5/6) + 2^13 = x</code>\nişleminin sonucu kaçtır?",
          "options": [
            "A) 8193",
            "B) 8194",
            "C) 8192",
            "D) 4097",
            "E) 8195"
          ],
          "correct": 0,
          "solution": "(1/2 + 1/3) = 5/6. (5/6) : (5/6) = 1. Sonuç = 1 + 2^13 = 8193."
        },
        {
          "id": "e6_q43",
          "subject": "Matematik",
          "number": 43,
          "text": "43. Bir babanın bugünkü yaşı 48, oğlunun bugünkü yaşı ise 12'dır.\nBuna göre kaç yıl sonra babanın yaşı oğlunun yaşının 3 katı olur?",
          "options": [
            "A) 4",
            "B) 5",
            "C) 6",
            "D) 7",
            "E) 8"
          ],
          "correct": 2,
          "solution": "48 + t = 3(12 + t) => 48 + t = 36 + 3t => 2t = 12 => t = 6 yıl sonra."
        },
        {
          "id": "e6_q44",
          "subject": "Matematik",
          "number": 44,
          "text": "44. Bir babanın bugünkü yaşı 48, oğlunun bugünkü yaşı ise 12'dır.\nBuna göre kaç yıl sonra babanın yaşı oğlunun yaşının 3 katı olur?",
          "options": [
            "A) 4",
            "B) 5",
            "C) 6",
            "D) 7",
            "E) 8"
          ],
          "correct": 2,
          "solution": "48 + t = 3(12 + t) => 48 + t = 36 + 3t => 2t = 12 => t = 6 yıl sonra."
        },
        {
          "id": "e6_q45",
          "subject": "Matematik",
          "number": 45,
          "text": "45. Bir babanın bugünkü yaşı 48, oğlunun bugünkü yaşı ise 12'dır.\nBuna göre kaç yıl sonra babanın yaşı oğlunun yaşının 3 katı olur?",
          "options": [
            "A) 4",
            "B) 5",
            "C) 6",
            "D) 7",
            "E) 8"
          ],
          "correct": 2,
          "solution": "48 + t = 3(12 + t) => 48 + t = 36 + 3t => 2t = 12 => t = 6 yıl sonra."
        },
        {
          "id": "e6_q46",
          "subject": "Matematik",
          "number": 46,
          "text": "46. Bir babanın bugünkü yaşı 48, oğlunun bugünkü yaşı ise 12'dır.\nBuna göre kaç yıl sonra babanın yaşı oğlunun yaşının 3 katı olur?",
          "options": [
            "A) 4",
            "B) 5",
            "C) 6",
            "D) 7",
            "E) 8"
          ],
          "correct": 2,
          "solution": "48 + t = 3(12 + t) => 48 + t = 36 + 3t => 2t = 12 => t = 6 yıl sonra."
        },
        {
          "id": "e6_q47",
          "subject": "Matematik",
          "number": 47,
          "text": "47. Bir babanın bugünkü yaşı 48, oğlunun bugünkü yaşı ise 12'dır.\nBuna göre kaç yıl sonra babanın yaşı oğlunun yaşının 3 katı olur?",
          "options": [
            "A) 4",
            "B) 5",
            "C) 6",
            "D) 7",
            "E) 8"
          ],
          "correct": 2,
          "solution": "48 + t = 3(12 + t) => 48 + t = 36 + 3t => 2t = 12 => t = 6 yıl sonra."
        },
        {
          "id": "e6_q48",
          "subject": "Matematik",
          "number": 48,
          "text": "48. Bir babanın bugünkü yaşı 48, oğlunun bugünkü yaşı ise 12'dır.\nBuna göre kaç yıl sonra babanın yaşı oğlunun yaşının 3 katı olur?",
          "options": [
            "A) 4",
            "B) 5",
            "C) 6",
            "D) 7",
            "E) 8"
          ],
          "correct": 2,
          "solution": "48 + t = 3(12 + t) => 48 + t = 36 + 3t => 2t = 12 => t = 6 yıl sonra."
        },
        {
          "id": "e6_q49",
          "subject": "Matematik",
          "number": 49,
          "text": "49. Bir babanın bugünkü yaşı 48, oğlunun bugünkü yaşı ise 12'dır.\nBuna göre kaç yıl sonra babanın yaşı oğlunun yaşının 3 katı olur?",
          "options": [
            "A) 4",
            "B) 5",
            "C) 6",
            "D) 7",
            "E) 8"
          ],
          "correct": 2,
          "solution": "48 + t = 3(12 + t) => 48 + t = 36 + 3t => 2t = 12 => t = 6 yıl sonra."
        },
        {
          "id": "e6_q50",
          "subject": "Matematik",
          "number": 50,
          "text": "50. Bir babanın bugünkü yaşı 48, oğlunun bugünkü yaşı ise 12'dır.\nBuna göre kaç yıl sonra babanın yaşı oğlunun yaşının 3 katı olur?",
          "options": [
            "A) 4",
            "B) 5",
            "C) 6",
            "D) 7",
            "E) 8"
          ],
          "correct": 2,
          "solution": "48 + t = 3(12 + t) => 48 + t = 36 + 3t => 2t = 12 => t = 6 yıl sonra."
        },
        {
          "id": "e6_q51",
          "subject": "Matematik",
          "number": 51,
          "text": "51. Bir babanın bugünkü yaşı 48, oğlunun bugünkü yaşı ise 12'dır.\nBuna göre kaç yıl sonra babanın yaşı oğlunun yaşının 3 katı olur?",
          "options": [
            "A) 4",
            "B) 5",
            "C) 6",
            "D) 7",
            "E) 8"
          ],
          "correct": 2,
          "solution": "48 + t = 3(12 + t) => 48 + t = 36 + 3t => 2t = 12 => t = 6 yıl sonra."
        },
        {
          "id": "e6_q52",
          "subject": "Matematik",
          "number": 52,
          "text": "52. Bir babanın bugünkü yaşı 48, oğlunun bugünkü yaşı ise 12'dır.\nBuna göre kaç yıl sonra babanın yaşı oğlunun yaşının 3 katı olur?",
          "options": [
            "A) 4",
            "B) 5",
            "C) 6",
            "D) 7",
            "E) 8"
          ],
          "correct": 2,
          "solution": "48 + t = 3(12 + t) => 48 + t = 36 + 3t => 2t = 12 => t = 6 yıl sonra."
        },
        {
          "id": "e6_q53",
          "subject": "Matematik",
          "number": 53,
          "text": "53. Bir babanın bugünkü yaşı 48, oğlunun bugünkü yaşı ise 12'dır.\nBuna göre kaç yıl sonra babanın yaşı oğlunun yaşının 3 katı olur?",
          "options": [
            "A) 4",
            "B) 5",
            "C) 6",
            "D) 7",
            "E) 8"
          ],
          "correct": 2,
          "solution": "48 + t = 3(12 + t) => 48 + t = 36 + 3t => 2t = 12 => t = 6 yıl sonra."
        },
        {
          "id": "e6_q54",
          "subject": "Matematik",
          "number": 54,
          "text": "54. Bir babanın bugünkü yaşı 48, oğlunun bugünkü yaşı ise 12'dır.\nBuna göre kaç yıl sonra babanın yaşı oğlunun yaşının 3 katı olur?",
          "options": [
            "A) 4",
            "B) 5",
            "C) 6",
            "D) 7",
            "E) 8"
          ],
          "correct": 2,
          "solution": "48 + t = 3(12 + t) => 48 + t = 36 + 3t => 2t = 12 => t = 6 yıl sonra."
        },
        {
          "id": "e6_q55",
          "subject": "Matematik",
          "number": 55,
          "text": "55. A ve B iki küme olmak üzere,\n<code>s(A) = 18</code>, <code>s(B) = 16</code> ve <code>s(A ∩ B) = 7</code>\nolduğuna göre <code>s(A ∪ B)</code> kaçtır?",
          "options": [
            "A) 25",
            "B) 27",
            "C) 29",
            "D) 31",
            "E) 33"
          ],
          "correct": 1,
          "solution": "s(A ∪ B) = s(A) + s(B) - s(A ∩ B) = 18 + 16 - 7 = 27."
        },
        {
          "id": "e6_q56",
          "subject": "Matematik",
          "number": 56,
          "text": "56. A ve B iki küme olmak üzere,\n<code>s(A) = 18</code>, <code>s(B) = 16</code> ve <code>s(A ∩ B) = 7</code>\nolduğuna göre <code>s(A ∪ B)</code> kaçtır?",
          "options": [
            "A) 25",
            "B) 27",
            "C) 29",
            "D) 31",
            "E) 33"
          ],
          "correct": 1,
          "solution": "s(A ∪ B) = s(A) + s(B) - s(A ∩ B) = 18 + 16 - 7 = 27."
        },
        {
          "id": "e6_q57",
          "subject": "Matematik",
          "number": 57,
          "text": "57. A ve B iki küme olmak üzere,\n<code>s(A) = 18</code>, <code>s(B) = 16</code> ve <code>s(A ∩ B) = 7</code>\nolduğuna göre <code>s(A ∪ B)</code> kaçtır?",
          "options": [
            "A) 25",
            "B) 27",
            "C) 29",
            "D) 31",
            "E) 33"
          ],
          "correct": 1,
          "solution": "s(A ∪ B) = s(A) + s(B) - s(A ∩ B) = 18 + 16 - 7 = 27."
        },
        {
          "id": "e6_q58",
          "subject": "Matematik",
          "number": 58,
          "text": "58. A ve B iki küme olmak üzere,\n<code>s(A) = 18</code>, <code>s(B) = 16</code> ve <code>s(A ∩ B) = 7</code>\nolduğuna göre <code>s(A ∪ B)</code> kaçtır?",
          "options": [
            "A) 25",
            "B) 27",
            "C) 29",
            "D) 31",
            "E) 33"
          ],
          "correct": 1,
          "solution": "s(A ∪ B) = s(A) + s(B) - s(A ∩ B) = 18 + 16 - 7 = 27."
        },
        {
          "id": "e6_q59",
          "subject": "Matematik",
          "number": 59,
          "text": "59. Dik kenar uzunlukları 3 cm ve 4 cm olan bir dik üçgenin hipotenüs uzunluğu kaç cm'dir?",
          "options": [
            "A) 4",
            "B) 5",
            "C) 6",
            "D) 7",
            "E) 8"
          ],
          "correct": 1,
          "solution": "Pisagor bağıntısı: a² + b² = c² => 3² + 4² = 25 = 5² => Hipotenüs = 5 cm (3-4-5 katı)."
        },
        {
          "id": "e6_q60",
          "subject": "Matematik",
          "number": 60,
          "text": "60. Dik kenar uzunlukları 3 cm ve 4 cm olan bir dik üçgenin hipotenüs uzunluğu kaç cm'dir?",
          "options": [
            "A) 4",
            "B) 5",
            "C) 6",
            "D) 7",
            "E) 8"
          ],
          "correct": 1,
          "solution": "Pisagor bağıntısı: a² + b² = c² => 3² + 4² = 25 = 5² => Hipotenüs = 5 cm (3-4-5 katı)."
        },
        {
          "id": "e6_q61",
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
          "id": "e6_q62",
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
          "id": "e6_q63",
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
          "id": "e6_q64",
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
          "id": "e6_q65",
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
          "id": "e6_q66",
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
          "id": "e6_q67",
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
          "id": "e6_q68",
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
          "id": "e6_q69",
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
          "id": "e6_q70",
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
          "id": "e6_q71",
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
          "id": "e6_q72",
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
          "id": "e6_q73",
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
          "id": "e6_q74",
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
          "id": "e6_q75",
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
          "id": "e6_q76",
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
          "id": "e6_q77",
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
          "id": "e6_q78",
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
          "id": "e6_q79",
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
          "id": "e6_q80",
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
          "id": "e6_q81",
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
          "id": "e6_q82",
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
          "id": "e6_q83",
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
          "id": "e6_q84",
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
          "id": "e6_q85",
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
          "id": "e6_q86",
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
          "id": "e6_q87",
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
          "id": "e6_q88",
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
          "id": "e6_q89",
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
          "id": "e6_q90",
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
          "id": "e6_q91",
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
          "id": "e6_q92",
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
          "id": "e6_q93",
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
          "id": "e6_q94",
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
          "id": "e6_q95",
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
          "id": "e6_q96",
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
          "id": "e6_q97",
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
          "id": "e6_q98",
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
          "id": "e6_q99",
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
          "id": "e6_q100",
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
          "id": "e6_q101",
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
          "id": "e6_q102",
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
          "id": "e6_q103",
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
          "id": "e6_q104",
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
          "id": "e6_q105",
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
          "id": "e6_q106",
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
          "id": "e6_q107",
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
          "id": "e6_q108",
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
          "id": "e6_q109",
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
          "id": "e6_q110",
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
          "id": "e6_q111",
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
          "id": "e6_q112",
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
          "id": "e6_q113",
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
          "id": "e6_q114",
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
          "id": "e6_q115",
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
          "id": "e6_q116",
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
          "id": "e6_q117",
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
          "id": "e6_q118",
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
          "id": "e6_q119",
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
          "id": "e6_q120",
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
    {
      "id": "deneme_7",
      "title": "KPSS 2026 Ortaöğretim - 7. Deneme Sınavı (120 Soru)",
      "totalDurationMinutes": 130,
      "questions": [
        {
          "id": "e7_q1",
          "subject": "Türkçe",
          "number": 1,
          "text": "1. Aşağıdaki cümlelerin hangisinde <u>'soğuk'</u> sözcüğü 'içten ve samimi olmayan' anlamında kullanılmıştır?",
          "options": [
            "A) Aramızda geçen tartışmadan sonra bana <u>soğuk</u> davrandı.",
            "B) Yolun karşısındaki durağa doğru hızlıca koştu.",
            "C) Günün ilk saatlerinde dışarıda serin bir hava vardı.",
            "D) Bahçedeki ağaçların gölgesinde dinlenmeyi seçti.",
            "E) Kitaplarını çantasına özenle yerleştirdi."
          ],
          "correct": 0,
          "solution": "Seçenekteki 'soğuk' kelimesi mecazi olarak 'içten ve samimi olmayan' anlamında kullanılmıştır."
        },
        {
          "id": "e7_q2",
          "subject": "Türkçe",
          "number": 2,
          "text": "2. Aşağıdaki cümlelerin hangisinde <u>'dil dökmek'</u> deyimi 'kandırmak için güzel sözler söylemek' anlamında kullanılmıştır?",
          "options": [
            "A) Sabah erkenden kalkıp iş yerine gitti.",
            "B) Kütüphanedeki sessizliği kimse bozmak istemiyordu.",
            "C) Onu ikna edebilmek için saatlerce <u>dil döktü</u>.",
            "D) Bahçede rengarenk çiçekler açmıştı.",
            "E) Raporun son halini inceleyip imzaladı."
          ],
          "correct": 2,
          "solution": "Deyim cümlede 'kandırmak için güzel sözler söylemek' anlamını karşılayacak şekilde yer almıştır."
        },
        {
          "id": "e7_q3",
          "subject": "Türkçe",
          "number": 3,
          "text": "3. (I) Şairin 73 yılında yayımlanan bu eseri yoğun bir ilgi gördü. (II) Kitapta yer alan imgeler okurun hayal dünyasını zenginleştiriyor. (III) Eser toplam 120 sayfadan ve 45 şiirden oluşmaktadır. (IV) Bence dönemin en başarılı şiir kitabı budur. (V) Kitabın ikinci baskısı geçen ay yapıldı.\n\nBu parçadaki numaralanmış cümlelerden hangisi <u>öznel</u> bir yargı içermektedir?",
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
          "id": "e7_q4",
          "subject": "Türkçe",
          "number": 4,
          "text": "4. (I) Şairin 74 yılında yayımlanan bu eseri yoğun bir ilgi gördü. (II) Kitapta yer alan imgeler okurun hayal dünyasını zenginleştiriyor. (III) Eser toplam 120 sayfadan ve 45 şiirden oluşmaktadır. (IV) Bence dönemin en başarılı şiir kitabı budur. (V) Kitabın ikinci baskısı geçen ay yapıldı.\n\nBu parçadaki numaralanmış cümlelerden hangisi <u>öznel</u> bir yargı içermektedir?",
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
          "id": "e7_q5",
          "subject": "Türkçe",
          "number": 5,
          "text": "5. (I) Şairin 75 yılında yayımlanan bu eseri yoğun bir ilgi gördü. (II) Kitapta yer alan imgeler okurun hayal dünyasını zenginleştiriyor. (III) Eser toplam 120 sayfadan ve 45 şiirden oluşmaktadır. (IV) Bence dönemin en başarılı şiir kitabı budur. (V) Kitabın ikinci baskısı geçen ay yapıldı.\n\nBu parçadaki numaralanmış cümlelerden hangisi <u>öznel</u> bir yargı içermektedir?",
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
          "id": "e7_q6",
          "subject": "Türkçe",
          "number": 6,
          "text": "6. (I) Şairin 76 yılında yayımlanan bu eseri yoğun bir ilgi gördü. (II) Kitapta yer alan imgeler okurun hayal dünyasını zenginleştiriyor. (III) Eser toplam 120 sayfadan ve 45 şiirden oluşmaktadır. (IV) Bence dönemin en başarılı şiir kitabı budur. (V) Kitabın ikinci baskısı geçen ay yapıldı.\n\nBu parçadaki numaralanmış cümlelerden hangisi <u>öznel</u> bir yargı içermektedir?",
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
          "id": "e7_q7",
          "subject": "Türkçe",
          "number": 7,
          "text": "7. (I) Şairin 77 yılında yayımlanan bu eseri yoğun bir ilgi gördü. (II) Kitapta yer alan imgeler okurun hayal dünyasını zenginleştiriyor. (III) Eser toplam 120 sayfadan ve 45 şiirden oluşmaktadır. (IV) Bence dönemin en başarılı şiir kitabı budur. (V) Kitabın ikinci baskısı geçen ay yapıldı.\n\nBu parçadaki numaralanmış cümlelerden hangisi <u>öznel</u> bir yargı içermektedir?",
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
          "id": "e7_q8",
          "subject": "Türkçe",
          "number": 8,
          "text": "8. (I) Şairin 78 yılında yayımlanan bu eseri yoğun bir ilgi gördü. (II) Kitapta yer alan imgeler okurun hayal dünyasını zenginleştiriyor. (III) Eser toplam 120 sayfadan ve 45 şiirden oluşmaktadır. (IV) Bence dönemin en başarılı şiir kitabı budur. (V) Kitabın ikinci baskısı geçen ay yapıldı.\n\nBu parçadaki numaralanmış cümlelerden hangisi <u>öznel</u> bir yargı içermektedir?",
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
          "id": "e7_q9",
          "subject": "Türkçe",
          "number": 9,
          "text": "9. (I) Şairin 79 yılında yayımlanan bu eseri yoğun bir ilgi gördü. (II) Kitapta yer alan imgeler okurun hayal dünyasını zenginleştiriyor. (III) Eser toplam 120 sayfadan ve 45 şiirden oluşmaktadır. (IV) Bence dönemin en başarılı şiir kitabı budur. (V) Kitabın ikinci baskısı geçen ay yapıldı.\n\nBu parçadaki numaralanmış cümlelerden hangisi <u>öznel</u> bir yargı içermektedir?",
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
          "id": "e7_q10",
          "subject": "Türkçe",
          "number": 10,
          "text": "10. (I) Şairin 80 yılında yayımlanan bu eseri yoğun bir ilgi gördü. (II) Kitapta yer alan imgeler okurun hayal dünyasını zenginleştiriyor. (III) Eser toplam 120 sayfadan ve 45 şiirden oluşmaktadır. (IV) Bence dönemin en başarılı şiir kitabı budur. (V) Kitabın ikinci baskısı geçen ay yapıldı.\n\nBu parçadaki numaralanmış cümlelerden hangisi <u>öznel</u> bir yargı içermektedir?",
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
          "id": "e7_q11",
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
          "id": "e7_q12",
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
          "id": "e7_q13",
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
          "id": "e7_q14",
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
          "id": "e7_q15",
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
          "id": "e7_q16",
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
          "id": "e7_q17",
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
          "id": "e7_q18",
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
          "id": "e7_q19",
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
          "id": "e7_q20",
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
          "id": "e7_q21",
          "subject": "Türkçe",
          "number": 21,
          "text": "21. Aşağıdaki cümlelerin hangisinde bir <u>yazım yanlışı</u> yapılmıştır?",
          "options": [
            "A) Türk Dil Kurumu yeni kılavuzunu yayımladı.",
            "B) 7. yüzyılda pek çok önemli gelişme yaşandı.",
            "C) Bu konuda <u>herşey</u> planlandığı gibi gidiyor.",
            "D) TBMM'nin aldığı tarihi karar Resmi Gazete'de duyuruldu.",
            "E) Yanı sıra pek çok yabancı konuk da törene katıldı."
          ],
          "correct": 2,
          "solution": "'Herşey' sözcüğü 'Her şey' şeklinde ayrı yazılmalıdır. Şey sözcüğü daima ayrı yazılır."
        },
        {
          "id": "e7_q22",
          "subject": "Türkçe",
          "number": 22,
          "text": "22. Aşağıdaki cümlelerin hangisinde bir <u>yazım yanlışı</u> yapılmıştır?",
          "options": [
            "A) Türk Dil Kurumu yeni kılavuzunu yayımladı.",
            "B) 7. yüzyılda pek çok önemli gelişme yaşandı.",
            "C) Bu konuda <u>herşey</u> planlandığı gibi gidiyor.",
            "D) TBMM'nin aldığı tarihi karar Resmi Gazete'de duyuruldu.",
            "E) Yanı sıra pek çok yabancı konuk da törene katıldı."
          ],
          "correct": 2,
          "solution": "'Herşey' sözcüğü 'Her şey' şeklinde ayrı yazılmalıdır. Şey sözcüğü daima ayrı yazılır."
        },
        {
          "id": "e7_q23",
          "subject": "Türkçe",
          "number": 23,
          "text": "23. Aşağıdaki cümlelerin hangisinde bir <u>yazım yanlışı</u> yapılmıştır?",
          "options": [
            "A) Türk Dil Kurumu yeni kılavuzunu yayımladı.",
            "B) 7. yüzyılda pek çok önemli gelişme yaşandı.",
            "C) Bu konuda <u>herşey</u> planlandığı gibi gidiyor.",
            "D) TBMM'nin aldığı tarihi karar Resmi Gazete'de duyuruldu.",
            "E) Yanı sıra pek çok yabancı konuk da törene katıldı."
          ],
          "correct": 2,
          "solution": "'Herşey' sözcüğü 'Her şey' şeklinde ayrı yazılmalıdır. Şey sözcüğü daima ayrı yazılır."
        },
        {
          "id": "e7_q24",
          "subject": "Türkçe",
          "number": 24,
          "text": "24. Aşağıdaki cümlelerin hangisinde bir <u>yazım yanlışı</u> yapılmıştır?",
          "options": [
            "A) Türk Dil Kurumu yeni kılavuzunu yayımladı.",
            "B) 7. yüzyılda pek çok önemli gelişme yaşandı.",
            "C) Bu konuda <u>herşey</u> planlandığı gibi gidiyor.",
            "D) TBMM'nin aldığı tarihi karar Resmi Gazete'de duyuruldu.",
            "E) Yanı sıra pek çok yabancı konuk da törene katıldı."
          ],
          "correct": 2,
          "solution": "'Herşey' sözcüğü 'Her şey' şeklinde ayrı yazılmalıdır. Şey sözcüğü daima ayrı yazılır."
        },
        {
          "id": "e7_q25",
          "subject": "Türkçe",
          "number": 25,
          "text": "25. Aşağıdaki cümlelerin hangisinde bir <u>yazım yanlışı</u> yapılmıştır?",
          "options": [
            "A) Türk Dil Kurumu yeni kılavuzunu yayımladı.",
            "B) 7. yüzyılda pek çok önemli gelişme yaşandı.",
            "C) Bu konuda <u>herşey</u> planlandığı gibi gidiyor.",
            "D) TBMM'nin aldığı tarihi karar Resmi Gazete'de duyuruldu.",
            "E) Yanı sıra pek çok yabancı konuk da törene katıldı."
          ],
          "correct": 2,
          "solution": "'Herşey' sözcüğü 'Her şey' şeklinde ayrı yazılmalıdır. Şey sözcüğü daima ayrı yazılır."
        },
        {
          "id": "e7_q26",
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
          "id": "e7_q27",
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
          "id": "e7_q28",
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
          "id": "e7_q29",
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
          "id": "e7_q30",
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
          "id": "e7_q31",
          "subject": "Matematik",
          "number": 31,
          "text": "31. a ve b birer pozitif tam sayı olmak üzere,\n<code>3a + 5b = 137</code>\neşitliğini sağlayan en küçük b değeri için a kaçtır?",
          "options": [
            "A) 7",
            "B) 9",
            "C) 11",
            "D) 13",
            "E) 15"
          ],
          "correct": 1,
          "solution": "Denklemde b yerine en küçük pozitif tam sayı değerleri verilerek a = 9 olarak bulunur."
        },
        {
          "id": "e7_q32",
          "subject": "Matematik",
          "number": 32,
          "text": "32. a ve b birer pozitif tam sayı olmak üzere,\n<code>3a + 5b = 137</code>\neşitliğini sağlayan en küçük b değeri için a kaçtır?",
          "options": [
            "A) 7",
            "B) 9",
            "C) 11",
            "D) 13",
            "E) 15"
          ],
          "correct": 1,
          "solution": "Denklemde b yerine en küçük pozitif tam sayı değerleri verilerek a = 9 olarak bulunur."
        },
        {
          "id": "e7_q33",
          "subject": "Matematik",
          "number": 33,
          "text": "33. a ve b birer pozitif tam sayı olmak üzere,\n<code>3a + 5b = 137</code>\neşitliğini sağlayan en küçük b değeri için a kaçtır?",
          "options": [
            "A) 7",
            "B) 9",
            "C) 11",
            "D) 13",
            "E) 15"
          ],
          "correct": 1,
          "solution": "Denklemde b yerine en küçük pozitif tam sayı değerleri verilerek a = 9 olarak bulunur."
        },
        {
          "id": "e7_q34",
          "subject": "Matematik",
          "number": 34,
          "text": "34. a ve b birer pozitif tam sayı olmak üzere,\n<code>3a + 5b = 137</code>\neşitliğini sağlayan en küçük b değeri için a kaçtır?",
          "options": [
            "A) 7",
            "B) 9",
            "C) 11",
            "D) 13",
            "E) 15"
          ],
          "correct": 1,
          "solution": "Denklemde b yerine en küçük pozitif tam sayı değerleri verilerek a = 9 olarak bulunur."
        },
        {
          "id": "e7_q35",
          "subject": "Matematik",
          "number": 35,
          "text": "35. a ve b birer pozitif tam sayı olmak üzere,\n<code>3a + 5b = 137</code>\neşitliğini sağlayan en küçük b değeri için a kaçtır?",
          "options": [
            "A) 7",
            "B) 9",
            "C) 11",
            "D) 13",
            "E) 15"
          ],
          "correct": 1,
          "solution": "Denklemde b yerine en küçük pozitif tam sayı değerleri verilerek a = 9 olarak bulunur."
        },
        {
          "id": "e7_q36",
          "subject": "Matematik",
          "number": 36,
          "text": "36. <code>(1/2 + 1/3) : (5/6) + 2^8 = x</code>\nişleminin sonucu kaçtır?",
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
          "id": "e7_q37",
          "subject": "Matematik",
          "number": 37,
          "text": "37. <code>(1/2 + 1/3) : (5/6) + 2^9 = x</code>\nişleminin sonucu kaçtır?",
          "options": [
            "A) 513",
            "B) 514",
            "C) 512",
            "D) 257",
            "E) 515"
          ],
          "correct": 0,
          "solution": "(1/2 + 1/3) = 5/6. (5/6) : (5/6) = 1. Sonuç = 1 + 2^9 = 513."
        },
        {
          "id": "e7_q38",
          "subject": "Matematik",
          "number": 38,
          "text": "38. <code>(1/2 + 1/3) : (5/6) + 2^10 = x</code>\nişleminin sonucu kaçtır?",
          "options": [
            "A) 1025",
            "B) 1026",
            "C) 1024",
            "D) 513",
            "E) 1027"
          ],
          "correct": 0,
          "solution": "(1/2 + 1/3) = 5/6. (5/6) : (5/6) = 1. Sonuç = 1 + 2^10 = 1025."
        },
        {
          "id": "e7_q39",
          "subject": "Matematik",
          "number": 39,
          "text": "39. <code>(1/2 + 1/3) : (5/6) + 2^11 = x</code>\nişleminin sonucu kaçtır?",
          "options": [
            "A) 2049",
            "B) 2050",
            "C) 2048",
            "D) 1025",
            "E) 2051"
          ],
          "correct": 0,
          "solution": "(1/2 + 1/3) = 5/6. (5/6) : (5/6) = 1. Sonuç = 1 + 2^11 = 2049."
        },
        {
          "id": "e7_q40",
          "subject": "Matematik",
          "number": 40,
          "text": "40. <code>(1/2 + 1/3) : (5/6) + 2^12 = x</code>\nişleminin sonucu kaçtır?",
          "options": [
            "A) 4097",
            "B) 4098",
            "C) 4096",
            "D) 2049",
            "E) 4099"
          ],
          "correct": 0,
          "solution": "(1/2 + 1/3) = 5/6. (5/6) : (5/6) = 1. Sonuç = 1 + 2^12 = 4097."
        },
        {
          "id": "e7_q41",
          "subject": "Matematik",
          "number": 41,
          "text": "41. <code>(1/2 + 1/3) : (5/6) + 2^13 = x</code>\nişleminin sonucu kaçtır?",
          "options": [
            "A) 8193",
            "B) 8194",
            "C) 8192",
            "D) 4097",
            "E) 8195"
          ],
          "correct": 0,
          "solution": "(1/2 + 1/3) = 5/6. (5/6) : (5/6) = 1. Sonuç = 1 + 2^13 = 8193."
        },
        {
          "id": "e7_q42",
          "subject": "Matematik",
          "number": 42,
          "text": "42. <code>(1/2 + 1/3) : (5/6) + 2^14 = x</code>\nişleminin sonucu kaçtır?",
          "options": [
            "A) 16385",
            "B) 16386",
            "C) 16384",
            "D) 8193",
            "E) 16387"
          ],
          "correct": 0,
          "solution": "(1/2 + 1/3) = 5/6. (5/6) : (5/6) = 1. Sonuç = 1 + 2^14 = 16385."
        },
        {
          "id": "e7_q43",
          "subject": "Matematik",
          "number": 43,
          "text": "43. Bir babanın bugünkü yaşı 50, oğlunun bugünkü yaşı ise 13'dır.\nBuna göre kaç yıl sonra babanın yaşı oğlunun yaşının 3 katı olur?",
          "options": [
            "A) 3",
            "B) 4",
            "C) 5",
            "D) 6",
            "E) 7"
          ],
          "correct": 2,
          "solution": "50 + t = 3(13 + t) => 50 + t = 39 + 3t => 2t = 11 => t = 5 yıl sonra."
        },
        {
          "id": "e7_q44",
          "subject": "Matematik",
          "number": 44,
          "text": "44. Bir babanın bugünkü yaşı 50, oğlunun bugünkü yaşı ise 13'dır.\nBuna göre kaç yıl sonra babanın yaşı oğlunun yaşının 3 katı olur?",
          "options": [
            "A) 3",
            "B) 4",
            "C) 5",
            "D) 6",
            "E) 7"
          ],
          "correct": 2,
          "solution": "50 + t = 3(13 + t) => 50 + t = 39 + 3t => 2t = 11 => t = 5 yıl sonra."
        },
        {
          "id": "e7_q45",
          "subject": "Matematik",
          "number": 45,
          "text": "45. Bir babanın bugünkü yaşı 50, oğlunun bugünkü yaşı ise 13'dır.\nBuna göre kaç yıl sonra babanın yaşı oğlunun yaşının 3 katı olur?",
          "options": [
            "A) 3",
            "B) 4",
            "C) 5",
            "D) 6",
            "E) 7"
          ],
          "correct": 2,
          "solution": "50 + t = 3(13 + t) => 50 + t = 39 + 3t => 2t = 11 => t = 5 yıl sonra."
        },
        {
          "id": "e7_q46",
          "subject": "Matematik",
          "number": 46,
          "text": "46. Bir babanın bugünkü yaşı 50, oğlunun bugünkü yaşı ise 13'dır.\nBuna göre kaç yıl sonra babanın yaşı oğlunun yaşının 3 katı olur?",
          "options": [
            "A) 3",
            "B) 4",
            "C) 5",
            "D) 6",
            "E) 7"
          ],
          "correct": 2,
          "solution": "50 + t = 3(13 + t) => 50 + t = 39 + 3t => 2t = 11 => t = 5 yıl sonra."
        },
        {
          "id": "e7_q47",
          "subject": "Matematik",
          "number": 47,
          "text": "47. Bir babanın bugünkü yaşı 50, oğlunun bugünkü yaşı ise 13'dır.\nBuna göre kaç yıl sonra babanın yaşı oğlunun yaşının 3 katı olur?",
          "options": [
            "A) 3",
            "B) 4",
            "C) 5",
            "D) 6",
            "E) 7"
          ],
          "correct": 2,
          "solution": "50 + t = 3(13 + t) => 50 + t = 39 + 3t => 2t = 11 => t = 5 yıl sonra."
        },
        {
          "id": "e7_q48",
          "subject": "Matematik",
          "number": 48,
          "text": "48. Bir babanın bugünkü yaşı 50, oğlunun bugünkü yaşı ise 13'dır.\nBuna göre kaç yıl sonra babanın yaşı oğlunun yaşının 3 katı olur?",
          "options": [
            "A) 3",
            "B) 4",
            "C) 5",
            "D) 6",
            "E) 7"
          ],
          "correct": 2,
          "solution": "50 + t = 3(13 + t) => 50 + t = 39 + 3t => 2t = 11 => t = 5 yıl sonra."
        },
        {
          "id": "e7_q49",
          "subject": "Matematik",
          "number": 49,
          "text": "49. Bir babanın bugünkü yaşı 50, oğlunun bugünkü yaşı ise 13'dır.\nBuna göre kaç yıl sonra babanın yaşı oğlunun yaşının 3 katı olur?",
          "options": [
            "A) 3",
            "B) 4",
            "C) 5",
            "D) 6",
            "E) 7"
          ],
          "correct": 2,
          "solution": "50 + t = 3(13 + t) => 50 + t = 39 + 3t => 2t = 11 => t = 5 yıl sonra."
        },
        {
          "id": "e7_q50",
          "subject": "Matematik",
          "number": 50,
          "text": "50. Bir babanın bugünkü yaşı 50, oğlunun bugünkü yaşı ise 13'dır.\nBuna göre kaç yıl sonra babanın yaşı oğlunun yaşının 3 katı olur?",
          "options": [
            "A) 3",
            "B) 4",
            "C) 5",
            "D) 6",
            "E) 7"
          ],
          "correct": 2,
          "solution": "50 + t = 3(13 + t) => 50 + t = 39 + 3t => 2t = 11 => t = 5 yıl sonra."
        },
        {
          "id": "e7_q51",
          "subject": "Matematik",
          "number": 51,
          "text": "51. Bir babanın bugünkü yaşı 50, oğlunun bugünkü yaşı ise 13'dır.\nBuna göre kaç yıl sonra babanın yaşı oğlunun yaşının 3 katı olur?",
          "options": [
            "A) 3",
            "B) 4",
            "C) 5",
            "D) 6",
            "E) 7"
          ],
          "correct": 2,
          "solution": "50 + t = 3(13 + t) => 50 + t = 39 + 3t => 2t = 11 => t = 5 yıl sonra."
        },
        {
          "id": "e7_q52",
          "subject": "Matematik",
          "number": 52,
          "text": "52. Bir babanın bugünkü yaşı 50, oğlunun bugünkü yaşı ise 13'dır.\nBuna göre kaç yıl sonra babanın yaşı oğlunun yaşının 3 katı olur?",
          "options": [
            "A) 3",
            "B) 4",
            "C) 5",
            "D) 6",
            "E) 7"
          ],
          "correct": 2,
          "solution": "50 + t = 3(13 + t) => 50 + t = 39 + 3t => 2t = 11 => t = 5 yıl sonra."
        },
        {
          "id": "e7_q53",
          "subject": "Matematik",
          "number": 53,
          "text": "53. Bir babanın bugünkü yaşı 50, oğlunun bugünkü yaşı ise 13'dır.\nBuna göre kaç yıl sonra babanın yaşı oğlunun yaşının 3 katı olur?",
          "options": [
            "A) 3",
            "B) 4",
            "C) 5",
            "D) 6",
            "E) 7"
          ],
          "correct": 2,
          "solution": "50 + t = 3(13 + t) => 50 + t = 39 + 3t => 2t = 11 => t = 5 yıl sonra."
        },
        {
          "id": "e7_q54",
          "subject": "Matematik",
          "number": 54,
          "text": "54. Bir babanın bugünkü yaşı 50, oğlunun bugünkü yaşı ise 13'dır.\nBuna göre kaç yıl sonra babanın yaşı oğlunun yaşının 3 katı olur?",
          "options": [
            "A) 3",
            "B) 4",
            "C) 5",
            "D) 6",
            "E) 7"
          ],
          "correct": 2,
          "solution": "50 + t = 3(13 + t) => 50 + t = 39 + 3t => 2t = 11 => t = 5 yıl sonra."
        },
        {
          "id": "e7_q55",
          "subject": "Matematik",
          "number": 55,
          "text": "55. A ve B iki küme olmak üzere,\n<code>s(A) = 19</code>, <code>s(B) = 17</code> ve <code>s(A ∩ B) = 7</code>\nolduğuna göre <code>s(A ∪ B)</code> kaçtır?",
          "options": [
            "A) 27",
            "B) 29",
            "C) 31",
            "D) 33",
            "E) 35"
          ],
          "correct": 1,
          "solution": "s(A ∪ B) = s(A) + s(B) - s(A ∩ B) = 19 + 17 - 7 = 29."
        },
        {
          "id": "e7_q56",
          "subject": "Matematik",
          "number": 56,
          "text": "56. A ve B iki küme olmak üzere,\n<code>s(A) = 19</code>, <code>s(B) = 17</code> ve <code>s(A ∩ B) = 7</code>\nolduğuna göre <code>s(A ∪ B)</code> kaçtır?",
          "options": [
            "A) 27",
            "B) 29",
            "C) 31",
            "D) 33",
            "E) 35"
          ],
          "correct": 1,
          "solution": "s(A ∪ B) = s(A) + s(B) - s(A ∩ B) = 19 + 17 - 7 = 29."
        },
        {
          "id": "e7_q57",
          "subject": "Matematik",
          "number": 57,
          "text": "57. A ve B iki küme olmak üzere,\n<code>s(A) = 19</code>, <code>s(B) = 17</code> ve <code>s(A ∩ B) = 7</code>\nolduğuna göre <code>s(A ∪ B)</code> kaçtır?",
          "options": [
            "A) 27",
            "B) 29",
            "C) 31",
            "D) 33",
            "E) 35"
          ],
          "correct": 1,
          "solution": "s(A ∪ B) = s(A) + s(B) - s(A ∩ B) = 19 + 17 - 7 = 29."
        },
        {
          "id": "e7_q58",
          "subject": "Matematik",
          "number": 58,
          "text": "58. A ve B iki küme olmak üzere,\n<code>s(A) = 19</code>, <code>s(B) = 17</code> ve <code>s(A ∩ B) = 7</code>\nolduğuna göre <code>s(A ∪ B)</code> kaçtır?",
          "options": [
            "A) 27",
            "B) 29",
            "C) 31",
            "D) 33",
            "E) 35"
          ],
          "correct": 1,
          "solution": "s(A ∪ B) = s(A) + s(B) - s(A ∩ B) = 19 + 17 - 7 = 29."
        },
        {
          "id": "e7_q59",
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
          "id": "e7_q60",
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
          "id": "e7_q61",
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
          "id": "e7_q62",
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
          "id": "e7_q63",
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
          "id": "e7_q64",
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
          "id": "e7_q65",
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
          "id": "e7_q66",
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
          "id": "e7_q67",
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
          "id": "e7_q68",
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
          "id": "e7_q69",
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
          "id": "e7_q70",
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
          "id": "e7_q71",
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
          "id": "e7_q72",
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
          "id": "e7_q73",
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
          "id": "e7_q74",
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
          "id": "e7_q75",
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
          "id": "e7_q76",
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
          "id": "e7_q77",
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
          "id": "e7_q78",
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
          "id": "e7_q79",
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
          "id": "e7_q80",
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
          "id": "e7_q81",
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
          "id": "e7_q82",
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
          "id": "e7_q83",
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
          "id": "e7_q84",
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
          "id": "e7_q85",
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
          "id": "e7_q86",
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
          "id": "e7_q87",
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
          "id": "e7_q88",
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
          "id": "e7_q89",
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
          "id": "e7_q90",
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
          "id": "e7_q91",
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
          "id": "e7_q92",
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
          "id": "e7_q93",
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
          "id": "e7_q94",
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
          "id": "e7_q95",
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
          "id": "e7_q96",
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
          "id": "e7_q97",
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
          "id": "e7_q98",
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
          "id": "e7_q99",
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
          "id": "e7_q100",
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
          "id": "e7_q101",
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
          "id": "e7_q102",
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
          "id": "e7_q103",
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
          "id": "e7_q104",
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
          "id": "e7_q105",
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
          "id": "e7_q106",
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
          "id": "e7_q107",
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
          "id": "e7_q108",
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
          "id": "e7_q109",
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
          "id": "e7_q110",
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
          "id": "e7_q111",
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
          "id": "e7_q112",
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
          "id": "e7_q113",
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
          "id": "e7_q114",
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
          "id": "e7_q115",
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
          "id": "e7_q116",
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
          "id": "e7_q117",
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
          "id": "e7_q118",
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
          "id": "e7_q119",
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
          "id": "e7_q120",
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
    {
      "id": "deneme_8",
      "title": "KPSS 2026 Ortaöğretim - 8. Deneme Sınavı (120 Soru)",
      "totalDurationMinutes": 130,
      "questions": [
        {
          "id": "e8_q1",
          "subject": "Türkçe",
          "number": 1,
          "text": "1. Aşağıdaki cümlelerin hangisinde <u>'derin'</u> sözcüğü 'ayrıntılı, kapsamlı ve esaslı' anlamında kullanılmıştır?",
          "options": [
            "A) Pencerenin kenarındaki nesne yere düştü.",
            "B) Yolun karşısındaki durağa doğru hızlıca koştu.",
            "C) Günün ilk saatlerinde dışarıda serin bir hava vardı.",
            "D) Konu üzerinde <u>derin</u> bir araştırma yapmadan karar vermeyiniz.",
            "E) Kitaplarını çantasına özenle yerleştirdi."
          ],
          "correct": 3,
          "solution": "Seçenekteki 'derin' kelimesi mecazi olarak 'ayrıntılı, kapsamlı ve esaslı' anlamında kullanılmıştır."
        },
        {
          "id": "e8_q2",
          "subject": "Türkçe",
          "number": 2,
          "text": "2. Aşağıdaki cümlelerin hangisinde <u>'göz yummak'</u> deyimi 'görmezden gelmek, hoşgörmek' anlamında kullanılmıştır?",
          "options": [
            "A) Sabah erkenden kalkıp iş yerine gitti.",
            "B) Kütüphanedeki sessizliği kimse bozmak istemiyordu.",
            "C) Tren vaktinde istasyona yanaşarak yolcularını aldı.",
            "D) Yapılan kural ihlallerine yönetim asla <u>göz yummadı</u>.",
            "E) Raporun son halini inceleyip imzaladı."
          ],
          "correct": 3,
          "solution": "Deyim cümlede 'görmezden gelmek, hoşgörmek' anlamını karşılayacak şekilde yer almıştır."
        },
        {
          "id": "e8_q3",
          "subject": "Türkçe",
          "number": 3,
          "text": "3. (I) Şairin 83 yılında yayımlanan bu eseri yoğun bir ilgi gördü. (II) Kitapta yer alan imgeler okurun hayal dünyasını zenginleştiriyor. (III) Eser toplam 120 sayfadan ve 45 şiirden oluşmaktadır. (IV) Bence dönemin en başarılı şiir kitabı budur. (V) Kitabın ikinci baskısı geçen ay yapıldı.\n\nBu parçadaki numaralanmış cümlelerden hangisi <u>öznel</u> bir yargı içermektedir?",
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
          "id": "e8_q4",
          "subject": "Türkçe",
          "number": 4,
          "text": "4. (I) Şairin 84 yılında yayımlanan bu eseri yoğun bir ilgi gördü. (II) Kitapta yer alan imgeler okurun hayal dünyasını zenginleştiriyor. (III) Eser toplam 120 sayfadan ve 45 şiirden oluşmaktadır. (IV) Bence dönemin en başarılı şiir kitabı budur. (V) Kitabın ikinci baskısı geçen ay yapıldı.\n\nBu parçadaki numaralanmış cümlelerden hangisi <u>öznel</u> bir yargı içermektedir?",
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
          "id": "e8_q5",
          "subject": "Türkçe",
          "number": 5,
          "text": "5. (I) Şairin 85 yılında yayımlanan bu eseri yoğun bir ilgi gördü. (II) Kitapta yer alan imgeler okurun hayal dünyasını zenginleştiriyor. (III) Eser toplam 120 sayfadan ve 45 şiirden oluşmaktadır. (IV) Bence dönemin en başarılı şiir kitabı budur. (V) Kitabın ikinci baskısı geçen ay yapıldı.\n\nBu parçadaki numaralanmış cümlelerden hangisi <u>öznel</u> bir yargı içermektedir?",
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
          "id": "e8_q6",
          "subject": "Türkçe",
          "number": 6,
          "text": "6. (I) Şairin 86 yılında yayımlanan bu eseri yoğun bir ilgi gördü. (II) Kitapta yer alan imgeler okurun hayal dünyasını zenginleştiriyor. (III) Eser toplam 120 sayfadan ve 45 şiirden oluşmaktadır. (IV) Bence dönemin en başarılı şiir kitabı budur. (V) Kitabın ikinci baskısı geçen ay yapıldı.\n\nBu parçadaki numaralanmış cümlelerden hangisi <u>öznel</u> bir yargı içermektedir?",
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
          "id": "e8_q7",
          "subject": "Türkçe",
          "number": 7,
          "text": "7. (I) Şairin 87 yılında yayımlanan bu eseri yoğun bir ilgi gördü. (II) Kitapta yer alan imgeler okurun hayal dünyasını zenginleştiriyor. (III) Eser toplam 120 sayfadan ve 45 şiirden oluşmaktadır. (IV) Bence dönemin en başarılı şiir kitabı budur. (V) Kitabın ikinci baskısı geçen ay yapıldı.\n\nBu parçadaki numaralanmış cümlelerden hangisi <u>öznel</u> bir yargı içermektedir?",
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
          "id": "e8_q8",
          "subject": "Türkçe",
          "number": 8,
          "text": "8. (I) Şairin 88 yılında yayımlanan bu eseri yoğun bir ilgi gördü. (II) Kitapta yer alan imgeler okurun hayal dünyasını zenginleştiriyor. (III) Eser toplam 120 sayfadan ve 45 şiirden oluşmaktadır. (IV) Bence dönemin en başarılı şiir kitabı budur. (V) Kitabın ikinci baskısı geçen ay yapıldı.\n\nBu parçadaki numaralanmış cümlelerden hangisi <u>öznel</u> bir yargı içermektedir?",
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
          "id": "e8_q9",
          "subject": "Türkçe",
          "number": 9,
          "text": "9. (I) Şairin 89 yılında yayımlanan bu eseri yoğun bir ilgi gördü. (II) Kitapta yer alan imgeler okurun hayal dünyasını zenginleştiriyor. (III) Eser toplam 120 sayfadan ve 45 şiirden oluşmaktadır. (IV) Bence dönemin en başarılı şiir kitabı budur. (V) Kitabın ikinci baskısı geçen ay yapıldı.\n\nBu parçadaki numaralanmış cümlelerden hangisi <u>öznel</u> bir yargı içermektedir?",
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
          "id": "e8_q10",
          "subject": "Türkçe",
          "number": 10,
          "text": "10. (I) Şairin 90 yılında yayımlanan bu eseri yoğun bir ilgi gördü. (II) Kitapta yer alan imgeler okurun hayal dünyasını zenginleştiriyor. (III) Eser toplam 120 sayfadan ve 45 şiirden oluşmaktadır. (IV) Bence dönemin en başarılı şiir kitabı budur. (V) Kitabın ikinci baskısı geçen ay yapıldı.\n\nBu parçadaki numaralanmış cümlelerden hangisi <u>öznel</u> bir yargı içermektedir?",
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
          "id": "e8_q11",
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
          "id": "e8_q12",
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
          "id": "e8_q13",
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
          "id": "e8_q14",
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
          "id": "e8_q15",
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
          "id": "e8_q16",
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
          "id": "e8_q17",
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
          "id": "e8_q18",
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
          "id": "e8_q19",
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
          "id": "e8_q20",
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
          "id": "e8_q21",
          "subject": "Türkçe",
          "number": 21,
          "text": "21. Aşağıdaki cümlelerin hangisinde bir <u>yazım yanlışı</u> yapılmıştır?",
          "options": [
            "A) Türk Dil Kurumu yeni kılavuzunu yayımladı.",
            "B) 8. yüzyılda pek çok önemli gelişme yaşandı.",
            "C) Bu konuda <u>herşey</u> planlandığı gibi gidiyor.",
            "D) TBMM'nin aldığı tarihi karar Resmi Gazete'de duyuruldu.",
            "E) Yanı sıra pek çok yabancı konuk da törene katıldı."
          ],
          "correct": 2,
          "solution": "'Herşey' sözcüğü 'Her şey' şeklinde ayrı yazılmalıdır. Şey sözcüğü daima ayrı yazılır."
        },
        {
          "id": "e8_q22",
          "subject": "Türkçe",
          "number": 22,
          "text": "22. Aşağıdaki cümlelerin hangisinde bir <u>yazım yanlışı</u> yapılmıştır?",
          "options": [
            "A) Türk Dil Kurumu yeni kılavuzunu yayımladı.",
            "B) 8. yüzyılda pek çok önemli gelişme yaşandı.",
            "C) Bu konuda <u>herşey</u> planlandığı gibi gidiyor.",
            "D) TBMM'nin aldığı tarihi karar Resmi Gazete'de duyuruldu.",
            "E) Yanı sıra pek çok yabancı konuk da törene katıldı."
          ],
          "correct": 2,
          "solution": "'Herşey' sözcüğü 'Her şey' şeklinde ayrı yazılmalıdır. Şey sözcüğü daima ayrı yazılır."
        },
        {
          "id": "e8_q23",
          "subject": "Türkçe",
          "number": 23,
          "text": "23. Aşağıdaki cümlelerin hangisinde bir <u>yazım yanlışı</u> yapılmıştır?",
          "options": [
            "A) Türk Dil Kurumu yeni kılavuzunu yayımladı.",
            "B) 8. yüzyılda pek çok önemli gelişme yaşandı.",
            "C) Bu konuda <u>herşey</u> planlandığı gibi gidiyor.",
            "D) TBMM'nin aldığı tarihi karar Resmi Gazete'de duyuruldu.",
            "E) Yanı sıra pek çok yabancı konuk da törene katıldı."
          ],
          "correct": 2,
          "solution": "'Herşey' sözcüğü 'Her şey' şeklinde ayrı yazılmalıdır. Şey sözcüğü daima ayrı yazılır."
        },
        {
          "id": "e8_q24",
          "subject": "Türkçe",
          "number": 24,
          "text": "24. Aşağıdaki cümlelerin hangisinde bir <u>yazım yanlışı</u> yapılmıştır?",
          "options": [
            "A) Türk Dil Kurumu yeni kılavuzunu yayımladı.",
            "B) 8. yüzyılda pek çok önemli gelişme yaşandı.",
            "C) Bu konuda <u>herşey</u> planlandığı gibi gidiyor.",
            "D) TBMM'nin aldığı tarihi karar Resmi Gazete'de duyuruldu.",
            "E) Yanı sıra pek çok yabancı konuk da törene katıldı."
          ],
          "correct": 2,
          "solution": "'Herşey' sözcüğü 'Her şey' şeklinde ayrı yazılmalıdır. Şey sözcüğü daima ayrı yazılır."
        },
        {
          "id": "e8_q25",
          "subject": "Türkçe",
          "number": 25,
          "text": "25. Aşağıdaki cümlelerin hangisinde bir <u>yazım yanlışı</u> yapılmıştır?",
          "options": [
            "A) Türk Dil Kurumu yeni kılavuzunu yayımladı.",
            "B) 8. yüzyılda pek çok önemli gelişme yaşandı.",
            "C) Bu konuda <u>herşey</u> planlandığı gibi gidiyor.",
            "D) TBMM'nin aldığı tarihi karar Resmi Gazete'de duyuruldu.",
            "E) Yanı sıra pek çok yabancı konuk da törene katıldı."
          ],
          "correct": 2,
          "solution": "'Herşey' sözcüğü 'Her şey' şeklinde ayrı yazılmalıdır. Şey sözcüğü daima ayrı yazılır."
        },
        {
          "id": "e8_q26",
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
          "id": "e8_q27",
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
          "id": "e8_q28",
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
          "id": "e8_q29",
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
          "id": "e8_q30",
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
          "id": "e8_q31",
          "subject": "Matematik",
          "number": 31,
          "text": "31. a ve b birer pozitif tam sayı olmak üzere,\n<code>3a + 5b = 155</code>\neşitliğini sağlayan en küçük b değeri için a kaçtır?",
          "options": [
            "A) 8",
            "B) 10",
            "C) 12",
            "D) 14",
            "E) 16"
          ],
          "correct": 1,
          "solution": "Denklemde b yerine en küçük pozitif tam sayı değerleri verilerek a = 10 olarak bulunur."
        },
        {
          "id": "e8_q32",
          "subject": "Matematik",
          "number": 32,
          "text": "32. a ve b birer pozitif tam sayı olmak üzere,\n<code>3a + 5b = 155</code>\neşitliğini sağlayan en küçük b değeri için a kaçtır?",
          "options": [
            "A) 8",
            "B) 10",
            "C) 12",
            "D) 14",
            "E) 16"
          ],
          "correct": 1,
          "solution": "Denklemde b yerine en küçük pozitif tam sayı değerleri verilerek a = 10 olarak bulunur."
        },
        {
          "id": "e8_q33",
          "subject": "Matematik",
          "number": 33,
          "text": "33. a ve b birer pozitif tam sayı olmak üzere,\n<code>3a + 5b = 155</code>\neşitliğini sağlayan en küçük b değeri için a kaçtır?",
          "options": [
            "A) 8",
            "B) 10",
            "C) 12",
            "D) 14",
            "E) 16"
          ],
          "correct": 1,
          "solution": "Denklemde b yerine en küçük pozitif tam sayı değerleri verilerek a = 10 olarak bulunur."
        },
        {
          "id": "e8_q34",
          "subject": "Matematik",
          "number": 34,
          "text": "34. a ve b birer pozitif tam sayı olmak üzere,\n<code>3a + 5b = 155</code>\neşitliğini sağlayan en küçük b değeri için a kaçtır?",
          "options": [
            "A) 8",
            "B) 10",
            "C) 12",
            "D) 14",
            "E) 16"
          ],
          "correct": 1,
          "solution": "Denklemde b yerine en küçük pozitif tam sayı değerleri verilerek a = 10 olarak bulunur."
        },
        {
          "id": "e8_q35",
          "subject": "Matematik",
          "number": 35,
          "text": "35. a ve b birer pozitif tam sayı olmak üzere,\n<code>3a + 5b = 155</code>\neşitliğini sağlayan en küçük b değeri için a kaçtır?",
          "options": [
            "A) 8",
            "B) 10",
            "C) 12",
            "D) 14",
            "E) 16"
          ],
          "correct": 1,
          "solution": "Denklemde b yerine en küçük pozitif tam sayı değerleri verilerek a = 10 olarak bulunur."
        },
        {
          "id": "e8_q36",
          "subject": "Matematik",
          "number": 36,
          "text": "36. <code>(1/2 + 1/3) : (5/6) + 2^9 = x</code>\nişleminin sonucu kaçtır?",
          "options": [
            "A) 513",
            "B) 514",
            "C) 512",
            "D) 257",
            "E) 515"
          ],
          "correct": 0,
          "solution": "(1/2 + 1/3) = 5/6. (5/6) : (5/6) = 1. Sonuç = 1 + 2^9 = 513."
        },
        {
          "id": "e8_q37",
          "subject": "Matematik",
          "number": 37,
          "text": "37. <code>(1/2 + 1/3) : (5/6) + 2^10 = x</code>\nişleminin sonucu kaçtır?",
          "options": [
            "A) 1025",
            "B) 1026",
            "C) 1024",
            "D) 513",
            "E) 1027"
          ],
          "correct": 0,
          "solution": "(1/2 + 1/3) = 5/6. (5/6) : (5/6) = 1. Sonuç = 1 + 2^10 = 1025."
        },
        {
          "id": "e8_q38",
          "subject": "Matematik",
          "number": 38,
          "text": "38. <code>(1/2 + 1/3) : (5/6) + 2^11 = x</code>\nişleminin sonucu kaçtır?",
          "options": [
            "A) 2049",
            "B) 2050",
            "C) 2048",
            "D) 1025",
            "E) 2051"
          ],
          "correct": 0,
          "solution": "(1/2 + 1/3) = 5/6. (5/6) : (5/6) = 1. Sonuç = 1 + 2^11 = 2049."
        },
        {
          "id": "e8_q39",
          "subject": "Matematik",
          "number": 39,
          "text": "39. <code>(1/2 + 1/3) : (5/6) + 2^12 = x</code>\nişleminin sonucu kaçtır?",
          "options": [
            "A) 4097",
            "B) 4098",
            "C) 4096",
            "D) 2049",
            "E) 4099"
          ],
          "correct": 0,
          "solution": "(1/2 + 1/3) = 5/6. (5/6) : (5/6) = 1. Sonuç = 1 + 2^12 = 4097."
        },
        {
          "id": "e8_q40",
          "subject": "Matematik",
          "number": 40,
          "text": "40. <code>(1/2 + 1/3) : (5/6) + 2^13 = x</code>\nişleminin sonucu kaçtır?",
          "options": [
            "A) 8193",
            "B) 8194",
            "C) 8192",
            "D) 4097",
            "E) 8195"
          ],
          "correct": 0,
          "solution": "(1/2 + 1/3) = 5/6. (5/6) : (5/6) = 1. Sonuç = 1 + 2^13 = 8193."
        },
        {
          "id": "e8_q41",
          "subject": "Matematik",
          "number": 41,
          "text": "41. <code>(1/2 + 1/3) : (5/6) + 2^14 = x</code>\nişleminin sonucu kaçtır?",
          "options": [
            "A) 16385",
            "B) 16386",
            "C) 16384",
            "D) 8193",
            "E) 16387"
          ],
          "correct": 0,
          "solution": "(1/2 + 1/3) = 5/6. (5/6) : (5/6) = 1. Sonuç = 1 + 2^14 = 16385."
        },
        {
          "id": "e8_q42",
          "subject": "Matematik",
          "number": 42,
          "text": "42. <code>(1/2 + 1/3) : (5/6) + 2^15 = x</code>\nişleminin sonucu kaçtır?",
          "options": [
            "A) 32769",
            "B) 32770",
            "C) 32768",
            "D) 16385",
            "E) 32771"
          ],
          "correct": 0,
          "solution": "(1/2 + 1/3) = 5/6. (5/6) : (5/6) = 1. Sonuç = 1 + 2^15 = 32769."
        },
        {
          "id": "e8_q43",
          "subject": "Matematik",
          "number": 43,
          "text": "43. Bir babanın bugünkü yaşı 52, oğlunun bugünkü yaşı ise 14'dır.\nBuna göre kaç yıl sonra babanın yaşı oğlunun yaşının 3 katı olur?",
          "options": [
            "A) 3",
            "B) 4",
            "C) 5",
            "D) 6",
            "E) 7"
          ],
          "correct": 2,
          "solution": "52 + t = 3(14 + t) => 52 + t = 42 + 3t => 2t = 10 => t = 5 yıl sonra."
        },
        {
          "id": "e8_q44",
          "subject": "Matematik",
          "number": 44,
          "text": "44. Bir babanın bugünkü yaşı 52, oğlunun bugünkü yaşı ise 14'dır.\nBuna göre kaç yıl sonra babanın yaşı oğlunun yaşının 3 katı olur?",
          "options": [
            "A) 3",
            "B) 4",
            "C) 5",
            "D) 6",
            "E) 7"
          ],
          "correct": 2,
          "solution": "52 + t = 3(14 + t) => 52 + t = 42 + 3t => 2t = 10 => t = 5 yıl sonra."
        },
        {
          "id": "e8_q45",
          "subject": "Matematik",
          "number": 45,
          "text": "45. Bir babanın bugünkü yaşı 52, oğlunun bugünkü yaşı ise 14'dır.\nBuna göre kaç yıl sonra babanın yaşı oğlunun yaşının 3 katı olur?",
          "options": [
            "A) 3",
            "B) 4",
            "C) 5",
            "D) 6",
            "E) 7"
          ],
          "correct": 2,
          "solution": "52 + t = 3(14 + t) => 52 + t = 42 + 3t => 2t = 10 => t = 5 yıl sonra."
        },
        {
          "id": "e8_q46",
          "subject": "Matematik",
          "number": 46,
          "text": "46. Bir babanın bugünkü yaşı 52, oğlunun bugünkü yaşı ise 14'dır.\nBuna göre kaç yıl sonra babanın yaşı oğlunun yaşının 3 katı olur?",
          "options": [
            "A) 3",
            "B) 4",
            "C) 5",
            "D) 6",
            "E) 7"
          ],
          "correct": 2,
          "solution": "52 + t = 3(14 + t) => 52 + t = 42 + 3t => 2t = 10 => t = 5 yıl sonra."
        },
        {
          "id": "e8_q47",
          "subject": "Matematik",
          "number": 47,
          "text": "47. Bir babanın bugünkü yaşı 52, oğlunun bugünkü yaşı ise 14'dır.\nBuna göre kaç yıl sonra babanın yaşı oğlunun yaşının 3 katı olur?",
          "options": [
            "A) 3",
            "B) 4",
            "C) 5",
            "D) 6",
            "E) 7"
          ],
          "correct": 2,
          "solution": "52 + t = 3(14 + t) => 52 + t = 42 + 3t => 2t = 10 => t = 5 yıl sonra."
        },
        {
          "id": "e8_q48",
          "subject": "Matematik",
          "number": 48,
          "text": "48. Bir babanın bugünkü yaşı 52, oğlunun bugünkü yaşı ise 14'dır.\nBuna göre kaç yıl sonra babanın yaşı oğlunun yaşının 3 katı olur?",
          "options": [
            "A) 3",
            "B) 4",
            "C) 5",
            "D) 6",
            "E) 7"
          ],
          "correct": 2,
          "solution": "52 + t = 3(14 + t) => 52 + t = 42 + 3t => 2t = 10 => t = 5 yıl sonra."
        },
        {
          "id": "e8_q49",
          "subject": "Matematik",
          "number": 49,
          "text": "49. Bir babanın bugünkü yaşı 52, oğlunun bugünkü yaşı ise 14'dır.\nBuna göre kaç yıl sonra babanın yaşı oğlunun yaşının 3 katı olur?",
          "options": [
            "A) 3",
            "B) 4",
            "C) 5",
            "D) 6",
            "E) 7"
          ],
          "correct": 2,
          "solution": "52 + t = 3(14 + t) => 52 + t = 42 + 3t => 2t = 10 => t = 5 yıl sonra."
        },
        {
          "id": "e8_q50",
          "subject": "Matematik",
          "number": 50,
          "text": "50. Bir babanın bugünkü yaşı 52, oğlunun bugünkü yaşı ise 14'dır.\nBuna göre kaç yıl sonra babanın yaşı oğlunun yaşının 3 katı olur?",
          "options": [
            "A) 3",
            "B) 4",
            "C) 5",
            "D) 6",
            "E) 7"
          ],
          "correct": 2,
          "solution": "52 + t = 3(14 + t) => 52 + t = 42 + 3t => 2t = 10 => t = 5 yıl sonra."
        },
        {
          "id": "e8_q51",
          "subject": "Matematik",
          "number": 51,
          "text": "51. Bir babanın bugünkü yaşı 52, oğlunun bugünkü yaşı ise 14'dır.\nBuna göre kaç yıl sonra babanın yaşı oğlunun yaşının 3 katı olur?",
          "options": [
            "A) 3",
            "B) 4",
            "C) 5",
            "D) 6",
            "E) 7"
          ],
          "correct": 2,
          "solution": "52 + t = 3(14 + t) => 52 + t = 42 + 3t => 2t = 10 => t = 5 yıl sonra."
        },
        {
          "id": "e8_q52",
          "subject": "Matematik",
          "number": 52,
          "text": "52. Bir babanın bugünkü yaşı 52, oğlunun bugünkü yaşı ise 14'dır.\nBuna göre kaç yıl sonra babanın yaşı oğlunun yaşının 3 katı olur?",
          "options": [
            "A) 3",
            "B) 4",
            "C) 5",
            "D) 6",
            "E) 7"
          ],
          "correct": 2,
          "solution": "52 + t = 3(14 + t) => 52 + t = 42 + 3t => 2t = 10 => t = 5 yıl sonra."
        },
        {
          "id": "e8_q53",
          "subject": "Matematik",
          "number": 53,
          "text": "53. Bir babanın bugünkü yaşı 52, oğlunun bugünkü yaşı ise 14'dır.\nBuna göre kaç yıl sonra babanın yaşı oğlunun yaşının 3 katı olur?",
          "options": [
            "A) 3",
            "B) 4",
            "C) 5",
            "D) 6",
            "E) 7"
          ],
          "correct": 2,
          "solution": "52 + t = 3(14 + t) => 52 + t = 42 + 3t => 2t = 10 => t = 5 yıl sonra."
        },
        {
          "id": "e8_q54",
          "subject": "Matematik",
          "number": 54,
          "text": "54. Bir babanın bugünkü yaşı 52, oğlunun bugünkü yaşı ise 14'dır.\nBuna göre kaç yıl sonra babanın yaşı oğlunun yaşının 3 katı olur?",
          "options": [
            "A) 3",
            "B) 4",
            "C) 5",
            "D) 6",
            "E) 7"
          ],
          "correct": 2,
          "solution": "52 + t = 3(14 + t) => 52 + t = 42 + 3t => 2t = 10 => t = 5 yıl sonra."
        },
        {
          "id": "e8_q55",
          "subject": "Matematik",
          "number": 55,
          "text": "55. A ve B iki küme olmak üzere,\n<code>s(A) = 20</code>, <code>s(B) = 18</code> ve <code>s(A ∩ B) = 8</code>\nolduğuna göre <code>s(A ∪ B)</code> kaçtır?",
          "options": [
            "A) 28",
            "B) 30",
            "C) 32",
            "D) 34",
            "E) 36"
          ],
          "correct": 1,
          "solution": "s(A ∪ B) = s(A) + s(B) - s(A ∩ B) = 20 + 18 - 8 = 30."
        },
        {
          "id": "e8_q56",
          "subject": "Matematik",
          "number": 56,
          "text": "56. A ve B iki küme olmak üzere,\n<code>s(A) = 20</code>, <code>s(B) = 18</code> ve <code>s(A ∩ B) = 8</code>\nolduğuna göre <code>s(A ∪ B)</code> kaçtır?",
          "options": [
            "A) 28",
            "B) 30",
            "C) 32",
            "D) 34",
            "E) 36"
          ],
          "correct": 1,
          "solution": "s(A ∪ B) = s(A) + s(B) - s(A ∩ B) = 20 + 18 - 8 = 30."
        },
        {
          "id": "e8_q57",
          "subject": "Matematik",
          "number": 57,
          "text": "57. A ve B iki küme olmak üzere,\n<code>s(A) = 20</code>, <code>s(B) = 18</code> ve <code>s(A ∩ B) = 8</code>\nolduğuna göre <code>s(A ∪ B)</code> kaçtır?",
          "options": [
            "A) 28",
            "B) 30",
            "C) 32",
            "D) 34",
            "E) 36"
          ],
          "correct": 1,
          "solution": "s(A ∪ B) = s(A) + s(B) - s(A ∩ B) = 20 + 18 - 8 = 30."
        },
        {
          "id": "e8_q58",
          "subject": "Matematik",
          "number": 58,
          "text": "58. A ve B iki küme olmak üzere,\n<code>s(A) = 20</code>, <code>s(B) = 18</code> ve <code>s(A ∩ B) = 8</code>\nolduğuna göre <code>s(A ∪ B)</code> kaçtır?",
          "options": [
            "A) 28",
            "B) 30",
            "C) 32",
            "D) 34",
            "E) 36"
          ],
          "correct": 1,
          "solution": "s(A ∪ B) = s(A) + s(B) - s(A ∩ B) = 20 + 18 - 8 = 30."
        },
        {
          "id": "e8_q59",
          "subject": "Matematik",
          "number": 59,
          "text": "59. Dik kenar uzunlukları 9 cm ve 12 cm olan bir dik üçgenin hipotenüs uzunluğu kaç cm'dir?",
          "options": [
            "A) 14",
            "B) 15",
            "C) 16",
            "D) 17",
            "E) 18"
          ],
          "correct": 1,
          "solution": "Pisagor bağıntısı: a² + b² = c² => 9² + 12² = 225 = 15² => Hipotenüs = 15 cm (3-4-5 katı)."
        },
        {
          "id": "e8_q60",
          "subject": "Matematik",
          "number": 60,
          "text": "60. Dik kenar uzunlukları 9 cm ve 12 cm olan bir dik üçgenin hipotenüs uzunluğu kaç cm'dir?",
          "options": [
            "A) 14",
            "B) 15",
            "C) 16",
            "D) 17",
            "E) 18"
          ],
          "correct": 1,
          "solution": "Pisagor bağıntısı: a² + b² = c² => 9² + 12² = 225 = 15² => Hipotenüs = 15 cm (3-4-5 katı)."
        },
        {
          "id": "e8_q61",
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
          "id": "e8_q62",
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
          "id": "e8_q63",
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
          "id": "e8_q64",
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
          "id": "e8_q65",
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
          "id": "e8_q66",
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
          "id": "e8_q67",
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
          "id": "e8_q68",
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
          "id": "e8_q69",
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
          "id": "e8_q70",
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
          "id": "e8_q71",
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
          "id": "e8_q72",
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
          "id": "e8_q73",
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
          "id": "e8_q74",
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
          "id": "e8_q75",
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
          "id": "e8_q76",
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
          "id": "e8_q77",
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
          "id": "e8_q78",
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
          "id": "e8_q79",
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
          "id": "e8_q80",
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
          "id": "e8_q81",
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
          "id": "e8_q82",
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
          "id": "e8_q83",
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
          "id": "e8_q84",
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
          "id": "e8_q85",
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
          "id": "e8_q86",
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
          "id": "e8_q87",
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
          "id": "e8_q88",
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
          "id": "e8_q89",
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
          "id": "e8_q90",
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
          "id": "e8_q91",
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
          "id": "e8_q92",
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
          "id": "e8_q93",
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
          "id": "e8_q94",
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
          "id": "e8_q95",
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
          "id": "e8_q96",
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
          "id": "e8_q97",
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
          "id": "e8_q98",
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
          "id": "e8_q99",
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
          "id": "e8_q100",
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
          "id": "e8_q101",
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
          "id": "e8_q102",
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
          "id": "e8_q103",
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
          "id": "e8_q104",
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
          "id": "e8_q105",
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
          "id": "e8_q106",
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
          "id": "e8_q107",
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
          "id": "e8_q108",
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
          "id": "e8_q109",
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
          "id": "e8_q110",
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
          "id": "e8_q111",
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
          "id": "e8_q112",
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
          "id": "e8_q113",
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
          "id": "e8_q114",
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
          "id": "e8_q115",
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
          "id": "e8_q116",
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
          "id": "e8_q117",
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
          "id": "e8_q118",
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
          "id": "e8_q119",
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
          "id": "e8_q120",
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
    {
      "id": "deneme_9",
      "title": "KPSS 2026 Ortaöğretim - 9. Deneme Sınavı (120 Soru)",
      "totalDurationMinutes": 130,
      "questions": [
        {
          "id": "e9_q1",
          "subject": "Türkçe",
          "number": 1,
          "text": "1. Aşağıdaki cümlelerin hangisinde <u>'tatlı'</u> sözcüğü 'hoşa giden, sevimli ve cana yakın' anlamında kullanılmıştır?",
          "options": [
            "A) Pencerenin kenarındaki nesne yere düştü.",
            "B) Çocuğun <u>tatlı</u> bakışları salondaki herkesi mest etti.",
            "C) Günün ilk saatlerinde dışarıda serin bir hava vardı.",
            "D) Bahçedeki ağaçların gölgesinde dinlenmeyi seçti.",
            "E) Kitaplarını çantasına özenle yerleştirdi."
          ],
          "correct": 1,
          "solution": "Seçenekteki 'tatlı' kelimesi mecazi olarak 'hoşa giden, sevimli ve cana yakın' anlamında kullanılmıştır."
        },
        {
          "id": "e9_q2",
          "subject": "Türkçe",
          "number": 2,
          "text": "2. Aşağıdaki cümlelerin hangisinde <u>'pabuç bırakmamak'</u> deyimi 'tehditten korkmamak' anlamında kullanılmıştır?",
          "options": [
            "A) Sabah erkenden kalkıp iş yerine gitti.",
            "B) Hiçbir haksız baskıya ve tehdide <u>pabuç bırakmadı</u>.",
            "C) Tren vaktinde istasyona yanaşarak yolcularını aldı.",
            "D) Bahçede rengarenk çiçekler açmıştı.",
            "E) Raporun son halini inceleyip imzaladı."
          ],
          "correct": 1,
          "solution": "Deyim cümlede 'tehditten korkmamak' anlamını karşılayacak şekilde yer almıştır."
        },
        {
          "id": "e9_q3",
          "subject": "Türkçe",
          "number": 3,
          "text": "3. (I) Şairin 93 yılında yayımlanan bu eseri yoğun bir ilgi gördü. (II) Kitapta yer alan imgeler okurun hayal dünyasını zenginleştiriyor. (III) Eser toplam 120 sayfadan ve 45 şiirden oluşmaktadır. (IV) Bence dönemin en başarılı şiir kitabı budur. (V) Kitabın ikinci baskısı geçen ay yapıldı.\n\nBu parçadaki numaralanmış cümlelerden hangisi <u>öznel</u> bir yargı içermektedir?",
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
          "id": "e9_q4",
          "subject": "Türkçe",
          "number": 4,
          "text": "4. (I) Şairin 94 yılında yayımlanan bu eseri yoğun bir ilgi gördü. (II) Kitapta yer alan imgeler okurun hayal dünyasını zenginleştiriyor. (III) Eser toplam 120 sayfadan ve 45 şiirden oluşmaktadır. (IV) Bence dönemin en başarılı şiir kitabı budur. (V) Kitabın ikinci baskısı geçen ay yapıldı.\n\nBu parçadaki numaralanmış cümlelerden hangisi <u>öznel</u> bir yargı içermektedir?",
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
          "id": "e9_q5",
          "subject": "Türkçe",
          "number": 5,
          "text": "5. (I) Şairin 95 yılında yayımlanan bu eseri yoğun bir ilgi gördü. (II) Kitapta yer alan imgeler okurun hayal dünyasını zenginleştiriyor. (III) Eser toplam 120 sayfadan ve 45 şiirden oluşmaktadır. (IV) Bence dönemin en başarılı şiir kitabı budur. (V) Kitabın ikinci baskısı geçen ay yapıldı.\n\nBu parçadaki numaralanmış cümlelerden hangisi <u>öznel</u> bir yargı içermektedir?",
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
          "id": "e9_q6",
          "subject": "Türkçe",
          "number": 6,
          "text": "6. (I) Şairin 96 yılında yayımlanan bu eseri yoğun bir ilgi gördü. (II) Kitapta yer alan imgeler okurun hayal dünyasını zenginleştiriyor. (III) Eser toplam 120 sayfadan ve 45 şiirden oluşmaktadır. (IV) Bence dönemin en başarılı şiir kitabı budur. (V) Kitabın ikinci baskısı geçen ay yapıldı.\n\nBu parçadaki numaralanmış cümlelerden hangisi <u>öznel</u> bir yargı içermektedir?",
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
          "id": "e9_q7",
          "subject": "Türkçe",
          "number": 7,
          "text": "7. (I) Şairin 97 yılında yayımlanan bu eseri yoğun bir ilgi gördü. (II) Kitapta yer alan imgeler okurun hayal dünyasını zenginleştiriyor. (III) Eser toplam 120 sayfadan ve 45 şiirden oluşmaktadır. (IV) Bence dönemin en başarılı şiir kitabı budur. (V) Kitabın ikinci baskısı geçen ay yapıldı.\n\nBu parçadaki numaralanmış cümlelerden hangisi <u>öznel</u> bir yargı içermektedir?",
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
          "id": "e9_q8",
          "subject": "Türkçe",
          "number": 8,
          "text": "8. (I) Şairin 98 yılında yayımlanan bu eseri yoğun bir ilgi gördü. (II) Kitapta yer alan imgeler okurun hayal dünyasını zenginleştiriyor. (III) Eser toplam 120 sayfadan ve 45 şiirden oluşmaktadır. (IV) Bence dönemin en başarılı şiir kitabı budur. (V) Kitabın ikinci baskısı geçen ay yapıldı.\n\nBu parçadaki numaralanmış cümlelerden hangisi <u>öznel</u> bir yargı içermektedir?",
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
          "id": "e9_q9",
          "subject": "Türkçe",
          "number": 9,
          "text": "9. (I) Şairin 99 yılında yayımlanan bu eseri yoğun bir ilgi gördü. (II) Kitapta yer alan imgeler okurun hayal dünyasını zenginleştiriyor. (III) Eser toplam 120 sayfadan ve 45 şiirden oluşmaktadır. (IV) Bence dönemin en başarılı şiir kitabı budur. (V) Kitabın ikinci baskısı geçen ay yapıldı.\n\nBu parçadaki numaralanmış cümlelerden hangisi <u>öznel</u> bir yargı içermektedir?",
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
          "id": "e9_q10",
          "subject": "Türkçe",
          "number": 10,
          "text": "10. (I) Şairin 100 yılında yayımlanan bu eseri yoğun bir ilgi gördü. (II) Kitapta yer alan imgeler okurun hayal dünyasını zenginleştiriyor. (III) Eser toplam 120 sayfadan ve 45 şiirden oluşmaktadır. (IV) Bence dönemin en başarılı şiir kitabı budur. (V) Kitabın ikinci baskısı geçen ay yapıldı.\n\nBu parçadaki numaralanmış cümlelerden hangisi <u>öznel</u> bir yargı içermektedir?",
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
          "id": "e9_q11",
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
          "id": "e9_q12",
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
          "id": "e9_q13",
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
          "id": "e9_q14",
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
          "id": "e9_q15",
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
          "id": "e9_q16",
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
          "id": "e9_q17",
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
          "id": "e9_q18",
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
          "id": "e9_q19",
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
          "id": "e9_q20",
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
          "id": "e9_q21",
          "subject": "Türkçe",
          "number": 21,
          "text": "21. Aşağıdaki cümlelerin hangisinde bir <u>yazım yanlışı</u> yapılmıştır?",
          "options": [
            "A) Türk Dil Kurumu yeni kılavuzunu yayımladı.",
            "B) 9. yüzyılda pek çok önemli gelişme yaşandı.",
            "C) Bu konuda <u>herşey</u> planlandığı gibi gidiyor.",
            "D) TBMM'nin aldığı tarihi karar Resmi Gazete'de duyuruldu.",
            "E) Yanı sıra pek çok yabancı konuk da törene katıldı."
          ],
          "correct": 2,
          "solution": "'Herşey' sözcüğü 'Her şey' şeklinde ayrı yazılmalıdır. Şey sözcüğü daima ayrı yazılır."
        },
        {
          "id": "e9_q22",
          "subject": "Türkçe",
          "number": 22,
          "text": "22. Aşağıdaki cümlelerin hangisinde bir <u>yazım yanlışı</u> yapılmıştır?",
          "options": [
            "A) Türk Dil Kurumu yeni kılavuzunu yayımladı.",
            "B) 9. yüzyılda pek çok önemli gelişme yaşandı.",
            "C) Bu konuda <u>herşey</u> planlandığı gibi gidiyor.",
            "D) TBMM'nin aldığı tarihi karar Resmi Gazete'de duyuruldu.",
            "E) Yanı sıra pek çok yabancı konuk da törene katıldı."
          ],
          "correct": 2,
          "solution": "'Herşey' sözcüğü 'Her şey' şeklinde ayrı yazılmalıdır. Şey sözcüğü daima ayrı yazılır."
        },
        {
          "id": "e9_q23",
          "subject": "Türkçe",
          "number": 23,
          "text": "23. Aşağıdaki cümlelerin hangisinde bir <u>yazım yanlışı</u> yapılmıştır?",
          "options": [
            "A) Türk Dil Kurumu yeni kılavuzunu yayımladı.",
            "B) 9. yüzyılda pek çok önemli gelişme yaşandı.",
            "C) Bu konuda <u>herşey</u> planlandığı gibi gidiyor.",
            "D) TBMM'nin aldığı tarihi karar Resmi Gazete'de duyuruldu.",
            "E) Yanı sıra pek çok yabancı konuk da törene katıldı."
          ],
          "correct": 2,
          "solution": "'Herşey' sözcüğü 'Her şey' şeklinde ayrı yazılmalıdır. Şey sözcüğü daima ayrı yazılır."
        },
        {
          "id": "e9_q24",
          "subject": "Türkçe",
          "number": 24,
          "text": "24. Aşağıdaki cümlelerin hangisinde bir <u>yazım yanlışı</u> yapılmıştır?",
          "options": [
            "A) Türk Dil Kurumu yeni kılavuzunu yayımladı.",
            "B) 9. yüzyılda pek çok önemli gelişme yaşandı.",
            "C) Bu konuda <u>herşey</u> planlandığı gibi gidiyor.",
            "D) TBMM'nin aldığı tarihi karar Resmi Gazete'de duyuruldu.",
            "E) Yanı sıra pek çok yabancı konuk da törene katıldı."
          ],
          "correct": 2,
          "solution": "'Herşey' sözcüğü 'Her şey' şeklinde ayrı yazılmalıdır. Şey sözcüğü daima ayrı yazılır."
        },
        {
          "id": "e9_q25",
          "subject": "Türkçe",
          "number": 25,
          "text": "25. Aşağıdaki cümlelerin hangisinde bir <u>yazım yanlışı</u> yapılmıştır?",
          "options": [
            "A) Türk Dil Kurumu yeni kılavuzunu yayımladı.",
            "B) 9. yüzyılda pek çok önemli gelişme yaşandı.",
            "C) Bu konuda <u>herşey</u> planlandığı gibi gidiyor.",
            "D) TBMM'nin aldığı tarihi karar Resmi Gazete'de duyuruldu.",
            "E) Yanı sıra pek çok yabancı konuk da törene katıldı."
          ],
          "correct": 2,
          "solution": "'Herşey' sözcüğü 'Her şey' şeklinde ayrı yazılmalıdır. Şey sözcüğü daima ayrı yazılır."
        },
        {
          "id": "e9_q26",
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
          "id": "e9_q27",
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
          "id": "e9_q28",
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
          "id": "e9_q29",
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
          "id": "e9_q30",
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
          "id": "e9_q31",
          "subject": "Matematik",
          "number": 31,
          "text": "31. a ve b birer pozitif tam sayı olmak üzere,\n<code>3a + 5b = 173</code>\neşitliğini sağlayan en küçük b değeri için a kaçtır?",
          "options": [
            "A) 9",
            "B) 11",
            "C) 13",
            "D) 15",
            "E) 17"
          ],
          "correct": 1,
          "solution": "Denklemde b yerine en küçük pozitif tam sayı değerleri verilerek a = 11 olarak bulunur."
        },
        {
          "id": "e9_q32",
          "subject": "Matematik",
          "number": 32,
          "text": "32. a ve b birer pozitif tam sayı olmak üzere,\n<code>3a + 5b = 173</code>\neşitliğini sağlayan en küçük b değeri için a kaçtır?",
          "options": [
            "A) 9",
            "B) 11",
            "C) 13",
            "D) 15",
            "E) 17"
          ],
          "correct": 1,
          "solution": "Denklemde b yerine en küçük pozitif tam sayı değerleri verilerek a = 11 olarak bulunur."
        },
        {
          "id": "e9_q33",
          "subject": "Matematik",
          "number": 33,
          "text": "33. a ve b birer pozitif tam sayı olmak üzere,\n<code>3a + 5b = 173</code>\neşitliğini sağlayan en küçük b değeri için a kaçtır?",
          "options": [
            "A) 9",
            "B) 11",
            "C) 13",
            "D) 15",
            "E) 17"
          ],
          "correct": 1,
          "solution": "Denklemde b yerine en küçük pozitif tam sayı değerleri verilerek a = 11 olarak bulunur."
        },
        {
          "id": "e9_q34",
          "subject": "Matematik",
          "number": 34,
          "text": "34. a ve b birer pozitif tam sayı olmak üzere,\n<code>3a + 5b = 173</code>\neşitliğini sağlayan en küçük b değeri için a kaçtır?",
          "options": [
            "A) 9",
            "B) 11",
            "C) 13",
            "D) 15",
            "E) 17"
          ],
          "correct": 1,
          "solution": "Denklemde b yerine en küçük pozitif tam sayı değerleri verilerek a = 11 olarak bulunur."
        },
        {
          "id": "e9_q35",
          "subject": "Matematik",
          "number": 35,
          "text": "35. a ve b birer pozitif tam sayı olmak üzere,\n<code>3a + 5b = 173</code>\neşitliğini sağlayan en küçük b değeri için a kaçtır?",
          "options": [
            "A) 9",
            "B) 11",
            "C) 13",
            "D) 15",
            "E) 17"
          ],
          "correct": 1,
          "solution": "Denklemde b yerine en küçük pozitif tam sayı değerleri verilerek a = 11 olarak bulunur."
        },
        {
          "id": "e9_q36",
          "subject": "Matematik",
          "number": 36,
          "text": "36. <code>(1/2 + 1/3) : (5/6) + 2^10 = x</code>\nişleminin sonucu kaçtır?",
          "options": [
            "A) 1025",
            "B) 1026",
            "C) 1024",
            "D) 513",
            "E) 1027"
          ],
          "correct": 0,
          "solution": "(1/2 + 1/3) = 5/6. (5/6) : (5/6) = 1. Sonuç = 1 + 2^10 = 1025."
        },
        {
          "id": "e9_q37",
          "subject": "Matematik",
          "number": 37,
          "text": "37. <code>(1/2 + 1/3) : (5/6) + 2^11 = x</code>\nişleminin sonucu kaçtır?",
          "options": [
            "A) 2049",
            "B) 2050",
            "C) 2048",
            "D) 1025",
            "E) 2051"
          ],
          "correct": 0,
          "solution": "(1/2 + 1/3) = 5/6. (5/6) : (5/6) = 1. Sonuç = 1 + 2^11 = 2049."
        },
        {
          "id": "e9_q38",
          "subject": "Matematik",
          "number": 38,
          "text": "38. <code>(1/2 + 1/3) : (5/6) + 2^12 = x</code>\nişleminin sonucu kaçtır?",
          "options": [
            "A) 4097",
            "B) 4098",
            "C) 4096",
            "D) 2049",
            "E) 4099"
          ],
          "correct": 0,
          "solution": "(1/2 + 1/3) = 5/6. (5/6) : (5/6) = 1. Sonuç = 1 + 2^12 = 4097."
        },
        {
          "id": "e9_q39",
          "subject": "Matematik",
          "number": 39,
          "text": "39. <code>(1/2 + 1/3) : (5/6) + 2^13 = x</code>\nişleminin sonucu kaçtır?",
          "options": [
            "A) 8193",
            "B) 8194",
            "C) 8192",
            "D) 4097",
            "E) 8195"
          ],
          "correct": 0,
          "solution": "(1/2 + 1/3) = 5/6. (5/6) : (5/6) = 1. Sonuç = 1 + 2^13 = 8193."
        },
        {
          "id": "e9_q40",
          "subject": "Matematik",
          "number": 40,
          "text": "40. <code>(1/2 + 1/3) : (5/6) + 2^14 = x</code>\nişleminin sonucu kaçtır?",
          "options": [
            "A) 16385",
            "B) 16386",
            "C) 16384",
            "D) 8193",
            "E) 16387"
          ],
          "correct": 0,
          "solution": "(1/2 + 1/3) = 5/6. (5/6) : (5/6) = 1. Sonuç = 1 + 2^14 = 16385."
        },
        {
          "id": "e9_q41",
          "subject": "Matematik",
          "number": 41,
          "text": "41. <code>(1/2 + 1/3) : (5/6) + 2^15 = x</code>\nişleminin sonucu kaçtır?",
          "options": [
            "A) 32769",
            "B) 32770",
            "C) 32768",
            "D) 16385",
            "E) 32771"
          ],
          "correct": 0,
          "solution": "(1/2 + 1/3) = 5/6. (5/6) : (5/6) = 1. Sonuç = 1 + 2^15 = 32769."
        },
        {
          "id": "e9_q42",
          "subject": "Matematik",
          "number": 42,
          "text": "42. <code>(1/2 + 1/3) : (5/6) + 2^16 = x</code>\nişleminin sonucu kaçtır?",
          "options": [
            "A) 65537",
            "B) 65538",
            "C) 65536",
            "D) 32769",
            "E) 65539"
          ],
          "correct": 0,
          "solution": "(1/2 + 1/3) = 5/6. (5/6) : (5/6) = 1. Sonuç = 1 + 2^16 = 65537."
        },
        {
          "id": "e9_q43",
          "subject": "Matematik",
          "number": 43,
          "text": "43. Bir babanın bugünkü yaşı 54, oğlunun bugünkü yaşı ise 15'dır.\nBuna göre kaç yıl sonra babanın yaşı oğlunun yaşının 3 katı olur?",
          "options": [
            "A) 2",
            "B) 3",
            "C) 4",
            "D) 5",
            "E) 6"
          ],
          "correct": 2,
          "solution": "54 + t = 3(15 + t) => 54 + t = 45 + 3t => 2t = 9 => t = 4 yıl sonra."
        },
        {
          "id": "e9_q44",
          "subject": "Matematik",
          "number": 44,
          "text": "44. Bir babanın bugünkü yaşı 54, oğlunun bugünkü yaşı ise 15'dır.\nBuna göre kaç yıl sonra babanın yaşı oğlunun yaşının 3 katı olur?",
          "options": [
            "A) 2",
            "B) 3",
            "C) 4",
            "D) 5",
            "E) 6"
          ],
          "correct": 2,
          "solution": "54 + t = 3(15 + t) => 54 + t = 45 + 3t => 2t = 9 => t = 4 yıl sonra."
        },
        {
          "id": "e9_q45",
          "subject": "Matematik",
          "number": 45,
          "text": "45. Bir babanın bugünkü yaşı 54, oğlunun bugünkü yaşı ise 15'dır.\nBuna göre kaç yıl sonra babanın yaşı oğlunun yaşının 3 katı olur?",
          "options": [
            "A) 2",
            "B) 3",
            "C) 4",
            "D) 5",
            "E) 6"
          ],
          "correct": 2,
          "solution": "54 + t = 3(15 + t) => 54 + t = 45 + 3t => 2t = 9 => t = 4 yıl sonra."
        },
        {
          "id": "e9_q46",
          "subject": "Matematik",
          "number": 46,
          "text": "46. Bir babanın bugünkü yaşı 54, oğlunun bugünkü yaşı ise 15'dır.\nBuna göre kaç yıl sonra babanın yaşı oğlunun yaşının 3 katı olur?",
          "options": [
            "A) 2",
            "B) 3",
            "C) 4",
            "D) 5",
            "E) 6"
          ],
          "correct": 2,
          "solution": "54 + t = 3(15 + t) => 54 + t = 45 + 3t => 2t = 9 => t = 4 yıl sonra."
        },
        {
          "id": "e9_q47",
          "subject": "Matematik",
          "number": 47,
          "text": "47. Bir babanın bugünkü yaşı 54, oğlunun bugünkü yaşı ise 15'dır.\nBuna göre kaç yıl sonra babanın yaşı oğlunun yaşının 3 katı olur?",
          "options": [
            "A) 2",
            "B) 3",
            "C) 4",
            "D) 5",
            "E) 6"
          ],
          "correct": 2,
          "solution": "54 + t = 3(15 + t) => 54 + t = 45 + 3t => 2t = 9 => t = 4 yıl sonra."
        },
        {
          "id": "e9_q48",
          "subject": "Matematik",
          "number": 48,
          "text": "48. Bir babanın bugünkü yaşı 54, oğlunun bugünkü yaşı ise 15'dır.\nBuna göre kaç yıl sonra babanın yaşı oğlunun yaşının 3 katı olur?",
          "options": [
            "A) 2",
            "B) 3",
            "C) 4",
            "D) 5",
            "E) 6"
          ],
          "correct": 2,
          "solution": "54 + t = 3(15 + t) => 54 + t = 45 + 3t => 2t = 9 => t = 4 yıl sonra."
        },
        {
          "id": "e9_q49",
          "subject": "Matematik",
          "number": 49,
          "text": "49. Bir babanın bugünkü yaşı 54, oğlunun bugünkü yaşı ise 15'dır.\nBuna göre kaç yıl sonra babanın yaşı oğlunun yaşının 3 katı olur?",
          "options": [
            "A) 2",
            "B) 3",
            "C) 4",
            "D) 5",
            "E) 6"
          ],
          "correct": 2,
          "solution": "54 + t = 3(15 + t) => 54 + t = 45 + 3t => 2t = 9 => t = 4 yıl sonra."
        },
        {
          "id": "e9_q50",
          "subject": "Matematik",
          "number": 50,
          "text": "50. Bir babanın bugünkü yaşı 54, oğlunun bugünkü yaşı ise 15'dır.\nBuna göre kaç yıl sonra babanın yaşı oğlunun yaşının 3 katı olur?",
          "options": [
            "A) 2",
            "B) 3",
            "C) 4",
            "D) 5",
            "E) 6"
          ],
          "correct": 2,
          "solution": "54 + t = 3(15 + t) => 54 + t = 45 + 3t => 2t = 9 => t = 4 yıl sonra."
        },
        {
          "id": "e9_q51",
          "subject": "Matematik",
          "number": 51,
          "text": "51. Bir babanın bugünkü yaşı 54, oğlunun bugünkü yaşı ise 15'dır.\nBuna göre kaç yıl sonra babanın yaşı oğlunun yaşının 3 katı olur?",
          "options": [
            "A) 2",
            "B) 3",
            "C) 4",
            "D) 5",
            "E) 6"
          ],
          "correct": 2,
          "solution": "54 + t = 3(15 + t) => 54 + t = 45 + 3t => 2t = 9 => t = 4 yıl sonra."
        },
        {
          "id": "e9_q52",
          "subject": "Matematik",
          "number": 52,
          "text": "52. Bir babanın bugünkü yaşı 54, oğlunun bugünkü yaşı ise 15'dır.\nBuna göre kaç yıl sonra babanın yaşı oğlunun yaşının 3 katı olur?",
          "options": [
            "A) 2",
            "B) 3",
            "C) 4",
            "D) 5",
            "E) 6"
          ],
          "correct": 2,
          "solution": "54 + t = 3(15 + t) => 54 + t = 45 + 3t => 2t = 9 => t = 4 yıl sonra."
        },
        {
          "id": "e9_q53",
          "subject": "Matematik",
          "number": 53,
          "text": "53. Bir babanın bugünkü yaşı 54, oğlunun bugünkü yaşı ise 15'dır.\nBuna göre kaç yıl sonra babanın yaşı oğlunun yaşının 3 katı olur?",
          "options": [
            "A) 2",
            "B) 3",
            "C) 4",
            "D) 5",
            "E) 6"
          ],
          "correct": 2,
          "solution": "54 + t = 3(15 + t) => 54 + t = 45 + 3t => 2t = 9 => t = 4 yıl sonra."
        },
        {
          "id": "e9_q54",
          "subject": "Matematik",
          "number": 54,
          "text": "54. Bir babanın bugünkü yaşı 54, oğlunun bugünkü yaşı ise 15'dır.\nBuna göre kaç yıl sonra babanın yaşı oğlunun yaşının 3 katı olur?",
          "options": [
            "A) 2",
            "B) 3",
            "C) 4",
            "D) 5",
            "E) 6"
          ],
          "correct": 2,
          "solution": "54 + t = 3(15 + t) => 54 + t = 45 + 3t => 2t = 9 => t = 4 yıl sonra."
        },
        {
          "id": "e9_q55",
          "subject": "Matematik",
          "number": 55,
          "text": "55. A ve B iki küme olmak üzere,\n<code>s(A) = 21</code>, <code>s(B) = 19</code> ve <code>s(A ∩ B) = 8</code>\nolduğuna göre <code>s(A ∪ B)</code> kaçtır?",
          "options": [
            "A) 30",
            "B) 32",
            "C) 34",
            "D) 36",
            "E) 38"
          ],
          "correct": 1,
          "solution": "s(A ∪ B) = s(A) + s(B) - s(A ∩ B) = 21 + 19 - 8 = 32."
        },
        {
          "id": "e9_q56",
          "subject": "Matematik",
          "number": 56,
          "text": "56. A ve B iki küme olmak üzere,\n<code>s(A) = 21</code>, <code>s(B) = 19</code> ve <code>s(A ∩ B) = 8</code>\nolduğuna göre <code>s(A ∪ B)</code> kaçtır?",
          "options": [
            "A) 30",
            "B) 32",
            "C) 34",
            "D) 36",
            "E) 38"
          ],
          "correct": 1,
          "solution": "s(A ∪ B) = s(A) + s(B) - s(A ∩ B) = 21 + 19 - 8 = 32."
        },
        {
          "id": "e9_q57",
          "subject": "Matematik",
          "number": 57,
          "text": "57. A ve B iki küme olmak üzere,\n<code>s(A) = 21</code>, <code>s(B) = 19</code> ve <code>s(A ∩ B) = 8</code>\nolduğuna göre <code>s(A ∪ B)</code> kaçtır?",
          "options": [
            "A) 30",
            "B) 32",
            "C) 34",
            "D) 36",
            "E) 38"
          ],
          "correct": 1,
          "solution": "s(A ∪ B) = s(A) + s(B) - s(A ∩ B) = 21 + 19 - 8 = 32."
        },
        {
          "id": "e9_q58",
          "subject": "Matematik",
          "number": 58,
          "text": "58. A ve B iki küme olmak üzere,\n<code>s(A) = 21</code>, <code>s(B) = 19</code> ve <code>s(A ∩ B) = 8</code>\nolduğuna göre <code>s(A ∪ B)</code> kaçtır?",
          "options": [
            "A) 30",
            "B) 32",
            "C) 34",
            "D) 36",
            "E) 38"
          ],
          "correct": 1,
          "solution": "s(A ∪ B) = s(A) + s(B) - s(A ∩ B) = 21 + 19 - 8 = 32."
        },
        {
          "id": "e9_q59",
          "subject": "Matematik",
          "number": 59,
          "text": "59. Dik kenar uzunlukları 3 cm ve 4 cm olan bir dik üçgenin hipotenüs uzunluğu kaç cm'dir?",
          "options": [
            "A) 4",
            "B) 5",
            "C) 6",
            "D) 7",
            "E) 8"
          ],
          "correct": 1,
          "solution": "Pisagor bağıntısı: a² + b² = c² => 3² + 4² = 25 = 5² => Hipotenüs = 5 cm (3-4-5 katı)."
        },
        {
          "id": "e9_q60",
          "subject": "Matematik",
          "number": 60,
          "text": "60. Dik kenar uzunlukları 3 cm ve 4 cm olan bir dik üçgenin hipotenüs uzunluğu kaç cm'dir?",
          "options": [
            "A) 4",
            "B) 5",
            "C) 6",
            "D) 7",
            "E) 8"
          ],
          "correct": 1,
          "solution": "Pisagor bağıntısı: a² + b² = c² => 3² + 4² = 25 = 5² => Hipotenüs = 5 cm (3-4-5 katı)."
        },
        {
          "id": "e9_q61",
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
          "id": "e9_q62",
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
          "id": "e9_q63",
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
          "id": "e9_q64",
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
          "id": "e9_q65",
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
          "id": "e9_q66",
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
          "id": "e9_q67",
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
          "id": "e9_q68",
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
          "id": "e9_q69",
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
          "id": "e9_q70",
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
          "id": "e9_q71",
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
          "id": "e9_q72",
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
          "id": "e9_q73",
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
          "id": "e9_q74",
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
          "id": "e9_q75",
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
          "id": "e9_q76",
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
          "id": "e9_q77",
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
          "id": "e9_q78",
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
          "id": "e9_q79",
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
          "id": "e9_q80",
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
          "id": "e9_q81",
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
          "id": "e9_q82",
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
          "id": "e9_q83",
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
          "id": "e9_q84",
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
          "id": "e9_q85",
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
          "id": "e9_q86",
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
          "id": "e9_q87",
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
          "id": "e9_q88",
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
          "id": "e9_q89",
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
          "id": "e9_q90",
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
          "id": "e9_q91",
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
          "id": "e9_q92",
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
          "id": "e9_q93",
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
          "id": "e9_q94",
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
          "id": "e9_q95",
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
          "id": "e9_q96",
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
          "id": "e9_q97",
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
          "id": "e9_q98",
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
          "id": "e9_q99",
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
          "id": "e9_q100",
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
          "id": "e9_q101",
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
          "id": "e9_q102",
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
          "id": "e9_q103",
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
          "id": "e9_q104",
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
          "id": "e9_q105",
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
          "id": "e9_q106",
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
          "id": "e9_q107",
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
          "id": "e9_q108",
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
          "id": "e9_q109",
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
          "id": "e9_q110",
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
          "id": "e9_q111",
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
          "id": "e9_q112",
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
          "id": "e9_q113",
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
          "id": "e9_q114",
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
          "id": "e9_q115",
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
          "id": "e9_q116",
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
          "id": "e9_q117",
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
          "id": "e9_q118",
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
          "id": "e9_q119",
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
          "id": "e9_q120",
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
    {
      "id": "deneme_10",
      "title": "KPSS 2026 Ortaöğretim - 10. Deneme Sınavı (120 Soru)",
      "totalDurationMinutes": 130,
      "questions": [
        {
          "id": "e10_q1",
          "subject": "Türkçe",
          "number": 1,
          "text": "1. Aşağıdaki cümlelerin hangisinde <u>'koyu'</u> sözcüğü 'hararetli, derinleşmiş ve samimi' anlamında kullanılmıştır?",
          "options": [
            "A) Pencerenin kenarındaki nesne yere düştü.",
            "B) Yolun karşısındaki durağa doğru hızlıca koştu.",
            "C) Eski dostlar balkonda <u>koyu</u> bir sohbete dalmıştı.",
            "D) Bahçedeki ağaçların gölgesinde dinlenmeyi seçti.",
            "E) Kitaplarını çantasına özenle yerleştirdi."
          ],
          "correct": 2,
          "solution": "Seçenekteki 'koyu' kelimesi mecazi olarak 'hararetli, derinleşmiş ve samimi' anlamında kullanılmıştır."
        },
        {
          "id": "e10_q2",
          "subject": "Türkçe",
          "number": 2,
          "text": "2. Aşağıdaki cümlelerin hangisinde <u>'yüreğine su serpilmek'</u> deyimi 'ferahlamak, rahatlamak' anlamında kullanılmıştır?",
          "options": [
            "A) Haberin asılsız olduğunu öğrenince <u>yüreğine su serpildi</u>.",
            "B) Kütüphanedeki sessizliği kimse bozmak istemiyordu.",
            "C) Tren vaktinde istasyona yanaşarak yolcularını aldı.",
            "D) Bahçede rengarenk çiçekler açmıştı.",
            "E) Raporun son halini inceleyip imzaladı."
          ],
          "correct": 0,
          "solution": "Deyim cümlede 'ferahlamak, rahatlamak' anlamını karşılayacak şekilde yer almıştır."
        },
        {
          "id": "e10_q3",
          "subject": "Türkçe",
          "number": 3,
          "text": "3. (I) Şairin 103 yılında yayımlanan bu eseri yoğun bir ilgi gördü. (II) Kitapta yer alan imgeler okurun hayal dünyasını zenginleştiriyor. (III) Eser toplam 120 sayfadan ve 45 şiirden oluşmaktadır. (IV) Bence dönemin en başarılı şiir kitabı budur. (V) Kitabın ikinci baskısı geçen ay yapıldı.\n\nBu parçadaki numaralanmış cümlelerden hangisi <u>öznel</u> bir yargı içermektedir?",
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
          "id": "e10_q4",
          "subject": "Türkçe",
          "number": 4,
          "text": "4. (I) Şairin 104 yılında yayımlanan bu eseri yoğun bir ilgi gördü. (II) Kitapta yer alan imgeler okurun hayal dünyasını zenginleştiriyor. (III) Eser toplam 120 sayfadan ve 45 şiirden oluşmaktadır. (IV) Bence dönemin en başarılı şiir kitabı budur. (V) Kitabın ikinci baskısı geçen ay yapıldı.\n\nBu parçadaki numaralanmış cümlelerden hangisi <u>öznel</u> bir yargı içermektedir?",
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
          "id": "e10_q5",
          "subject": "Türkçe",
          "number": 5,
          "text": "5. (I) Şairin 105 yılında yayımlanan bu eseri yoğun bir ilgi gördü. (II) Kitapta yer alan imgeler okurun hayal dünyasını zenginleştiriyor. (III) Eser toplam 120 sayfadan ve 45 şiirden oluşmaktadır. (IV) Bence dönemin en başarılı şiir kitabı budur. (V) Kitabın ikinci baskısı geçen ay yapıldı.\n\nBu parçadaki numaralanmış cümlelerden hangisi <u>öznel</u> bir yargı içermektedir?",
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
          "id": "e10_q6",
          "subject": "Türkçe",
          "number": 6,
          "text": "6. (I) Şairin 106 yılında yayımlanan bu eseri yoğun bir ilgi gördü. (II) Kitapta yer alan imgeler okurun hayal dünyasını zenginleştiriyor. (III) Eser toplam 120 sayfadan ve 45 şiirden oluşmaktadır. (IV) Bence dönemin en başarılı şiir kitabı budur. (V) Kitabın ikinci baskısı geçen ay yapıldı.\n\nBu parçadaki numaralanmış cümlelerden hangisi <u>öznel</u> bir yargı içermektedir?",
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
          "id": "e10_q7",
          "subject": "Türkçe",
          "number": 7,
          "text": "7. (I) Şairin 107 yılında yayımlanan bu eseri yoğun bir ilgi gördü. (II) Kitapta yer alan imgeler okurun hayal dünyasını zenginleştiriyor. (III) Eser toplam 120 sayfadan ve 45 şiirden oluşmaktadır. (IV) Bence dönemin en başarılı şiir kitabı budur. (V) Kitabın ikinci baskısı geçen ay yapıldı.\n\nBu parçadaki numaralanmış cümlelerden hangisi <u>öznel</u> bir yargı içermektedir?",
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
          "id": "e10_q8",
          "subject": "Türkçe",
          "number": 8,
          "text": "8. (I) Şairin 108 yılında yayımlanan bu eseri yoğun bir ilgi gördü. (II) Kitapta yer alan imgeler okurun hayal dünyasını zenginleştiriyor. (III) Eser toplam 120 sayfadan ve 45 şiirden oluşmaktadır. (IV) Bence dönemin en başarılı şiir kitabı budur. (V) Kitabın ikinci baskısı geçen ay yapıldı.\n\nBu parçadaki numaralanmış cümlelerden hangisi <u>öznel</u> bir yargı içermektedir?",
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
          "id": "e10_q9",
          "subject": "Türkçe",
          "number": 9,
          "text": "9. (I) Şairin 109 yılında yayımlanan bu eseri yoğun bir ilgi gördü. (II) Kitapta yer alan imgeler okurun hayal dünyasını zenginleştiriyor. (III) Eser toplam 120 sayfadan ve 45 şiirden oluşmaktadır. (IV) Bence dönemin en başarılı şiir kitabı budur. (V) Kitabın ikinci baskısı geçen ay yapıldı.\n\nBu parçadaki numaralanmış cümlelerden hangisi <u>öznel</u> bir yargı içermektedir?",
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
          "id": "e10_q10",
          "subject": "Türkçe",
          "number": 10,
          "text": "10. (I) Şairin 110 yılında yayımlanan bu eseri yoğun bir ilgi gördü. (II) Kitapta yer alan imgeler okurun hayal dünyasını zenginleştiriyor. (III) Eser toplam 120 sayfadan ve 45 şiirden oluşmaktadır. (IV) Bence dönemin en başarılı şiir kitabı budur. (V) Kitabın ikinci baskısı geçen ay yapıldı.\n\nBu parçadaki numaralanmış cümlelerden hangisi <u>öznel</u> bir yargı içermektedir?",
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
          "id": "e10_q11",
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
          "id": "e10_q12",
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
          "id": "e10_q13",
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
          "id": "e10_q14",
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
          "id": "e10_q15",
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
          "id": "e10_q16",
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
          "id": "e10_q17",
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
          "id": "e10_q18",
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
          "id": "e10_q19",
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
          "id": "e10_q20",
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
          "id": "e10_q21",
          "subject": "Türkçe",
          "number": 21,
          "text": "21. Aşağıdaki cümlelerin hangisinde bir <u>yazım yanlışı</u> yapılmıştır?",
          "options": [
            "A) Türk Dil Kurumu yeni kılavuzunu yayımladı.",
            "B) 10. yüzyılda pek çok önemli gelişme yaşandı.",
            "C) Bu konuda <u>herşey</u> planlandığı gibi gidiyor.",
            "D) TBMM'nin aldığı tarihi karar Resmi Gazete'de duyuruldu.",
            "E) Yanı sıra pek çok yabancı konuk da törene katıldı."
          ],
          "correct": 2,
          "solution": "'Herşey' sözcüğü 'Her şey' şeklinde ayrı yazılmalıdır. Şey sözcüğü daima ayrı yazılır."
        },
        {
          "id": "e10_q22",
          "subject": "Türkçe",
          "number": 22,
          "text": "22. Aşağıdaki cümlelerin hangisinde bir <u>yazım yanlışı</u> yapılmıştır?",
          "options": [
            "A) Türk Dil Kurumu yeni kılavuzunu yayımladı.",
            "B) 10. yüzyılda pek çok önemli gelişme yaşandı.",
            "C) Bu konuda <u>herşey</u> planlandığı gibi gidiyor.",
            "D) TBMM'nin aldığı tarihi karar Resmi Gazete'de duyuruldu.",
            "E) Yanı sıra pek çok yabancı konuk da törene katıldı."
          ],
          "correct": 2,
          "solution": "'Herşey' sözcüğü 'Her şey' şeklinde ayrı yazılmalıdır. Şey sözcüğü daima ayrı yazılır."
        },
        {
          "id": "e10_q23",
          "subject": "Türkçe",
          "number": 23,
          "text": "23. Aşağıdaki cümlelerin hangisinde bir <u>yazım yanlışı</u> yapılmıştır?",
          "options": [
            "A) Türk Dil Kurumu yeni kılavuzunu yayımladı.",
            "B) 10. yüzyılda pek çok önemli gelişme yaşandı.",
            "C) Bu konuda <u>herşey</u> planlandığı gibi gidiyor.",
            "D) TBMM'nin aldığı tarihi karar Resmi Gazete'de duyuruldu.",
            "E) Yanı sıra pek çok yabancı konuk da törene katıldı."
          ],
          "correct": 2,
          "solution": "'Herşey' sözcüğü 'Her şey' şeklinde ayrı yazılmalıdır. Şey sözcüğü daima ayrı yazılır."
        },
        {
          "id": "e10_q24",
          "subject": "Türkçe",
          "number": 24,
          "text": "24. Aşağıdaki cümlelerin hangisinde bir <u>yazım yanlışı</u> yapılmıştır?",
          "options": [
            "A) Türk Dil Kurumu yeni kılavuzunu yayımladı.",
            "B) 10. yüzyılda pek çok önemli gelişme yaşandı.",
            "C) Bu konuda <u>herşey</u> planlandığı gibi gidiyor.",
            "D) TBMM'nin aldığı tarihi karar Resmi Gazete'de duyuruldu.",
            "E) Yanı sıra pek çok yabancı konuk da törene katıldı."
          ],
          "correct": 2,
          "solution": "'Herşey' sözcüğü 'Her şey' şeklinde ayrı yazılmalıdır. Şey sözcüğü daima ayrı yazılır."
        },
        {
          "id": "e10_q25",
          "subject": "Türkçe",
          "number": 25,
          "text": "25. Aşağıdaki cümlelerin hangisinde bir <u>yazım yanlışı</u> yapılmıştır?",
          "options": [
            "A) Türk Dil Kurumu yeni kılavuzunu yayımladı.",
            "B) 10. yüzyılda pek çok önemli gelişme yaşandı.",
            "C) Bu konuda <u>herşey</u> planlandığı gibi gidiyor.",
            "D) TBMM'nin aldığı tarihi karar Resmi Gazete'de duyuruldu.",
            "E) Yanı sıra pek çok yabancı konuk da törene katıldı."
          ],
          "correct": 2,
          "solution": "'Herşey' sözcüğü 'Her şey' şeklinde ayrı yazılmalıdır. Şey sözcüğü daima ayrı yazılır."
        },
        {
          "id": "e10_q26",
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
          "id": "e10_q27",
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
          "id": "e10_q28",
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
          "id": "e10_q29",
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
          "id": "e10_q30",
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
          "id": "e10_q31",
          "subject": "Matematik",
          "number": 31,
          "text": "31. a ve b birer pozitif tam sayı olmak üzere,\n<code>3a + 5b = 191</code>\neşitliğini sağlayan en küçük b değeri için a kaçtır?",
          "options": [
            "A) 10",
            "B) 12",
            "C) 14",
            "D) 16",
            "E) 18"
          ],
          "correct": 1,
          "solution": "Denklemde b yerine en küçük pozitif tam sayı değerleri verilerek a = 12 olarak bulunur."
        },
        {
          "id": "e10_q32",
          "subject": "Matematik",
          "number": 32,
          "text": "32. a ve b birer pozitif tam sayı olmak üzere,\n<code>3a + 5b = 191</code>\neşitliğini sağlayan en küçük b değeri için a kaçtır?",
          "options": [
            "A) 10",
            "B) 12",
            "C) 14",
            "D) 16",
            "E) 18"
          ],
          "correct": 1,
          "solution": "Denklemde b yerine en küçük pozitif tam sayı değerleri verilerek a = 12 olarak bulunur."
        },
        {
          "id": "e10_q33",
          "subject": "Matematik",
          "number": 33,
          "text": "33. a ve b birer pozitif tam sayı olmak üzere,\n<code>3a + 5b = 191</code>\neşitliğini sağlayan en küçük b değeri için a kaçtır?",
          "options": [
            "A) 10",
            "B) 12",
            "C) 14",
            "D) 16",
            "E) 18"
          ],
          "correct": 1,
          "solution": "Denklemde b yerine en küçük pozitif tam sayı değerleri verilerek a = 12 olarak bulunur."
        },
        {
          "id": "e10_q34",
          "subject": "Matematik",
          "number": 34,
          "text": "34. a ve b birer pozitif tam sayı olmak üzere,\n<code>3a + 5b = 191</code>\neşitliğini sağlayan en küçük b değeri için a kaçtır?",
          "options": [
            "A) 10",
            "B) 12",
            "C) 14",
            "D) 16",
            "E) 18"
          ],
          "correct": 1,
          "solution": "Denklemde b yerine en küçük pozitif tam sayı değerleri verilerek a = 12 olarak bulunur."
        },
        {
          "id": "e10_q35",
          "subject": "Matematik",
          "number": 35,
          "text": "35. a ve b birer pozitif tam sayı olmak üzere,\n<code>3a + 5b = 191</code>\neşitliğini sağlayan en küçük b değeri için a kaçtır?",
          "options": [
            "A) 10",
            "B) 12",
            "C) 14",
            "D) 16",
            "E) 18"
          ],
          "correct": 1,
          "solution": "Denklemde b yerine en küçük pozitif tam sayı değerleri verilerek a = 12 olarak bulunur."
        },
        {
          "id": "e10_q36",
          "subject": "Matematik",
          "number": 36,
          "text": "36. <code>(1/2 + 1/3) : (5/6) + 2^11 = x</code>\nişleminin sonucu kaçtır?",
          "options": [
            "A) 2049",
            "B) 2050",
            "C) 2048",
            "D) 1025",
            "E) 2051"
          ],
          "correct": 0,
          "solution": "(1/2 + 1/3) = 5/6. (5/6) : (5/6) = 1. Sonuç = 1 + 2^11 = 2049."
        },
        {
          "id": "e10_q37",
          "subject": "Matematik",
          "number": 37,
          "text": "37. <code>(1/2 + 1/3) : (5/6) + 2^12 = x</code>\nişleminin sonucu kaçtır?",
          "options": [
            "A) 4097",
            "B) 4098",
            "C) 4096",
            "D) 2049",
            "E) 4099"
          ],
          "correct": 0,
          "solution": "(1/2 + 1/3) = 5/6. (5/6) : (5/6) = 1. Sonuç = 1 + 2^12 = 4097."
        },
        {
          "id": "e10_q38",
          "subject": "Matematik",
          "number": 38,
          "text": "38. <code>(1/2 + 1/3) : (5/6) + 2^13 = x</code>\nişleminin sonucu kaçtır?",
          "options": [
            "A) 8193",
            "B) 8194",
            "C) 8192",
            "D) 4097",
            "E) 8195"
          ],
          "correct": 0,
          "solution": "(1/2 + 1/3) = 5/6. (5/6) : (5/6) = 1. Sonuç = 1 + 2^13 = 8193."
        },
        {
          "id": "e10_q39",
          "subject": "Matematik",
          "number": 39,
          "text": "39. <code>(1/2 + 1/3) : (5/6) + 2^14 = x</code>\nişleminin sonucu kaçtır?",
          "options": [
            "A) 16385",
            "B) 16386",
            "C) 16384",
            "D) 8193",
            "E) 16387"
          ],
          "correct": 0,
          "solution": "(1/2 + 1/3) = 5/6. (5/6) : (5/6) = 1. Sonuç = 1 + 2^14 = 16385."
        },
        {
          "id": "e10_q40",
          "subject": "Matematik",
          "number": 40,
          "text": "40. <code>(1/2 + 1/3) : (5/6) + 2^15 = x</code>\nişleminin sonucu kaçtır?",
          "options": [
            "A) 32769",
            "B) 32770",
            "C) 32768",
            "D) 16385",
            "E) 32771"
          ],
          "correct": 0,
          "solution": "(1/2 + 1/3) = 5/6. (5/6) : (5/6) = 1. Sonuç = 1 + 2^15 = 32769."
        },
        {
          "id": "e10_q41",
          "subject": "Matematik",
          "number": 41,
          "text": "41. <code>(1/2 + 1/3) : (5/6) + 2^16 = x</code>\nişleminin sonucu kaçtır?",
          "options": [
            "A) 65537",
            "B) 65538",
            "C) 65536",
            "D) 32769",
            "E) 65539"
          ],
          "correct": 0,
          "solution": "(1/2 + 1/3) = 5/6. (5/6) : (5/6) = 1. Sonuç = 1 + 2^16 = 65537."
        },
        {
          "id": "e10_q42",
          "subject": "Matematik",
          "number": 42,
          "text": "42. <code>(1/2 + 1/3) : (5/6) + 2^17 = x</code>\nişleminin sonucu kaçtır?",
          "options": [
            "A) 131073",
            "B) 131074",
            "C) 131072",
            "D) 65537",
            "E) 131075"
          ],
          "correct": 0,
          "solution": "(1/2 + 1/3) = 5/6. (5/6) : (5/6) = 1. Sonuç = 1 + 2^17 = 131073."
        },
        {
          "id": "e10_q43",
          "subject": "Matematik",
          "number": 43,
          "text": "43. Bir babanın bugünkü yaşı 56, oğlunun bugünkü yaşı ise 16'dır.\nBuna göre kaç yıl sonra babanın yaşı oğlunun yaşının 3 katı olur?",
          "options": [
            "A) 2",
            "B) 3",
            "C) 4",
            "D) 5",
            "E) 6"
          ],
          "correct": 2,
          "solution": "56 + t = 3(16 + t) => 56 + t = 48 + 3t => 2t = 8 => t = 4 yıl sonra."
        },
        {
          "id": "e10_q44",
          "subject": "Matematik",
          "number": 44,
          "text": "44. Bir babanın bugünkü yaşı 56, oğlunun bugünkü yaşı ise 16'dır.\nBuna göre kaç yıl sonra babanın yaşı oğlunun yaşının 3 katı olur?",
          "options": [
            "A) 2",
            "B) 3",
            "C) 4",
            "D) 5",
            "E) 6"
          ],
          "correct": 2,
          "solution": "56 + t = 3(16 + t) => 56 + t = 48 + 3t => 2t = 8 => t = 4 yıl sonra."
        },
        {
          "id": "e10_q45",
          "subject": "Matematik",
          "number": 45,
          "text": "45. Bir babanın bugünkü yaşı 56, oğlunun bugünkü yaşı ise 16'dır.\nBuna göre kaç yıl sonra babanın yaşı oğlunun yaşının 3 katı olur?",
          "options": [
            "A) 2",
            "B) 3",
            "C) 4",
            "D) 5",
            "E) 6"
          ],
          "correct": 2,
          "solution": "56 + t = 3(16 + t) => 56 + t = 48 + 3t => 2t = 8 => t = 4 yıl sonra."
        },
        {
          "id": "e10_q46",
          "subject": "Matematik",
          "number": 46,
          "text": "46. Bir babanın bugünkü yaşı 56, oğlunun bugünkü yaşı ise 16'dır.\nBuna göre kaç yıl sonra babanın yaşı oğlunun yaşının 3 katı olur?",
          "options": [
            "A) 2",
            "B) 3",
            "C) 4",
            "D) 5",
            "E) 6"
          ],
          "correct": 2,
          "solution": "56 + t = 3(16 + t) => 56 + t = 48 + 3t => 2t = 8 => t = 4 yıl sonra."
        },
        {
          "id": "e10_q47",
          "subject": "Matematik",
          "number": 47,
          "text": "47. Bir babanın bugünkü yaşı 56, oğlunun bugünkü yaşı ise 16'dır.\nBuna göre kaç yıl sonra babanın yaşı oğlunun yaşının 3 katı olur?",
          "options": [
            "A) 2",
            "B) 3",
            "C) 4",
            "D) 5",
            "E) 6"
          ],
          "correct": 2,
          "solution": "56 + t = 3(16 + t) => 56 + t = 48 + 3t => 2t = 8 => t = 4 yıl sonra."
        },
        {
          "id": "e10_q48",
          "subject": "Matematik",
          "number": 48,
          "text": "48. Bir babanın bugünkü yaşı 56, oğlunun bugünkü yaşı ise 16'dır.\nBuna göre kaç yıl sonra babanın yaşı oğlunun yaşının 3 katı olur?",
          "options": [
            "A) 2",
            "B) 3",
            "C) 4",
            "D) 5",
            "E) 6"
          ],
          "correct": 2,
          "solution": "56 + t = 3(16 + t) => 56 + t = 48 + 3t => 2t = 8 => t = 4 yıl sonra."
        },
        {
          "id": "e10_q49",
          "subject": "Matematik",
          "number": 49,
          "text": "49. Bir babanın bugünkü yaşı 56, oğlunun bugünkü yaşı ise 16'dır.\nBuna göre kaç yıl sonra babanın yaşı oğlunun yaşının 3 katı olur?",
          "options": [
            "A) 2",
            "B) 3",
            "C) 4",
            "D) 5",
            "E) 6"
          ],
          "correct": 2,
          "solution": "56 + t = 3(16 + t) => 56 + t = 48 + 3t => 2t = 8 => t = 4 yıl sonra."
        },
        {
          "id": "e10_q50",
          "subject": "Matematik",
          "number": 50,
          "text": "50. Bir babanın bugünkü yaşı 56, oğlunun bugünkü yaşı ise 16'dır.\nBuna göre kaç yıl sonra babanın yaşı oğlunun yaşının 3 katı olur?",
          "options": [
            "A) 2",
            "B) 3",
            "C) 4",
            "D) 5",
            "E) 6"
          ],
          "correct": 2,
          "solution": "56 + t = 3(16 + t) => 56 + t = 48 + 3t => 2t = 8 => t = 4 yıl sonra."
        },
        {
          "id": "e10_q51",
          "subject": "Matematik",
          "number": 51,
          "text": "51. Bir babanın bugünkü yaşı 56, oğlunun bugünkü yaşı ise 16'dır.\nBuna göre kaç yıl sonra babanın yaşı oğlunun yaşının 3 katı olur?",
          "options": [
            "A) 2",
            "B) 3",
            "C) 4",
            "D) 5",
            "E) 6"
          ],
          "correct": 2,
          "solution": "56 + t = 3(16 + t) => 56 + t = 48 + 3t => 2t = 8 => t = 4 yıl sonra."
        },
        {
          "id": "e10_q52",
          "subject": "Matematik",
          "number": 52,
          "text": "52. Bir babanın bugünkü yaşı 56, oğlunun bugünkü yaşı ise 16'dır.\nBuna göre kaç yıl sonra babanın yaşı oğlunun yaşının 3 katı olur?",
          "options": [
            "A) 2",
            "B) 3",
            "C) 4",
            "D) 5",
            "E) 6"
          ],
          "correct": 2,
          "solution": "56 + t = 3(16 + t) => 56 + t = 48 + 3t => 2t = 8 => t = 4 yıl sonra."
        },
        {
          "id": "e10_q53",
          "subject": "Matematik",
          "number": 53,
          "text": "53. Bir babanın bugünkü yaşı 56, oğlunun bugünkü yaşı ise 16'dır.\nBuna göre kaç yıl sonra babanın yaşı oğlunun yaşının 3 katı olur?",
          "options": [
            "A) 2",
            "B) 3",
            "C) 4",
            "D) 5",
            "E) 6"
          ],
          "correct": 2,
          "solution": "56 + t = 3(16 + t) => 56 + t = 48 + 3t => 2t = 8 => t = 4 yıl sonra."
        },
        {
          "id": "e10_q54",
          "subject": "Matematik",
          "number": 54,
          "text": "54. Bir babanın bugünkü yaşı 56, oğlunun bugünkü yaşı ise 16'dır.\nBuna göre kaç yıl sonra babanın yaşı oğlunun yaşının 3 katı olur?",
          "options": [
            "A) 2",
            "B) 3",
            "C) 4",
            "D) 5",
            "E) 6"
          ],
          "correct": 2,
          "solution": "56 + t = 3(16 + t) => 56 + t = 48 + 3t => 2t = 8 => t = 4 yıl sonra."
        },
        {
          "id": "e10_q55",
          "subject": "Matematik",
          "number": 55,
          "text": "55. A ve B iki küme olmak üzere,\n<code>s(A) = 22</code>, <code>s(B) = 20</code> ve <code>s(A ∩ B) = 9</code>\nolduğuna göre <code>s(A ∪ B)</code> kaçtır?",
          "options": [
            "A) 31",
            "B) 33",
            "C) 35",
            "D) 37",
            "E) 39"
          ],
          "correct": 1,
          "solution": "s(A ∪ B) = s(A) + s(B) - s(A ∩ B) = 22 + 20 - 9 = 33."
        },
        {
          "id": "e10_q56",
          "subject": "Matematik",
          "number": 56,
          "text": "56. A ve B iki küme olmak üzere,\n<code>s(A) = 22</code>, <code>s(B) = 20</code> ve <code>s(A ∩ B) = 9</code>\nolduğuna göre <code>s(A ∪ B)</code> kaçtır?",
          "options": [
            "A) 31",
            "B) 33",
            "C) 35",
            "D) 37",
            "E) 39"
          ],
          "correct": 1,
          "solution": "s(A ∪ B) = s(A) + s(B) - s(A ∩ B) = 22 + 20 - 9 = 33."
        },
        {
          "id": "e10_q57",
          "subject": "Matematik",
          "number": 57,
          "text": "57. A ve B iki küme olmak üzere,\n<code>s(A) = 22</code>, <code>s(B) = 20</code> ve <code>s(A ∩ B) = 9</code>\nolduğuna göre <code>s(A ∪ B)</code> kaçtır?",
          "options": [
            "A) 31",
            "B) 33",
            "C) 35",
            "D) 37",
            "E) 39"
          ],
          "correct": 1,
          "solution": "s(A ∪ B) = s(A) + s(B) - s(A ∩ B) = 22 + 20 - 9 = 33."
        },
        {
          "id": "e10_q58",
          "subject": "Matematik",
          "number": 58,
          "text": "58. A ve B iki küme olmak üzere,\n<code>s(A) = 22</code>, <code>s(B) = 20</code> ve <code>s(A ∩ B) = 9</code>\nolduğuna göre <code>s(A ∪ B)</code> kaçtır?",
          "options": [
            "A) 31",
            "B) 33",
            "C) 35",
            "D) 37",
            "E) 39"
          ],
          "correct": 1,
          "solution": "s(A ∪ B) = s(A) + s(B) - s(A ∩ B) = 22 + 20 - 9 = 33."
        },
        {
          "id": "e10_q59",
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
          "id": "e10_q60",
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
          "id": "e10_q61",
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
          "id": "e10_q62",
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
          "id": "e10_q63",
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
          "id": "e10_q64",
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
          "id": "e10_q65",
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
          "id": "e10_q66",
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
          "id": "e10_q67",
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
          "id": "e10_q68",
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
          "id": "e10_q69",
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
          "id": "e10_q70",
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
          "id": "e10_q71",
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
          "id": "e10_q72",
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
          "id": "e10_q73",
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
          "id": "e10_q74",
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
          "id": "e10_q75",
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
          "id": "e10_q76",
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
          "id": "e10_q77",
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
          "id": "e10_q78",
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
          "id": "e10_q79",
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
          "id": "e10_q80",
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
          "id": "e10_q81",
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
          "id": "e10_q82",
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
          "id": "e10_q83",
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
          "id": "e10_q84",
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
          "id": "e10_q85",
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
          "id": "e10_q86",
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
          "id": "e10_q87",
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
          "id": "e10_q88",
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
          "id": "e10_q89",
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
          "id": "e10_q90",
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
          "id": "e10_q91",
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
          "id": "e10_q92",
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
          "id": "e10_q93",
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
          "id": "e10_q94",
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
          "id": "e10_q95",
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
          "id": "e10_q96",
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
          "id": "e10_q97",
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
          "id": "e10_q98",
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
          "id": "e10_q99",
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
          "id": "e10_q100",
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
          "id": "e10_q101",
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
          "id": "e10_q102",
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
          "id": "e10_q103",
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
          "id": "e10_q104",
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
          "id": "e10_q105",
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
          "id": "e10_q106",
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
          "id": "e10_q107",
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
          "id": "e10_q108",
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
          "id": "e10_q109",
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
          "id": "e10_q110",
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
          "id": "e10_q111",
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
          "id": "e10_q112",
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
          "id": "e10_q113",
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
          "id": "e10_q114",
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
          "id": "e10_q115",
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
          "id": "e10_q116",
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
          "id": "e10_q117",
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
          "id": "e10_q118",
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
          "id": "e10_q119",
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
          "id": "e10_q120",
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
    }
  ]
};
