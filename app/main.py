from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_host(host):
    # Basic validation and escaping of host input
    return ''.join(c if c.isalnum() else '_' for c in host)

@app.get("/ping")
def ping(host: str):
    escaped_host = escape_host(host)
    subprocess.call(f"ping {escaped_host}", shell=False)
    return {"status": "completed"}