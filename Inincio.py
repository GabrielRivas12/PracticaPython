from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')  # Decorador de la ruta principal
def inicio():
    return render_template('index.html')

@app.route('/contacto', methods=['GET', 'POST'])
def contacto():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        email = request.form.get('email')
        mensaje = request.form.get('mensaje')
        print(request.form)
        return 'Mensaje enviado'
    else:
        return render_template('contactos.html')


@app.route('/login')
def login():
      return render_template('login.html')

@app.route('/usuario')
def usuario():
      return render_template('usuario.html')




if __name__ == '__main__':
    app.run(debug=True, port=8000) #ejecuta la aplicacion en modo depuracion