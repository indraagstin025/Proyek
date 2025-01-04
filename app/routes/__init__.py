# app/routes/__init__.py
from app.routes.auth import Blueprint as auth_bp
from app.routes.document import Blueprint as document_bp
from app.routes.dashboard import Blueprint as dashboard_bp

def register_blueprints(app):
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(document_bp)
