"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User
from api.utils import generate_sitemap, APIException

#jay added at start of project (1)
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required

api = Blueprint('api', __name__)
#jay added at start of project (2)
# Create a route to authenticate your users and return JWTs. The # create_access_token() function is used to actually generate the JWT. #jay added at start of project (3) changed from app.roujte to api.route
@api.route("/token", methods=["POST"])
def create_token():
    email = request.json.get("email", None)
    password = request.json.get("password", None)
    if email != "test" or password != "test":
        return jsonify({"msg": "Bad email or password"}), 401

    access_token = create_access_token(identity=email)
    return jsonify(access_token=access_token)

# Protect a route with jwt_required, which will kick out requests
# without a valid JWT present.
@api.route("/hello", methods=["GET"])
@jwt_required()
def get_hello():
    msg = {"message": "Hello from the backend!"}
    return jsonify(msg)