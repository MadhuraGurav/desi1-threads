from dash import dcc, html, Input, Output
import plotly.express as px
import pandas as pd
import dash

# Sample data
df = pd.DataFrame({
    "Year": [2015, 2016, 2017, 2018, 2019],
    "Sales": [100, 200, 300, 400, 500],
    "Profit": [50, 100, 150, 200, 250]  # New metric: Profit
})

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout of the dashboard
app.layout = html.Div([
    html.H1("Sales Dashboard"),
    dcc.Dropdown(
        id='metric-dropdown',
        options=[
            {'label': 'Sales', 'value': 'Sales'},
            {'label': 'Profit', 'value': 'Profit'}
        ],
        value='Sales',
        clearable=False
    ),
    dcc.Graph(id='sales-graph')
])

# Define callback to update graph based on dropdown selection
@app.callback(
    Output('sales-graph', 'figure'),
    [Input('metric-dropdown', 'value')]
)
def update_graph(selected_metric):
    if selected_metric == 'Sales':
        title = 'Sales Over Years'
    else:
        title = 'Profit Over Years'
    return px.line(df, x='Year', y=selected_metric, title=title)

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)

