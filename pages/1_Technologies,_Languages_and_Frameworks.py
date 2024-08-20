import streamlit as st
import pandas as pd
import plotly.express as px

ent_df = st.session_state.ent_data

skill_counts = ent_df.loc[ent_df['type'] == 'LANG_FRAM', 'ent'].value_counts()

fig = px.bar(skill_counts.head(20), x='count',
             labels={
                 'ent':'',
                 'count':'Count'
             }
)
fig.update_layout(yaxis={'categoryorder':'total ascending'}, height=800)

st.set_page_config(
    page_title='Dashboard - Technologies, Languages and Frameworks',
    page_icon='🤖',
    layout='wide'
)

st.markdown(
    '## Technologies, Languages and Frameworks'
)

st.markdown(
    '### Top 20 Skills'
)

st.plotly_chart(
    fig, use_container_width=True
)

st.markdown(
    '### Full List of Skills'
)

st.dataframe(
    data=skill_counts, use_container_width=True,
    column_config={
        'ent':'Skill',
        'count':'Count'
    }
)
