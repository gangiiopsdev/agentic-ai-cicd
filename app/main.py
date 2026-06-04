from fastapi import FastAPI
import subprocess
def run_ping(host):
    # Use shlex.quote to safely escape the input
    safe_host = subprocess.list2cmdline([host])
    subprocess.call(f'ping {safe_host}', shell=False)
app = FastAPI()
@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}
@app.get('/ping')
def ping(host: str):
    run_ping(host)
    return {'status': 'completed'}