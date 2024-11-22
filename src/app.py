from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from api.extensions import db
#from api.controllers import User, Users
from api.controllers import Articulo,Articulos, Proveedores,Proveedor,Categorias,Categoria
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with, abort

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db.init_app(app)
# db = SQLAlchemy(app)
api = Api(app)


with app.app_context():
    db.create_all()

class Articulos(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    nombre = db.Column(db.String(80), nullable=False)
    descripcion = db.Column(db.String(200))
    categoria_id = db.Column(db.Integer, db.ForeignKey('categoria.id'), nullable=False)
    proveedor_id = db.Column(db.Integer, db.ForeignKey('proveedor.id'), nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    precio = db.Column(db.Float, nullable=False)
    
    def __repr__(self):
        return f"<Articulo (nombre={self.nombre}, precio={self.precio})>"

class Categorias(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    categoria = db.Column(db.String(80), unique=True, nullable=False)
    
    def __repr__(self):
        return f"<Categoria (nombre={self.categoria})>"

class Proveedores(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    proveedor = db.Column(db.String(80), unique=True, nullable=False)
    
    def __repr__(self):
        return f"<Proveedor (nombre={self.proveedor})>"

# --- Parsers ---
articulo_args = reqparse.RequestParser()
articulo_args.add_argument("nombre", type=str, required=True, help="El nombre es obligatorio")
articulo_args.add_argument("descripcion", type=str)
articulo_args.add_argument("categoria_id", type=int, required=True, help="La categoría es obligatoria")
articulo_args.add_argument("proveedor_id", type=int, required=True, help="El proveedor es obligatorio")
articulo_args.add_argument("stock", type=int, required=True, help="El stock es obligatorio")
articulo_args.add_argument("precio", type=float, required=True, help="El precio es obligatorio")

# --- Fields para la serialización ---
articulo_fields = {
    "id": fields.Integer,
    "nombre": fields.String,
    "descripcion": fields.String,
    "categoria_id": fields.Integer,
    "proveedor_id": fields.Integer,
    "stock": fields.Integer,
    "precio": fields.Float
}

# --- Clases Resource ---
class Articulos(Resource):
    @marshal_with(articulo_fields)
    def post(self):
        args = articulo_args.parse_args()
        nuevo_articulo = Articulo(
            nombre=args["nombre"],
            descripcion=args["descripcion"],
            categoria_id=args["categoria_id"],
            proveedor_id=args["proveedor_id"],
            stock=args["stock"],
            precio=args["precio"]
        )
        db.session.add(nuevo_articulo)
        db.session.commit()
        return Articulo.query.all(), 201
    
    @marshal_with(articulo_fields)
    def get(self):
        articulos = Articulo.query.all()
        return articulos

class Articulo(Resource):
    @marshal_with(articulo_fields)
    def get(self, articulo_id):
        articulo = Articulo.query.filter_by(id=articulo_id).first()
        if not articulo:
            abort(404, message="Artículo no encontrado")
        return articulo, 200
    
    @marshal_with(articulo_fields)
    def patch(self, articulo_id):
        args = articulo_args.parse_args()
        articulo = Articulo.query.filter_by(id=articulo_id).first()
        if not articulo:
            abort(404, message="Artículo no encontrado")
        
        articulo.nombre = args["nombre"]
        articulo.descripcion = args["descripcion"]
        articulo.categoria_id = args["categoria_id"]
        articulo.proveedor_id = args["proveedor_id"]
        articulo.stock = args["stock"]
        articulo.precio = args["precio"]
        
        db.session.commit()
        return articulo, 200
    
    @marshal_with(articulo_fields)
    def delete(self, articulo_id):
        articulo = Articulo.query.filter_by(id=articulo_id).first()
        if not articulo:
            abort(404, message="Artículo no encontrado")
        
        db.session.delete(articulo)
        db.session.commit()
        return Articulo.query.all(), 200


# --- Fields para la serialización ---
categoria_fields = {
    "id": fields.Integer,
    "categoria": fields.String
}

proveedor_fields = {
    "id": fields.Integer,
    "proveedor": fields.String
}


# --- Clases Resource ---
class Categorias(Resource):
    @marshal_with(categoria_fields)
    def get(self):
        categorias = Categorias.query.all()
        return categorias, 200
    
    @marshal_with(categoria_fields)
    def post(self):
        args = categoria_args.parse_args()
        nueva_categoria = Categorias(categoria=args["categoria"])
        db.session.add(nueva_categoria)
        db.session.commit()
        return nueva_categoria, 201

class Categoria(Resource):
    @marshal_with(categoria_fields)
    def get(self, categoria_id):
        categoria = Categorias.query.filter_by(id=categoria_id).first()
        if not categoria:
            abort(404, message="Categoría no encontrada")
        return categoria, 200

class Proveedores(Resource):
    @marshal_with(proveedor_fields)
    def get(self):
        proveedores = Proveedores.query.all()
        return proveedores, 200
    
    @marshal_with(proveedor_fields)
    def post(self):
        args = proveedor_args.parse_args()
        nuevo_proveedor = Proveedores(proveedor=args["proveedor"])
        db.session.add(nuevo_proveedor)
        db.session.commit()
        return nuevo_proveedor, 201

class Proveedor(Resource):
    @marshal_with(proveedor_fields)
    def get(self, proveedor_id):
        proveedor = Proveedores.query.filter_by(id=proveedor_id).first()
        if not proveedor:
            abort(404, message="Proveedor no encontrado")
        return proveedor, 200



#api.add_resource(Users, "/api/users/")
#api.add_resource(User, "/api/users/<int:user_id>")

api.add_resource(Articulos, "/api/articulos/")
api.add_resource(Articulo, "/api/articulos/<int:articulo_id>")

api.add_resource(Categorias, "/api/categorias/")
api.add_resource(Categoria, "/api/categorias/<int:categoria_id>")

api.add_resource(Proveedores, "/api/proveedores/")  
api.add_resource(Proveedor, "/api/proveedores/<int:proveedor_id>")



@app.route('/')

def hello():
    return "<p>Hello, World!</p>"

if __name__ == '__main__':
    app.run(debug=True)

