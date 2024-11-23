from flask import Flask, json
from api.controllers import Articulos, Articulo, Categorias,Categoria,Proveedores,Proveedor  
from flask_sqlalchemy import SQLAlchemy  
from api.models import  db, Articulos,Categorias,Proveedores
from unittest.mock import MagicMock, patch, Mock
from flask_restful import Api
import unittest
import pytest

@pytest.fixture
def app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['TESTING'] = True

    db.init_app(app)

    with app.app_context():
        db.create_all()
        yield app
    with app.app_context():
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()


def test_create_proveedor(client):
    response = client.post('/proveedores', json={'proveedor': 'Tech Supplier'})
    assert response.status_code == 201
    assert response.get_json()[0]['proveedor'] == 'Tech Supplier'

def test_get_proveedores(client):
    response = client.get('/proveedores')
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)

def test_delete_proveedor(client):
    # Crear y luego eliminar un proveedor
    response = client.post('/proveedores', json={'proveedor': 'Best Supplies'})
    proveedor_id = response.get_json()[0]['id']

    delete_response = client.delete(f'/proveedores/{proveedor_id}')
    assert delete_response.status_code == 200
    assert response.get_json() == []  # Verifica que no hay proveedores después de eliminarlo








def test_create_categoria(client):
    response = client.post('/categorias', json={'categoria': 'Electrónica'})
    assert response.status_code == 201
    assert response.get_json()[0]['categoria'] == 'Electrónica'

def test_get_categorias(client):
    response = client.get('/categorias')
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)

def test_get_categoria_no_existente(client):
    response = client.get('/categorias/999')
    assert response.status_code == 404
    assert response.get_json()['message'] == 'Categoría no encontrada'









def test_create_articulo(client):
    # Crear un nuevo artículo
    response = client.post('/articulos', json={
        'nombre': 'Laptop ASUS',
        'descripcion': 'Laptop gaming',
        'categoria_id': 1,
        'proveedor_id': 1,
        'stock': 10,
        'precio': 1500.00
    })
    assert response.status_code == 201
    data = response.get_json()
    assert data[0]['nombre'] == 'Laptop ASUS'

def test_get_articulos(client):
    # Obtener la lista de artículos
    response = client.get('/articulos')
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)

def test_get_articulo_no_existente(client):
    # Intentar obtener un artículo inexistente
    response = client.get('/articulos/999')  # ID inexistente
    assert response.status_code == 404
    assert response.get_json()['message'] == 'Artículo no encontrado'

def test_delete_articulo(client):
    # Crear y luego eliminar un artículo
    response = client.post('/articulos', json={
        'nombre': 'Monitor Dell',
        'descripcion': 'Monitor 27 pulgadas',
        'categoria_id': 1,
        'proveedor_id': 1,
        'stock': 5,
        'precio': 300.00
    })
    articulo_id = response.get_json()[0]['id']

    delete_response = client.delete(f'/articulos/{articulo_id}')
    assert delete_response.status_code == 200
    assert delete_response.get_json() == []  # Verifica que la lista de artículos esté vacía











#def test_user_get_not_found(client):
#    response = client.get('/users/999')
#    assert response.status_code == 404
#
#def test_verify_email(client):
#    mock_users_repository = MagicMock()
#    mock_users_repository.get_all.return_value = {
#            "email": "john@usebouncer.com",
#            "status": "deliverable",
#            "reason": "accepted_email",
#            "domain": {
#                "name": "usebouncer.com",
#                "acceptAll": "no",
#                "disposable": "no",
#                "free": "no"
#            },
#            "account": {
#                "role": "no",
#                "disabled": "no",
#                "fullMailbox": "no"
#            },
#            "dns": {
#                "type": "MX",
#                "record": "aspmx.l.google.com."
#            },
#            "provider": "google.com",
#            "score": 100,
#            "toxic": "unknown"
#            }
#    assert mock_users_repository.get_all.return_value["status"] == "deliverable"
#    assert mock_users_repository.get_all.return_value["reason"] == "accepted_email"
#
#@patch.object(User, 'get')
#def test_user_get(mock_get):
#    mock_user = Mock()
#    mock_user.id = 1
#    mock_user.username = 'XXXX'
#    mock_user.email = 'XXXX@XXXX.com'
#    mock_get.return_value = mock_user
#
#    result = User.get()
#    assert result == mock_user
#    assert result.id == 1
#    assert result.username == 'XXXX'
#    assert result.email == 'XXXX@XXXX.com'
#    mock_get.assert_called_once()
#
#class TestUser(unittest.TestCase):
#    def setUp(self):
#       self.app = Flask(__name__)
#       self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
#       self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#       self.api = Api(self.app)
#       self.api.add_resource(User, '/users/<int:user_id>')
#       self.client = self.app.test_client()
#       self.app_context = self.app.app_context()
#       self.app_context.push()
#       db.init_app(self.app)
#       db.create_all()
#    
#    @patch('api.controllers.UserModel.query')
#    def test_get(self, mock_query):
#        mock_query.filter_by.return_value.first.return_value = UserModel(id=1, username='test', email='test@test.com')
#
#        response = self.client.get('/users/1')
#
#        self.assertEqual(response.status_code, 200)
#        self.assertIn('test', response.get_data(as_text=True))
#        self.assertIn('test@test.com', response.get_data(as_text=True))