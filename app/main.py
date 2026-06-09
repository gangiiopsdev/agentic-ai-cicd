from fastapi import FastAPI
import subprocess
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Sanitize input to prevent command injection
    safe_host = subprocess.quote(host)
    args = ['ping', safe_host]
    try:
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        return JSONResponse(content={'status': 'completed', 'output': result.stdout}, status_code=200)
    except subprocess.CalledProcessError as e:
        return JSONResponse(content={'status': 'error', 'output': e.stderr}, status_code=500)