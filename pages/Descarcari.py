import streamlit as st
import pandas as pd
#@st.cache
#def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
 #   return df.to_csv().encode('utf-8')

#csv = convert_df(my_large_df)
data_df = pd.DataFrame(
    {
        "progres": [20, 55, 100, 80],
    }
)

st.data_editor(
    data_df,
    column_config={
        "progres": st.column_config.ProgressColumn(
            "Raport Progres pe activitati procentual",
            help="Progresul lucrarilor aflate in executie",
            format="%d",
            min_value=0,
            max_value=100,
        ),
    },
    hide_index=True,
)

options = st.multiselect(
    'Selectati procerurile de lucru',
    ['PTE 001', 'PTE 002', 'PTE 003', 'PTE 004', 'PTE 005', 'PTE 006'],
    ['PTE 005', 'PTE 006'])

text_contents = '''This is some text'''
st.download_button('Download PTE 00X', text_contents)


# Puteți adăuga un logo și un titlu în bara laterală dacă doriți
st.sidebar.image('./assets/rimavis.PNG', use_column_width=True)
st.sidebar.title('Generarea PTE-uri necesare PM')

