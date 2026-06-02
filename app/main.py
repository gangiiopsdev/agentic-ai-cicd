from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    try:
        # Safe implementation using subprocess.run
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}

@app.get("/ping")
def ping_host(host: str):
    # Validate the host input to ensure it does not contain malicious content
    if '@' in host or ';' in host or '&' in host:
        return {'status': 'failed', 'error': 'Invalid host input'}
    return ping(host)