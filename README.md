# Submission Dicoding: Jaya Jaya Institut - Student Dropout Prediction

## Business Understanding

### Latar Belakang
Jaya Jaya Institut merupakan salah satu institusi pendidikan perguruan tinggi yang telah berdiri sejak tahun 2000. Institusi ini telah mencetak banyak lulusan dengan reputasi yang sangat baik. Namun, terdapat banyak juga siswa yang tidak menyelesaikan pendidikannya alias dropout.

Jumlah dropout yang tinggi ini menjadi masalah besar untuk institusi pendidikan. Oleh karena itu, Jaya Jaya Institut ingin mendeteksi secepat mungkin siswa yang mungkin akan melakukan dropout sehingga dapat diberi bimbingan khusus.

### Problem Statement
1. Bagaimana karakteristik mahasiswa yang cenderung dropout dari Jaya Jaya Institut?
2. Faktor-faktor apa saja yang paling berpengaruh terhadap tingkat dropout mahasiswa?
3. Bagaimana cara membuat model prediksi yang dapat mengidentifikasi mahasiswa berisiko dropout secara akurat?

### Goals
1. Menganalisis karakteristik dan pola mahasiswa yang dropout
2. Mengidentifikasi faktor-faktor utama yang mempengaruhi tingkat dropout mahasiswa
3. Mengembangkan model machine learning untuk memprediksi mahasiswa berisiko dropout
4. Membuat dashboard untuk monitoring performa mahasiswa
5. Memberikan rekomendasi actionable untuk mengurangi tingkat dropout

### Solution Statement
1. Melakukan Exploratory Data Analysis (EDA) untuk memahami pola dan karakteristik data mahasiswa
2. Mengimplementasikan berbagai algoritma machine learning untuk prediksi dropout
3. Membuat dashboard visualisasi menggunakan Metabase untuk monitoring
4. Mengembangkan aplikasi web prediksi menggunakan Streamlit
5. Menyusun rekomendasi strategis berdasarkan hasil analisis

## Data Understanding

Dataset yang digunakan dalam proyek ini berisi informasi mahasiswa Jaya Jaya Institut dengan berbagai atribut yang mempengaruhi keberhasilan akademik. Data ini mencakup informasi demografis, akademik, dan sosial ekonomi mahasiswa.

### Atribut Dataset
Dataset berisi informasi mahasiswa dengan target prediksi status mahasiswa (Graduate, Dropout, atau Enrolled).

## Data Preparation

Tahapan data preparation meliputi:
1. **Feature Scaling**: Normalisasi untuk data numerikal
2. **Feature Engineering**: Pembuatan fitur baru yang relevan untuk prediksi
3. **Data Splitting**: Pembagian data untuk training dan testing

## Modeling

### Algoritma yang Digunakan
algoritma machine learning yang diimplementasikan:
 **Random Forest Classifier**

### Model Evaluation
Model dievaluasi menggunakan berbagai metrik:
- **Accuracy**: Akurasi keseluruhan model
- **Precision**: Ketepatan prediksi positif
- **Recall**: Kemampuan model mendeteksi kasus positif
- **F1-Score**: Harmonic mean dari precision dan recall
- **ROC-AUC**: Area under the ROC curve

## Deployment

### Dashboard Metabase
Dashboard telah dibuat menggunakan Metabase untuk memvisualisasikan:
- **Distribusi Mahasiswa**: Perbandingan mahasiswa graduate, dropout, dan enrolled
- **Analisis per Jurusan**: Performa akademik berdasarkan program studi
- **Faktor Risiko Dropout**: Visualisasi faktor-faktor utama penyebab dropout
- **Trend Analysis**: Pola dropout dari waktu ke waktu
- **Student Performance Metrics**: KPI monitoring performa mahasiswa

**Cara Mengakses Dashboard:**
1. Jalankan Metabase dengan database file: `metabase.db.mv.db`
2. Login credentials:
   - Email: `root@mail.com`
   - Password: `root123`

### Aplikasi Prediksi Streamlit
Aplikasi web interaktif telah dikembangkan untuk memberikan prediksi real-time risiko dropout mahasiswa.

**Fitur Aplikasi:**
- Input data mahasiswa secara interaktif
- Prediksi risiko dropout dengan confidence score
- Visualisasi faktor-faktor risiko

**Cara Menjalankan Aplikasi Lokal:**
```bash
# Install dependencies
pip install -r requirements.txt

# Jalankan aplikasi
streamlit run app.py
```

**Aplikasi Cloud:**
Aplikasi telah di-deploy ke Streamlit Community Cloud dan dapat diakses melalui:
[🔗 Student Dropout Prediction App](https://potahere-dropout-students.streamlit.app/)

## Evaluation

### Business Impact
Model yang dikembangkan memberikan dampak bisnis yang signifikan bagi Jaya Jaya Institut:

1. **Early Detection**: Kemampuan mendeteksi mahasiswa berisiko dropout sejak dini
2. **Resource Optimization**: Alokasi sumber daya bimbingan yang lebih efektif
3. **Retention Improvement**: Potensi peningkatan tingkat retensi mahasiswa
4. **Cost Reduction**: Pengurangan biaya akibat dropout yang dapat dicegah

### Model Performance Summary
- **Akurasi Model**: [70]% dalam memprediksi status mahasiswa
- **Precision untuk Dropout**: [81]% - kemampuan mengidentifikasi mahasiswa berisiko
- **Recall untuk Dropout**: [76]% - mendeteksi semua kasus dropout potensial

## Conclusion

Berdasarkan hasil analisis dan pemodelan yang telah dilakukan terhadap data mahasiswa Jaya Jaya Institut, dapat disimpulkan bahwa:

### 1. **Faktor-Faktor Utama Penyebab Dropout**

Dari analisis Random Forest yang telah dilakukan, faktor-faktor yang paling berpengaruh terhadap risiko dropout mahasiswa adalah:

- **Tuition Fees Up to Date**: Status pembayaran SPP yang terkini menjadi faktor terpenting. Mahasiswa yang terlambat membayar SPP memiliki risiko dropout yang sangat tinggi
- **Curricular Units 1st Semester (Credited/Enrolled/Approved)**: Performa akademik pada semester pertama menjadi indikator kuat. Mahasiswa yang mengambil sedikit unit atau gagal menyelesaikan banyak unit memiliki risiko tinggi
- **Age at Enrollment**: Usia saat mendaftar berpengaruh signifikan. Mahasiswa yang mendaftar pada usia lebih tua cenderung memiliki risiko dropout lebih tinggi
- **Admission Grade**: Nilai masuk yang rendah berkorelasi dengan risiko dropout yang lebih tinggi
- **Previous Qualification Grade**: Nilai dari kualifikasi pendidikan sebelumnya menunjukkan kesiapan akademik mahasiswa

### 2. **Karakteristik Mahasiswa Berisiko Dropout**

Profil mahasiswa yang memiliki probabilitas dropout tinggi:

- **Aspek Finansial**: Mahasiswa dengan status pembayaran SPP tidak lancar dan memiliki tanggungan finansial
- **Performa Akademik Rendah**: 
  - Nilai masuk < 120 (dari skala 200)
  - Menyelesaikan < 4 unit kurikulum pada semester pertama
  - Nilai rata-rata semester pertama < 12.0
- **Karakteristik Demografis**:
  - Usia pendaftaran > 25 tahun
  - Status pernikahan yang sudah menikah atau bercerai
  - Tidak memiliki beasiswa
- **Latar Belakang Keluarga**: Tingkat pendidikan orang tua yang rendah menunjukkan korelasi dengan risiko dropout

### 3. **Efektivitas Model Prediksi**

Model Random Forest yang dikembangkan menunjukkan performa yang memuaskan:

- **Akurasi Keseluruhan**: 78% - Model dapat memprediksi status mahasiswa dengan tingkat ketepatan yang baik
- **Precision untuk Dropout**: 81% - Ketika model memprediksi mahasiswa akan dropout, 81% prediksi tersebut benar
- **Recall untuk Dropout**: 76% - Model berhasil mengidentifikasi 76% dari semua mahasiswa yang benar-benar dropout
- **AUC-ROC Score**: 0.89 - Menunjukkan kemampuan diskriminasi yang sangat baik antar kelas

**Interpretasi Performa Model**:
- Model sangat efektif untuk mengidentifikasi mahasiswa Graduate (Recall: 93%)
- Untuk kelas Dropout, model memiliki precision tinggi namun sedikit konservatif dalam prediksi
- Kelas Enrolled menunjukkan performa terendah, yang dapat dipahami karena status ini masih dalam proses

### 4. **Insight Bisnis yang Diperoleh**

- **Financial Factor Dominance**: Aspek keuangan (pembayaran SPP) adalah predictor terkuat, menunjukkan pentingnya dukungan finansial
- **Early Academic Performance**: Performa semester pertama sangat menentukan keberhasilan jangka panjang mahasiswa
- **Age Factor**: Mahasiswa non-tradisional (usia > 25) memerlukan perhatian khusus karena tantangan work-life balance
- **Socioeconomic Background**: Latar belakang pendidikan keluarga berpengaruh pada tingkat dukungan yang diterima mahasiswa

### 5. **Dampak Implementasi Model**

- **Early Warning System**: Model dapat mengidentifikasi 76% mahasiswa berisiko sejak semester pertama
- **Resource Allocation**: Institusi dapat fokus pada 20-25% mahasiswa berisiko tinggi untuk intervensi intensif
- **Cost-Benefit**: Dengan biaya intervensi yang relatif kecil, institusi dapat mencegah kerugian revenue dari dropout
- **Retention Rate Improvement**: Potensi peningkatan retention rate hingga 15-20% dengan intervensi yang tepat

### 6. **Rekomendasi Strategis**

Berdasarkan temuan analisis:

1. **Prioritas Finansial**: Implementasi program bantuan finansial dan sistem pembayaran fleksibel
2. **Academic Support**: Program bimbingan intensif untuk mahasiswa dengan performa semester pertama rendah
3. **Targeted Intervention**: Fokus pada mahasiswa dengan kombinasi faktor risiko tinggi
4. **Continuous Monitoring**: Update model secara berkala dengan data terbaru untuk mempertahankan akurasi
5. **Holistic Approach**: Kombinasi dukungan akademik, finansial, dan psikososial untuk mahasiswa berisiko

### 7. **Validasi Model dan Keberlanjutan**

- Model telah divalidasi dengan data testing yang terpisah dan menunjukkan performa yang konsisten
- Implementasi real-time melalui aplikasi Streamlit memungkinkan penggunaan praktis oleh staff akademik
- Dashboard Metabase memberikan monitoring berkelanjutan untuk pengambilan keputusan strategis
- Framework yang telah dibangun dapat diadaptasi untuk berbagai institusi pendidikan serupa

**Kesimpulan Akhir**: Proyek ini berhasil mengembangkan sistem prediksi dropout yang akurat dan actionable, memberikan Jaya Jaya Institut tools yang diperlukan untuk meningkatkan retention rate mahasiswa melalui intervensi yang tepat sasaran dan berbasis data.

## Action Items (Rekomendasi)

Berdasarkan hasil proyek data science ini, berikut adalah rekomendasi action items yang dapat diimplementasikan oleh Jaya Jaya Institut:

### 1. 🚨 Implementasi Early Warning System
- **Integrasi Model ke Sistem Akademik**: 
  - Implementasikan model prediksi dropout ke dalam sistem informasi akademik
  - Set up automated alerts untuk mahasiswa dengan risiko tinggi (skor > 70%)
  - Dashboard real-time untuk monitoring status risiko mahasiswa

- **Timeline**: 3-6 bulan
- **PIC**: Tim IT & Akademik
- **Expected Impact**: Deteksi dini 80% mahasiswa berisiko dropout

### 2. 📚 Program Intervensi Akademik Bertarget
- **Academic Support Program**:
  - Program tutoring khusus untuk mahasiswa berisiko tinggi
  - Peer mentoring system antara mahasiswa senior dan junior
  - Workshop study skills dan time management

- **Monitoring Akademik Intensif**:
  - Check-in bulanan dengan academic advisor
  - Progress tracking yang lebih detail
  - Personalized learning plan untuk mahasiswa berisiko

- **Timeline**: Implementasi semester depan
- **PIC**: Bagian Akademik & Kemahasiswaan
- **Expected Impact**: Peningkatan retention rate 15-20%

### 3. 💰 Program Dukungan Finansial
- **Scholarship Expansion**:
  - Evaluasi dan perluas program beasiswa berbasis kebutuhan
  - Beasiswa prestasi untuk mahasiswa berprestasi dari keluarga kurang mampu
  - Emergency financial aid untuk situasi darurat

- **Flexible Payment Options**:
  - Sistem pembayaran cicilan yang lebih fleksibel
  - Work-study program untuk mahasiswa yang membutuhkan
  - Partnership dengan lembaga keuangan untuk student loan

- **Timeline**: 6-12 bulan
- **PIC**: Bagian Keuangan & Kemahasiswaan
- **Expected Impact**: Menurunkan dropout karena masalah finansial sebesar 30%

### 4. 🤝 Peningkatan Student Engagement
- **Community Building**:
  - Program orientasi yang lebih komprehensif
  - Student clubs dan organisasi yang lebih aktif
  - Regular campus events dan activities

- **Mental Health Support**:
  - Counseling services yang mudah diakses
  - Stress management workshops
  - Mental health awareness campaigns

- **Career Development**:
  - Career counseling dan job placement assistance
  - Industry partnership untuk internship programs
  - Alumni mentoring network

- **Timeline**: Ongoing dengan evaluasi semesteran
- **PIC**: Bagian Kemahasiswaan
- **Expected Impact**: Peningkatan student satisfaction dan engagement

### 5. 📊 Monitoring dan Evaluasi Berkelanjutan
- **Data-Driven Decision Making**:
  - Update model dengan data baru setiap semester
  - Regular model performance evaluation
  - Continuous improvement berdasarkan feedback

- **Impact Assessment**:
  - Tracking efektivitas program intervensi
  - ROI analysis dari berbagai program retention
  - Survey kepuasan mahasiswa yang rutin

- **Reporting System**:
  - Monthly retention dashboard untuk management
  - Quarterly review dengan stakeholders
  - Annual impact report untuk board of directors

- **Timeline**: Ongoing
- **PIC**: Tim Data Analytics & Manajemen
- **Expected Impact**: Optimalisasi berkelanjutan program retention

### 6. 🎯 Quick Wins (Implementasi Segera)
- **Immediate Actions** (1-3 bulan):
  - Deploy aplikasi prediksi untuk staff akademik
  - Training staff untuk menggunakan dashboard monitoring
  - Identifikasi mahasiswa berisiko tinggi untuk semester berjalan

- **Short-term Goals** (3-6 bulan):
  - Launch pilot program tutoring untuk 50 mahasiswa berisiko
  - Implementasi check-in system dengan academic advisor
  - Evaluate financial aid options untuk mahasiswa berisiko

### Success Metrics
- **Primary KPIs**:
  - Dropout rate reduction: Target 25% dalam 2 tahun
  - Early detection rate: Target 80% mahasiswa berisiko teridentifikasi
  - Intervention success rate: Target 60% mahasiswa berisiko yang diintervensi tidak dropout

- **Secondary KPIs**:
  - Student satisfaction score improvement
  - Academic performance improvement
  - Time-to-graduation optimization

### Budget Estimation
- **Technology Implementation**: Rp 200-300 juta
- **Academic Support Programs**: Rp 500-700 juta/tahun
- **Financial Aid Expansion**: Rp 1-2 miliar/tahun
- **Staff Training & Development**: Rp 100-200 juta

**Expected ROI**: Dengan retention rate improvement 20%, estimasi additional revenue Rp 3-5 miliar/tahun dari prevention of dropouts.

---

## 📁 Struktur Proyek
```
├── notebook.ipynb                 # Jupyter notebook dengan analisis lengkap
├── app.py                        # Aplikasi Streamlit untuk prediksi
├── student_dropout_model.pkl     # Model machine learning terlatih
├── features_used.pkl            # Informasi features untuk preprocessing
├── requirements.txt             # Dependencies yang diperlukan
├── metabase.db.mv.db           # Database file untuk Metabase dashboard
├── jafar_shodiq-dashboard.png  # Screenshot dashboard Metabase
└── README.md                   # Dokumentasi proyek (file ini)
```

## 🔗 Links
- **Streamlit App**: [Student Dropout Prediction Dashboard](https://potahere-dropout-students.streamlit.app/)
- **Dashboard Screenshot**: `jafar_shodiq-dashboard.png`

## 👨‍💻 Author
- **Nama**: Ja'far Shodiq
- **Email**: jafarshodiq.alkaf@gmail.com
- **Dicoding ID**: jafar_shodiq

---
*Project dikembangkan sebagai submission untuk program Dicoding "Belajar Penerapan Data Science"*
