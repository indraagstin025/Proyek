# app/routes/__init__.py
from .auth import blueprint as auth_blueprint
from .document import blueprint as document_blueprint

def register_blueprints(app):
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(document_blueprint)
