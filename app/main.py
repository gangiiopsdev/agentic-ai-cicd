from fastapi import FastAPI
import subprocess
import shlex

global app = FastAPI()

def safe_subprocess(command: str, args: list) -> None:
    full_command = [command] + shlex.split(' '.join(args))
    subprocess.run(full_command, check=True)

@app.get("/ping")
def ping(host: str):
    # Safe implementation with input validation
    if not host.strip().endswith('.com') or '.' not in host:
        return {"error": "Invalid host"}
    safe_subprocess("ping", [host])
    return {"status": "completed"}