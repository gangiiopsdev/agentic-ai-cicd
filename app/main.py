from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_host(host):
    return shlex.quote(host)

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    safe_host = sanitize_host(host)
    try:
        result = subprocess.run(['ping', '-c', '1', safe_host], check=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}