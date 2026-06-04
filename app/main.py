from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    try:
        # Safe implementation using subprocess.run with shell=False and quoting to prevent command injection
        result = subprocess.run(shlex.split(f'ping {host}'), capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return str(e)

def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    status = safe_ping(host)
    return {'status': status}