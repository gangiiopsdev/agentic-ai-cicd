from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Sanitize input to prevent command injection
    allowed_hosts = ['example.com', 'localhost']
    if host not in allowed_hosts:
        return {'status': 'error', 'message': 'Invalid host'}
    try:
        output = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': e.stderr}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)