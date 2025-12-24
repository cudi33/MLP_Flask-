# Medical Cost Prediction – Çoklu Doğrusal Regresyon ve Flask Uygulaması

## 👤 Öğrenci Bilgileri

- **Ad Soyad:** Cudi Şami
- **Öğrenci Numarası:** 2012721308
- **GitHub Repo Bağlantısı:** https://github.com/cudi33/MLP_Flask-

---

## 📌 Proje Amacı

Bu projenin amacı, bireylerin demografik ve sağlıkla ilgili özelliklerini
kullanarak **tıbbi harcamalarını (charges)** tahmin eden bir
**Çoklu Doğrusal Regresyon (Multiple Linear Regression)** modeli geliştirmek
ve bu modeli **Flask tabanlı basit bir web arayüzü** üzerinden sunmaktır.

---

## 📊 Kullanılan Veri Seti

- **Dosya:** `insurance.csv`
- **Gözlem Sayısı:** 1338
- **Bağımlı Değişken (Target):**
  - `charges` (Tıbbi harcama)

### Bağımsız Değişkenler:

- `age` (Yaş)
- `bmi` (Vücut Kitle İndeksi)
- `children` (Çocuk sayısı)
- `smoker` (Sigara kullanımı)
- `region` (Bölge)

---

## 🔧 Veri Ön İşleme (Data Preprocessing)

### 1️⃣ Eksik Veri Analizi

- Veri setinde eksik (missing) değer bulunmamaktadır.
- Bu nedenle veri silme veya doldurma işlemi uygulanmamıştır.

### 2️⃣ Kategorik Verilerin Kodlanması

- Kategorik değişkenler için **One-Hot Encoding** yöntemi kullanılmıştır.
- Bu yöntem, kategorik değişkenler arasında yapay sıralama oluşmasını
  engellediği için tercih edilmiştir.

### 3️⃣ Veri Tipi Dönüşümü

- One-Hot Encoding sonrası tüm değişkenler `float` veri tipine
  dönüştürülmüştür.
- Amaç, istatistiksel modelleme sırasında veri tipi uyumsuzluklarını
  önlemektir.

---

## 🔍 Backward Elimination (Geriye Doğru Eleme)

İstatistiksel olarak anlamsız değişkenleri belirlemek için
**Backward Elimination** yöntemi uygulanmıştır.

### Uygulanan Adımlar:

1. Tüm bağımsız değişkenlerle OLS modeli kurulmuştur.
2. Her değişkenin **p-value** değeri incelenmiştir.
3. **p > 0.05** olan değişkenler modelden çıkarılmıştır.
4. Model, yalnızca istatistiksel olarak anlamlı değişkenler kalana kadar
   yeniden eğitilmiştir.

### Sonuç:

- `sex_male` ve `region_northwest` değişkenleri istatistiksel olarak
  anlamsız bulunmuş ve modelden çıkarılmıştır.
- Kalan değişkenlerin tamamı anlamlıdır.

---

## 📈 Model Kurulumu ve Değerlendirme

### Kullanılan Model:

- **Multiple Linear Regression**

### Performans Metrikleri:

- **R² (R-Kare)**
- **MAE (Mean Absolute Error)**
- **MSE (Mean Squared Error)**

### Sonuçlar:

- Backward Elimination öncesi ve sonrası performans değerleri
  büyük ölçüde benzer çıkmıştır.
- Bu durum, çıkarılan değişkenlerin model başarısına anlamlı bir katkı
  sağlamadığını göstermektedir.
- Daha az değişken içeren, daha sade ve yorumlanabilir bir model elde
  edilmiştir.

---

## ⚠️ Modelin Sınırlılıkları

- Doğrusal regresyon modeli matematiksel yapısı gereği bazı uç
  değerler için **negatif tahminler** üretebilir.
- Bu durum bir hata değildir, doğrusal regresyonun bilinen bir
  sınırlılığıdır.
- Model çıktıları projede olduğu gibi korunmuş ve yalnızca
  akademik olarak yorumlanmıştır.

---

## 🌐 Flask Web Arayüzü

Model, **Flask** kullanılarak geliştirilen basit bir web arayüzü
üzerinden kullanıma sunulmuştur.

### Özellikler:

- Kullanıcıdan modelde kullanılan giriş değişkenleri alınır.
- Eğitilmiş model (`model.pkl`) yüklenir.
- Tahmin edilen tıbbi harcama ekranda gösterilir.
- Arayüz sade ve işlevseldir.

---

## 📁 Proje Dosya Yapısı

```
Medical_Cost_Prediction/
│
├── insurance.csv
├── model.pkl
├── app.py
├── Medical_Cost_Prediction.ipynb
├── README.md
│
└── templates/
    └── index.html
```


---

## ▶️ Uygulamanın Çalıştırılması

```bash
pip install flask numpy pandas scikit-learn statsmodels
python app.py
``` 
Tarayıcıdan:
http://.......... 

---

✅ Sonuç

Bu projede, çoklu doğrusal regresyon kullanılarak tıbbi harcamaların
tahmini başarıyla gerçekleştirilmiş ve model Flask tabanlı bir arayüzle
sunulmuştur. Proje, verilen tüm gereksinimleri eksiksiz şekilde
karşılamaktadır.






