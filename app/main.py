from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str) -> dict:
    # Enhanced validation to prevent injection attacks
    allowed_hosts = ['8.8.8.8', '127.0.0.1']
    if host not in allowed_hosts:
        return {'status': 'error', 'output': 'Invalid input'}
    try:
        result = subprocess.run(['ping'], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)