import streamlit as st
import eda
import app

navigation= st.sidebar.selectbox('Pilih Halaman : ', ('Exploratory Data Analysis','Spotify Reviews Sentiments'))

if navigation=='Exploratory Data Analysis':
    eda.run()
else:
    app.run()
