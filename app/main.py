from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host):
    if not host.isnumeric():
        return {'status': 'error', 'message': 'Invalid host'}
    command = ['ping'] + [arg.strip() for arg in shlex.split(host) if arg.strip()]
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    return {'status': 'completed', 'output': output.decode('utf-8'), 'error': error.decode('utf-8')}
app = FastAPI()
@app.get('/ping')
def ping(host: str):
    return safe_ping(host)