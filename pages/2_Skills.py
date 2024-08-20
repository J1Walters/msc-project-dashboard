import streamlit as st
import pandas as pd
import plotly.express as px

ent_df = st.session_state.ent_data

h_skill_counts = ent_df.loc[ent_df['type'] == 'H_SKILL', 'ent'].value_counts()

h_skill_fig = px.bar(h_skill_counts.head(20), x='count',
             labels={
                 'ent':'',
                 'count':'Count'
             }
)
h_skill_fig.update_layout(yaxis={'categoryorder':'total ascending'}, height=800)

s_skill_counts = ent_df.loc[ent_df['type'] == 'S_SKILL', 'ent'].value_counts()

s_skill_fig = px.bar(s_skill_counts.head(20), x='count',
             labels={
                 'ent':'',
                 'count':'Count'
             }
)
s_skill_fig.update_layout(yaxis={'categoryorder':'total ascending'}, height=800)

st.set_page_config(
    page_title='Dashboard - Skills',
    page_icon='💡',
    layout='wide'
)

st.markdown(
    '## Hard and Soft Skills'
)

st.markdown(
    '### Top 20 Hard Skills'
)

st.plotly_chart(
    h_skill_fig, use_container_width=True
)

st.markdown(
    '### Top 20 Soft Skills'
)

st.plotly_chart(
    s_skill_fig, use_container_width=True
)

st.markdown(
    '### Full List of Hard Skills'
)

st.dataframe(
    data=h_skill_counts, use_container_width=True,
    column_config={
        'ent':'Skill',
        'count':'Count'
    }
)

st.markdown(
    '### Full List of Soft Skills'
)

st.dataframe(
    data=s_skill_counts, use_container_width=True,
    column_config={
        'ent':'Skill',
        'count':'Count'
    }
)
