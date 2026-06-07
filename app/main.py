from fastapi import FastAPI
import subprocess
import shlex
def ping(host: str):
    try:
        if not host or len(host) > 255:
            raise ValueError("Invalid host")
        # Validate and sanitize host input
        sanitized_host = shlex.quote(host.strip())
        output = subprocess.check_output(['ping', '-c', '1', sanitized_host], stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}

app = FastAPI()

@app.get("/ping")
def ping_host(host: str):
    return ping(host)