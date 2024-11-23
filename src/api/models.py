from .extensions import db

class Articulo(db.Model):
    __tablename__ = 'articulos'  # Usar nombres de tablas en plural para consistencia
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    nombre = db.Column(db.String(80), nullable=False)
    descripcion = db.Column(db.String(200))
    categoria_id = db.Column(db.Integer, db.ForeignKey('categorias.id'), nullable=False)
    proveedor_id = db.Column(db.Integer, db.ForeignKey('proveedores.id'), nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    precio = db.Column(db.Float, nullable=False)
    
    # Relaciones con otras tablas
    categoria = db.relationship('Categoria', back_populates='articulos')
    proveedor = db.relationship('Proveedor', back_populates='articulos')

    def __repr__(self):
        return f"<Articulo (nombre={self.nombre}, precio={self.precio})>"

class Categoria(db.Model):
    __tablename__ = 'categorias'  # Usar nombres de tablas en plural
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    categoria = db.Column(db.String(80), unique=True, nullable=False)
    
    # Relación con Articulo
    articulos = db.relationship('Articulo', back_populates='categoria')

    def __repr__(self):
        return f"<Categoria (nombre={self.categoria})>"

class Proveedor(db.Model):
    __tablename__ = 'proveedores'  # Usar nombres de tablas en plural
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    proveedor = db.Column(db.String(80), unique=True, nullable=False)
    
    # Relación con Articulo
    articulos = db.relationship('Articulo', back_populates='proveedor')

    def __repr__(self):
        return f"<Proveedor (nombre={self.proveedor})>"
