from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Sanitize input and use a full path for the command
    safe_host = shlex.quote(host)
    subprocess.call(['/bin/ping', safe_host])
    return {'status': 'completed'}