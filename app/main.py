from fastapi import FastAPI
import subprocess
import shlex
def validate_host(host: str) -> bool:
    return host.isalnum() and ' ' not in host

async def execute_ping(host: str):
    if not validate_host(host):
        raise ValueError("Invalid host name")
    try:
        result = subprocess.run(shlex.split(f'ping -c 1 {host}'), check=True, capture_output=True, text=True)
        return {
            "status": "completed",
            "output": result.stdout
        }
    except subprocess.CalledProcessError as e:
        raise ValueError(str(e))

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return await execute_ping(host)