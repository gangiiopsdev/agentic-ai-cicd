from fastapi import FastAPI
import subprocess
from fastapi.responses import JSONResponse

app = FastAPI()

def run_ping(host: str):
    if not is_valid_host(host):
        return JSONResponse(status_code=400, content={'error': 'Invalid host'})
    args = ['ping', '--', host]
    result = subprocess.run(args, capture_output=True, text=True)
    if result.returncode != 0:
        return JSONResponse(status_code=500, content={'error': result.stderr.strip()})
    return {'output': result.stdout.strip()}

def is_valid_host(host: str) -> bool:
    allowed_hosts = ['example.com', '127.0.0.1']  # Replace with actual validation logic
    return host in allowed_hosts

@app.get("/ping")
def ping(host: str):
    result = run_ping(host)
    if isinstance(result, JSONResponse):
        return result
    return {'status': 'completed'}