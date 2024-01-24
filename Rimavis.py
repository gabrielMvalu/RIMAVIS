# app.py
import streamlit as st
from streamlit import config as _config

# Asigurați-vă că titlul paginii este setat conform preferințelor dvs.
st.set_page_config(page_title='Aplicația SEAP', page_icon=None, layout='centered', initial_sidebar_state='auto')

# Puteți adăuga un logo și un titlu în bara laterală dacă doriți
st.sidebar.image('./assets/rimavis.PNG', use_column_width=True)
st.sidebar.title('Navigare')

col1, col2, col3 = st.columns(3)
col1.metric("Temperatura", "2 °C", "1.2 °C")
col2.metric("Vant", "3 Kmph", "-8%")
col3.metric("Umiditate", "86%", "4%")

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

st.divider()  # 👈 Draws a horizontal rule

# sectiune lucrari efectuate

tab1, tab2, tab3 = st.tabs(["Teren multisport", "Pensiunea Tania", "Casa"])
with tab1:
   st.header("Teren multisport")
   st.image("https://www.terenuri-sportive.ro/media/k2/items/cache/9b2c4b44fb86522964124ed80d03c5e8_XL.jpg", width=500)
with tab2:
   st.header("Pensiunea")
   st.image("http://blog.hotelguru.ro/wp-content/uploads/2014/08/Zan-Hotel-Voineasa.jpg", width=500)
with tab3:
   st.header("Vila")
   st.image("https://as1.ftcdn.net/v2/jpg/05/69/93/30/1000_F_569933034_MroIMSRUQ4KQxcupear51lsezFlhzd9T.jpg", width=500)

container = st.container(border=True)
container.write(" ")

#Sectiune adaugare 
prompt = st.chat_input("Adauga mesaj/sau valori/comunicari interne")
if prompt:
    st.write(f"User has sent the following prompt: {prompt}")

st.divider()  # 👈 Draws a horizontal rule

st.write("Meniuri comandate")

st.divider()  # 👈 Another horizontal rule
#Sectiune meniuri comandate
st.bar_chart({"meniuri": [1, 5, 2, 6, 2, 1]})
with st.expander(f"{prompt}"):
    st.write("Meniurile comandate luna curenta")
    st.image("https://static.streamlit.io/examples/dice.jpg")




# Restul logicii paginii principale poate fi adăugată aici dacă este necesar
# Sidebar       
#with st.sidebar:
#    st.image("./assets/rimavis.PNG",   use_column_width=True)
