from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize input
    if not all(c.isalnum() or c in [".", "-"] for c in host):
        return {'status': 'failed', 'error': 'Invalid hostname'}
    return safe_ping(host)