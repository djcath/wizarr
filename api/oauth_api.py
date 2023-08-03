from flask import send_file
from flask_jwt_extended import jwt_required, current_user
from flask_restx import Namespace, Resource


api = Namespace("OAuth", description="OAuth related operations", path="/oauth")

