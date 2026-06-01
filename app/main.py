from fastapi import FastAPI
import subprocess
global_params = {'ping': 'ping'}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if host in global_params:
        subprocess.call([global_params[host], host])
    else:
        return {"error": "Invalid command"}
    return {"status": "completed"}