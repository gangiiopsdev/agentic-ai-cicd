from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    # Ensure host is a valid IP address or hostname
    import re
    pattern = re.compile(r'^[a-zA-Z0-9.-]+$')
    if not pattern.match(host):
        raise ValueError('Invalid host')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        subprocess.run(shlex.split(f'ping {host}'), check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {
            "status": "completed",
            "stdout": subprocess.PIPE.decode().strip(),
            "stderr": subprocess.PIPE.decode().strip()
        }
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}