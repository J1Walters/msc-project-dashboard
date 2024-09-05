import streamlit as st
import pandas as pd
from trend_functions.functions import date_list, skill_map, get_plot_df, create_plot

# Load data
year_df = pd.read_csv('./data/yearly_trend.csv')
month_df = pd.read_csv('./data/monthly_trend.csv')
week_df = pd.read_csv('./data/weekly_trend.csv')

st.set_page_config(
    page_title='Dashboard - Trends',
    page_icon='📈',
    layout='wide'
)

# Sidebar
st.sidebar.write('Data sourced from Gradcracker and Indeed.')

st.markdown(
    '## Trends'
)

# Select time period
time_period = st.selectbox('Time Period:', ('Weekly', 'Monthly', 'Yearly'))
date = st.selectbox('Option:', options=date_list(time_period))

# Select skill type
skill_type = st.selectbox('Skill Type:', ('Technologies, Languages and Frameworks', 'Hard Skills', 'Soft Skills'))

# Change number of skills displayed
num_displayed = st.slider('No. of Increasing/Decreasing Skills:', min_value=1, max_value=10, value=5)

# Create plot for weekly
if time_period == 'Weekly':
    skill = skill_map(skill_type)
    df_for_plot = get_plot_df(week_df, skill, date, num_displayed, min_count=5)
    fig = create_plot(df_for_plot, time='Week', skill=skill_type, date=date)
# Create plot for monthly
if time_period == 'Monthly':
    skill = skill_map(skill_type)
    df_for_plot = get_plot_df(month_df, skill, date, num_displayed, min_count=5)
    fig = create_plot(df_for_plot, time='Month', skill=skill_type, date=date)
# Create plot for yearly
if time_period == 'Yearly':
    skill = skill_map(skill_type)
    df_for_plot = get_plot_df(year_df, skill, date, num_displayed, min_count=5)
    fig = create_plot(df_for_plot, time='Year', skill=skill_type, date=date)

# Plot figure
st.plotly_chart(fig, use_container_width=True)
