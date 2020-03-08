import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
from dash.dependencies import Input, Output
import json

pokemon_dataset = pd.read_csv('pokemon.csv')

layout = open('templates/dash_template.html', 'r').read()


def createdashboard(app):
    app_dash = dash.Dash(
        __name__,
        server=app,
        routes_pathname_prefix='/dash/',
        index_string=layout
    )
    return app_dash


def createlayout(appdash):
    appdash.layout = html.Div([

        html.Div([
            html.Div(

                dcc.Graph(
                    id='Legendary_Pokemons',
                    figure={
                        'data': [
                            go.Scatter(x=pokemon_dataset.loc[pokemon_dataset['is_legendary'] == True, 'attack'],
                                       y=pokemon_dataset.loc[pokemon_dataset['is_legendary'] == True, 'defense'],
                                       mode='markers'
                                       )
                        ],
                        'layout': go.Layout(
                            title='Legendary Pokemons statistics',
                            xaxis={'title': 'Attack'},
                            yaxis={'title': 'Defense'},
                            hovermode='closest'
                        )
                    }
                 ),
                style={'width':'70%', 'float':'left'}, className='eight columns'
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
                        'data': [
                            go.Scatter(x=pokemon_dataset.loc[:, 'attack'],
                                       y=pokemon_dataset.loc[:, 'defense'],
                                       mode='markers'
                                       )
                        ],
                        'layout': go.Layout(
                            title='All Pokemons statistics',
                            xaxis={'title': 'Attack'},
                            yaxis={'title': 'Defense'},
                            hovermode='closest'
                        )
                    }), style={'width':'70%', 'float':'left'},
                        className='eleven columns'
                ),
            html.Div(html.Pre(id='hover-data2', style={'paddingTop': 35}), className='four columns')
        ],
        className='row'
        ),


    ])
    return appdash

