from fastapi import FastAPI
import subprocess
def safe_ping(host):
    try:
        return subprocess.run(['ping', host], check=True)
    except subprocess.CalledProcessError as e:
        raise Exception(f'Ping failed: {e}')

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return {'status': safe_ping(host)}