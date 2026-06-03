from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Sanitize the host input to prevent injection attacks
    safe_host = shlex.quote(host)
    try:
        result = subprocess.run(['ping', safe_host], check=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}