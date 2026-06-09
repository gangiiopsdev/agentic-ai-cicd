from fastapi import FastAPI
import subprocess
from fastapi import HTTPException
from shlex import quote as cmd_quote

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if not host.isalnum() or len(host) > 255:
        raise HTTPException(status_code=400, detail='Invalid hostname')
    result = subprocess.run(['ping', cmd_quote(host)], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}