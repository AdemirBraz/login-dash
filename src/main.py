from dash import Dash, html, callback, Output, Input ,State
from layout.case import armação
import dash_bootstrap_components as dbc
app = Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div([
    html.Div(children=armação(),id='my-Div')
])

@callback(Output('login-btn', 'n_clicks'), Input('login-btn', 'n_clicks'))
def handle_login(n_clicks):
    if n_clicks is None:
        return 0
    return n_clicks

if __name__ == "__main__":
    app.run(debug=True)
