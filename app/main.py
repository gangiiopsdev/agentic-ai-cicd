from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    if not host or not isinstance(host, str):
        raise ValueError('Invalid host input')
    ping_command = ['ping', shlex.quote(host)]
    try:
        subprocess.run(ping_command, check=True, stdout=subprocess.DEVNULL)
    except subprocess.CalledProcessError as e:
        print(f'Ping failed with error: {e}')

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    safe_ping(host)
    return {'status': 'completed'}