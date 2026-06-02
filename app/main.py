from fastapi import FastAPI
import subprocess
from shlex import quote

def safe_ping(host: str):
    try:
        result = subprocess.run(['ping', quote(host)], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': str(e)}

app = FastAPI()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if not host.isalnum():
        return {'status': 'error', 'output': 'Invalid input'}
    try:
        result = subprocess.run(['nslookup', quote(host)], capture_output=True, text=True, check=True)
        address = result.stdout.split('Address: ')[1].strip()
        return safe_ping(address)
    except (subprocess.CalledProcessError, IndexError) as e:
        return {'status': 'error', 'output': str(e)}