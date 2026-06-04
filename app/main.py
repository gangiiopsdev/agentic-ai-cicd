from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def safe_ping(host):
    # Validate host input to allow only alphanumeric characters and dots
    if not re.match(r'^[a-zA-Z0-9.]+$', host):
        return 'Invalid host'
    try:
        result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, timeout=5)
        return result.stdout
    except Exception as e:
        return str(e)

def escape_command(command: str) -> str:
    # Escape any potentially dangerous characters in the command
    escaped_command = ''.join([c if c.isalnum() or c.isspace() else '_' for c in command])
    return escaped_command

@app.get("/ping")
def ping(host: str):
    safe_host = escape_command(host)
    return {"status": safe_ping(safe_host)}