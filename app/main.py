from fastapi import FastAPI
import subprocess

def is_valid_host(host: str) -> bool:
    # Simple example of host validation
    return '.' in host and len(host.split('.')) == 4

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        raise ValueError('Invalid host provided')
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True, check=False)
    return {'stdout': result.stdout, 'stderr': result.stderr}