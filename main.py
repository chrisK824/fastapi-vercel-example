import uvicorn
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


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8080)