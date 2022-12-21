import pathlib
import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


basedir = pathlib.Path(__file__).parent.resolve()  # Base Directory where code is being run
connex_app = connexion.App(__name__, specification_dir=basedir)

app = connex_app.app
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{basedir / 'people.db'}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False  # No event driven tracking

db = SQLAlchemy(app)  #initializes SQLAlchemy by passing the app configuration information to SQLAlchemy 
ma = Marshmallow(app)  #initializes Marshmallow and allows it to work with the SQLAlchemy components attached to the app