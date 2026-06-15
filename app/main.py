from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host):
    if not all(c.isalnum() or c in '-.' for c in host):  # Validate input
        raise ValueError('Invalid hostname')
    try:
        result = subprocess.run(shlex.split(f'ping {host}'), capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    output = safe_ping(host)
    return {"status": "completed", "output": output}