from dash import Dash, html, dcc
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

# Create a Dash app
app = Dash(__name__)

# Load your data into a pandas DataFrame (assuming it has columns 'date' and 'profit')
df = pd.read_csv('output.csv')

# Convert the 'date' column to datetime format
df['date'] = pd.to_datetime(df['date'])

# Create the line trace
line_trace = go.Scatter(x=df['date'], y=df['Sales'], mode='lines', name='Line Chart')

date_to_highlight = pd.to_datetime('2021-01-15')
vertical_line = {
    'type': 'line',
    'x0': date_to_highlight,
    'y0': df['Sales'].min(),
    'x1': date_to_highlight,
    'y1': df['Sales'].max(),
    'line': {
        'color': 'red',
        'width': 1,
        'dash': 'dash'
    }
}

# Create the figure with the line trace
fig = go.Figure(data=[line_trace],layout={'shapes':[vertical_line]})

# Set the layout of the figure
fig.update_layout(title='Line Chart', xaxis_title='Date', yaxis_title='Sales')

# Define the layout of the Dash app
app.layout = html.Div(children=[
    html.H1(children='Sales of Pink Morsel'),
    dcc.Graph(figure=fig)
])

# Run the Dash app
if __name__ == '__main__':
    app.run_server(debug=True)
