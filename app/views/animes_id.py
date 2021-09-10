from flask import Blueprint
from app.services import get_specific_id

bp_animes = Blueprint('animes_id', __name__, url_prefix='/')

@bp_animes.get('/animes/<int:anime_id>')
def filter(anime_id):

    result = get_specific_id(anime_id)

    if result == "table doesn't exist" or result == []:
        return {'error' : 'Not Found'}, 404

    return {'data' : result }, 200