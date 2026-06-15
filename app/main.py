from fastapi import FastAPI
import subprocess
def execute_ping(host):
    args = ['ping', host]
    return subprocess.call(args)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return execute_ping(host)