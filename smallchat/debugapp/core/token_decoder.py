import json
import jwt

APP_SECRET = "51d53142-1528-4067-8be2-4ebca222776c"

class TokenDecoder:

    def __init__(self, jwt_token):

        self.jwt_token = jwt_token

    def decode_token(self):

        return jwt.decode(self.jwt_token, APP_SECRET, algorithms=['HS256'])