from fastapi import FastAPI
import subprocess
def safe_ping(host):
    valid_hosts = ['example.com', 'another.example.com']
    if host in valid_hosts:
        args = ['ping', host]
        subprocess.call(args)
        return {"status": "completed"}
    else:
        return {"error": "Invalid host"}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)