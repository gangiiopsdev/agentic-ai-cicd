from fastapi import FastAPI
import subprocess
callable_ping = lambda host: subprocess.call(['ping', host])

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    callable_ping(host)
    return {"status": "completed"}