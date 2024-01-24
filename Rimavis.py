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
  
       <h1 class='title'>Lista de lucrari SC Rimavis Invest SRL</h1>
       """, unsafe_allow_html=True)

# sectiune lucrari efectuate

tab1, tab2, tab3 = st.tabs(["Teren multisport", "Pensiunea Tania", "Casa"])
with tab1:
   st.header("Teren multisport")
   st.image("https://static.streamlit.io/examples/cat.jpg", width=200)
with tab2:
   st.header("Pensiunea")
   st.image("https://static.streamlit.io/examples/dog.jpg", width=200)
with tab3:
   st.header("Vila")
   st.image("https://static.streamlit.io/examples/owl.jpg", width=200)

container = st.container(border=True)
container.write("meniuri comandate")

#Sectiune adaugare 
prompt = st.chat_input("Adauga mesaj/sau valori/comunicari interne")
if prompt:
    st.write(f"User has sent the following prompt: {prompt}")
       
#Sectiune meniuri comandate
st.bar_chart({"meniuri": [1, 5, 2, 6, 2, 1]})
with st.expander(prompt):
    st.write("Meniurile comandate luna curenta")
    st.image("https://static.streamlit.io/examples/dice.jpg")




# Restul logicii paginii principale poate fi adăugată aici dacă este necesar
# Sidebar       
#with st.sidebar:
#    st.image("./assets/rimavis.PNG",   use_column_width=True)
