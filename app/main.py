from fastapi import FastAPI
import subprocess
def ping(host: str):
    pinger = subprocess.Popen(['ping', host], stdout=subprocess.PIPE)
    pinger.wait()
    return {'status': 'completed'}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_host(host: str):
    return ping(host)