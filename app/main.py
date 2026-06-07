from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    # Use shlex.quote to safely escape host input
    ping_command = ['ping', shlex.quote(host)]
    subprocess.run(ping_command, check=True)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        safe_ping(host)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}