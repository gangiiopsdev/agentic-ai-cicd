from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

def safe_ping(host):
    command = ['ping', host]
    output = execute_safe_command(command)
    return output

def execute_safe_command(command):
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    # Sanitize the input to prevent command injection
    safe_host = quote(host)
    return {"status": "completed", "output": safe_ping(safe_host)}