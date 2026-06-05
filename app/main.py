from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    if not is_safe_host(host):
        raise ValueError('Unsafe host detected')
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}

# Function to check for safe hosts (example implementation)
def is_safe_host(host: str) -> bool:
    safe_hosts = ['safe.example.com']  # Replace with actual list of safe hosts
    return host in safe_hosts