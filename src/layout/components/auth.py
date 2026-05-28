from dash import html
import dash_bootstrap_components as dbc

def login_header():
    return html.H3(
        "Acessar Conta", 
        className="text-center mb-4 fw-bold text-primary"
    )

def email_input():
    return html.Div([
        dbc.Label("E-mail", html_for="Gmail", className="text-muted small mb-1"),
        dbc.Input(id="Gmail", type="email", placeholder="exemplo@email.com", className="py-2")
    ], className="mb-3")

def password_input():
    return html.Div([
        dbc.Label("Senha", html_for="Senha", className="text-muted small mb-1"),
        dbc.Input(id="Senha", type="password", placeholder="Digite sua senha", className="py-2")
    ], className="mb-4")

def login_button():
    return dbc.Button(
        "Entrar", 
        id="login-btn", 
        color="primary", 
        className="w-100 py-2 fw-bold text-uppercase"
    )
