# app.py
import streamlit as st
from streamlit import config as _config

# Asigurați-vă că titlul paginii este setat conform preferințelor dvs.
st.set_page_config(page_title='Aplicația SEAP', page_icon=None, layout='centered', initial_sidebar_state='auto')

# Puteți adăuga un logo și un titlu în bara laterală dacă doriți
st.sidebar.image('./assets/rimavis.PNG', use_column_width=True)
st.sidebar.title('Navigare')


# Logo 
col1, col2, col3 = st.columns([0.25,1,0.25])
col2.image("./assets/rimavis.PNG", use_column_width=True)
new_line(2)


# Restul logicii paginii principale poate fi adăugată aici dacă este necesar
# Sidebar       
with st.sidebar:
    st.image("./assets/rimavis.PNG",   use_column_width=True)
