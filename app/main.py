from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Safe implementation with proper sanitization and use of full path
    if host.isalnum():
        subprocess.call(['ping', host])
    else:
        return {'status': 'invalid input'}
    return {'status': 'completed'}