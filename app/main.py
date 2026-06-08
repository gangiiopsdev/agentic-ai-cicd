from fastapi import FastAPI
import subprocess
class SafePing:
    def __init__(self):
        self.ping_command = ['ping', '-c', '1']

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    safe_host = subprocess.list2cmdline([host])
    subprocess.run(SafePing.ping_command + [safe_host], check=True)
    return {'status': 'completed'}