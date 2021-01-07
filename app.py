import datetime
import pandas_datareader as web
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

# Initialize the Dash app
app = dash.Dash(__name__, external_stylesheets = [dbc.themes.DARKLY])

# Dashboard description
description = """This dashboard is built with Plotly Dash.  It takes user 
                 input and gets stock data if the input is a valid stock 
                 ticker.  It then generates a graph of closing prices for 
                 the specified stock."""

# Setup the Dash app layout
app.layout = html.Div(
    children = [dbc.Row(children = [
        dbc.Col(
            html.Div(
                className = "container input-panel", 
                children = [
                    html.H3("Stock Market Dashboard"),
                    html.P(description), 
                    dbc.Input(
                        id = "stock-ticker-input", 
                        value = "", 
                        placeholder = "Enter a valid stock ticker...", 
                        type = "text"
                    )
                ]
            ), 
            md = 4, 
            width = 12
        ), 
        dbc.Col(
            html.Div(
                className = "container graph-panel", 
                children = [
                    html.Div(id = "closing-prices")
                ]
            ), 
            md = 8, 
            width = 12
        )
    ])]
)

# Callback to get the corresponding closing prices graph based on user input
@app.callback(Output("closing-prices", "children"), 
             [Input("stock-ticker-input", "value")])
def update_closing_prices_graph(input): 
    start = datetime.datetime(2010, 1, 1)
    end = datetime.datetime.now()

    try:
        stock_df = web.DataReader(input, "yahoo", start, end)

        graph = dcc.Graph(
            id = "closing-prices-graph", 
            figure = {
                "data": [{
                    "x": stock_df.index, 
                    "y": stock_df.Close, 
                    "type": "line"
                }], 
                "layout": {
                    "title": input, 
                    "xaxis": {"title": "Date"}, 
                    "yaxis": {"title": "Price ($)"}
                }
            }, 
        )
        return graph
    except:
        if str(input) == "":
            alert = dbc.Alert(
                "Please input a valid stock ticker to display a proper graph.",
                color = "danger", 
                dismissable = True
            )
        else:
            alert = dbc.Alert(
                str(input) + " is not a valid stock ticker.", 
                color = "danger", 
                dismissable = True
            )
        return alert

# Run the Dash app
if __name__ == '__main__':
    app.run_server()