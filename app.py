from librerias import *
from rutas.ruta_inicio_sesion import *

app = Flask(__name__)
jwt = JWTManager(app)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
app.config['JWT_SECRET_KEY'] = 'super-secret' # Clave secreta para firmar los JWT

app.register_blueprint(inicio_de_sesion)



def pagina_no_encontrada(error):
    return "<h1>Pagina no encontrada ...<h1>"

if __name__ == "__main__":
    app.register_error_handler(404, pagina_no_encontrada)
    app.run(host="0.0.0.0", port=5600, debug=True)