from fastapi import FastAPI
import subprocess
import shlex
class PingRequest:
    def __init__(self, host: str):
        self.host = host

def sanitize_host(host: str):
    # Example sanitization: allow only alphanumeric characters and a limited set of allowed characters
    return ''.join(c for c in host if c.isalnum() or c in '.-')

@app.get("/ping")
def ping(request: PingRequest):
    sanitized_host = sanitize_host(request.host)
    try:
        cmd = ['ping', '-c', '4', shlex.quote(sanitized_host)]
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}