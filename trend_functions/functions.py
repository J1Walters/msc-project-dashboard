import pandas as pd
import plotly.express as px

# Load data
year_df = pd.read_csv('./data/yearly_trend.csv')
month_df = pd.read_csv('./data/monthly_trend.csv')
week_df = pd.read_csv('./data/weekly_trend.csv')

def date_list(time_period):
    """Return the list of dates within a time period"""
    # Dates for weekly
    if time_period == 'Weekly':
        return list(week_df['time_period'].unique()[::-1])
    # Dates for monthly
    if time_period == 'Monthly':
        return list(month_df['time_period'].unique()[::-1])
    # Dates for yearly
    if time_period == 'Yearly':
        return list(year_df['time_period'].unique()[::-1])
    
def skill_map(skill_choice):
    '''Map skills choice to entity name'''
    if skill_choice == 'Technologies, Languages and Frameworks':
        return 'LANG_FRAM'
    if skill_choice == 'Hard Skills':
        return 'H_SKILL'
    if skill_choice == 'Soft Skills':
        return 'S_SKILL'

def get_top_increase(df, skill, date, num, min_count):
    """Get the specified number of the top increasing skills"""
    # Filter by skill
    filtered_df = df.loc[df['type'] == skill]
    # Filter by time
    filtered_df = filtered_df.loc[filtered_df['time_period'] == date]
    # Get top number of increasing skills
    top_increase = (filtered_df.loc[(filtered_df['perc_change'] > 0) & (filtered_df['count'] > min_count)]
                    .sort_values(by='perc_change', ascending=False)
                    .head(num)
    )
    # Add marker column for increasing
    top_increase['status'] = 'Increasing'
    return top_increase

def get_top_decrease(df, skill, date, num, min_count):
    """Get the specified number of the top decreasing skills"""
    # Filter by skill
    filtered_df = df.loc[df['type'] == skill]
    # Filter by time
    filtered_df = filtered_df.loc[filtered_df['time_period'] == date]
    # Get top number of decreasing skills
    top_decrease = (filtered_df.loc[(filtered_df['perc_change'] < 0) & (filtered_df['count'] > min_count)]
                    .sort_values(by='perc_change', ascending=False)
                    .tail(num)
    )
    # Add marker column for decreasing
    top_decrease['status'] = 'Decreasing'
    return top_decrease

def get_plot_df(df, skill, date, num=5, min_count=5):
    """Get merged dataframe for plotting"""
    top_increase = get_top_increase(df, skill, date, num, min_count)
    top_decrease = get_top_decrease(df, skill, date, num, min_count)
    plot_df = pd.concat([top_increase, top_decrease], axis=0)
    return plot_df


def create_plot(df, time, skill, date):
    """Create the plot using plotly"""
    fig = px.bar(df, x='new_ent', y='perc_change', color='status',
                 labels={
                     'perc_change':f'Change From Previous {time} (%)',
                     'new_ent':f'{skill}<br>{date}',
                     'status':'Status'
        }
    )
    return fig