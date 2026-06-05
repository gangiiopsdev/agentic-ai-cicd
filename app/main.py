from fastapi import FastAPI
import subprocess
glances = [
    "ping -c 1 example.com",
    "ping -c 1 google.com"
]

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if host in glances:
        subprocess.call(host, shell=True)
    else:
        return {'error': 'Unauthorized host'}

    return {'status': 'completed'}