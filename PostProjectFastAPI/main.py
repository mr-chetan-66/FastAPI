# .venv/Scripts/activate


from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

import models
from database import engine
from db_route import router

app=FastAPI()
app.include_router(router)


origin=[
    'https://localhost:3000'
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origin,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

models.Base.metadata.create_all(engine)
app.mount('/images',StaticFiles(directory='images'),name="images")