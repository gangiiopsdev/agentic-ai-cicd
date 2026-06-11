from fastapi import FastAPI
import subprocess
import shlex
import ipaddress

def safe_ping(host: str) -> str:
    try:
        ipaddress.ip_address(host)
    except ValueError:
        raise ValueError('Invalid IP address')
    args = ['ping'] + [shlex.quote(h.strip()) for h in shlex.split(host)]
    output = subprocess.run(args, capture_output=True, text=True, check=True, shell=False)  # Ensure shell=False
    return output.stdout

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        result = safe_ping(host)
        return {'status': 'completed', 'output': result}
    except ValueError as e:
        return {'status': 'failed', 'error': str(e)}