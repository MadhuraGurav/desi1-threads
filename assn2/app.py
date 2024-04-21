import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# Sample datasets
data1 = pd.DataFrame({
    'X': [1, 2, 3, 4, 5],
    'Y': [10, 15, 7, 12, 9]
})

data2 = pd.DataFrame({
    'X': [3, 4, 5, 6, 7],
    'Y': [8, 12, 14, 10, 5]
})

# Initialize the Dash app
app = dash.Dash(_name_)

# Define the layout of the dashboard
app.layout = html.Div([
    dcc.Dropdown(
        id='dropdown',
        options=[
            {'label': 'Dataset 1', 'value': 'data1'},
            {'label': 'Dataset 2', 'value': 'data2'}
        ],
        value='data1'
    ),
    dcc.Graph(id='scatter-plot')
])

# Define the callback to update the scatter plot based on dropdown selection
@app.callback(
    Output('scatter-plot', 'figure'),
    [Input('dropdown', 'value')]
)
def update_scatter_plot(selected_dataset):
    if selected_dataset == 'data1':
        df = data1
    else:
        df = data2
    
    fig = px.scatter(df, x='X', y='Y', title='Scatter Plot')
    return fig

# Run the Dash app
if _name_ == '_main_':
    app.run_server(debug=True)