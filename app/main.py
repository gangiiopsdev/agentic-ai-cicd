from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host):
    try:
        # Sanitize the host input using a whitelist approach or regex
        allowed_hosts = ['example.com', 'test.com']  # Example list of allowed hosts
        if host in allowed_hosts:
            result = subprocess.run(shlex.split(f'ping {host}'), capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': result.stdout}
        else:
            return {'status': 'error', 'output': 'Invalid host'}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': str(e)}

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)