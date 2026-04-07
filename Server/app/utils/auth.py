import jwt
import datetime
from flask import current_app

def create_jwt(user_id):
    payload = {
        "user_id": user_id,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    }
    return jwt.encode(payload, current_app.config['SECRET_KEY'], algorithm="HS256")
###Add create_jwt function for generating JSON Web Tokens
