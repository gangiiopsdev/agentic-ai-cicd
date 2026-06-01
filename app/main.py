from fastapi import FastAPI
import subprocess
import shlex

def safe_ping(host: str):
    ping_command = ['ping', shlex.quote(host)]
    subprocess.run(ping_command, stdout=subprocess.DEVNULL)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    safe_ping(host)
    return {'status': 'completed'}