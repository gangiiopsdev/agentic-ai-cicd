from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def safe_ping(host):
        ping_command = ['ping', host]
        result = subprocess.run(ping_command, capture_output=True, text=True)
        return result.stdout,

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return SafePing.safe_ping(host)