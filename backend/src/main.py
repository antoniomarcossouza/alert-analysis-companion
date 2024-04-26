import uvicorn
from fastapi import FastAPI

app = FastAPI(
    title="Alert Review Helper",
    version="1.0.0",
    docs_url="/docs",
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        log_level="debug",
        reload=True,
    )
