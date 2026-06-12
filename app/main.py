from fastapi import FastAPI
import subprocess
import shlex
def sanitize_input(input_str):
    return ''.join(e for e in input_str if e.isalnum() or e in ['-', '.', ':', '@'])
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    # Use a whitelist of allowed hosts
    allowed_hosts = ["example.com", "test.com"]
    if sanitized_host not in allowed_hosts:
        return {"status": "error", "message": "Host not allowed"}
    # Validate command arguments against a whitelist
    allowed_commands = ["ping"]
    if shlex.split(sanitized_host)[0] not in allowed_commands:
        return {"status": "error", "message": "Command not allowed"}
    result = subprocess.run(["ping", *shlex.split(sanitized_host)], check=True, capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}