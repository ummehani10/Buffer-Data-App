import pandas as pd
import requests
import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from .. import config

#### OPTIONS BOUGHT
def app():

    r =  requests.get(f"{config.BASE_URL}/options/stats/all/")
    data=r.json()['all_options']
    st.write(
    """
    # Options Stats
    """
    )

    st.subheader(f"Current number of options bought = {r.json()['current_value']}")

    df = pd.DataFrame(data)

    fig = px.line(        
            df, #Data Frame
            x = "created_at", #Columns from the data frame
            y = "option_count",
            title = "Cumulative number of options bought vs time"
        )
    fig.update_xaxes(gridcolor='grey')
    fig.update_yaxes(gridcolor='grey')
    fig.update_traces(line_color = "red")
    st.plotly_chart(fig)
