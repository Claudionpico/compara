import flask
import flask_restless
from flask_cors import CORS

from config import config
import os

def create_app(app, config_name, database_engine):
    """
    Generate app based on Flask instance.

    :type config_name: string
    :param config_name: Config Type (i.e. development, staging, production).

    :rtype: Object
    :return: Flask Object.
    """

    # Load generic configs.
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    # Save environment type
    app.config['ENVIRONMENT'] = config_name

    # Init database from environment variable.
    databases_conf = app.config['GENERAL']['databases']
    app.config['SQLALCHEMY_DATABASE_URI'] = databases_conf[database_engine]
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    # app.config['SQLALCHEMY_POOL_RECYCLE'] = databases_conf['pool_recycle']
    app.config['SQLALCHEMY_POOL_RECYCLE'] = 299
    app.config['SQLALCHEMY_POOL_TIMEOUT'] = 20

    from api_0_1.models.model import db
    db.init_app(app)
    db.app = app

    # Import model classes.
    from api_0_1.models.car import Car
    from api_0_1.models.user import User

    # Create db if not exist (defined at above models).
    db.create_all()

    # Import views clasess.
    from api_0_1.views.cars import Cars
    from api_0_1.views.users import Users
    from api.constants import data
    Cars = Cars()
    Users = Users()

    def initDb(data):
        car = Car()
        car.name = data[0]
        car.plate = data[1]
        db.session.add(car)
        db.session.commit()

    init = map(lambda x:initDb(x), data)

    # Create the Flask-Restless API manager.
    manager = flask_restless.APIManager(app, flask_sqlalchemy_db=db)

    # Create API endpoints.
    manager.create_api(
        Car,
        url_prefix=Cars.url_prefix,
        methods=Cars.methods,
        include_columns=Cars.include_columns,
        exclude_columns=Cars.exclude_columns,
        preprocessors=Cars.preprocessors,
        postprocessors=Cars.postprocessors
    )
    manager.create_api(
        User,
        url_prefix=Users.url_prefix,
        methods=Users.methods,
        include_columns=Users.include_columns,
        exclude_columns=Users.exclude_columns,
        preprocessors=Users.preprocessors,
        postprocessors=Users.postprocessors
    )

    return app


try:
    if os.environ['ENV']:
        environment = os.environ['ENV']
except KeyError, e:
    environment = 'development'

try:
    if os.environ['DATABASE']:
        database = os.environ['DATABASE']
except KeyError, e:
    database = 'mysql'

app = flask.Flask(__name__)
create_app(app, environment, database)

CORS(
    app,
    origins='*',
    supports_credentials=True,
    expose_headers=['Content-Length'],
    allow_headers=['Content-Type', 'Authorization']
)
