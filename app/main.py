from fastapi import FastAPI
import subprocess
given_host = '8.8.8.8'

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation with input validation and sanitization
    allowed_hosts = ['8.8.8.8', '127.0.0.1']  # Example allowed hosts
    if host in allowed_hosts:
        subprocess.call(['ping', subprocess.list2cmdline([subprocess.escape(host)])])
    else:
        return {'error': 'Invalid host'}

    return {'status': 'completed'}