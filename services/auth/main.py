from fastapi import FastAPI
from database.mongodb import get_db_status

# app routes import
from api.admin.auth import adminAuthRouter



app = FastAPI()

# admin routes
app.include_router(adminAuthRouter,  prefix="/admin/auth",) 

