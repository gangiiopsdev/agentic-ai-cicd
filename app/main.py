from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not is_safe_host(host):
        return {'status': 'error', 'message': 'Invalid host'}
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}

def is_safe_host(host: str) -> bool:
    allowed_hosts = ['127.0.0.1', '::1']  # Example allowed hosts
    return host in allowed_hosts