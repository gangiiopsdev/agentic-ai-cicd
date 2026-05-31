from fastapi import FastAPI
import subprocess
def safe_ping(host: str) -> dict:
    if not host or 'ping' not in host or host == '.' or host.startswith('-') or host.startswith('/'):  # Basic validation
        return {'status': 'error', 'output': 'Invalid input'}
    try:
        result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)