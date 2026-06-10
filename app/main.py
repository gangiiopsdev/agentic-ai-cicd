from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    allowed_hosts = ['google.com', 'example.com']
    if host not in allowed_hosts:
        raise ValueError('Host not allowed')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        # Sanitize the input to prevent shell injection
        sanitized_host = subprocess.list2cmdline([host])
        result = subprocess.run(['/usr/bin/ping', '-c', '1', sanitized_host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}