# app.py
import streamlit as st
from streamlit import config as _config
import streamlit as st
from PIL import Image
import pandas as pd
from io import BytesIO






def main():
    
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Patrick+Hand&display=swap');
        .title {
            color: #7FBBE9; /* A modern shade of blue */
            font-family: 'Comic Sans MS', cursive, sans-serif; /* Comic Sans MS with fallbacks */
            font-size: 30px; /* Adjust the size as needed */
            font-weight: 700; /* 700 is for bold text */
            text-align: center; /* Center align for modern aesthetics */
            margin-bottom: 20px; /* Add some space below the title */
        }
        </style>
    
        <h1 class='title'>Pregatirea datelor in vederea intocmirii documentatiei pentru 'Licitatii SEAP'</h1>
        """, unsafe_allow_html=True)
  
    # Asigurați-vă că titlul paginii este setat conform preferințelor dvs.
    st.set_page_config(page_title='Aplicația SEAP', page_icon=None, layout='centered', initial_sidebar_state='auto')    # Sidebar pentru încărcarea și afișarea logo-ului și textului
  
    st.sidebar.title("Încărcarea Documentelor")
    logo_path = "LogoSTR.PNG"
    try:
        logo = Image.open(logo_path)
        st.sidebar.image(logo, use_column_width=True)
    except IOError:
        st.sidebar.error("Eroare la încărcarea logo-ului.")
    st.sidebar.markdown("<small>© Castemill S.R.L.</small>", unsafe_allow_html=True)


# Puteți adăuga un logo și un titlu în bara laterală dacă doriți
st.sidebar.image('logo.png', use_column_width=True)
st.sidebar.title('Navigare')

# Restul logicii paginii principale poate fi adăugată aici dacă este necesar
