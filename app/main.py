from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate input to prevent injection attacks
    if not host.isalnum() or len(host) > 64:
        return {'error': 'Invalid input for host'}

    try:
        result = subprocess.run(['ping', shlex.quote(host)], check=True, capture_output=True, shell=False)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'error': str(e.stderr)}

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}