import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
year_df = pd.read_csv('./data/yearly_trend.csv')
month_df = pd.read_csv('./data/monthly_trend.csv')
week_df = pd.read_csv('./data/weekly_trend.csv')

# Define functions
def get_top_increase(df, skill, num=5, min_count=5):
    """Get the specified number of the top increasing skills"""
    filtered_df = df.loc[df['type'] == skill]
    top_increase = (filtered_df.loc[(filtered_df['perc_change'] > 0) & (filtered_df['count'] > min_count)]
                    .sort_values(by='perc_change', ascending=False)
                    .head(num)
    )
    return top_increase

def get_top_decrease(df, skill, num=5, min_count=5):
    """Get the specified number of the top decreasing skills"""
    filtered_df = df.loc[df['type'] == skill]
    top_decrease = (filtered_df.loc[(filtered_df['perc_change'] < 0) & (filtered_df['count'] > min_count)]
                    .sort_values(by='perc_change', ascending=True)
                    .head(num)
    )
    return top_decrease

def create_plot(df):
    pass

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