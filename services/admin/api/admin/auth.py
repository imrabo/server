from fastapi import APIRouter, HTTPException
from model.admin import AdminModel
from database.mongodb import admin_collection
from datetime import datetime
from services.passwordHashing import hash_password, verify_password
from services.my_jwt import encode_jwt

adminAuthRouter = APIRouter()

# Sign-In Endpoint
@adminAuthRouter.post("/sign-in")
async def adminSignIn(data: AdminModel):
    mail = data.mail
    password = data.password
    print(f"Attempting to sign in with email: {mail}, password: {password}")
    
    if not mail and not password:
        return HTTPException(status_code=400, detail="all filed must be needed")

    
    try:
        # Find user by email and password
        user = await admin_collection.find_one({"mail": mail})
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


# Sign-Up Endpoint
@adminAuthRouter.post("/sign-up")
async def adminSignUp(data: AdminModel):
    name = data.name
    mail = data.mail
    password = data.password
    createAt = data.createdAt
    updateAt = data.updateAt 
    role = "admin"
    
    if not name and not mail and not password:
        return HTTPException(status_code=400, detail="all filed required")

    try:
        # Check if the email already exists
        existing_user = await admin_collection.find_one({'mail': mail})
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
        res = await admin_collection.insert_one(user_data)
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
# @adminAuthRouter.get("/forget-password")
# async def adminForgetPassword(data: ForgetPasswordAdminScheme):
#     return data
