from fastapi import FastAPI
import subprocess
import shlex
global ping
ping = None
app = FastAPI()
@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}
@app.get('/ping')
def ping(host: str):
    global ping
    if ping is None:
        args = shlex.split(f'ping -c 4 {host}')  # Limit the number of pings to avoid abuse
        ping = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False)
    return {
        'status': 'completed',
        'output': ping.stdout.decode('utf-8') if ping is not None else '',
        'error': ping.stderr.decode('utf-8') if ping is not None else ''
    }