import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

main_layout = html.Div([

    html.Div([
        html.Div(

            dcc.Graph(
                id='Legendary_Pokemons',
                figure={
                    'data': []
                }
            ),
            style={'width': '70%', 'float': 'left'}, className='eight columns'
        ),

        html.Div(html.Pre(id='hover-data', style={'paddingTop': 35}), className='four columns')
    ],
        className='row'
    ),

    html.Div([
        html.Div(
            dcc.Graph(
                id='All_Pokemons',
                figure={
                    'data': []
                }), style={'width': '70%', 'float': 'left'},
            className='eleven columns'
        ),
        html.Div(html.Pre(id='hover-data2', style={'paddingTop': 35}), className='four columns')
    ],
        className='row'
    ),

])
