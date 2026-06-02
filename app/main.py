from fastapi import FastAPI, HTTPException
import subprocess
def safe_ping(host: str):
    allowed_hosts = ['example.com', 'another-example.com']  # Replace with actual allowed hosts
    if host not in allowed_hosts:
        raise ValueError("Invalid host")
    args = ['ping', '-c', '1', host]
    result = subprocess.run(args, capture_output=True, text=True, check=False)
    return result.stdout
def ping(host: str):
    output = safe_ping(host)
    return {'status': 'completed', 'output': output}

app = FastAPI()
@app.get("/ping")
def ping_endpoint(host: str):
    if host not in ['example.com', 'another-example.com']:
        raise HTTPException(status_code=403, detail="Invalid host")
    return {'status': 'completed', 'output': output}