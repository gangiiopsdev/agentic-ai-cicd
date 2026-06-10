from fastapi import FastAPI
import subprocess
def safe_subprocess(command: str, args: list):
    if any(arg.startswith('-') for arg in args):
        raise ValueError(f'Command {command} contains shell-escaped arguments.')
    subprocess.run([command] + args, check=True, capture_output=True)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not host.isalnum():  # Basic validation to avoid shell injection
        raise ValueError('Invalid host name')
    safe_subprocess('ping', [host])
    return {"status": "completed"}