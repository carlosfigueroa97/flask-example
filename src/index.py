from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("home.html")
    #return "<h1>Hola Mundo!</h1>"

@app.route('/about')
def about():
    return render_template("about.html")
    #return "<h1>Acerca de...</h1>"

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
    app.run(port=5000, debug=False)