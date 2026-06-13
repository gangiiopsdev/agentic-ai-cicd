from fastapi import FastAPI
import subprocess
class SafeSubprocess:
    @staticmethod
def ping(host: str):
        safe_host = subprocess.quote(host)
        subprocess.run(['ping', safe_host], check=True, text=True)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_safe(host: str):
    SafeSubprocess.ping(host)
    return {'status': 'completed'}