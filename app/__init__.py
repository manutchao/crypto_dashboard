from flask import Flask


def create_app():
    app = Flask(__name__)
    from .cryptocurrencies import cryptocurrencies as cp_blueprint

    app.register_blueprint(cp_blueprint, url_prefix="/cryptocurrencies")

    @app.route("/test/")
    def test_page():
        return "<h1>Hello World</h1>"

    return app
