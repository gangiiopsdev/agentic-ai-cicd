from fastapi import FastAPI
import subprocess
import shlex
def run_secure_command(command_parts):
    command = ' '.join(shlex.quote(part) for part in command_parts)
    subprocess.run(command, shell=False, check=True)
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    # Secure implementation
    allowed_hosts = ['127.0.0.1', '::1']  # Example of allowed hosts
    if host not in allowed_hosts:
        raise Exception("Invalid host")
    run_secure_command(['ping', host])
    return {"status": "completed"}