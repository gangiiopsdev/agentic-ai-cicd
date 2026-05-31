from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate input to prevent command injection
    allowed_hosts = ['example.com', 'test.com']
    if host not in allowed_hosts:
        return "Invalid host"
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, timeout=5)
        return result.stdout
    except Exception as e:
        return str(e)