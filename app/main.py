from fastapi import FastAPI
import subprocess
import os

app = FastAPI()

def escape_shell_command(command: str) -> str:
    return ''.join(shlex.quote(arg) for arg in shlex.split(command))

@app.get("/ping")
def ping(host: str):
    try:
        escaped_host = escape_shell_command(host)
        result = subprocess.run(['ping', escaped_host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except Exception as e:
        return {"status": "error", "message": str(e)}