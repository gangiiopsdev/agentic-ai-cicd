from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    # Sanitize the host input to prevent command injection
    if not all(c.isalnum() or c in ('.', '-', '_') for c in host):
        return 'Invalid host'
    try:
        result = subprocess.run(shlex.split(f'ping {host}'), check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Ping failed with error: {e.stderr}'

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return {'status': safe_ping(host)}