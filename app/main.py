from fastapi import FastAPI
import subprocess
def safe_ping(host):
    # Safe implementation using list of arguments to prevent shell injection
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

app = FastAPI()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if not host.isalnum() and not '.' in host:
        raise HTTPException(status_code=400, detail='Invalid input')
    result = safe_ping(host)
    return {'status': 'completed', 'result': result}