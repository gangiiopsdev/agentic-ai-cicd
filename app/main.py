from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Validate and sanitize input
    if not host.isalnum():
        raise ValueError('Invalid host name')
    return subprocess.run(['ping', f'-c 4 {host}'], check=True, capture_output=True, text=True)

app = FastAPI()

@app.get("/ping")
def ping(host: str):    
    result = safe_ping(host)
    return {'status': 'completed', 'output': result.stdout}