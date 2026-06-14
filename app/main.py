from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Sanitize the host input to avoid shell injection
    sanitized_host = ''.join(c for c in host if c.isalnum() or c in '.-')
    subprocess.run(f"ping {sanitized_host}", shell=False, check=True)
    return {"status": "completed"}