import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.io as pio

pio.templates.default = 'plotly'

# Load data as a session variable
if 'ent_data' not in st.session_state:
    st.session_state.ent_data = pd.read_csv('./data/multihash_maxout_vec_ents_clean.csv')

# Load in data
ent_df = st.session_state.ent_data
# Get total number of entities
num_ents = ent_df.loc[ent_df['type'] == 'LANG_FRAM'].shape[0]

# Get counts and proportions for each unique entity
skill_counts = ent_df.loc[ent_df['type'] == 'LANG_FRAM', 'new_ent'].value_counts()
skill_props = ent_df.loc[ent_df['type'] == 'LANG_FRAM', 'new_ent'].value_counts(normalize=True)
skill_df = pd.concat([skill_counts, skill_props], axis=1)
# Get number of unique entities
num_uniq_ents = skill_df.shape[0]

# Create figure
fig = px.bar(skill_props.head(20), x='proportion', text_auto=True,
             labels={
                 'new_ent':'',
                 'proportion':'Proportion'
             }
)
fig.update_layout(xaxis={'tickformat':'.2%'}, yaxis={'categoryorder':'total ascending'}, height=800, dragmode=False)

st.set_page_config(
    page_title='Dashboard - Technologies, Languages and Frameworks',
    page_icon='🤖',
    layout='wide'
)

# Sidebar
st.sidebar.write(f'Total number of technologies, languages and frameworks entities: {num_ents}')
st.sidebar.write(f'Number of unique technologies, languages and frameworks entities: {num_uniq_ents}')
st.sidebar.write('Data sourced from Gradcracker and Indeed.')

st.markdown(
    '## Technologies, Languages and Frameworks'
)

st.markdown(
    '### Top 20 Skills'
)

# Display plot
st.plotly_chart(
    fig
)

st.markdown(
    '### Full List of Skills'
)

# Display table
st.dataframe(
    data=skill_df, use_container_width=True,
    column_config={
        'new_ent':'Skill',
        'count':'Count',
        'proportion':'Proportion'
    }
)
