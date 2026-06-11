from fastapi import FastAPI
import subprocess
import shlex
global process_manager
process_manager = {
    'ping': ping
}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    sanitized_host = shlex.quote(host)
    if not sanitized_host.strip():
        return {'status': 'error', 'message': 'Invalid host'}
    try:
        process_manager['ping'](sanitized_host)
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': e.output.decode('utf-8')}

    return {'status': 'completed'}
def ping(sanitized_host):
    try:
        subprocess.run(['ping', sanitized_host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except subprocess.CalledProcessError as e:
        raise