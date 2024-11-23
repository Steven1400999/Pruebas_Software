from flask import Flask, json
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
import unittest
import pytest
from api.models import db, Articulo, Categoria, Proveedor

# Evitar importaciones duplicadas
from api.controllers import ArticuloResource, ArticulosResource, CategoriaResource, CategoriasResource, ProveedorResource, ProveedoresResource

# Configuración de pytest para la aplicación
@pytest.fixture
def app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['TESTING'] = True

    db.init_app(app)

    # Registrar las rutas de las API
    api = Api(app)
   # api.add_resource(ProveedorResource, '/proveedores')
   # api.add_resource(CategoriaResource, '/categorias')
   # api.add_resource(ArticuloResource, '/articulos')
    api.add_resource(ArticulosResource, '/api/articulos')
    api.add_resource(ArticuloResource, '/api/articulos/<int:articulo_id>')
    api.add_resource(CategoriasResource, '/api/categorias')
    api.add_resource(CategoriaResource, '/api/categorias/<int:categoria_id>')
    api.add_resource(ProveedoresResource, '/api/proveedores')
    api.add_resource(ProveedorResource, '/api/proveedores/<int:proveedor_id>')
    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

# Pruebas para proveedores
def test_create_proveedor(client):
    response = client.post('/api/proveedores', json={'proveedor': 'Tech Supplier'})
    assert response.status_code == 201
    assert response.get_json()['proveedor'] == 'Tech Supplier'

def test_get_proveedores(client):
    response = client.get('/api/proveedores')
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)

def test_delete_proveedor(client):
    response = client.post('/api/proveedores', json={'proveedor': 'Best Supplies'})
    proveedor_id = response.get_json()['id']

    delete_response = client.delete(f'/api/proveedores/{proveedor_id}')
    assert delete_response.status_code == 200
    assert client.get('/api/proveedores').get_json() == []  # Confirma que la lista está vacía

# Pruebas para categorías
def test_create_categoria(client):
    response = client.post('/api/categorias', json={'categoria': 'Electrónica'})
    assert response.status_code == 201
    assert response.get_json()['categoria'] == 'Electrónica'

def test_get_categorias(client):
    response = client.get('/api/categorias')
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)

def test_get_categoria_no_existente(client):
    response = client.get('/api/categorias/999')
    assert response.status_code == 404
    assert response.get_json()['message'] == 'Categoría no encontrada'

# Pruebas para artículos
def test_create_articulo(client):
    # Primero crear un proveedor y una categoría
    client.post('/api/proveedores', json={'proveedor': 'Tech Supplier'})
    client.post('/api/categorias', json={'categoria': 'Electrónica'})
    
    # Luego crear el artículo
    response = client.post('/api/articulos', json={
        'nombre': 'Laptop ASUS',
        'descripcion': 'Laptop gaming',
        'categoria_id': 1,
        'proveedor_id': 1,
        'stock': 10,
        'precio': 1500.00
    })
    assert response.status_code == 201
    data = response.get_json()
    assert data['nombre'] == 'Laptop ASUS'

def test_get_articulos(client):
    response = client.get('/api/articulos')
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)

def test_get_articulo_no_existente(client):
    response = client.get('/api/articulos/999')
    assert response.status_code == 404
    assert response.get_json()['message'] == 'Artículo no encontrado'

def test_delete_articulo(client):
    # Primero crear un proveedor, categoría y artículo
    client.post('/api/proveedores', json={'proveedor': 'Best Supplier'})
    client.post('/api/categorias', json={'categoria': 'Accesorios'})
    response = client.post('/api/articulos', json={
        'nombre': 'Monitor Dell',
        'descripcion': 'Monitor 27 pulgadas',
        'categoria_id': 1,
        'proveedor_id': 1,
        'stock': 5,
        'precio': 300.00
    })
    articulo_id = response.get_json()['id']

    # Luego eliminar el artículo
    delete_response = client.delete(f'/api/articulos/{articulo_id}')
    assert delete_response.status_code == 200
    assert client.get('/api/articulos').get_json() == []  # Confirma que la lista está vacía
