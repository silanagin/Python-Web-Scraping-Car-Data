import requests 
import pandas as pd



url = requests.get("https://dummyjson.com/products/category/vehicle")
if url.status_code==200:
    print("Siteden Veri Çekilebilir")

    data = url.json()
    araclar = data["products"]
    arac_listesi = []

    print("---ARAÇLAR---")
    for arac in araclar:
        arac_listesi.append({
        "Araç Adı": arac.get("title"),
        "Fiyat ($)": arac.get("price"),
        "Puan": arac.get("rating"),
        "Stok": arac.get("stock")
        })
        print(f"- {arac.get('title')} | Fiyat: ${arac.get('price')}")

    df = pd.DataFrame(arac_listesi)
    df.to_csv('araba_verileri.csv', index=False, encoding="utf-8-sig")
    print("\nVeriler 'araba_verileri.csv' dosyasına kaydedildi!")  
    print("Hızlı Veri Analizi Özeti")
    print(f"Toplam Araç Sayısı: {len(df)}")
    print(f"En Pahalı Araç: {df.loc[df['Fiyat ($)'].idxmax()]['Araç Adı']} (${df['Fiyat ($)'].max()})")
    print(f"En Yüksek Puan: {df.loc[df['Puan'].idxmax()]['Araç Adı']} ({df['Puan'].max()} Puan)")
else:
    print("Siteden Veri Çekilemez")