import pandas as pd
import requests
import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from .. import config

#### Options details

def app():

    r =  requests.get(f"{config.BASE_URL}/options/?environment=mainnet")
    data=r.json()['data']

    st.write(
    """
    ## *Buffer Finance*
    # Option details
    """
    )

    # st.subheader(f"Current number of IBFR holders = {data['current_value']}")
    df = pd.DataFrame(data) 
    del df['internal_txns']
    st.table(df)