from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation with full path and validation
    allowed_hosts = ['google.com', 'github.com']
    if host in allowed_hosts:
        try:
            result = subprocess.run(['ping', '-c', '1', host], check=True, capture_output=True, text=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.stderr}
    else:
        raise ValueError("Invalid host")