from dash import Dash, html
import dash_bootstrap_components as dbc
from layout.pages import login

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div([
    login.login_modal()
])

if __name__ == "__main__":
    app.run(debug=True)
