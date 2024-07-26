import routes.user_route as user_route

url_prefix = '/api/v1'

# Registrar las rutas de la aplicacion
def register_routes(app):
  app.register_blueprint(user_route.user_bp, url_prefix=f'{url_prefix}/{user_route.NAME_ROUTE}')

