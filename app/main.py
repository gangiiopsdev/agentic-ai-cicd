from fastapi import FastAPI
import subprocess
def execute_ping(host):
    args = ['ping', host]
    subprocess.call(args, shell=False)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    execute_ping(host)
    return {"status": "completed"}