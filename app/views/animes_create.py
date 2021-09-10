from flask import Blueprint, request
from app.services import post_one, check_post_or_patch_entries

bp_animes = Blueprint('animes_create', __name__, url_prefix='/')

@bp_animes.post('/animes')
def get_create():

    data = request.get_json()

    entries_are_not_ok = check_post_or_patch_entries(data)

    if entries_are_not_ok:
        return entries_are_not_ok, 422

    data['anime'] = data['anime'].title()

    result = post_one(data)

    if result == 'anime already exists':
        return {'error': result}, 409

    return data, 201