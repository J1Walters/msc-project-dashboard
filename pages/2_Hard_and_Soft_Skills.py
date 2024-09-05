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
# Get total number of entities for each type
num_h_ents = ent_df.loc[ent_df['type'] == 'H_SKILL'].shape[0]
num_s_ents = ent_df.loc[ent_df['type'] == 'S_SKILL'].shape[0]

# Get counts and proportions for each unique entity
h_skill_counts = ent_df.loc[ent_df['type'] == 'H_SKILL', 'new_ent'].value_counts()
h_skill_props = ent_df.loc[ent_df['type'] == 'H_SKILL', 'new_ent'].value_counts(normalize=True)
h_skill_df = pd.concat([h_skill_counts, h_skill_props], axis=1)
# Get number of unique entities
num_uniq_h_ents = h_skill_df.shape[0]

# Create figure
h_skill_fig = px.bar(h_skill_props.head(20), x='proportion', text_auto=True,
             labels={
                 'new_ent':'',
                 'proportion':'Proportion'
             }
)
h_skill_fig.update_layout(xaxis={'tickformat':'.2%'}, yaxis={'categoryorder':'total ascending'}, height=800)

# Get counts and proportions for each unique entity
s_skill_counts = ent_df.loc[ent_df['type'] == 'S_SKILL', 'new_ent'].value_counts()
s_skill_props = ent_df.loc[ent_df['type'] == 'S_SKILL', 'new_ent'].value_counts(normalize=True)
s_skill_df = pd.concat([s_skill_counts, s_skill_props], axis=1)
# Get number of unique entities
num_uniq_s_ents = s_skill_df.shape[0]

# Create figure
s_skill_fig = px.bar(s_skill_props.head(20), x='proportion', text_auto=True,
             labels={
                 'new_ent':'',
                 'proportion':'Proportion'
             }
)
s_skill_fig.update_layout(xaxis={'tickformat':'.2%'}, yaxis={'categoryorder':'total ascending'}, height=800)

st.set_page_config(
    page_title='Dashboard - Skills',
    page_icon='💡',
    layout='wide'
)

# Sidebar
st.sidebar.write(f'Total number of hard skill entities: {num_h_ents}')
st.sidebar.write(f'Number of unique hard skill entities: {num_uniq_h_ents}')
st.sidebar.write(f'Total number of soft skill entities: {num_s_ents}')
st.sidebar.write(f'Number of unique soft skill entities: {num_uniq_s_ents}')
st.sidebar.write('Data sourced from Gradcracker and Indeed.')

st.markdown(
    '## Hard and Soft Skills'
)

st.markdown(
    '### Top 20 Hard Skills'
)

# Display plot
st.plotly_chart(
    h_skill_fig, use_container_width=True
)

st.markdown(
    '### Top 20 Soft Skills'
)

# Display plot
st.plotly_chart(
    s_skill_fig, use_container_width=True
)

st.markdown(
    '### Full List of Hard Skills'
)

# Display table
st.dataframe(
    data=h_skill_df, use_container_width=True,
    column_config={
        'new_ent':'Skill',
        'count':'Count',
        'proportion':'Proportion'
    }
)

st.markdown(
    '### Full List of Soft Skills'
)

# Display table
st.dataframe(
    data=s_skill_df, use_container_width=True,
    column_config={
        'new_ent':'Skill',
        'count':'Count',
        'proportion':'Proportion'
    }
)
