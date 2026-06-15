from fastapi import FastAPI
import subprocess
import shlex
from shlex import quote

generate_ping_command = ['ping', '{}']

def safe_subprocess(command):
    try:
        result = subprocess.run(command, check=True, text=True, capture_output=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e.stderr)

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize input to prevent command injection
    sanitized_host = host.strip()
    if not all(c.isalnum() or c in [',', '.', '-', '_'] for c in sanitized_host):
        return {"status": "error", "message": "Invalid host name"}
    safe_command = ['ping', quote(sanitized_host)]
    result = safe_subprocess(safe_command)
    return {"status": "completed", "output": result}