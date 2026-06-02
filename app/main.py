from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host):
    # Safe implementation using shlex.quote to escape arguments
    args = ['ping', shlex.quote(host)]
    subprocess.run(args, check=True)
app = FastAPI()
@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}
@app.get('/safe-ping')
def safe_ping_route(host: str):
    try:
        safe_ping(shlex.quote(host))
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}