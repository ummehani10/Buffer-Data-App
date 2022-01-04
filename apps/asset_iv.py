import pandas as pd
import requests
import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from .. import config


#### Asset IVs

def app():

    r =  requests.get(f"{config.BASE_URL}/options/assets/iv/")
    data=r.json()

    st.write(
    """
    # Options Asset IVs
    """
    )
    df = pd.DataFrame(list(zip(data['assets'], data['iv'])), columns =['ASSET NAMES', 'IV (in %)']) 

    st.table(df)
    chosen_asset = st.selectbox('Choose an asset to view the changes in IV',df['ASSET NAMES'])
    
    if chosen_asset:
        
        r =  requests.get(f"{config.BASE_URL}/options/assets/iv/change/?asset={chosen_asset}")
        data=r.json()
        
        df = pd.DataFrame(data) 
        st.table(df)
        


