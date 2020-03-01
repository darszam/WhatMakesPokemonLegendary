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


if __name__ == '__main__':
    app.run(debug=True)
