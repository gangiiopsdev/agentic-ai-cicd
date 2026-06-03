from fastapi import FastAPI
import subprocess
from fastapi.responses import JSONResponse
import shlex

class SafeSubprocess:
    @staticmethod
def run(command: str, *args, **kwargs):
        command = shlex.split(command)
        return subprocess.run(command, *args, **kwargs)

app = FastAPI()

async def is_safe_host(host):
    # Implement your logic to check if the host is safe
    return True

def validate_host(host):
    allowed_hosts = ['example.com', 'test.com']  # Example list of allowed hosts
    return host in allowed_hosts

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return JSONResponse(content={"error": "Host is not safe"}, status_code=400)
    try:
        result = SafeSubprocess.run(f'ping {host}', capture_output=True, text=True, timeout=5, check=True)
        return JSONResponse(content={"status": "completed", "output": result.stdout}, status_code=200)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=400)