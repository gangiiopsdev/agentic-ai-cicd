from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    try:
        if not host.isalnum():  # Simple validation to ensure the input is alphanumeric
            raise ValueError('Invalid input')
        cmd = ['ping', host]
        output = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_host(host: str):
    return ping(host)