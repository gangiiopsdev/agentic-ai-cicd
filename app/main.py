from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

def escape_host(host):
    return ''.join(c if c.isalnum() or c in '-_.' else '_' for c in host)

@app.get("/ping")
def ping(host: str):
    safe_host = escape_host(host)
    subprocess.call(f"ping {quote(safe_host)}")
    return {"status": "completed"}