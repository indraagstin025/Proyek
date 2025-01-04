import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    @staticmethod
    def get_env(key, default=None):
        """Ambil variabel lingkungan dengan fallback."""
        return os.getenv(key, default)

    # Kunci rahasia untuk aplikasi
    SECRET_KEY = get_env('SECRET_KEY', 'default-secret-key')

    # Konfigurasi database
    SQLALCHEMY_DATABASE_URI = get_env('DATABASE_URL', f'sqlite:///{os.path.join(BASE_DIR, "app.db")}')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Konfigurasi email
    MAIL_SERVER = get_env('MAIL_SERVER', 'smtp.gmail.com')
    MAIL_PORT = int(get_env('MAIL_PORT', 587))
    MAIL_USE_TLS = get_env('MAIL_USE_TLS', 'true').lower() in ['true', '1', 'yes']
    MAIL_USE_SSL = get_env('MAIL_USE_SSL', 'false').lower() in ['true', '1', 'yes']
    MAIL_USERNAME = get_env('MAIL_USERNAME')
    MAIL_PASSWORD = get_env('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = get_env('MAIL_DEFAULT_SENDER', MAIL_USERNAME)

    # Konfigurasi reset password
    PASSWORD_RESET_SALT = get_env('PASSWORD_RESET_SALT', 'default-salt')
    PASSWORD_RESET_MAX_AGE = int(get_env('PASSWORD_RESET_MAX_AGE', 3600))  # Dalam detik (default: 1 jam)

class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    TESTING = True
    DEBUG = False
    WTF_CSRF_ENABLED = False
    MAIL_SUPPRESS_SEND = True

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    LOGGING_LEVEL = 'ERROR'
    
    
class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
