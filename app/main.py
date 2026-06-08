from fastapi import FastAPI
import subprocess
from shlex import quote as escape_shell_arg

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    safe_host = ' '.join([escape_shell_arg(arg) for arg in host.split()])
    result = subprocess.run(['ping', safe_host], capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}