import dash
import dash_bootstrap_components as dbc
import socket




app = dash.Dash(__name__,
    external_stylesheets=[dbc.themes.VAPOR],
)

server = app.server


app.layout = dbc.Container([
    dbc.Label(f'hi, {socket.getfqdn()}'),
])



if __name__ == '__main__':
    app.run_server(debug=False)
