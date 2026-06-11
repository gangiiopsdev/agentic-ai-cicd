from fastapi import FastAPI
import subprocess

app = FastAPI()

allowed_hosts = ['example.com', '127.0.0.1']
def safe_ping(host: str):
    if host not in allowed_hosts:
        raise ValueError('Invalid host')
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

@app.get("/ping")
def ping(host: str):
    output = safe_ping(host)
    return {"status": "completed", "output": output}