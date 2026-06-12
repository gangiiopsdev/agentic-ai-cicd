from fastapi import FastAPI
import subprocess
import shlex
from fastapi.exceptions import HTTPException

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
    command = ['ping', shlex.quote(host)]
    subprocess.run(command, check=True)
    return {'status': 'completed'}