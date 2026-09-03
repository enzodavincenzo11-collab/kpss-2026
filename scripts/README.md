# KPSS 2026 Yardımcı Scriptler ve Veri Oluşturucular

Bu klasördeki betikler, KPSS 2026 platformu için deneme sorularını, konu anlatımlarını ve müfredat verilerini üretmek ve `data.js` dosyasına derlemek için kullanılan Python araçlarıdır:

1. **`generate_120_unique_questions.py`**:
   - 120 adet %100 benzersiz, ÖSYM standartlarında orijinal KPSS sorusunu ve detaylı çözümlerini üretir.

2. **`build_comprehensive_kpss_system.py`**:
   - 5 temel dersin (Matematik, Türkçe, Tarih, Coğrafya, Vatandaşlık) tüm müfredatını, sayfa sayfa konu anlatım metinlerini ve 120 deneme sorusunu birleştirerek `c:\Users\oktay\Desktop\kpss\data.js` dosyasına yazar.

3. **`mock_questions.json`**:
   - Üretilen 120 deneme sorusunun ham JSON veri kaynağıdır.
