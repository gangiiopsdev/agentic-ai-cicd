from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        command = ['ping', host]
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        if result.returncode == 0:
            return {'status': 'completed', 'output': result.stdout}
        else:
            return {'status': 'failed', 'error': result.stderr}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}