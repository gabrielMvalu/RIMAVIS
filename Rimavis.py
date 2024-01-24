# app.py
import streamlit as st
from streamlit import config as _config

# Asigurați-vă că titlul paginii este setat conform preferințelor dvs.
st.set_page_config(page_title='Aplicația SEAP', page_icon=None, layout='centered', initial_sidebar_state='auto')

# Puteți adăuga un logo și un titlu în bara laterală dacă doriți
st.sidebar.image('logo.png', use_column_width=True)
st.sidebar.title('Navigare')

# Restul logicii paginii principale poate fi adăugată aici dacă este necesar
# Sidebar       
with st.sidebar:
    st.image("./assets/Rimavis.png",   use_column_width=True)