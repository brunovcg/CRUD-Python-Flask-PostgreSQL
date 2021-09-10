from flask import Blueprint, request
from app.services import patch_one, check_post_or_patch_entries

bp_animes = Blueprint('animes_patch', __name__, url_prefix='/')

# Em vez de @app, utilizamos a instancia de blueprint criada, bp_hello
@bp_animes.patch('/animes/<int:anime_id>')
def update(anime_id):

    data = request.get_json()

    entries_are_not_ok = check_post_or_patch_entries(data)

    if entries_are_not_ok:
        return entries_are_not_ok, 422

    result = patch_one(anime_id, data)



    return {'data': anime_id}, 200