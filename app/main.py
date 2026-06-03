from fastapi import FastAPI
import subprocess
import shlex
def execute_ping(host: str):
    # Sanitize the host input to prevent command injection
    safe_host = shlex.quote(host)
    try:
        output = subprocess.run(['ping', '-c', '1', safe_host], stderr=subprocess.PIPE, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}

app = FastAPI()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return execute_ping(host)