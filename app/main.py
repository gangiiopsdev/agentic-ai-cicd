from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

def ping(host: str):
    args = ['ping', quote(host)]
    result = subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {'status': 'completed', 'output': result.stdout.decode('utf-8')}

app.get('/')(home)
app.get('/ping')(ping)