from fastapi import FastAPI
from config import cors
from apps.api.view import router
from apps.constant import constant

# Create app object and add routes to it
app = FastAPI(title="Testing", middleware=cors.middleware)

# routes
app.include_router(router, prefix=f"/api/{constant.API_V1}")