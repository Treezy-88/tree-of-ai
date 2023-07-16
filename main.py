from flask import Flask
import utils
import config
import database
import routes
import models

def init_app():
    app = Flask(__name__)
    app.config['DATABASE_URI'] = config.DATABASE_URI
    app.config['SECRET_KEY'] = config.SECRET_KEY
    app.config['DEBUG_MODE'] = config.DEBUG_MODE

    database.init_db(app)
    routes.init_routes(app)

    return app

def run_app(app):
    if app.config['DEBUG_MODE']:
        app.run(debug=True)
    else:
        app.run()

if __name__ == "__main__":
    app = init_app()
    run_app(app)