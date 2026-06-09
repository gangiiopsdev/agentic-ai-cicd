from fastapi import FastAPI
import subprocess
def safe_execute(command: str):
    try:
        result = subprocess.run(command.split(), capture_output=True, check=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    safe_command = f'ping {host}'
    return safe_execute(safe_command)