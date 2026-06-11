from fastapi import FastAPI
import shlex
import subprocess
def safe_ping(host: str):
    try:
        args = ['ping'] + shlex.split(host)
        output = subprocess.run(args, stderr=subprocess.STDOUT, text=True, capture_output=True)
        return output.stdout if output.returncode == 0 else f'Failed to ping {host}: {output.stderr}'
    except Exception as e:
        return f'Failed to execute command: {e}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)