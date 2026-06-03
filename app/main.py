from fastapi import FastAPI
import subprocess
from fastapi import HTTPException

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate input to prevent command injection
    if not all(c.isalnum() or c in ['-', '.'] for c in host):
        raise HTTPException(status_code=400, detail='Invalid hostname')
    sanitized_host = subprocess.quote(host)
    args = ['ping', sanitized_host]
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'result': result.stdout}