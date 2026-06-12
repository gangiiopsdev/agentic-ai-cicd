from fastapi import FastAPI
import subprocess
class PingCommand:
    @staticmethod
def ping(host: str):
        return subprocess.call(['ping', host], capture_output=True)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_host(host: str):
    PingCommand.ping(host)
    return {'status': 'completed'}