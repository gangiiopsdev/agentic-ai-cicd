from fastapi import FastAPI
import subprocess
from fastapi.responses import JSONResponse

app = FastAPI()

def run_ping(host: str):
    if not is_valid_host(host):
        return JSONResponse(status_code=400, content={'error': 'Invalid host'}).
    args = ['ping', host]
    subprocess.run(args, check=True)

def is_valid_host(host: str) -> bool:
    allowed_hosts = ['example.com', '127.0.0.1']  # Replace with actual validation logic
    return host in allowed_hosts

@app.get("/ping")
def ping(host: str):
    result = run_ping(host)
    if isinstance(result, JSONResponse):
        return result
    return {'status': 'completed'}