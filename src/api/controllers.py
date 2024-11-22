from flask import Flask, Response
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with, abort
from api.models import UserModel, db
import json, re

user_args = reqparse.RequestParser()
user_args.add_argument("username", type=str, required=True, help="Username is required")
user_args.add_argument("email", type=str, required=True, help="Email is required")

userFields = {
    "id": fields.Integer,
    "username": fields.String,
    "email": fields.String
}

class Users(Resource):
    @marshal_with(userFields)
    def post(self):
        args = user_args.parse_args()

        if not args['username'] or args['username'].isspace():
            response=Response(json.dumps({'error':'Username cannot be empty'}),
            status=400,
            mimetype='application/json')
            return abort(response)
        if not args['email'] or args['email'].isspace():
            response=Response(json.dumps({'error':'Email cannot be empty'}),
            status=400,
            mimetype='application/json')
            return abort(response)

        email = args['email'].strip()
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            response=Response(json.dumps({'error':'Invalid email format'}),
            status=400,
            mimetype='application/json')
            return abort(response) 

        user = UserModel(username=args["username"], email=args["email"])
        db.session.add(user)
        db.session.commit()
        users = UserModel.query.all()
        return users, 201
    
    @marshal_with(userFields)
    def get(self):
        users = UserModel.query.all()
        return users
    
class User(Resource):
    @marshal_with(userFields)
    def get(self, user_id):
        user = UserModel.query.filter_by(id=user_id).first()
        if not user:
            abort(404, message="User not found")
        return user, 200
    
    @marshal_with(userFields)
    def patch(self, user_id):
        args = user_args.parse_args()
        user = UserModel.query.filter_by(id=user_id).first()
        if not user:
            abort(404, message="User not found")
        user.username = args["username"]
        user.email = args["email"]
        db.session.commit()
        return user, 200
    
    @marshal_with(userFields)
    def delete(self, user_id):
        user = UserModel.query.filter_by(id=user_id).first()
        if not user:
            abort(404, message="User not found")
        db.session.delete(user)
        db.session.commit()
        users = UserModel.query.all()
        return users