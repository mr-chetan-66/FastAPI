# .venv/Scripts/activate


from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

import models
from database import engine
from db_route import router

app=FastAPI()
app.include_router(router)


from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

models.Base.metadata.create_all(engine)
app.mount('/images',StaticFiles(directory='images'),name="images")