import streamlit as st
import pandas as pd
import plotly.express as px

# Load in data
loc_df = st.session_state.loc_data

geo_df = loc_df.groupby('settlement').agg({'lat':'mean', 'long':'mean', 'settlement':'count'})
geo_df.rename(columns={'settlement':'num_jobs'}, inplace=True)

states_df = loc_df['state'].value_counts()

map_fig = px.scatter_mapbox(geo_df, lat='lat', lon='long', size='num_jobs', size_max=30,
                        hover_name=geo_df.index, zoom=4.8, mapbox_style='open-street-map'
)
map_fig.update_layout(height=750)

pie_fig = px.pie(states_df, values='count', names=states_df.index)

st.set_page_config(
    page_title='Dashboard - Locations',
    page_icon='📍'
)

st.sidebar.write('Data sourced from Gradcracker and Indeed.')

st.markdown(
    '## Job Locations'
)

st.markdown(
    '### Map'
)

st.plotly_chart(
    map_fig, use_container_width=True
)

st.markdown(
    '### National Breakdown'
)

st.plotly_chart(
    pie_fig, use_container_width=True
)

st.markdown(
    '### Full List of Locations'
)

st.dataframe(
    loc_df['settlement'].value_counts(), use_container_width=True,
    column_config={
        'settlement':'Location',
        'count':'Count'
    }
)