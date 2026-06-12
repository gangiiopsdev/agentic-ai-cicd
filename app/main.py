from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    # Use shlex.quote to safely quote arguments
    args = ['ping', '-c', '1'] + shlex.split(host)
    goodPing = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = goodPing.communicate()
    if error:
        return {'status': 'failed', 'error': error.decode()}
    else:
        return {'status': 'completed', 'output': output.decode()}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)