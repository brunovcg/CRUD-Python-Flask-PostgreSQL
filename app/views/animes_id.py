from flask import Blueprint

bp_animes = Blueprint('animes_id', __name__, url_prefix='/')

# Em vez de @app, utilizamos a instancia de blueprint criada, bp_hello
@bp_animes.get('/animes/<int:anime_id>')
def filter(anime_id):
    return {'data': anime_id}, 200