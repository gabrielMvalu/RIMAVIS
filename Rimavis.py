# app.py
import streamlit as st
from streamlit import config as _config

# Asigurați-vă că titlul paginii este setat conform preferințelor dvs.
st.set_page_config(page_title='Aplicația SEAP', page_icon=None, layout='centered', initial_sidebar_state='auto')

# Puteți adăuga un logo și un titlu în bara laterală dacă doriți
st.sidebar.image('./assets/rimavis.PNG', use_column_width=True)
st.sidebar.title('Navigare')


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
  
       <h1 class='title'>Pregatirea documentatiei 'Ofertant' - licitatii SEAP</h1>
       """, unsafe_allow_html=True)

# Restul logicii paginii principale poate fi adăugată aici dacă este necesar
# Sidebar       
#with st.sidebar:
#    st.image("./assets/rimavis.PNG",   use_column_width=True)
