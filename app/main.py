from fastapi import FastAPI, HTTPException
import subprocess

app = FastAPI()

def safe_ping(host: str):
    allowed_hosts = ['example.com', 'another-example.com']  # Replace with actual allowed hosts
    if host not in allowed_hosts:
        raise ValueError("Invalid host")
    args = ['ping', '-c', '1', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

@app.get("/ping")
def ping(host: str):
    output = safe_ping(host)
    return {'status': 'completed', 'output': output}