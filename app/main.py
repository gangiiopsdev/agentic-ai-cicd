from fastapi import FastAPI, HTTPException
import subprocess
import shlex
globally_allowed_hosts = ['example.com']

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if host not in globally_allowed_hosts:
        raise HTTPException(status_code=403, detail='Unauthorized host')
    try:
        result = subprocess.run(['ping', shlex.quote(host)], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        raise HTTPException(status_code=500, detail=f'Ping failed: {e}')