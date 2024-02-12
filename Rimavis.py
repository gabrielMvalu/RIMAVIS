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
with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
    
if not openai_api_key:
    st.error("Vă rugăm să introduceți cheia API OpenAI în bara laterală.")
else:
    # Inițializarea clientului OpenAI cu cheia API introdusă
    client = OpenAI(api_key=openai_api_key)

    # Inițializarea stării sesiunii pentru model și mesaje
    if "openai_model" not in st.session_state:
        st.session_state["openai_model"] = "gpt-4-0125-preview"

    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Afișarea mesajelor anterioare
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Input pentru mesaj nou de la utilizator
    if prompt := st.chat_input("Adaugati mesajul aici."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Generarea răspunsului asistentului și afișarea acestuia
        with st.chat_message("assistant"):
            stream = client.chat.completions.create(
                model=st.session_state["openai_model"],
                messages=[
                    {"role": m["role"], "content": m["content"]}
                    for m in st.session_state.messages
                ],
                stream=True,
            )
            response = st.write_stream(stream)
        st.session_state.messages.append({"role": "assistant", "content": response})
