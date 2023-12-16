from fastapi import FastAPI
from fastapi.responses import JSONResponse


app = FastAPI()


@app.get("/")
def index():
    return JSONResponse(
        content={
            "message": "Hello from Vercel!"
        }
    )
