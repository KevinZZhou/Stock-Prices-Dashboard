import datetime
import pandas_datareader as web
import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Initialize the Dash app
app = dash.Dash(__name__)

# Setup the Dash app layout
app.layout = html.Div(
    children = [html.Div(
        className = "row", 
        children = [
            html.Div(
                className = "three columns div-user-controls", 
                children = []
            ), 
            html.Div(
                className = "nine columns div-for-charts bg-grey", 
                children = []
            )
        ]
    )]
)

# Run the Dash app
if __name__ == '__main__':
    app.run_server()