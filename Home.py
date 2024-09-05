import streamlit as st
import pandas as pd

# Load data as a session variable
if 'loc_data' not in st.session_state:
    st.session_state.loc_data = pd.read_csv('./data/location.csv')
if 'ent_data' not in st.session_state:
    st.session_state.ent_data = pd.read_csv('./data/multihash_maxout_vec_ents_clean.csv')

# Load data
loc_df = st.session_state.loc_data
# Get total number of job listings in dataset
num_jobs = loc_df.shape[0]

st.set_page_config(
    page_title='Dashboard - Home',
    page_icon='🏠'
)

# Sidebar
st.sidebar.success('Please select a page from above.')
st.sidebar.write(f'Total number of jobs: {num_jobs}')
st.sidebar.write('Data sourced from Gradcracker and Indeed.')

st.title('📊 Analysing the UK Tech Job Market Using Natural Language Processing')
st.markdown(
    'Welcome to the job insights dashboard.'
)
st.markdown(
    '''
    The dashboard consists of the following pages, which are all accessible from the side bar on the left hand side:
    - Technologies, Languages and Frameworks
    - Hard and Soft Skills
    - Education
    - Locations
    - Trends
    
    The side bar can be accessed on mobile via the arrow in the top left corner.
    Please note that display issues may occur on mobile devices.
    '''
)