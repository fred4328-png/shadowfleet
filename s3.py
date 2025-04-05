import streamlit as st
import pandas as pd
from streamlit_dynamic_filters import DynamicFilters
import plotly.express as px


data = pd.read_csv('traj_gdf.csv', index_col=0)

df = pd.DataFrame(data)

dynamic_filters = DynamicFilters(df, filters=['name', 'mmsi', 'trajectory_id', 'route_start', 'route_end',
       'route_length_hours', 'pct_of_route_without_signal', 'distance',
       'direction', 'navigational_status', 'destination',
       'number_of_received_positions', 'periods_without_signal',
       'minutes_without_signal', 'longest_period_without_signal',
       'median_distance_to_common_route', 'mean_distance_to_common_route',
       'max_distance_to_common_route'])

with st.sidebar:
    st.write("Apply filters in any order")


dynamic_filters.display_filters(location='sidebar')

dynamic_filters.display_df()

user_input = st.text_input("Enter Trajectory ID")

# Create a button to trigger the action
if st.button("Submit"):
    # Display the user input when button is pressed
    data = pd.read_csv('{}.csv'.format(user_input))
    fig = px.line_map(data, lat='lat', lon='lon', hover_name="MMSI", hover_data=["Name","TS","SOG", "Destination", "IMO"],
                        color_discrete_sequence=["red"], zoom=5, height=600)
    fig.update_layout(map_style="carto-darkmatter")
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    st.plotly_chart(fig)
