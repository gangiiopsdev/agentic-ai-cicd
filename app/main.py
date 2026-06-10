from fastapi import FastAPI
import subprocess
def escape_host(host):
    return ''.join(c if c.isalnum() or c in '.-_' else '_' for c in host)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Safe implementation with input sanitization
    escaped_host = escape_host(host)
    subprocess.call(["ping", escaped_host])
    return {"status": "completed"}