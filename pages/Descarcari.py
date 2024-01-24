import streamlit as st


#@st.cache
#def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
 #   return df.to_csv().encode('utf-8')

#csv = convert_df(my_large_df)

#st.download_button(
#    label="Download data as CSV",
#    data=csv,
#    file_name='large_df.csv',
#    mime='text/csv',
#)

data_df = pd.DataFrame(
    {
        "progres": [20, 55, 100, 80],
    }
)

st.data_editor(
    data_df,
    column_config={
        "progres": st.column_config.ProgressColumn(
            "Raport Progres pe activitati %",
            help="Progresul lucrarilor aflate in executie",
            format="f'%'",
            min_value=0,
            max_value=100,
        ),
    },
    hide_index=True,
)


text_contents = '''This is some text'''
st.download_button('Download text', text_contents)


# Puteți adăuga un logo și un titlu în bara laterală dacă doriți
st.sidebar.image('./assets/rimavis.PNG', use_column_width=True)
st.sidebar.title('Generarea PTE-uri necesare PM')

