# pages/About.py
import streamlit as st

def run():
    st.title('Plan tehnic de executie')
    st.write('Aceasta este pagina despre aplicația noastră pentru licitații pe SEAP.')

# Puteți adăuga un logo și un titlu în bara laterală dacă doriți
st.sidebar.image('./assets/rimavis.PNG', use_column_width=True)
st.sidebar.title('Generarea PTE-uri necesare PM')

if __name__ == '__main__':
    run()
