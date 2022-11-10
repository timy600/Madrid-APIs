from flask import Flask

# from apis.cryptos.ctrl_extract import extract_pages
from apis import api_bp


def create_app():
    app = Flask(__name__)
    app.config["RESTPLUS_MASK_SWAGGER"] = False
    # app.register_blueprint(overview_pages)  # todo: replace app with imported server
    # app.register_blueprint(extract_pages)
    app.register_blueprint(api_bp)
    return app


if __name__ == "__main__":
    create_app()
    print("done")
