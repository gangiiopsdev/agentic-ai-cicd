from fastapi import FastAPI
import subprocess
import shlex
def validate_host(host):
    # Simple validation to allow only alphanumeric and hyphen characters
    if not host.isalnum() and '-' not in host:
        raise ValueError("Invalid host")

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        validate_host(host)
        args = shlex.split(f'ping {host}')  # Avoid using shlex.quote for the command itself
        subprocess.run(args, check=True)
        return {"status": "completed"}
    except ValueError as e:
        return {"error": str(e)}