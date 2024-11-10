from fastapi import APIRouter, HTTPException
from model.client import ClientModel
from database.mongodb import client_collection
from datetime import datetime
from services.passwordHashing import hash_password, verify_password
from services.my_jwt import encode_jwt

from controller.client.auth.sign_in import signInClientController

clientAuthRouter = APIRouter()

# Sign-In Endpoint
@clientAuthRouter.post("/sign-in")
async def adminSignIn(data: ClientModel):
    return await signInClientController(data=data)


# Sign-Up Endpoint
@clientAuthRouter.post("/sign-up")
async def adminSignUp(data: ClientModel):
    name = data.name
    mail = data.mail
    password = data.password
    createAt = data.createdAt
    updateAt = data.updateAt 
    role = "client"
    
    if not name and not mail and not password:
        return HTTPException(status_code=400, detail="all filed required")

    try:
        # Check if the email already exists
        existing_user = await client_collection.find_one({'mail': mail})
        if existing_user:
            raise HTTPException(status_code=400, detail="User already exists")
        
        newpassword = hash_password(password=password)

        # Insert new user data into MongoDB
        user_data = {
            'name': name,
            'mail': mail,
            'password': newpassword,
            'role':role,
            'createdAt': createAt,
            'updatedAt': updateAt
        }
        res = await client_collection.insert_one(user_data)
        print(res)

        # If insert successful, return success
        if res.inserted_id:
            token = encode_jwt({'id':str(res.inserted_id),'name':name, 'mail':mail, 'role':role})
            return {"msg": "User created successfully", "id": str(res.inserted_id), "token":token}
        
        raise HTTPException(status_code=400, detail="Failed to create user")
    
    except Exception as e:
        # Handle any exception during the sign-up process
        print(f"Error occurred: {str(e)}")
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")

# Uncomment the forget-password route when ready
@clientAuthRouter.get("/forget-password")
async def adminForgetPassword(data: ClientModel):
    mail = ClientModel.mail
    
    if not mail: 
        return HTTPException(status_code=400, detail="mail must be required")
    
    try:
        user = await client_collection.find_one({'mail': mail})
        if not user:
            raise HTTPException(status_code=400, detail="User Not exists")
        
        
        
    
    except Exception as e:
        pass
    
    
    return data
