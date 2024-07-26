import os
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Configuración de la base de datos y de la aplicación
config = {
  'port': int(os.getenv('PORT', 5000)),
  'debug': os.getenv('DEBUG', False),
  'secret_key': os.getenv('SECRET_KEY', 'my_secret'),
  'algorithm': os.getenv('ALGORITHM', 'HS256'),
  'jwt_expiration_time': int(os.getenv('JWT_EXPIRATION_TIME', 3600)),
  'quart_env': os.getenv('QUART_ENV', 'development'),
  'db': {
    'host': os.getenv('DB_HOST', 'localhost'),
    'port': int(os.getenv('DB_PORT', '3306')),
    'user': os.getenv('DB_USER', 'root'),
    'password': os.getenv('DB_PASSWORD', 'password'),
    'name': os.getenv('DB_NAME', 'my_database'),
  },
}
