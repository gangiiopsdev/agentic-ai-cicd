from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_host(host):
    return ''.join(c for c in host if c.isalnum() or c in ('.', '-', '_'))

@app.get("/ping")
def ping(host: str):
    escaped_host = escape_host(host)
    subprocess.call(f"ping {escaped_host}", shell=True)
    return {"status": "completed"}