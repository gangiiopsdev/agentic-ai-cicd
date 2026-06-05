from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_subprocess(command, args):
    return [' '.join([command] + [shlex.quote(arg) for arg in args])]

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        result = subprocess.run(safe_subprocess('ping', [host]), capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}