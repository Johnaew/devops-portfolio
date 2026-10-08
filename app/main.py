from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI(title="DevOps Portfolio Demo")


@app.get("/")
def home():
	return {"message": "My DevOps portfolio app is running"}


@app.get("/health")
def health():
	return {"status": "healthy"}


Instrumentator().instrument(app).expose(app, include_in_schema=False)
