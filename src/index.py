from flask import Flask, render_template, request, json

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("home.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/signUp')
def sign_up():
    return render_template("formulario.html")

@app.route('/signUpUser', methods=['POST'])
def sign_up_user():
    name = request.form['nom']
    ncontrol = request.form['trol']
    return render_template("mensaje.html", nom=name, ncontrol=ncontrol)

@app.route('/articulos')
def articulos():
    return "<h1>Artículos</h1>"

@app.route('/articulos/id')
def lista_articulos():
    return "<h1>Consulta de Artículos: {}</h1>".format(id)

@app.errorhandler(404)
def page_not_found(error):
    return "<h1>Página no encontrada</h1>"

if __name__ == '__main__':
    app.run(port=80, debug=True)