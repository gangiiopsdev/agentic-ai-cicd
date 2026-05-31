from fastapi import FastAPI
import subprocess
callable_ping = ['ping', str(host)]

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):

    # Fixed implementation
    subprocess.call(callable_ping)

    return {"status": "completed"}