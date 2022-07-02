import dash
import dash_bootstrap_components as dbc
import psutil




app = dash.Dash(__name__,
    external_stylesheets=[dbc.themes.VAPOR],
)

server = app.server


app.layout = dbc.Container([
    dbc.Label(f'hi, {psutil.Process().username()}'),
])



if __name__ == '__main__':
    app.run_server(debug=False)
