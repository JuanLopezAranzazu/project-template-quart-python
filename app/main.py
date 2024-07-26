from quart import Quart, jsonify
import config.global_config as global_config
import routes.index as index
import db.db_config as db_config
import models.user_model as user_model
import asyncio

config = global_config.config

app = Quart(__name__)

# Inicializar la base de datos
# asyncio.run(db_config.init_db())

@app.route('/')
async def hello():
  return 'Hello, World!'

# Rutas de la aplicacion
index.register_routes(app)

# Manejadores de errores
@app.errorhandler(404)
def not_found(error):
  return jsonify({'error': 'Resource not found', 'message': str(error)}), 404

@app.errorhandler(400)
def bad_request(error):
  return jsonify({'error': 'Bad Request', 'message': str(error)}), 400

@app.errorhandler(409)
def conflict(error):
  return jsonify({'error': 'Conflict', 'message': str(error)}), 409

@app.errorhandler(Exception)
def handle_exception(error):
  return jsonify({'error': 'An unexpected error occurred', 'message': str(error)}), 500


# Iniciar la aplicacion
if __name__ == '__main__':
  port = config['port']
  app.run(debug=True, port=port)


  