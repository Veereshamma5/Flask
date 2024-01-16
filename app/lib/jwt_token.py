import jwt
import hashlib


class JwtToken:
    @staticmethod
    def create_sha256_hash(text):
        hash = hashlib.sha256()
        hash.update(text.encode())
        return hash.hexdigest()

    @staticmethod
    def validate_token(token, client_id, client_secret):
        try:
            key_text = f'{client_id}:{client_secret}'
            print("KEY TEXT IS:::::::::::", key_text)
            jwt_key = JwtToken.create_sha256_hash(key_text)
            print("JWT_KEY IS::::::", jwt_key)
            jwt_payload = jwt.decode(token, jwt_key)

        except jwt.ExpiredSignatureError:
            return False
        except jwt.InvalidTokenError:
            print("Inside Invalid token")
            return False

        return jwt_payload
