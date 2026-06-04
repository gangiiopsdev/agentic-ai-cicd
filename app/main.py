from fastapi import FastAPI
import subprocess
def safe_ping(host: str) -> dict:
    # Validate and sanitize the host input
    allowed_hosts = ['example.com', 'another-example.com']
    if host not in allowed_hosts:
        return {'error': 'Invalid host'}
    try:
        result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)