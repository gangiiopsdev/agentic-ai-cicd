from fastapi import FastAPI
import subprocess
generate_safe_command = {'ping': ['ping', '{}']}
app = FastAPI()
@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}
@app.get('/ping')
def ping(host: str):
    if host in generate_safe_command:
        subprocess.call(generate_safe_command[host])
    else:
        raise ValueError('Unsafe input detected')
    return {'status': 'completed'}