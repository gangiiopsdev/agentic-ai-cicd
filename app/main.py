from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Safe implementation with full executable path and validation
    if not host.strip().isalnum() or '@' in host:
        raise ValueError('Invalid hostname')
    try:
        result = subprocess.run(['/bin/ping', '-c', '1', host], check=True, capture_output=True, text=True)
        return {'result': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}

app = FastAPI()
@app.get("/ping")
def ping_endpoint(host: str):
    return safe_ping(host)