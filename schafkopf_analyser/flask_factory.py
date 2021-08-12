from flask import Flask


def create_app(test_config=None) -> Flask:
    app = Flask(__name__)

    # Apply testing config
    if test_config is not None:
        app.config.update(test_config)

    @app.route('/')
    def hello_world():  # put application's code here
        return "test"

    return app
