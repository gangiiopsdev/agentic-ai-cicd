from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    cmd = ['ping'] + shlex.split(host)
    try:
        output = subprocess.run(cmd, capture_output=True, text=True, check=True, shell=False)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': str(e)}

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)