import os
from flask import Flask
from flask_login import LoginManager
from dotenv import load_dotenv
from app.extensions import init_extensions, db, mail
from app.routes import register_blueprints
from app.routes.auth import auth_bp
from app.routes.dashboard import dashboard_bp
from app.routes.document import document_bp

import pymysql

# Load environment variables
load_dotenv()

# Setup MySQL driver
pymysql.install_as_MySQLdb()

# Fungsi untuk membuat aplikasi
def create_app(config_name='default'):
    app = Flask(__name__,
                template_folder=os.path.join(os.getcwd(), 'app', 'templates'),
                static_folder=os.path.join(os.getcwd(), 'app', 'static'))
    
    # Konfigurasi aplikasi berdasarkan environment
    if config_name == 'testing':
        app.config.from_object('config.TestingConfig')
    elif config_name == 'development':
        app.config.from_object('config.DevelopmentConfig')
    elif config_name == 'production' :
        app.config.from_object('config.ProductionConfig')
    
    # Inisialisasi ekstensi
    init_extensions(app)
    register_blueprints(app)
    mail.init_app(app)
    

    
    # Tambahkan header untuk mencegah cache
    @app.after_request
    def add_header(response):
        response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
        response.headers['Pragma'] = 'no-cache'
        response.headers['Expires'] = '-1'
        return response
    
    return app
