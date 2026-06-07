from fastapi import FastAPI
import subprocess
import shlex
def escape_host(host: str) -> str:
    return shlex.quote(host)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    host = escape_host(host)
    command = ['ping', host]
    result = subprocess.run(command, capture_output=True, text=True)
    return {'status': result.stdout}