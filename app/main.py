from fastapi import FastAPI
import subprocess
global_params = {'host': None}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    global_params['host'] = host
    command = ['ping', global_params['host']]
    subprocess.call(command)
    return {"status": "completed"}