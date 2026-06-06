from fastapi import FastAPI
import subprocess
def execute_safe_ping(host):
    # Safe implementation
    cmd = ['ping', host]
    subprocess.run(cmd, check=True)

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Sanitize input to prevent command injection
    if not host.isalnum():
        return {'error': 'Invalid characters in host'}
    try:
        execute_safe_ping(host)
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}
    return {'status': 'completed'}