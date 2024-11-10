# jwt_utils.py
import jwt
from datetime import datetime, timedelta, timezone

SECRET_KEY = 'key'

def encode_jwt(payload: dict):
    """
    Encode a payload to create a JWT token.
    :param payload: dict
    :return: str (JWT token)
    """
    payload['exp'] = datetime.now(timezone.utc) + timedelta(hours=1)  # Set expiration time to 1 hour
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return token

def decode_jwt(token: str):
    """
    Decode a JWT token to get the payload.
    :param token: str
    :return: dict (decoded payload)
    :raises Exception: if token is expired or invalid
    """
    try:
        decoded_payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return decoded_payload
    except jwt.ExpiredSignatureError:
        raise Exception("Token has expired")  # More specific error message for expired token
    except jwt.InvalidTokenError:
        raise Exception("Invalid token")  # More specific error message for invalid token

# # Example usage (uncomment to test)
# if __name__ == "__main__":
#     # Example payload
#     payload = {"user_id": 123, "username": "john_doe"}
    
#     # Encode JWT
#     token = encode_jwt(payload)
#     print("Encoded JWT:", token)
    
#     # Decode JWT
#     try:
#         decoded_payload = decode_jwt(token)
#         print("Decoded Payload:", decoded_payload)
#     except Exception as e:
#         print(f"Error: {e}")
