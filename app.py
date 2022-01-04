import pandas as pd
import requests
import streamlit as st
import plotly.graph_objects as go
import plotly.express as px

import streamlit as st
from multiapp import MultiApp
from apps import ibfr_holders, all_options_stats, asset_iv, option_details # import your app modules here

app = MultiApp()

# Add all your application here
app.add_app("All Option Stats", all_options_stats.app)

app.add_app("IBFR Holders", ibfr_holders.app)

app.add_app("Asset IVs", asset_iv.app)

app.add_app("All Option Details", option_details.app)

# The main app
app.run()

