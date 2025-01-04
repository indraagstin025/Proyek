import os
from app import create_app

# Gunakan variabel lingkungan untuk menentukan environment
config_name = os.getenv('FLASK_ENV', 'production')
application = create_app(config_name=config_name)

if __name__ == "__main__":
    # Jalankan aplikasi Flask
    application.run()
