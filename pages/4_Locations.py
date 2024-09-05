import streamlit as st
import pandas as pd
import plotly.express as px

# Load data as a session variable
if 'loc_data' not in st.session_state:
    st.session_state.loc_data = pd.read_csv('./data/location.csv')

# Load in data
loc_df = st.session_state.loc_data

# Get dataframe with settlement counts and proportions
loc_counts = loc_df['settlement'].value_counts()
loc_props = loc_df['settlement'].value_counts(normalize=True)
loc_count_props = pd.concat([loc_counts, loc_props], axis=1)

# Get number of unique locations
num_uniq_locs = loc_count_props.shape[0]

# Get number of jobs in multiple locations and remote jobs
num_multi = loc_df.loc[loc_df['location'] == 'Multiple Locations'].shape[0]
num_remote = loc_df.loc[loc_df['location'] == 'Remote'].shape[0]

# Group by settlement and average out any descrepencies in latitude and longitude
geo_df = loc_df.groupby('settlement').agg({'lat':'mean', 'long':'mean', 'settlement':'count'})
geo_df.rename(columns={'settlement':'num_jobs'}, inplace=True)

# Get counts for each nation within UK
states_df = loc_df['state'].value_counts()

# Create map figure
map_fig = px.density_mapbox(geo_df, lat='lat', lon='long', z='num_jobs', opacity=0.9, radius=30,
                        hover_name=geo_df.index, zoom=4.8, mapbox_style='open-street-map', center=dict(lat=54, lon=-2.5),
                        labels={
                            'lat':'Latitude',
                            'long':'Longitude',
                            'num_jobs':'Number of Jobs'
                        }
)
map_fig.update_layout(height=750)

# Create pie chart
pie_fig = px.pie(states_df, values='count', names=states_df.index)

st.set_page_config(
    page_title='Dashboard - Locations',
    page_icon='📍'
)

# Sidebar
st.sidebar.write(f'Number of unique locations: {num_uniq_locs}')
st.sidebar.write('Data sourced from Gradcracker and Indeed.')

st.markdown(
    '## Job Locations'
)

st.markdown(
    '### Map'
)

# Plot map
st.plotly_chart(
    map_fig
)

# Display number of jobs in multiple locations and remote
st.write(f'Number of Jobs in Multiple Locations: {num_multi}')
st.write(f'Number of Remote Jobs: {num_remote}')

st.markdown(
    '### National Breakdown'
)

# Plot pie chart
st.plotly_chart(
    pie_fig, use_container_width=True
)

st.markdown(
    '### Full List of Locations'
)

st.dataframe(
    loc_count_props, use_container_width=True,
    column_config={
        'settlement':'Location',
        'count':'Count',
        'proportion':'Proportion'
    }
)