from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host):
    try:
        args = shlex.split('ping ' + host)
        result = subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return str(e.stderr)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize input to prevent injection attacks
    if not all(c.isalnum() or c in '._-@' for c in host):  # Basic validation example
        return "Invalid host"
    return safe_ping(host)