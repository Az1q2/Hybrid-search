from fastapi import FastAPI

app = FastAPI(
    title="Hybrid Search & RAG Engine",
    description="Hybrid search",
    version="0.1.0"
)

@app.get("/healthcheck", tags=["System"])
async def healthcheck():
    # проверка статуса сервиса, если всё нормально, то выводит ок
    return {
        "status": "ok",
        "version": app.version
    }