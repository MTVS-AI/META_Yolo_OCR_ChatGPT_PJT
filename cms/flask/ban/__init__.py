from flask import Flask

def create_app():
    app = Flask(__name__)

    from .views import main_views
    from ban.modules import modules

    app.register_blueprint(main_views.bp)

    return app