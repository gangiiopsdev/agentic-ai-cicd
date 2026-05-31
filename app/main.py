from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    # Sanitize the host parameter
    allowed_hosts = ['example.com', 'test.com']  # Define a whitelist of allowed hosts
    if host not in allowed_hosts:
        raise ValueError('Invalid host')
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

@app.get("/ping")
def ping(host: str):
    response = safe_ping(host)
    return {"status": "completed", "output": response}