from flask import Flask

app=Flask(__name__)

@app.route('/') # esto es un decordor de la ruta principal

def home(): # funtion de la ruta principal
    return "hola, mundo"

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


if __name__ == '__main__':
    app.run(debug=True, port=8000) #ejecuta la aplicacion en modo depuracion