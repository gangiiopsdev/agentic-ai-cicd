from fastapi import FastAPI
import subprocess
import shlex
def run_secure_command(command_parts):
    # Constructing the command safely using shlex.quote
    command = ' '.join(shlex.quote(part) for part in command_parts)
    # Executing the command securely without shell=True
    subprocess.run(command, check=True)
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    run_secure_command(['ping', host])
    return {"status": "completed"}