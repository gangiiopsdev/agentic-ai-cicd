from fastapi import FastAPI
import subprocess
def safe_ping(host):
    # Validate and sanitize the host input
    allowed_hosts = ['example.com', 'test.com']
    if host not in allowed_hosts:
        raise ValueError('Host is not allowed')
    cmd = ['ping', '-c', '1', host]
    result = subprocess.run(cmd, check=True, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)