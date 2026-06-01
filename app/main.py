from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Validate the host input to ensure it's safe to use in a subprocess call
    if not is_safe_host(host):
        raise ValueError('Unsafe host input')
    args = ['ping', host]
    try:
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return e.stderr

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    output = safe_ping(host)
    return {'status': 'completed', 'output': output}

def is_safe_host(host: str) -> bool:
    # Implement your own validation logic here to ensure the host is safe
    allowed_hosts = ['example.com', 'localhost']
    return host in allowed_hosts