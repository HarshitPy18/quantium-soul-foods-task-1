import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

# 1. Load the data you processed in Task 2
df = pd.read_csv('formatted_data.csv')

# 2. Sort the dataframe by date so the line chart connects the dots in the right order
df = df.sort_values(by='date')

# 3. Initialize the Dash web application
app = dash.Dash(__name__)

# 4. Create the line chart using Plotly Express
fig = px.line(
    df, 
    x='date', 
    y='sales', 
    title='Pink Morsel Sales (Highlighting Jan 15th Price Increase)'
)

# 5. Define the layout of the app (the HTML structure)
app.layout = html.Div(
    children=[
        html.H1(
            children='Soul Foods: Pink Morsel Sales Visualizer',
            style={'textAlign': 'center'} # Centers the header text
        ),
        dcc.Graph(
            id='sales-line-chart',
            figure=fig
        )
    ]
)

# 6. Run the local server
if __name__ == '__main__':
    app.run(debug=True)