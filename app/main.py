from fastapi import FastAPI
import subprocess
global host
host = 'example.com'

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str=host):
    args = ['ping', host]
    subprocess.call(args)
    return {"status": "completed"}