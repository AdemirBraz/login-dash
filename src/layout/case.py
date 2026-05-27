from dash import Dash,html
import dash_bootstrap_components as dbc

def armação():
    content=dbc.Container([
                dbc.Card(
                    dbc.CardBody([
                    dbc.Badge(children='LOGIN'),
                    dbc.Input(id='Gmail',type='email',placeholder='Email'),
                    dbc.Input(id='Senha',type='password',placeholder='Senha'),
                    dbc.Button('Login', id='login-btn', color='primary', className='mt-3')
    ]),
                ),
    ])
    return content