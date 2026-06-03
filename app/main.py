from fastapi import FastAPI
import subprocess
def safe_ping(host):
    # Ensure host input is safe by validating and sanitizing it
    allowed_hosts = ['example.com', 'test.com']
    if host in allowed_hosts:
        try:
            return subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        except subprocess.CalledProcessError as e:
            raise ValueError(f'Ping failed: {e}')
    else:
        raise ValueError('Invalid host')
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    return {'status': safe_ping(host)}