from flask import Blueprint
from app.services import delete_one

bp_animes = Blueprint('animes_delete', __name__, url_prefix='/')

@bp_animes.delete('/animes/<int:anime_id>')
def delete(anime_id):

    result = delete_one(anime_id)

    if result == 'Not Found':
        return {'error':'Not Found'}, 404


    return result, 200