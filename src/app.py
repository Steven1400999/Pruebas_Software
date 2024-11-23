from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource, reqparse, fields, marshal_with

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
api = Api(app)

# --- Modelos ---
class ArticuloModel(db.Model):
    __tablename__ = 'articulos'  # Nombres de tablas en plural
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    nombre = db.Column(db.String(80), nullable=False)
    descripcion = db.Column(db.String(200))
    categoria_id = db.Column(db.Integer, db.ForeignKey('categorias.id'), nullable=False)
    proveedor_id = db.Column(db.Integer, db.ForeignKey('proveedores.id'), nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    precio = db.Column(db.Float, nullable=False)

    categoria = db.relationship('CategoriaModel', backref='articulos')
    proveedor = db.relationship('ProveedorModel', backref='articulos')

class CategoriaModel(db.Model):
    __tablename__ = 'categorias'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    categoria = db.Column(db.String(80), unique=True, nullable=False)

class ProveedorModel(db.Model):
    __tablename__ = 'proveedores'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    proveedor = db.Column(db.String(80), unique=True, nullable=False)

with app.app_context():
    db.create_all()

# --- Parsers ---
articulo_args = reqparse.RequestParser()
articulo_args.add_argument("nombre", type=str, required=True, help="El nombre es obligatorio")
articulo_args.add_argument("descripcion", type=str)
articulo_args.add_argument("categoria_id", type=int, required=True, help="La categoría es obligatoria")
articulo_args.add_argument("proveedor_id", type=int, required=True, help="El proveedor es obligatorio")
articulo_args.add_argument("stock", type=int, required=True, help="El stock es obligatorio")
articulo_args.add_argument("precio", type=float, required=True, help="El precio es obligatorio")

categoria_args = reqparse.RequestParser()
categoria_args.add_argument("categoria", type=str, required=True, help="La categoría es obligatoria")

proveedor_args = reqparse.RequestParser()
proveedor_args.add_argument("proveedor", type=str, required=True, help="El proveedor es obligatorio")

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

categoria_fields = {
    "id": fields.Integer,
    "categoria": fields.String
}

proveedor_fields = {
    "id": fields.Integer,
    "proveedor": fields.String
}

# --- Clases Resource ---
class ArticulosResource(Resource):
    @marshal_with(articulo_fields)
    def get(self):
        articulos = ArticuloModel.query.all()
        return articulos, 200
    
    @marshal_with(articulo_fields)
    def post(self):
        args = articulo_args.parse_args()
        nuevo_articulo = ArticuloModel(**args)
        db.session.add(nuevo_articulo)
        db.session.commit()
        return nuevo_articulo, 201

class ArticuloResource(Resource):
    @marshal_with(articulo_fields)
    def get(self, articulo_id):
        articulo = ArticuloModel.query.get_or_404(articulo_id, description="Artículo no encontrado")
        return articulo, 200
    
    @marshal_with(articulo_fields)
    def patch(self, articulo_id):
        args = articulo_args.parse_args()
        articulo = ArticuloModel.query.get_or_404(articulo_id, description="Artículo no encontrado")
        
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
        articulo = ArticuloModel.query.get_or_404(articulo_id, description="Artículo no encontrado")
        db.session.delete(articulo)
        db.session.commit()
        return {"message": "Artículo eliminado"}, 200

class CategoriasResource(Resource):
    @marshal_with(categoria_fields)
    def get(self):
        categorias = CategoriaModel.query.all()
        return categorias, 200
    
    @marshal_with(categoria_fields)
    def post(self):
        args = categoria_args.parse_args()
        nueva_categoria = CategoriaModel(**args)
        db.session.add(nueva_categoria)
        db.session.commit()
        return nueva_categoria, 201

class CategoriaResource(Resource):
    @marshal_with(categoria_fields)
    def get(self, categoria_id):
        categoria = CategoriaModel.query.get_or_404(categoria_id, description="Categoría no encontrada")
        return categoria, 200

class ProveedoresResource(Resource):
    @marshal_with(proveedor_fields)
    def get(self):
        proveedores = ProveedorModel.query.all()
        return proveedores, 200
    
    @marshal_with(proveedor_fields)
    def post(self):
        args = proveedor_args.parse_args()
        nuevo_proveedor = ProveedorModel(**args)
        db.session.add(nuevo_proveedor)
        db.session.commit()
        return nuevo_proveedor, 201

class ProveedorResource(Resource):
    @marshal_with(proveedor_fields)
    def get(self, proveedor_id):
        proveedor = ProveedorModel.query.get_or_404(proveedor_id, description="Proveedor no encontrado")
        return proveedor, 200

# --- Rutas ---
api.add_resource(ArticulosResource, '/api/articulos')
api.add_resource(ArticuloResource, '/api/articulos/<int:articulo_id>')
api.add_resource(CategoriasResource, '/api/categorias')
api.add_resource(CategoriaResource, '/api/categorias/<int:categoria_id>')
api.add_resource(ProveedoresResource, '/api/proveedores')
api.add_resource(ProveedorResource, '/api/proveedores/<int:proveedor_id>')

@app.route('/')
def hello():
    return "<p>Hello, World!</p>"

if __name__ == '__main__':
    app.run(debug=True)
