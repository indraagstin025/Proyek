from app import create_app

# Pastikan aplikasi dibuat dengan konfigurasi yang benar
application = create_app(config_name='production')

if __name__ == "__main__":
    application.run()
