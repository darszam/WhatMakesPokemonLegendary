from flask import Flask, render_template
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


app_dash = dash.Dash(
    __name__,
    server=app,
    routes_pathname_prefix='/dash/'
)

pokemon_dataset = pd.read_csv('pokemon.csv')

app_dash.layout = html.Div([
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
    )
])
if __name__ == '__main__':
    app_dash.run_server(debug=True)
