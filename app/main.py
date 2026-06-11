from fastapi import FastAPI
import subprocess
import shlex

def safe_ping(host: str):
    # Safe implementation
    command = ['ping', host]
    sanitized_host = shlex.quote(host)
    full_command = command + [sanitized_host]
    try:
        subprocess.run(full_command, check=True, shell=False)
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    result = safe_ping(host)
    if isinstance(result, dict) and 'error' in result:
        return result
    else:
        return {'status': 'completed'}