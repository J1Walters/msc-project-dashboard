import streamlit as st
import pandas as pd

# Load data as a session variable
if 'loc_data' not in st.session_state:
    st.session_state.loc_data = pd.read_csv('./data/location.csv')
if 'ent_data' not in st.session_state:
    st.session_state.ent_data = pd.read_csv('./data/entities.csv')

st.set_page_config(
    page_title='Dashboard - Home',
    page_icon='🏠'
)

st.sidebar.success('Please select a page from above.')

st.title('Analysing the UK Tech Job Market Using Natural Language Processing')
st.markdown(
    'Welcome to the job insights dashboard. Please select a page from the sidebar.'
)
