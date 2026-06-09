from fastapi import FastAPI
import subprocess
def validate_host(host: str):
    # Simple validation example
    allowed_hosts = ['example.com', 'localhost']
    return host in allowed_hosts

app = FastAPI()

def ping(host: str):
    if not validate_host(host):
        raise ValueError('Invalid host')
    try:
        args = ['ping', host]
        result = subprocess.run(args, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_safe(host: str):
    return ping(host)