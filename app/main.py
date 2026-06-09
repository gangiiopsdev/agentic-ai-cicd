from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Validate the input more strictly to avoid command injection
    allowed_hosts = ['example.com', 'localhost']
    if host not in allowed_hosts:
        return False
    args = ['ping', '-c', '1', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout
global app = FastAPI()
@app.get("/ping")
def ping(host: str):
    return {'status': safe_ping(host)}