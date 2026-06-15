from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def validate_host(host):
    allowed_hosts = ['example.com', 'test.com']
    if host in allowed_hosts:
        return True
    else:
        raise ValueError('Invalid host')

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize input
    if validate_host(host):
        # Safer implementation using subprocess.run with shlex.split for safe argument parsing
        command = ['ping', shlex.quote(host)]
        subprocess.run(command, check=True)
        return {"status": "completed"}
    else:
        return {"error": "Invalid host"}