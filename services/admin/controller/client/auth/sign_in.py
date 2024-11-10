from fastapi import HTTPException
from database.mongodb import client_collection
from services.passwordHashing import verify_password
from services.my_jwt import encode_jwt


async def signInClientController(data):
    mail = data.mail
    password = data.password
    print(f"Attempting to sign in with email: {mail}, password: {password}")
    
    if not mail and not password:
        return HTTPException(status_code=400, detail="all filed must be needed")

    
    try:
        # Find user by email and password
        user = await client_collection.find_one({"mail": mail})
        check_password = verify_password(plain_password=password, hashed_password=user['password'])
        token = encode_jwt({'id':str(user['_id']),'name':user['name'], 'mail':user['mail']})
        # print(check_password)
        
        if user and check_password:
            # print(f"User found: {user}")
            return {
                "msg": "User signed in successfully",
                "id": str(user['_id']),
                "token":token
            }
        else:
            raise HTTPException(status_code=400, detail="Invalid credentials")
    
    except Exception as e:
        print(f"Error occurred: {str(e)}")
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")