from fastapi import FastAPI
import subprocess
import shlex
def run_secure_command(command_parts):
    command = ' '.join(shlex.quote(part) for part in command_parts)
    subprocess.run(command, shell=False, check=True)
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    # Validate and sanitize input
    if not host.isalnum() or len(host) > 64:
        raise ValueError("Invalid host")
    run_secure_command(['ping', host])
    return {"status": "completed"}