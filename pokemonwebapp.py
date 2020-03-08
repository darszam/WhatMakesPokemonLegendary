from flask import Flask, render_template
import dash_analysis

app = Flask(__name__)

app_dash = dash_analysis.createdashboard(app)
app_dash = dash_analysis.createlayout(app_dash)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/dash')
def dashboard():
    return render_template('dash_template.html', dash_url=app_dash.routes_pathname_prefix)


@app_dash.callback(dash_analysis.Output('hover-data', 'children'),
                   [dash_analysis.Input('Legendary_Pokemons', 'hoverData')])
def callback_image(hoverData):
    return dash_analysis.json.dumps(hoverData, indent=2)


@app_dash.callback(dash_analysis.Output('hover-data2', 'children'),
                   [dash_analysis.Input('All_Pokemons', 'hoverData')])
def callback_image2(hoverData):
    return dash_analysis.json.dumps(hoverData, indent=2)


app_dash.css.append_css({'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'})

if __name__ == '__main__':
    app.run(debug=True)
