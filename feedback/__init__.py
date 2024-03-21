import os
from flask import Flask


def create_app() -> Flask:
    app = Flask(__name__)
    app.secret_key = os.environ.get("SECRETKEY")

    from .views import home
    app.register_blueprint(home)
    return app


