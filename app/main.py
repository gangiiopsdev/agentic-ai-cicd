from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Fixed implementation with argument quoting to mitigate shell injection risk
    subprocess.call(['ping', host])

    return {"status": "completed"}