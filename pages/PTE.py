# pages/PTE.py
import streamlit as st
import base64

def run():
    st.title('Plan tehnic de executie')
    st.write('Selectati PTE necesar pentru licitatia in curs.')

    agree = st.checkbox('PROCEDURA TEHNICA DE EXECUTIE \n PRIVIND EXECUTAREA FUNDATIILOR DIRECTE DIN BETON')
    
    if agree:
        st.write('Procedura selectata... pasul urmator -> download document')
        
        # Locația fișierului pe server
        file_path = './assets/Procedura_Tehnica_de_Executie_Fundatii_Directe_Din_Beton.docx'
        
        # Funcția pentru a converti fișierul într-un format descărcabil
        def get_binary_file_downloader_html(bin_file, file_label='File'):
            with open(bin_file, 'rb') as f:
                data = f.read()
            bin_str = base64.b64encode(data).decode()
            href = f'<a href="data:application/octet-stream;base64,{bin_str}" download="{bin_file}">Descarca {file_label}</a>'
            return href

        # Adăugați butonul de descărcare
        st.markdown(get_binary_file_downloader_html(file_path, 'Procedura Tehnica de Executie'), unsafe_allow_html=True)

# Puteți adăuga un logo și un titlu în bara laterală dacă doriți
st.sidebar.image('./assets/rimavis.PNG', use_column_width=True)
st.sidebar.title('Generarea PTE-uri necesare PM')

if __name__ == '__main__':
    run()

