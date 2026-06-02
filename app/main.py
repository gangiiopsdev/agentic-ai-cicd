from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def ping(host: str):
        safe_host = subprocess.quote(host)
        subprocess.run(['ping', safe_host], capture_output=True, text=True)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_route(host: str):
    SafePing.ping(host)
    return {'status': 'completed'}