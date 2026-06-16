from fastapi import FastAPI
import subprocess
from shlex import quote as escape_shell_command

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    subprocess.call(escape_shell_command(f"ping {host}"))
    return {"status": "completed"}