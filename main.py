from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum

# Import the API routers
from backend.square import router as square_router
from backend.hello import router as hello_router

# Define the API
api_app = FastAPI()

# Add a ping route to check health
@api_app.get("/ping")
def read_root():
    return {"message": "Pong!"}

# Define API routes
api_app.include_router(hello_router)
api_app.include_router(square_router)

# Define the Frontend
app = FastAPI()
app.mount("/api", api_app)
app.mount("/", StaticFiles(directory="frontend/build", html=True), name="build")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["8"],
    allow_headers=["*"],
)

# Define the Lambda handler
handler = Mangum(app)