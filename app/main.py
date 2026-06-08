from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    # Sanitize host input
    safe_host = shlex.quote(host)
    try:
        result = subprocess.run(['ping', safe_host], capture_output=True, text=True, shell=False)
        return {'status': 'completed', 'output': result.stdout}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)