from flask import Response, json
from flask_restful import Resource, reqparse, abort, fields, marshal_with
from api.models import db, Articulo, Categoria, Proveedor  # Corregido para usar los nombres de los modelos correctos
import re

# --- Parsers para Artículos ---
articulo_args = reqparse.RequestParser()
articulo_args.add_argument("nombre", type=str, required=True, help="El nombre del artículo es obligatorio")
articulo_args.add_argument("descripcion", type=str)
articulo_args.add_argument("categoria_id", type=int, required=True, help="La categoría es obligatoria")
articulo_args.add_argument("proveedor_id", type=int, required=True, help="El proveedor es obligatorio")
articulo_args.add_argument("stock", type=int, required=True, help="El stock es obligatorio")
articulo_args.add_argument("precio", type=float, required=True, help="El precio es obligatorio")

# --- Fields para serializar Artículos ---
articulo_fields = {
    "id": fields.Integer,
    "nombre": fields.String,
    "descripcion": fields.String,
    "categoria_id": fields.Integer,
    "proveedor_id": fields.Integer,
    "stock": fields.Integer,
    "precio": fields.Float
}

# --- Controlador para Artículos ---
class ArticulosResource(Resource):
    @marshal_with(articulo_fields)
    def post(self):
        args = articulo_args.parse_args()
        nuevo_articulo = Articulo(  # Corregido para usar Articulo en lugar de Articulos
            nombre=args["nombre"],
            descripcion=args["descripcion"],
            categoria_id=args["categoria_id"],
            proveedor_id=args["proveedor_id"],
            stock=args["stock"],
            precio=args["precio"]
        )
        db.session.add(nuevo_articulo)
        db.session.commit()
        return nuevo_articulo, 201
    
    @marshal_with(articulo_fields)
    def get(self):
        articulos = Articulo.query.all()  # Corregido para usar Articulo
        return articulos

class ArticuloResource(Resource):
    @marshal_with(articulo_fields)
    def get(self, articulo_id):
        articulo = Articulo.query.filter_by(id=articulo_id).first()  # Corregido para usar Articulo
        if not articulo:
            abort(404, message="Artículo no encontrado")
        return articulo, 200
    
    @marshal_with(articulo_fields)
    def patch(self, articulo_id):
        args = articulo_args.parse_args()
        articulo = Articulo.query.filter_by(id=articulo_id).first()  # Corregido para usar Articulo
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
        articulo = Articulo.query.filter_by(id=articulo_id).first()  # Corregido para usar Articulo
        if not articulo:
            abort(404, message="Artículo no encontrado")
        db.session.delete(articulo)
        db.session.commit()
        return {"message": "Artículo eliminado"}, 200

# --- Parsers para Categorías ---
categoria_args = reqparse.RequestParser()
categoria_args.add_argument("categoria", type=str, required=True, help="El nombre de la categoría es obligatorio")

# --- Fields para serializar Categoría ---
categoria_fields = {
    "id": fields.Integer,
    "categoria": fields.String
}

# --- Controlador para Categorías ---
class CategoriasResource(Resource):
    @marshal_with(categoria_fields)
    def post(self):
        args = categoria_args.parse_args()
        nueva_categoria = Categoria(categoria=args["categoria"])  # Corregido para usar Categoria
        db.session.add(nueva_categoria)
        db.session.commit()
        return nueva_categoria, 201
    
    @marshal_with(categoria_fields)
    def get(self):
        categorias = Categoria.query.all()  # Corregido para usar Categoria
        return categorias

class CategoriaResource(Resource):
    @marshal_with(categoria_fields)
    def get(self, categoria_id):
        categoria = Categoria.query.filter_by(id=categoria_id).first()  # Corregido para usar Categoria
        if not categoria:
            abort(404, message="Categoría no encontrada")
        return categoria, 200
    
    @marshal_with(categoria_fields)
    def patch(self, categoria_id):
        args = categoria_args.parse_args()
        categoria = Categoria.query.filter_by(id=categoria_id).first()  # Corregido para usar Categoria
        if not categoria:
            abort(404, message="Categoría no encontrada")
        categoria.categoria = args["categoria"]
        db.session.commit()
        return categoria, 200
    
    @marshal_with(categoria_fields)
    def delete(self, categoria_id):
        categoria = Categoria.query.filter_by(id=categoria_id).first()  # Corregido para usar Categoria
        if not categoria:
            abort(404, message="Categoría no encontrada")
        db.session.delete(categoria)
        db.session.commit()
        return {"message": "Categoría eliminada"}, 200

# --- Parsers para Proveedores ---
proveedor_args = reqparse.RequestParser()
proveedor_args.add_argument("proveedor", type=str, required=True, help="El nombre del proveedor es obligatorio")

# --- Fields para serializar Proveedor ---
proveedor_fields = {
    "id": fields.Integer,
    "proveedor": fields.String
}

# --- Controlador para Proveedores ---
class ProveedoresResource(Resource):
    @marshal_with(proveedor_fields)
    def post(self):
        args = proveedor_args.parse_args()
        nuevo_proveedor = Proveedor(proveedor=args["proveedor"])  # Corregido para usar Proveedor
        db.session.add(nuevo_proveedor)
        db.session.commit()
        return nuevo_proveedor, 201
    
    @marshal_with(proveedor_fields)
    def get(self):
        proveedores = Proveedor.query.all()  # Corregido para usar Proveedor
        return proveedores

class ProveedorResource(Resource):
    @marshal_with(proveedor_fields)
    def get(self, proveedor_id):
        proveedor = Proveedor.query.filter_by(id=proveedor_id).first()  # Corregido para usar Proveedor
        if not proveedor:
            abort(404, message="Proveedor no encontrado")
        return proveedor, 200
    
    @marshal_with(proveedor_fields)
    def patch(self, proveedor_id):
        args = proveedor_args.parse_args()
        proveedor = Proveedor.query.filter_by(id=proveedor_id).first()  # Corregido para usar Proveedor
        if not proveedor:
            abort(404, message="Proveedor no encontrado")
        proveedor.proveedor = args["proveedor"]
        db.session.commit()
        return proveedor, 200
    
    @marshal_with(proveedor_fields)
    def delete(self, proveedor_id):
        proveedor = Proveedor.query.filter_by(id=proveedor_id).first()  # Corregido para usar Proveedor
        if not proveedor:
            abort(404, message="Proveedor no encontrado")
        db.session.delete(proveedor)
        db.session.commit()
        return {"message": "Proveedor eliminado"}, 200
