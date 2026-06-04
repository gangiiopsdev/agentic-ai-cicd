from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if host in ['localhost', '127.0.0.1']:
        subprocess.call(['ping', host], shell=False)
        return {"status": "completed"}
    else:
        raise ValueError("Unsafe host")

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)