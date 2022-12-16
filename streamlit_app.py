import pickle 
import pandas as pd
import streamlit as st

#read model
hf_model = pickle.load(open('fp3_model.sav', 'rb'))

#judul web
st.title('Check Heart Failure Prediction')
st.markdown(
    "<p style='text-align: center;'>Made by <b><a href='https://www.linkedin.com/in/rosita-nurul-janatin-561145214/'>'Rosita Nurul Janatin</a></b> , <b><a href='https://www.linkedin.com/in/haikalefendi/'>'Haikal Efendi</a></b> & <b><a href='https://www.linkedin.com/in/ni-made-kirei-kharisma-handayani-90528b21a/'>Ni Made Kirei Kharisma Handayani</a></b></p>",
    unsafe_allow_html=True
)
st.image('https://cdn-cas.orami.co.id/parenting/images/anatomi-jantung_ZjuHsBf.width-800.jpegquality-80.jpg')

#bagi kolom
col1, col2, col3 = st.columns(3)

#form
with col1:
    age = st.text_input('Input nilai Age')
    anaemia = st.text_input('Input nilai Anaemia')
    creatinine_phosphokinase = st.text_input('Input nilai Creatinine Phosphokinase')
    diabetes = st.text_input('Input nilai Diabetes')

with col2:
    ejection_fraction = st.text_input('Input nilai Ejection Fraction')
    high_blood_pressure = st.text_input('Input nilai High Blood Pressure')
    platelets = st.text_input('Input nilai Platelets')
    serum_creatinine = st.text_input('Input nilai Serum Creatinine')

with col3: 
    serum_sodium = st.text_input('Input nilai Serum Sodium')
    sex = st.text_input('Input nilai Sex')
    smoking = st.text_input('Input nilai Smoking')
    time = st.text_input('Input nilai Time')

if anaemia==1: 
    anaemia_0, anaemia_1 = 0, 1
else:
    anaemia_0, anaemia_1 = 1, 0

if diabetes==1: 
    diabetes_0, diabetes_1 = 0, 1
else:
    diabetes_0, diabetes_1 = 1, 0

if high_blood_pressure==1: 
    hbp_0, hbp_1 = 0, 1
else:
    hbp_0, hbp_1 = 1, 0

if sex==1: 
    sex_0, sex_1 = 0, 1
else:
    sex_0, sex_1 = 1, 0

if smoking==1: 
    smoking_0, smoking_1 = 0, 1
else:
    smoking_0, smoking_1 = 1, 0

feature = [[
            age,
            anaemia_0, anaemia_1,
            creatinine_phosphokinase,
            diabetes_0, diabetes_1,
            ejection_fraction,
            hbp_0, hbp_1,
            platelets, 
            serum_creatinine,
            serum_sodium,
            sex_0, sex_1,
            smoking_0, smoking_1,
            time]]
            


new_df = pd.DataFrame(feature, columns=['age', 'creatinine_phosphokinase', 'ejection_fraction', 'platelets',
       'serum_creatinine', 'serum_sodium', 'time', 'anae_0', 'anae_1', 'dia_0',
       'dia_1', 'hbp_0', 'hbp_1', 'sex_0', 'sex_1', 'smoking_0', 'smoking_1'])


#code untuk prediksi
hf_diag = ''

#membuat tombol untuk prediksi
if st.button('Test Prediksi Gagal Jantung'):
    hf_prediction = hf_model.predict(new_df)

    if(hf_prediction[0] == 1):
        hf_diag = 'Pasien terkena gagal jantung'
    else:
        hf_diag = 'Pasien tidak terkena gagal jantung'

    st.success(hf_diag)