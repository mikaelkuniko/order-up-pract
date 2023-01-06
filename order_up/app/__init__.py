from flask import Flask
from .config import Configuration
from .models import db, Employee   # New import
from flask_login import LoginManager
# from .routes import orders
# from .routes.session import session_router
from .routes import orders_router, session_router

app = Flask(__name__)
app.config.from_object(Configuration)
app.register_blueprint(orders_router, url_prefix="")
app.register_blueprint(session_router, url_prefix = '/session')
db.init_app(app)  # Configure the application with SQLAlchemy

login = LoginManager(app)
login.login_view = "session.login"


@login.user_loader
def load_user(id):
    return Employee.query.get(int(id))
