from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Sanitize input to prevent shell injection
    safe_host = ''.join(filter(str.isalnum, host))
    args = ['ping', safe_host]
    subprocess.run(args, check=True)
    return {'status': 'completed'}