import dash_bootstrap_components as dbc
from layout.components.auth import login_header, email_input, password_input, login_button

def login_modal():
    content = dbc.Container(
        dbc.Row(
            dbc.Col(
                dbc.Card(
                    dbc.CardBody([
                        login_header(),
                        email_input(),
                        password_input(),
                        login_button()
                    ]),
                    className="shadow-lg border border-secondary border-opacity-50 rounded-3 p-4 bg-dark bg-opacity-75 text-white",
                    style={"backdropFilter": "blur(10px)"}
                ),
                xs=11, sm=8, md=6, lg=4, xl=4
            ),
            className="justify-content-center align-items-center min-vh-100"
        ),
        fluid=True,
        className="bg-dark"
    )
    return content
