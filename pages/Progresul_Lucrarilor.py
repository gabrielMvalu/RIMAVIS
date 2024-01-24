import streamlit as st

def run():
    st.title('Progresul lucrarilor in executie')
    st.write('Exemplu lucrare ABC...')

    #Progres lucrare
    
    progress_text = "Operation in progress. Please wait."
    my_bar = st.progress(0, text=progress_text)
    
    for percent_complete in range(1000):
        time.sleep(0.01)
        my_bar.progress(percent_complete + 1, text=progress_text)
    time.sleep(1)
    my_bar.empty()
    
    st.button("Rerun")


# Puteți adăuga un logo și un titlu în bara laterală dacă doriți
st.sidebar.image('./assets/rimavis.PNG', use_column_width=True)
st.sidebar.title('Generarea PTE-uri necesare PM')




if __name__ == '__main__':
    run()
