from fastapi import FastAPI
import subprocess
import shlex

global_app = FastAPI()

@global_app.get("/ping")
def ping(host: str):
    # Safe implementation with input validation and sanitization
    if not host.isalnum():
        return {"status": "error", "message": "Invalid hostname"}
    args = shlex.split(f'ping {host}')
    result = subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {"status": "completed", "output": result.stdout.decode()}