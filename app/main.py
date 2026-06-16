from fastapi import FastAPI
import subprocess

def run_ping(host):
    try:
        # Sanitize the host input to prevent command injection
        if not host.isalnum() or ' ' in host:
            raise ValueError('Invalid host input')
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Use a whitelist of allowed hosts or validate the host input more strictly
    allowed_hosts = ['example.com', 'test.com']
    if host not in allowed_hosts:
        raise ValueError('Invalid host input')
    return run_ping(host)