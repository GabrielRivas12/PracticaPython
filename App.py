from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')  # Decorador de la ruta principal
def inicio():
    return render_template('index.html')

@app.route('/contacto')
def contacto(): # funtion de la ruta de contactos
    return "Pagina de contactosss"

@app.route('/about') # funtion de la ruta de about
def about():
    return "esta es el acerca de"

@app.route('/servicios/<nombre>')
def servicios (nombre):
    return 'El nomnre del servicio es %s ' % nombre

@app.route ('/edad/<edad>')
def edad (edad):
    return 'La edad es: {} años'.format(edad)

@app.route ('/suma/<int:num1>/<int:num2>')
def suma (num1, num2):
    resultado=num1 + num2
    return 'La suma de {} y {} es: {}'.format( num1, num2, resultado)

@app.route ('/edadvalor/<int:edad>')
def edadvalor (edad):
    if edad < 18:
        return 'Eres menor de edad'
    elif edad >= 18 and edad < 65:
        return 'Eres mayor de edad {} años'.format(edad)
    else: 
        return 'Eres un adulto mayor {} años'.format(edad) 


if __name__ == '__main__':
    app.run(debug=True, port=8000) #ejecuta la aplicacion en modo depuracion