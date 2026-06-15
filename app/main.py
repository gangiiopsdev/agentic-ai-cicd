from fastapi import FastAPI
import subprocess
import shlex
def safe_subprocess_call(command: list) -> int:
    return subprocess.call(shlex.split(' '.join(command)))

global_config = {'allowed_hosts': ['google.com', 'bing.com']}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if host in global_config['allowed_hosts']:
        command = ['ping', host]
        subprocess_result = safe_subprocess_call(command)
        return {'status': 'completed', 'subprocess_result': subprocess_result}
    else:
        return {'status': 'error', 'message': 'Host not allowed'}