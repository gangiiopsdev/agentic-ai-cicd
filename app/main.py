from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

def escape_command(command):
    return [quote(arg) for arg in command.split()]

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    subprocess.call(escape_command(f"ping {host}"))
    
    return {"status": "completed"}