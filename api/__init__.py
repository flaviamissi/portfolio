from flask import Flask

from api.single_page import single_page
from api.api import api

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True,
                static_folder='../static',
                template_folder='../templates')

    # app.config.from_mapping(
    #     SECRET_KEY='dev',
    #     DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    # )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    # try:
    #     os.makedirs(app.instance_path)
    # except OSError:
    #     pass

    app.register_blueprint(single_page)
    app.register_blueprint(api)

    return app
