import os
from app import create_app

# Tentukan environment aplikasi
config_name = os.getenv('FLASK_ENV', 'production')  # Default ke 'production'

# Buat instance aplikasi Flask
application = create_app(config_name=config_name)

if __name__ == "__main__":
    application.run()
