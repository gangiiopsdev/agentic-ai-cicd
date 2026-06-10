from fastapi import FastAPI
import subprocess
cimport = {'ping': ['8.8.8.8', '127.0.0.1']}

app = FastAPI()

@app.get('/')
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get('/ping')
def ping(host: str):
    if host in cimport['ping']:
        subprocess.run(['ping', host], capture_output=True, text=True)
        return {"status": "completed"}
    else:
        return {"status": "error", "message": "Invalid host"}