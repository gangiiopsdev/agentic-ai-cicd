from fastapi import FastAPI
import subprocess
import re
def is_valid_host(host):
    pattern = r'^([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])$'
    if re.match(pattern, host):  # Simple IP address validation
        return True
    return False
generate_ping_command = lambda host: f"ping {host}" if is_valid_host(host) else None

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        command = generate_ping_command(host)
        if command is not None:
            subprocess.call(command, shell=False)
            return {"status": "completed"}
        else:
            return {"status": "failed", "error": "Invalid host"}
    except Exception as e:
        return {"status": "failed", "error": str(e)}