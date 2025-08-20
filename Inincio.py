from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')  # Decorador de la ruta principal
def inicio():
    return render_template('index.html')

@app.route('/contacto', methods=['GET', 'POST'])
def contacto():
    usuario={ #Diccionaroio para almacenar los datos del formulario
         'nombre': '',
         'email': '',
         'mensaje': ''
    }
    if request.method == 'POST':
       usuario['nombre'] = request.args.get('nombre')
       usuario['email'] = request.args.get('email')
       usuario['mensaje'] = request.args.get('mensaje')
    return render_template('contacto.html', user=usuario)


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

@app.route('/login')
def login():
      return render_template('login.html')

@app.route('/usuario')
def usuario():
      return render_template('usuario.html')




if __name__ == '__main__':
    app.run(debug=True, port=8000) #ejecuta la aplicacion en modo depuracion