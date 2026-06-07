from fastapi import FastAPI
import subprocess
import shlex
def ping(host: str):
    # Safe implementation using subprocess.run
    args = shlex.split(f'ping {host}')
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'stdout': result.stdout, 'stderr': result.stderr}

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    if not is_valid_host(host):
        raise HTTPException(status_code=400, detail="Invalid host")
    return ping(host)

def is_valid_host(host: str) -> bool:
    # Add logic to validate the host input
    allowed_hosts = ['example.com', 'test.example.com']
    return host in allowed_hosts