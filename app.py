import streamlit as st
import pandas as pd
import numpy as np
import joblib
import pickle
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns

# Konfigurasi halaman
st.set_page_config(
    page_title="Student Dropout Prediction Dashboard",
    page_icon="🎓",
    layout="wide"
)

# Load model dan features
@st.cache_resource
def load_model_and_features():
    try:
        model = joblib.load('student_dropout_model.pkl')
        with open('features_used.pkl', 'rb') as f:
            features = pickle.load(f)
        return model, features
    except FileNotFoundError:
        st.error("Model atau file features tidak ditemukan. Pastikan file 'student_dropout_model.pkl' dan 'features_used.pkl' ada di direktori yang sama.")
        return None, None

# Load model dan features
model, feature_columns = load_model_and_features()

# Sidebar untuk panduan penggunaan
st.sidebar.title("📋 Panduan Penggunaan Dashboard")
st.sidebar.markdown("""
### 🎯 Tujuan Dashboard
Dashboard ini membantu memprediksi risiko dropout mahasiswa berdasarkan berbagai faktor akademik dan sosio-ekonomi.

### 📊 Cara Menggunakan:

#### 1️⃣ Prediksi Individual
- Masukkan data mahasiswa pada form di tab "Prediksi Individual"
- Klik tombol "Prediksi" untuk melihat hasil
- Hasil menampilkan probabilitas dan status prediksi

#### 2️⃣ Prediksi Batch (File CSV)
- Siapkan file CSV dengan kolom yang sesuai
- Upload file pada tab "Prediksi Batch"
- Download hasil prediksi dalam format CSV

### 📝 Format Data yang Diperlukan:
- **Marital_status**: 1-6 (1=Single, 2=Married, dll)
- **Application_mode**: Kode metode aplikasi
- **Application_order**: 0-9 (0=pilihan pertama)
- **Course**: Kode program studi
- **Daytime_evening_attendance**: 1=Siang, 0=Malam
- **Previous_qualification**: Kode kualifikasi sebelumnya
- **Previous_qualification_grade**: 0-200
- **Nationality**: Kode kebangsaan
- **Mothers_qualification**: Kode pendidikan ibu
- **Fathers_qualification**: Kode pendidikan ayah
- **Mothers_occupation**: Kode pekerjaan ibu
- **Fathers_occupation**: Kode pekerjaan ayah
- **Admission_grade**: 0-200
- **Displaced**: 1=Ya, 0=Tidak
- **Educational_special_needs**: 1=Ya, 0=Tidak
- **Debtor**: 1=Ya, 0=Tidak
- **Tuition_fees_up_to_date**: 1=Ya, 0=Tidak
- **Gender**: 1=Laki-laki, 0=Perempuan
- **Scholarship_holder**: 1=Ya, 0=Tidak
- **Age_at_enrollment**: Umur saat mendaftar
- **International**: 1=Ya, 0=Tidak
- **Curricular_units_***: Nilai unit kurikulum
- **Unemployment_rate**: Tingkat pengangguran (%)
- **Inflation_rate**: Tingkat inflasi (%)
- **GDP**: GDP per kapita

### ⚠️ Catatan Penting:
- Pastikan semua field diisi dengan benar
- Nilai numerik harus dalam rentang yang valid
- Status prediksi: 0=Dropout, 1=Graduate, 2=Enrolled
""")

# Main title
st.title("🎓 Student Dropout Prediction Dashboard")
st.markdown("Dashboard untuk memprediksi risiko dropout mahasiswa berdasarkan data akademik dan sosio-ekonomi")

if model is None or feature_columns is None:
    st.stop()

# Tabs untuk berbagai fungsi
tab1, tab2, tab3 = st.tabs(["🔍 Prediksi Individual", "📄 Prediksi Batch", "📊 Analisis Data"])

# Tab 1: Prediksi Individual
with tab1:
    st.header("Prediksi Individual")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("Data Demografis")
        marital_status = st.selectbox("Status Pernikahan", 
                                    options=[1,2,3,4,5,6],
                                    format_func=lambda x: {1:"Single", 2:"Married", 3:"Widower", 4:"Divorced", 5:"De facto union", 6:"Legally separated"}[x])
        
        gender = st.selectbox("Jenis Kelamin", options=[0,1], format_func=lambda x: "Perempuan" if x==0 else "Laki-laki")
        age_at_enrollment = st.number_input("Umur saat Mendaftar", min_value=16, max_value=70, value=20)
        nationality = st.number_input("Kode Kebangsaan", min_value=1, max_value=100, value=1)
        international = st.selectbox("Mahasiswa Internasional", options=[0,1], format_func=lambda x: "Tidak" if x==0 else "Ya")
        displaced = st.selectbox("Pindahan dari Keluarga", options=[0,1], format_func=lambda x: "Tidak" if x==0 else "Ya")
    
    with col2:
        st.subheader("Data Akademik")
        course = st.number_input("Kode Program Studi", min_value=1, max_value=10000, value=33)
        application_mode = st.number_input("Mode Aplikasi", min_value=1, max_value=50, value=1)
        application_order = st.number_input("Urutan Aplikasi", min_value=0, max_value=9, value=0)
        daytime_evening = st.selectbox("Waktu Kuliah", options=[0,1], format_func=lambda x: "Malam" if x==0 else "Siang")
        previous_qualification = st.number_input("Kualifikasi Sebelumnya", min_value=1, max_value=50, value=1)
        previous_qualification_grade = st.number_input("Nilai Kualifikasi Sebelumnya", min_value=0.0, max_value=200.0, value=120.0)
        admission_grade = st.number_input("Nilai Masuk", min_value=0.0, max_value=200.0, value=120.0)
    
    with col3:
        st.subheader("Data Keluarga & Ekonomi")
        mothers_qualification = st.number_input("Kualifikasi Ibu", min_value=1, max_value=50, value=1)
        fathers_qualification = st.number_input("Kualifikasi Ayah", min_value=1, max_value=50, value=1)
        mothers_occupation = st.number_input("Pekerjaan Ibu", min_value=0, max_value=200, value=1)
        fathers_occupation = st.number_input("Pekerjaan Ayah", min_value=0, max_value=200, value=1)
        
        educational_special_needs = st.selectbox("Kebutuhan Khusus Pendidikan", options=[0,1], format_func=lambda x: "Tidak" if x==0 else "Ya")
        debtor = st.selectbox("Status Debitur", options=[0,1], format_func=lambda x: "Tidak" if x==0 else "Ya")
        tuition_fees_up_to_date = st.selectbox("SPP Terkini", options=[0,1], format_func=lambda x: "Tidak" if x==0 else "Ya")
        scholarship_holder = st.selectbox("Penerima Beasiswa", options=[0,1], format_func=lambda x: "Tidak" if x==0 else "Ya")
    
    # Data tambahan
    st.subheader("Data Ekonomi & Kurikulum")
    col4, col5 = st.columns(2)
    
    with col4:
        unemployment_rate = st.number_input("Tingkat Pengangguran (%)", min_value=0.0, max_value=50.0, value=10.0)
        inflation_rate = st.number_input("Tingkat Inflasi (%)", min_value=-10.0, max_value=20.0, value=2.0)
        gdp = st.number_input("GDP per Kapita", min_value=0.0, max_value=100000.0, value=25000.0)
    
    with col5:
        # Simplified curricular units inputs
        curricular_1st_sem_credited = st.number_input("Unit Kurikulum Sem 1 (Credited)", min_value=0, max_value=30, value=0)
        curricular_1st_sem_enrolled = st.number_input("Unit Kurikulum Sem 1 (Enrolled)", min_value=0, max_value=30, value=6)
        curricular_1st_sem_evaluations = st.number_input("Evaluasi Sem 1", min_value=0, max_value=30, value=6)
        curricular_1st_sem_approved = st.number_input("Unit Disetujui Sem 1", min_value=0, max_value=30, value=6)
        curricular_1st_sem_grade = st.number_input("Nilai Sem 1", min_value=0.0, max_value=20.0, value=13.0)
    
    # Button untuk prediksi
    if st.button("🔮 Prediksi Status Mahasiswa", type="primary"):
        # Prepare input data dengan semua fitur yang diperlukan
        input_data = {
            'Marital_status': marital_status,
            'Application_mode': application_mode,
            'Application_order': application_order,
            'Course': course,
            'Daytime_evening_attendance': daytime_evening,
            'Previous_qualification': previous_qualification,
            'Previous_qualification_grade': previous_qualification_grade,
            'Nationality': nationality,
            'Mothers_qualification': mothers_qualification,
            'Fathers_qualification': fathers_qualification,
            'Mothers_occupation': mothers_occupation,
            'Fathers_occupation': fathers_occupation,
            'Admission_grade': admission_grade,
            'Displaced': displaced,
            'Educational_special_needs': educational_special_needs,
            'Debtor': debtor,
            'Tuition_fees_up_to_date': tuition_fees_up_to_date,
            'Gender': gender,
            'Scholarship_holder': scholarship_holder,
            'Age_at_enrollment': age_at_enrollment,
            'International': international,
            'Curricular_units_1st_sem_credited': curricular_1st_sem_credited,
            'Curricular_units_1st_sem_enrolled': curricular_1st_sem_enrolled,
            'Curricular_units_1st_sem_evaluations': curricular_1st_sem_evaluations,
            'Curricular_units_1st_sem_approved': curricular_1st_sem_approved,
            'Curricular_units_1st_sem_grade': curricular_1st_sem_grade,
            'Curricular_units_2nd_sem_credited': 0,
            'Curricular_units_2nd_sem_enrolled': 0,
            'Curricular_units_2nd_sem_evaluations': 0,
            'Curricular_units_2nd_sem_approved': 0,
            'Curricular_units_2nd_sem_grade': 0,
            'Unemployment_rate': unemployment_rate,
            'Inflation_rate': inflation_rate,
            'GDP': gdp
        }
        
        # Tambahkan fitur yang di-engineer
        input_data['Parents_education_diff'] = abs(mothers_qualification - fathers_qualification)
        input_data['Financial_burden'] = debtor + tuition_fees_up_to_date
        input_data['Academic_background'] = (previous_qualification_grade + admission_grade) / 2
        
        try:
            # Convert to DataFrame
            input_df = pd.DataFrame([input_data])
            
            # Pastikan urutan kolom sesuai dengan yang digunakan saat training
            input_df = input_df.reindex(columns=feature_columns, fill_value=0)
            
            # Prediksi
            prediction = model.predict(input_df)[0]
            prediction_proba = model.predict_proba(input_df)[0]
            
            # DEBUG: Tampilkan nilai prediction untuk debugging
            st.write(f"DEBUG - Prediction value: {prediction}, Type: {type(prediction)}")
            
            # Display results
            st.success("Prediksi berhasil!")
            
            col_result1, col_result2 = st.columns(2)
            
            with col_result1:
                # Mapping untuk string prediction ke color
                color_map = {
                    "Dropout": "🔴",
                    "Graduate": "🟢", 
                    "Enrolled": "🟡"
                }
                
                # Validasi bahwa prediction ada dalam mapping
                if prediction in color_map:
                    st.metric(
                        label="Status Prediksi",
                        value=f"{color_map[prediction]} {prediction}"
                    )
                else:
                    st.error(f"Nilai prediksi tidak valid: {prediction}")
                    st.metric(
                        label="Status Prediksi",
                        value="❓ Unknown"
                    )
            
            with col_result2:
                max_proba = max(prediction_proba)
                st.metric(
                    label="Tingkat Keyakinan",
                    value=f"{max_proba:.2%}"
                )
            
            # Visualisasi probabilitas
            st.subheader("Distribusi Probabilitas")
            
            # Dapatkan class labels dari model
            try:
                class_labels = model.classes_
            except:
                class_labels = ['Dropout', 'Graduate', 'Enrolled']
            
            prob_df = pd.DataFrame({
                'Status': class_labels,
                'Probabilitas': prediction_proba
            })
            
            fig, ax = plt.subplots(figsize=(10, 4))
            colors = ['red' if status == 'Dropout' else 'green' if status == 'Graduate' else 'orange' 
                        for status in class_labels]
            
            bars = ax.bar(prob_df['Status'], prob_df['Probabilitas'], 
                            color=colors, alpha=0.7)
            ax.set_ylabel('Probabilitas')
            ax.set_title('Probabilitas Prediksi untuk Setiap Status')
            ax.set_ylim(0, 1)
            
            # Tambahkan nilai di atas bar
            for bar, prob in zip(bars, prediction_proba):
                ax.text(bar.get_x() + bar.get_width()/2., bar.get_height() + 0.01,
                        f'{prob:.3f}', ha='center', va='bottom')
            
            st.pyplot(fig)
            
        except Exception as e:
            st.error(f"Error dalam prediksi: {str(e)}")
            st.info("Terjadi kesalahan saat melakukan prediksi. Pastikan semua input valid.")
            # Tambahkan info debug untuk troubleshooting
            st.write("Debug info:")
            st.write(f"Feature columns length: {len(feature_columns) if feature_columns else 'None'}")
            st.write(f"Input data keys: {list(input_data.keys()) if 'input_data' in locals() else 'None'}")

# Tab 2: Prediksi Batch
with tab2:
    st.header("Prediksi Batch dari File CSV")
    
    # Template download
    st.subheader("📥 Download Template")
    if st.button("Download Template CSV"):
        # Create sample template
        template_data = {col: [0] for col in feature_columns}
        template_df = pd.DataFrame(template_data)
        csv = template_df.to_csv(index=False)
        st.download_button(
            label="Download Template",
            data=csv,
            file_name="student_data_template.csv",
            mime="text/csv"
        )
    
    st.subheader("📤 Upload File untuk Prediksi")
    uploaded_file = st.file_uploader("Pilih file CSV", type=['csv'])
    
    if uploaded_file is not None:
        try:
            # Read uploaded file
            df_upload = pd.read_csv(uploaded_file)
            
            st.subheader("Preview Data")
            st.dataframe(df_upload.head())
            
            # Check if all required columns exist
            missing_cols = set(feature_columns) - set(df_upload.columns)
            if missing_cols:
                st.error(f"Kolom yang hilang: {missing_cols}")
                st.info("Pastikan file CSV Anda memiliki semua kolom yang diperlukan. Download template untuk referensi.")
            else:
                if st.button("🚀 Jalankan Prediksi Batch", type="primary"):
                    # Ensure column order matches training data
                    df_upload_ordered = df_upload.reindex(columns=feature_columns, fill_value=0)
                    
                    # Make predictions
                    predictions = model.predict(df_upload_ordered)
                    predictions_proba = model.predict_proba(df_upload_ordered)
                    
                    # Add results to dataframe
                    df_results = df_upload.copy()
                    df_results['Predicted_Status'] = predictions
                    
                    # Tidak perlu mapping karena predictions sudah string
                    df_results['Predicted_Status_Label'] = predictions
                    
                    # Ambil class labels dari model
                    try:
                        class_labels = model.classes_
                        # Buat kolom probabilitas berdasarkan class labels
                        for i, label in enumerate(class_labels):
                            df_results[f'{label}_Probability'] = predictions_proba[:, i]
                    except:
                        # Fallback jika model tidak memiliki classes_
                        df_results['Dropout_Probability'] = predictions_proba[:, 0]
                        df_results['Graduate_Probability'] = predictions_proba[:, 1] if predictions_proba.shape[1] > 1 else 0
                        df_results['Enrolled_Probability'] = predictions_proba[:, 2] if predictions_proba.shape[1] > 2 else 0
                    
                    df_results['Confidence'] = predictions_proba.max(axis=1)
                    
                    st.success(f"Prediksi selesai untuk {len(df_results)} mahasiswa!")
                    
                    # Show summary
                    st.subheader("📊 Ringkasan Hasil")
                    col1, col2, col3 = st.columns(3)
                    
                    with col1:
                        dropout_count = (predictions == 'Dropout').sum()
                        st.metric("Prediksi Dropout", dropout_count, f"{dropout_count/len(predictions):.1%}")
                    
                    with col2:
                        graduate_count = (predictions == 'Graduate').sum()
                        st.metric("Prediksi Graduate", graduate_count, f"{graduate_count/len(predictions):.1%}")
                    
                    with col3:
                        enrolled_count = (predictions == 'Enrolled').sum()
                        st.metric("Prediksi Enrolled", enrolled_count, f"{enrolled_count/len(predictions):.1%}")
                    
                    # Show detailed results
                    st.subheader("📋 Hasil Detail")
                    st.dataframe(df_results)
                    
                    # Download results
                    csv_results = df_results.to_csv(index=False)
                    st.download_button(
                        label="📥 Download Hasil Prediksi",
                        data=csv_results,
                        file_name="student_predictions_results.csv",
                        mime="text/csv"
                    )
                    
        except Exception as e:
            st.error(f"Error membaca file: {str(e)}")
            st.info("Pastikan file CSV Anda memiliki format yang benar.")

# Tab 3: Analisis Data
with tab3:
    st.header("📊 Analisis Feature Importance")
    
    if hasattr(model, 'feature_importances_'):
        # Get feature importance
        importance_df = pd.DataFrame({
            'Feature': feature_columns,
            'Importance': model.feature_importances_
        }).sort_values('Importance', ascending=False)
        
        # Plot top 15 features
        fig, ax = plt.subplots(figsize=(12, 8))
        top_features = importance_df.head(15)
        sns.barplot(data=top_features, x='Importance', y='Feature', ax=ax)
        ax.set_title('Top 15 Feature Importance')
        ax.set_xlabel('Importance Score')
        
        st.pyplot(fig)
        
        st.subheader("📋 Tabel Feature Importance")
        st.dataframe(importance_df)
        
        # Download feature importance
        csv_importance = importance_df.to_csv(index=False)
        st.download_button(
            label="📥 Download Feature Importance",
            data=csv_importance,
            file_name="feature_importance.csv",
            mime="text/csv"
        )
    else:
        st.info("Model tidak mendukung feature importance analysis.")

# Footer
st.markdown("---")
st.markdown("🎓 **Student Dropout Prediction Dashboard** | Developed for Educational Institution Analysis")