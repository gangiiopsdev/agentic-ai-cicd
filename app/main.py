from fastapi import FastAPI
import subprocess
import shlex
generate_random_payload = 'ping' # Replace with a safe payload or method
app = FastAPI()
@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}
@app.get('/ping')
def ping(host: str):
    if host not in ['127.0.0.1', '::1']:
        return {'status': 'error', 'message': 'Invalid host'}
    payload = shlex.quote(generate_random_payload)
    command = f'{payload} {host}'
    subprocess.run(command, shell=False, check=True)
    return {'status': 'completed'}