from .extensions import db

class Articulos(db.Model):
    __tablename__ = 'Articulos'  # Nombre de la tabla en la base de datos
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    nombre = db.Column(db.String(80), nullable=False)
    descripcion = db.Column(db.String(200))
    categoria_id = db.Column(db.Integer, db.ForeignKey('Categorias.id'), nullable=False)
    proveedor_id = db.Column(db.Integer, db.ForeignKey('Proveedores.id'), nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    precio = db.Column(db.Float, nullable=False)
    
    # Relaciones con otras tablas
    categoria = db.relationship('Categoria', back_populates='articulos')
    proveedor = db.relationship('Proveedor', back_populates='articulos')

    def __repr__(self):
        return f"<Articulo (nombre={self.nombre}, precio={self.precio})>"

class Categorias(db.Model):
    __tablename__ = 'Categorias'
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    categoria = db.Column(db.String(80), unique=True, nullable=False)
    
    # Relación con Articulos
    articulos = db.relationship('Articulo', back_populates='categoria')

    def __repr__(self):
        return f"<Categoria (nombre={self.categoria})>"

class Proveedores(db.Model):
    __tablename__ = 'Proveedores'
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    proveedor = db.Column(db.String(80), unique=True, nullable=False)
    
    # Relación con Articulos
    articulos = db.relationship('Articulo', back_populates='proveedor')

    def __repr__(self):
        return f"<Proveedor (nombre={self.proveedor})>"
