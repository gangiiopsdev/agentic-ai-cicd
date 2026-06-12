from fastapi import FastAPI
import subprocess
def ping(host: str):
    try:
        # Sanitize input to avoid command injection
        host = subprocess.call(['ping', '-c', '1', host], timeout=5, check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}

app = FastAPI()
@app.get("/ping")
def ping_route(host: str):
    return ping(host)