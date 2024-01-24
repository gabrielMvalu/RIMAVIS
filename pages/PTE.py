# pages/About.py
import streamlit as st

def run():
    st.title('Plan tehnic de executie')
    st.write('Selectati PTE nececsar pentru licitatia in curs.')

    agree = st.checkbox('I agree')
    
    if agree:
        st.write('Great!')


st.bar_chart({"data": [1, 5, 2, 6, 2, 1]})

with st.expander("See explanation"):
    st.write("Meniurile comandate luna curenta")
    st.image("https://static.streamlit.io/examples/dice.jpg")



# Puteți adăuga un logo și un titlu în bara laterală dacă doriți
st.sidebar.image('./assets/rimavis.PNG', use_column_width=True)
st.sidebar.title('Generarea PTE-uri necesare PM')




if __name__ == '__main__':
    run()
