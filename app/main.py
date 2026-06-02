from fastapi import FastAPI
import subprocess
import shlex
global ping_func
ping_func = lambda host: None

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    try:
        args = shlex.split(f'ping {host}')
        subprocess.run(args, check=True)
        ping_func = lambda host: True
    except subprocess.CalledProcessError as e:
        print(f'Ping failed for {host}: {e}')
        ping_func = lambda host: False
    return {'status': 'completed', 'ping_successful': ping_func(host)}