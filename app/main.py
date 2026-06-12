from fastapi import FastAPI
import subprocess
global pinger
pinger = subprocess.Popen(['ping', 'example.com'], stdout=subprocess.PIPE)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    global pinger
    pinger.terminate()
    pinger.wait()
    return {'status': 'completed'}