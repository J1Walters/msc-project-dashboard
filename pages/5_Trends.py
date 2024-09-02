import streamlit as st
import pandas as pd
import plotly.express as px

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

# Select time period
time_period = st.selectbox('Time Period:', ('Weekly', 'Monthly', 'Yearly'))

# Plot for weekly
if time_period == 'Weekly':
    st.write('Week')
# Plot for monthly
if time_period == 'Monthly':
    st.write('Month')
# Plot for yearly
if time_period == 'Yearly':
    st.write('Year')