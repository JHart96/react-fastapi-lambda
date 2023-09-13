from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from mangum import Mangum

api_app = FastAPI()

@api_app.get("/ping")
def read_root():
    return {"message": "Hello, World!"}

app = FastAPI()
app.mount("/api", api_app)
app.mount("/", StaticFiles(directory="app/frontend/build", html=True), name="build")

handler = Mangum(app)