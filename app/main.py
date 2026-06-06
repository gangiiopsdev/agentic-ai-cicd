from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Sanitize input to prevent shell injection
    if '/' in host or '\' in host:
        raise ValueError("Invalid hostname")
    args = ['ping', '-c', '1', host]
    result = subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return result.stdout.decode('utf-8')

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    safe_ping_output = safe_ping(host)
    return {'status': 'completed', 'output': safe_ping_output}