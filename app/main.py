from fastapi import FastAPI
import subprocess
from fastapi.responses import JSONResponse
def safe_ping(host: str):
    if not host.isalnum():
        return JSONResponse(content={'error': 'Invalid input'}, status_code=400)
    try:
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return JSONResponse(content={'status': 'completed', 'stdout': result.stdout.decode(), 'stderr': result.stderr.decode() if result.stderr else None}, status_code=200)
    except subprocess.CalledProcessError as e:
        return JSONResponse(content={'error': str(e)}, status_code=500)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if not host.isalnum():
        return JSONResponse(content={'error': 'Invalid input'}, status_code=400)
    try:
        result = subprocess.run(['ping', '-c', '1', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return JSONResponse(content={'status': 'completed', 'stdout': result.stdout.decode(), 'stderr': result.stderr.decode() if result.stderr else None}, status_code=200)
    except subprocess.CalledProcessError as e:
        return JSONResponse(content={'error': str(e)}, status_code=500)