
from flask import Flask,render_template,request
from flask_mysqldb  import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'big_pizza'
mysql = MySQL(app)

@app.route('/')
def index():
    return 'hola'

@app.route('/', methods=['POST'])
def categoria():
    if request.method == 'POST':
        nombre = request.form['Nombre_categoria']
        estado = request.form['Estado']
        descripcion = request.form['Descripcion']
        print(nombre)
        print(estado)
        print(descripcion)
        return 'corecto'
    
    
    
@app.route('/comentario')
def comentario():
    return 'si habra algun comentario'

@app.route('/orden')
def ordenar():
    return 'aqui el cliente ordena'

@app.route('/eli_orden')
def eli_orden():
    return 'eliminar orden'

@app.route('/edit_orden')
def edit_orden():
    return 'editar las ordenes'

if __name__ == '__main__':
    app.run(port= 3000, debug=True)