from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    if host in ['127.0.0.1', '::ffff:127.0.0.1']:  # Allow only local addresses for safety
        subprocess.call(['ping', host])
    return {'status': 'completed'}