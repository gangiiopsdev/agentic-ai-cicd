from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_host(host):
    # Example sanitization: allow only alphanumeric characters and a limited set of allowed characters
    return ''.join(c for c in host if c.isalnum() or c in '.-')

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_host(host)
    try:
        args = shlex.split(f'ping -c 4 {sanitized_host}')  # Limit the number of pings to prevent DoS
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}

# Use a more secure method to avoid command injection
def ping_secure(host: str):
    sanitized_host = sanitize_host(host)
    cmd = ['ping', '-c', '4', sanitized_host]
    result = subprocess.run(cmd, capture_output=True, text=True, check=True)
    return {"status": "completed", "output": result.stdout}