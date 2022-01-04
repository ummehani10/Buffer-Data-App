import pandas as pd
import requests
import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from .. import config

#### IBFR HOLDERS


def app():

    r =  requests.get(f"{config.BASE_URL}/ibfr/holders/")
    data=r.json()

    st.write(
    """
    ## *Buffer Finance*
    # IBFR Holder Stats
    """
    )

    st.subheader(f"Current number of IBFR holders = {data['current_value']}")

    df = pd.DataFrame(dict(
        Timeline = data['dates'],
        IBFR_holders =data['ibfr_holder_count']
    ))

    fig = px.line(        
            df, #Data Frame
            x = "Timeline", #Columns from the data frame
            y = "IBFR_holders",
            title = "Number of IBFR holders vs time"
        )
    fig.update_xaxes(gridcolor='grey')
    fig.update_yaxes(gridcolor='grey')
    fig.update_traces(line_color = "red")
    st.plotly_chart(fig)

