from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    if host == 'localhost':
        subprocess.call(['ping', host])
        return {'status': 'completed'}
    else:
        return {'error': 'Invalid host'}, 403

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)