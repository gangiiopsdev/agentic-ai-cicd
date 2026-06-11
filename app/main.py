from fastapi import FastAPI
import subprocess
generate_command = ['ping', host]

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Safer implementation
    if not validate_host(host):
        return {'status': 'invalid host'}, 400
    subprocess.call(['ping', host])
    return {'status': 'completed'}

def validate_host(host: str) -> bool:
    allowed_hosts = ['127.0.0.1', '::1']  # Example list of allowed hosts
    return host in allowed_hosts