from fastapi import FastAPI, HTTPException
import subprocess
import shlex
global_config = {
    'ALLOWED_HOSTS': ['localhost', '127.0.0.1'],
}
app = FastAPI()
@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}
@app.get('/ping')
def ping(host: str):
    if host not in global_config['ALLOWED_HOSTS']:
        raise HTTPException(status_code=403, detail='Host not allowed')
    # Secure implementation
    args = shlex.split(f'ping {host}')
    subprocess.run(args, check=True, capture_output=True)
    return {'status': 'completed'}