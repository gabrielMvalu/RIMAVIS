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

text_contents = '''This is some text'''
st.download_button('Download text', text_contents)


# Puteți adăuga un logo și un titlu în bara laterală dacă doriți
st.sidebar.image('./assets/rimavis.PNG', use_column_width=True)
st.sidebar.title('Generarea PTE-uri necesare PM')

