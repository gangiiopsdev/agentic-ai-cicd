from fastapi import FastAPI
import subprocess
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return JSONResponse(content={'status': 'completed', 'output': result.stdout})
    except subprocess.CalledProcessError as e:
        return JSONResponse(content={'status': 'failed', 'error': str(e)}, status_code=500)