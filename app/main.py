from fastapi import FastAPI
import subprocess
class Ping:
    def __init__(self, host):
        self.host = host

def ping(host: str):
    # Safe implementation using subprocess.run with shell=False
    subprocess.call(['ping', host], shell=False)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_endpoint(host: str):
    ping_instance = Ping(host)
    return {'status': 'completed'}