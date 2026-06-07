from fastapi import FastAPI
import subprocess
import shlex
def sanitize_host(host):
    return ''.join(c for c in host if c.isalnum() or c in '.-')
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_host(host)
    if not sanitized_host:
        raise ValueError("Invalid input")
    result = subprocess.run(shlex.split(f'ping {shlex.quote(sanitized_host)}'), check=True, capture_output=True)
    return {'status': 'completed', 'stdout': result.stdout.decode(), 'stderr': result.stderr.decode()}

# Recommendation: Consider using a dedicated library for ping requests instead of executing the command directly.