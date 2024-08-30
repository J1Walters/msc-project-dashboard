import streamlit as st
import pandas as pd
import plotly.express as px

# Load in data
ent_df = st.session_state.ent_data
# Get total number of entities
num_ents = ent_df.loc[ent_df['type'] == 'REQUIREMENT'].shape[0]

# Get counts and proportions for each unique entity
skill_counts = ent_df.loc[ent_df['type'] == 'REQUIREMENT', 'new_ent'].value_counts()
skill_props = ent_df.loc[ent_df['type'] == 'REQUIREMENT', 'new_ent'].value_counts(normalize=True)
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
fig.update_layout(xaxis={'tickformat':'.2%'}, yaxis={'categoryorder':'total ascending'}, height=800)

st.set_page_config(
    page_title='Dashboard - Education',
    page_icon='🎓',
    layout='wide'
)

# Sidebar
st.sidebar.write('Data sourced from Gradcracker and Indeed.')
st.sidebar.write(f'Total number of requirement entities: {num_ents}')
st.sidebar.write(f'Number of unique requirement entities: {num_uniq_ents}')

st.markdown(
    '## Education/Requirements'
)

st.markdown(
    '### Top 20'
)

# Display plot
st.plotly_chart(
    fig, use_container_width=True
)

st.markdown(
    '### Full List of Requirements'
)

# Display table
st.dataframe(
    data=skill_df, use_container_width=True,
    column_config={
        'new_ent':'Requirement',
        'count':'Count',
        'proportion':'Proportion'
    }
)
