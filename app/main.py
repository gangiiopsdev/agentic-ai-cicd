from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation using subprocess.Popen with shell=False and arguments explicitly passed
    if host in ['127.0.0.1', '::1']:  # Example allowed hosts, adjust as needed
        subprocess.call(['ping', host])
    else:
        return {'error': 'Invalid host'}
    return {'status': 'completed'}