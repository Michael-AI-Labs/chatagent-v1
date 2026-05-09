from fastapi import FastAPI
import uvicorn

from chat_route import router as chat_router


app = FastAPI()

app.include_router(chat_router)


@app.get("/health")
def health_check():
    return {"status": "ok"}


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True,
    )