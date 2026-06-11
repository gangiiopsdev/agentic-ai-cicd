from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    try:
        # Sanitize the host using shlex.quote to ensure it is a valid command line argument
        sanitized_host = shlex.quote(host)
        subprocess.call(['ping', sanitized_host], shell=False)
        return {'status': 'completed'}
    except Exception as e:
        return {'error': str(e)}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)