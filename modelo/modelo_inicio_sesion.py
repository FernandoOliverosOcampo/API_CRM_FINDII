from librerias import *
from modelo.supabase.keys import *
from modelo.generales.generales import *

class modeloIniciarSesion():
    
    def iniciar_sesion(self):
        
        datos = request.json
        email = datos.get('email')
        password = datos.get('password')
        
        response = supabase.auth.sign_in_with_password({"email": email, "password": password})
        
        if 'error' in response:
            return jsonify({"msg": "Credenciales inválidas"}), 401
        
        access_token = response.session.access_token if response.session else None
    
        tabla_usuario = supabase.table('TABLA_USUARIOS')
        try:
            api_response = tabla_usuario.select('*').eq('email', email).execute()
            data_usuario = api_response.data
            print(api_response.data)# Extract data from APIResponse object
        except Exception as e:
            return jsonify({"msg": "Error al obtener los datos del usuario: " + str(e)}), 500
    
        return jsonify({"acceso": "AUTORIZADO", "usuario": data_usuario, "access_token": access_token}), 200
