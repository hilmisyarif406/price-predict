import streamlit as st

from pyngrok import ngrok
from joblib import load

trained_model = load('model_regresi.pkl')

form = st.form(key='my-form')

model = form.selectbox('Masukkan Model Mobil: ', options=['GT86', 'Corolla', 'RAV4', 'Yaris', 'Auris', 'Aygo', 'C-HR', 'Prius', 'Avensis', 'Verso', 'Hilux', 'PROACE VERSO', 'Land Cruiser','Supra','Camry','Verso-S','IQ',' Urban Cruiser'])
year = form.slider("Masukkan tahun: ",min_value=1998, max_value=2020)
transmisi = form.selectbox("Masukkan transmisi: ", options=['Manual', 'Automatic', 'Semi-Auto', 'Other'])
mileage = form.number_input("Masukkan Mil: ", format='%d')
fuel = form.selectbox("Masukkan fuel: ", options=['Petrol', 'Other', 'Hybrid', 'Diesel'])
tax = form.number_input("Masukkan Tax: ", format='%d')
mpg = form.number_input("Masukkan Mpg: ")
engine = form.number_input("Masukkan engine: ")

submit = form.form_submit_button("Predict!")

if submit:
    final = trained_model.predict([[
        str(model),
        int(year),
        str(transmisi),
        int(mileage),
        str(fuel),
        int(tax),
        float(mpg),
        float(engine)]])
    st.write("Hasil Predict: ")
    st.write("Harga ", final[0]*100)

ngrok_tunnel = ngrok.connect(8501)
print('Public URL: ', ngrok_tunnel.public_url)
