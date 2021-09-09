from flask import Flask


def init_app(app: Flask):


    
    from app.views.animes_create import bp_animes
    app.register_blueprint(bp_animes)


    from app.views.animes_get import bp_animes
    app.register_blueprint(bp_animes)


    from app.views.animes_delete import bp_animes
    app.register_blueprint(bp_animes)


    from app.views.animes_id import bp_animes
    app.register_blueprint(bp_animes)


    from app.views.animes_patch import bp_animes
    app.register_blueprint(bp_animes)