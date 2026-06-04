from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    subprocess.run(['ping', host], check=True)

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        safe_ping(host)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}