from flask import Blueprint

bp_animes = Blueprint('animes_create', __name__, url_prefix='/')

# Em vez de @app, utilizamos a instancia de blueprint criada, bp_hello
@bp_animes.post('/animes')
def get_create():
    return {'data': 'hello'}, 200