import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import pandas as pd

# Load and sort data
df = pd.read_csv('formatted_data.csv')
df = df.sort_values(by='date')

# Initialize the app
app = dash.Dash(__name__)

# Define our CSS color palette (Dark Mode!)
colors = {
    'background': '#1e1e2f',
    'text': '#ffffff',
    'primary': '#ff6b6b'
}

# The App Layout with our new RadioItems and CSS styling
app.layout = html.Div(style={'backgroundColor': colors['background'], 'color': colors['text'], 'fontFamily': 'Arial, sans-serif', 'padding': '40px', 'minHeight': '100vh'}, children=[
    
    html.H1(
        children='Soul Foods: Pink Morsel Sales Visualizer',
        style={'textAlign': 'center', 'color': colors['primary'], 'marginBottom': '30px'}
    ),
    
    html.Div(
        children='Filter by Region:',
        style={'textAlign': 'center', 'fontSize': '20px', 'fontWeight': 'bold', 'marginBottom': '15px'}
    ),
    
    # The new Radio Button component
    html.Div(
        dcc.RadioItems(
            id='region-filter',
            options=[
                {'label': 'All Regions', 'value': 'all'},
                {'label': 'North', 'value': 'north'},
                {'label': 'East', 'value': 'east'},
                {'label': 'South', 'value': 'south'},
                {'label': 'West', 'value': 'west'}
            ],
            value='all',
            inline=True,
            style={'display': 'flex', 'justifyContent': 'center', 'gap': '30px', 'fontSize': '18px'}
        ),
        style={'marginBottom': '40px'}
    ),

    # The graph (it's empty at first, the callback fills it!)
    dcc.Graph(
        id='sales-line-chart'
    )
])

# The Callback: This connects the radio button to the graph
@app.callback(
    Output('sales-line-chart', 'figure'),
    Input('region-filter', 'value')
)
def update_graph(selected_region):
    # 1. Filter the dataframe based on the radio button choice
    if selected_region == 'all':
        filtered_df = df
    else:
        filtered_df = df[df['region'] == selected_region]
        
    # 2. Draw the new line chart
    fig = px.line(
        filtered_df, 
        x='date', 
        y='sales', 
        title=f'Pink Morsel Sales: {selected_region.capitalize()} Region(s)',
        color_discrete_sequence=[colors['primary']] # Make the line match our accent color
    )
    
    # 3. Inject our CSS colors into the Plotly chart itself
    fig.update_layout(
        plot_bgcolor=colors['background'],
        paper_bgcolor=colors['background'],
        font_color=colors['text'],
        title_x=0.5 # Center the chart title
    )
    
    return fig

if __name__ == '__main__':
    app.run(debug=True)