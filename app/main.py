from fastapi import FastAPI
import subprocess
cimport ping3

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    response_time = ping3.ping(host)
    if response_time is not None:
        return {"status": "completed", "response_time": response_time}
    else:
        return {"status": "failed"}