from dash import dcc, html, Input, Output, callback
import dash_bootstrap_components as dbc

text = dcc.Markdown(
    '''
    ## About
    This is the training page.
    '''
)

intro = dbc.Row(text, className='h-100')

layout = dbc.Container([intro], className="h-100")
