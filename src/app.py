from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from api.extensions import db
from api.controllers import User, Users
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with, abort

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db.init_app(app)
# db = SQLAlchemy(app)
api = Api(app)


with app.app_context():
    db.create_all()

# class UserModel(db.Model):
#    id = db.Column(db.Integer, primary_key=True)
#    username = db.Column(db.String(80), unique=True, nullable=False)
#    email = db.Column(db.String(120), unique=True, nullable=False)

#    def __repr__(self):
#        return f"User (username = {self.username}, email: {self.email})>"
    
#user_args = reqparse.RequestParser()
#user_args.add_argument("username", type=str, required=True, help="Username is required")
#user_args.add_argument("email", type=str, required=True, help="Email is required")

# userFields = {
#    "id": fields.Integer,
#    "username": fields.String,
#    "email": fields.String
# }

#class Users(Resource):
#    @marshal_with(userFields)
#    def post(self):
#        args = user_args.parse_args()
#        user = UserModel(username=args["username"], email=args["email"])
#        db.session.add(user)
#        db.session.commit()
#        users = UserModel.query.all()
#        return users, 201
#    
#    @marshal_with(userFields)
#    def get(self):
#        users = UserModel.query.all()
#        return users
    
#class User(Resource):
#    @marshal_with(userFields)
#    def get(self, user_id):
#        user = UserModel.query.filter_by(id=user_id).first()
#        if not user:
#            abort(404, message="User not found")
#        return user, 200
#    
#    @marshal_with(userFields)
#    def patch(self, user_id):
#        args = user_args.parse_args()
#        user = UserModel.query.filter_by(id=user_id).first()
#        if not user:
#            abort(404, message="User not found")
#        user.name = args["username"]
#        user.email = args["email"]
#        db.session.commit()
#        return user, 200
    
#    @marshal_with(userFields)
#    def delete(self, user_id):
#        user = UserModel.query.filter_by(id=user_id).first()
#        if not user:
#            abort(404, message="User not found")
#        db.session.delete(user)
#        db.session.commit()
#        users = UserModel.query.all()
#        return users

api.add_resource(Users, "/api/users/")
api.add_resource(User, "/api/users/<int:user_id>")


@app.route('/')

def hello():
    return "<p>Hello, World!</p>"

if __name__ == '__main__':
    app.run(debug=True)

