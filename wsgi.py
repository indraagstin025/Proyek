import os
from app import create_app  # Impor fungsi create_app dari app/__init__.py

# Gunakan variabel lingkungan untuk menentukan environment
config_name = os.getenv('FLASK_ENV', 'production')

# Buat instance aplikasi Flask menggunakan fungsi create_app
application = create_app(config_name=config_name)

if __name__ == "__main__":
    # Jalankan aplikasi Flask hanya jika dijalankan langsung
    application.run(debug=(config_name == 'development'))
