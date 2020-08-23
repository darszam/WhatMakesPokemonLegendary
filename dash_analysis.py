import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
from pages.analysis_layout import *
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
    graph_01_legendary_pokemons_data = go.Scatter(
        x=pokemon_dataset.loc[pokemon_dataset['is_legendary'] == True, 'attack'],
        y=pokemon_dataset.loc[pokemon_dataset['is_legendary'] == True, 'defense'],
        mode='markers'
        )

    graph_01_legendary_pokemons_layout = go.Layout(
        title='Legendary Pokemons statistics',
        xaxis={'title': 'Attack'},
        yaxis={'title': 'Defense'},
        hovermode='closest'
    )

    graph_01_legendary_pokemons_graph_object = dcc.Graph(
                id='Legendary_Pokemons',
                figure={
                    'data': [graph_01_legendary_pokemons_data],
                    'layout': graph_01_legendary_pokemons_layout
                }
            )

    graph_02_all_pokemons_data = go.Scatter(x=pokemon_dataset.loc[:, 'attack'],
                                            y=pokemon_dataset.loc[:, 'defense'],
                                            mode='markers'
                                            )

    graph_02_all_pokemons_layout =  go.Layout(
                            title='All Pokemons statistics',
                            xaxis={'title': 'Attack'},
                            yaxis={'title': 'Defense'},
                            hovermode='closest'
                        )

    graph_02_all_pokemons_graph_object = dcc.Graph(
        id='All_Pokemons',
        figure={
            'data': [graph_02_all_pokemons_data],
            'layout': graph_02_all_pokemons_layout
        }
    )

    main_layout['Legendary_Pokemons'] = graph_01_legendary_pokemons_graph_object

    main_layout['All_Pokemons'] = graph_02_all_pokemons_graph_object

    appdash.layout = main_layout
    return appdash
