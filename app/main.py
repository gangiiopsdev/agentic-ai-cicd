from fastapi import FastAPI
import subprocess
import shlex
generate_ping_command = ['ping', '{host}']

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    safe_host = shlex.quote(host)
    result = subprocess.call(generate_ping_command + [safe_host])
    return {'status': 'completed', 'result': result}