from fastapi import FastAPI
import subprocess
import shlex
def validate_host(host):
    allowed_hosts = ['example.com', 'test.com']  # Define allowed hosts
    if host not in allowed_hosts:
        raise ValueError('Invalid host provided')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    validate_host(host)
    command = ['ping', shlex.quote(host)]
    # Use a safe method to prevent command injection
    subprocess.run(command, check=True, capture_output=True, text=True)
    return {"status": "completed", "output": command.stdout}