from fastapi import FastAPI
import subprocess
from fastapi.responses import JSONResponse

app = FastAPI()

def ping(host: str):
    # Secure implementation
    if not is_safe_host(host):
        return JSONResponse(status_code=400, content={'error': 'Invalid host'}), False
    args = ['ping', f'"{host}"']  # Escape the command line argument to prevent injection
    subprocess.call(args, shell=False)  # Ensure shell=False to avoid shell injection
    return None, True

def is_safe_host(host: str):
    # Implement safe hostname check
    allowed_hosts = ['example.com', 'test.com']
    return host in allowed_hosts

@app.get("/ping")
def ping_endpoint(host: str): 
    result, success = ping(host)
    if not success:
        return result
    return {'status': 'Pong'}