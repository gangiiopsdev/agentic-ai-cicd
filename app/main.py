from fastapi import FastAPI
import subprocess
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation using check_output to capture output and handle errors
    try:
        result = subprocess.check_output(['ping', host], text=True, stderr=subprocess.STDOUT)
        return JSONResponse(content={'status': 'completed', 'output': result}, status_code=200)
    except subprocess.CalledProcessError as e:
        return JSONResponse(content={'status': 'failed', 'error': e.output}, status_code=500)