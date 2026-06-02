from fastapi import FastAPI
import subprocess
import shlex

def safe_ping(host):
    # Use shlex.split to safely split the command into arguments
    args = shlex.split('ping ' + host)
    result = subprocess.run(args, capture_output=True, text=True, check=False)
    return {'status': 'completed', 'output': result.stdout}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)