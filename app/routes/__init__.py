# app/routes/__init__.py
from app.routes.auth import auth_bp
from app.routes.document import  document_bp
from app.routes.dashboard import dashboard_bp

def register_blueprints(app):
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(document_bp)
