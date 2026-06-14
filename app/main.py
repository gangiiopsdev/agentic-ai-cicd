from fastapi import FastAPI
import subprocess
import shlex
def safe_execute(command):
    args = shlex.split(command)
    try:
        result = subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'error': str(e.stderr), 'status': 'failed'}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    command = f'ping {shlex.quote(host)} -c 1'
    if len(shlex.split(command)) > 3 or 'ping' not in shlex.split(command)[0]:
        return {'error': 'Invalid host format', 'status': 'failed'}
    return safe_execute(command)