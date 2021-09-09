from flask import Blueprint

bp_animes = Blueprint('animes_delete', __name__, url_prefix='/')

# Em vez de @app, utilizamos a instancia de blueprint criada, bp_hello
@bp_animes.delete('/animes/<int:anime_id>')
def delete(anime_id):
    return {'data': anime_id}, 200