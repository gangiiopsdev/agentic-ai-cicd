from fastapi import FastAPI
import subprocess
from shlex import quote
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if not all(c.isalnum() or c in ['-', '.', '_'] for c in host):
        return JSONResponse(status_code=400, content={'error': 'Invalid input'})
    try:
        output = subprocess.check_output(['ping', quote(host)], stderr=subprocess.STDOUT, timeout=10)
        return {'status': 'completed', 'output': output.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return JSONResponse(status_code=500, content={'error': e.output.decode('utf-8')})