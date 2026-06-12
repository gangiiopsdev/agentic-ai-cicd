from fastapi import FastAPI
import subprocess
def safe_ping(host):
    # Use a whitelist of allowed hosts or use parameterized inputs
    allowed_hosts = ['example.com', 'test.com']
    if host in allowed_hosts:
        args = ['ping', host]
        subprocess.run(args, check=True)
    return {"status": "completed"}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)