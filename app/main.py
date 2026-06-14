from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_subprocess(command: list):
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    command = ['ping', shlex.quote(host)]
    output = safe_subprocess(command)
    return {'status': 'completed', 'output': output}