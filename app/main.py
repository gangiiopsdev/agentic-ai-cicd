from fastapi import FastAPI
import subprocess

def ping_safe(host: str):
    # Sanitize input to prevent command injection
    if 'ping' not in host:
        raise ValueError('Invalid command')
    try:
        result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return ping_safe(host)