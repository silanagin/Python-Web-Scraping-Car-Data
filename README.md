# 🚗 Vehicle Data Web Scraping & Analysis

Bu proje, DummyJSON API servisinden araç verilerini çekip işleyen, verileri `.csv` formatında dışa aktaran ve temel veri analizi özetini sunan bir Python çalışmasıdır.

## 🛠️ Kullanılan Teknolojiler
* **Python 3**
* **Requests** (API veri çekme)
* **Pandas** (Veri analizi ve `.csv` dışa aktarımı)

## 📊 Proje Çıktıları & Analiz Özet
* **API Bağlantısı:** HTTP 200 Durum Kodu ile veriler başarıyla çekildi.
* **Veri Depolama:** `araba_verileri.csv` dosyasına başarıyla kaydedildi.
* **Hızlı Analiz:** 
  * Toplam araç sayısı hesaplandı.
  * En pahalı araç ve en yüksek puanlı araç verileri Pandas `idxmax()` metodu ile dinamik olarak tespit edildi.
