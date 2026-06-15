from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

def ping(host: str):
    # Secure implementation
    args = ['ping', quote(host)]
    result = subprocess.run(args, check=True, timeout=5, capture_output=True, text=True)
    return {'stdout': result.stdout, 'stderr': result.stderr}

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)