from app import create_app

# Buat aplikasi menggunakan konfigurasi production
application = create_app(config_name='production')

# Pastikan .env telah dimuat sebelumnya
import os
from dotenv import load_dotenv

env_file = os.path.join(os.getcwd(), '.env')
if os.path.exists(env_file):
    load_dotenv(env_file)
