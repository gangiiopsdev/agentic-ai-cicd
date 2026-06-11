from fastapi import FastAPI
import subprocess
from shlex import quote

def safe_subprocess(command: str, *args):
    cmd_parts = [arg for arg in command.split(' ')]
    subprocess.run(cmd_parts, check=True)

app = FastAPI()

@app.get("/ping")
def ping(host: str):  
    # Sanitize input to prevent command injection
    safe_host = quote(host)
    if not safe_host:
        raise ValueError("Invalid input")
    try:
        result = subprocess.run(['ping', '-c', '1'] + [safe_host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}