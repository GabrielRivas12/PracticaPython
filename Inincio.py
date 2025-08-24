from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')  # Decorador de la ruta principal
def inicio():
    return render_template('index.html')

@app.route('/contactos', methods=['GET', 'POST'])
def contacto():
    usuario={ #Diccionaroio para almacenar los datos del formulario
         'nombre': '',
         'email': '',
         'mensaje': ''
    }
    if request.method == 'GET':
       usuario['nombre'] = request.args.get('nombre')
       usuario['email'] = request.args.get('email')
       usuario['mensaje'] = request.args.get('mensaje')
    return render_template('contactos.html', user=usuario)


@app.route('/contactopost', methods=['GET', 'POST'])
def contactopost():
    usuario={ #Diccionaroio para almacenar los datos del formulario
         'nombre': '',
         'email': '',
         'mensaje': ''
    }
    if request.method == 'POST':
       
       usuario['nombre'] = request.form.get('nombre')
       usuario['email'] = request.form.get('email')
       usuario['mensaje'] = request.form.get('mensaje')
    return render_template('contactospost.html', user=usuario)


@app.route('/formulario', methods=['GET', 'POST'])
def formulario():
    usuario={ #Diccionaroio para almacenar los datos del formulario
         'numeroc': '',
         'nombre': '',
         'apellidos': '',
         'direccion': '',
         'mensaje': ''
    }
    if request.method == 'GET':
       usuario['numeroc'] = request.args.get('numeroc')
       usuario['nombre'] = request.args.get('nombre')
       usuario['apellidos'] = request.args.get('apellidos')
       usuario['direccion'] = request.args.get('direccion')
       usuario['mensaje'] = request.args.get('mensaje')
    return render_template('formulario.html', user=usuario)


@app.route('/formulariopost', methods=['GET', 'POST'])
def formulariopost():
    usuario={ #Diccionaroio para almacenar los datos del formulario
         'numeroc': '',
         'nombre': '',
         'apellidos': '',
         'direccion': '',
         'mensaje': ''
    }
    if request.method == 'POST':
       usuario['numeroc'] = request.form.get('numeroc')
       usuario['nombre'] = request.form.get('nombre')
       usuario['apellidos'] = request.form.get('apellidos')
       usuario['direccion'] = request.form.get('direccion')
       usuario['mensaje'] = request.form.get('mensaje')
    return render_template('formulariopost.html', user=usuario)





@app.route('/login')
def login():
      return render_template('login.html')

@app.route('/usuario')
def usuario():
      return render_template('usuario.html')




if __name__ == '__main__':
    app.run(debug=True, port=8000) #ejecuta la aplicacion en modo depuracion