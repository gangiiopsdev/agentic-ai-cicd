from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_host(host):
    # Escape or validate host input
    return ''.join(e for e in host if e.isalnum() or e in ['.', '-'])

@app.get("/ping")
def ping(host: str):
    escaped_host = escape_host(host)
    subprocess.call(f"ping {escaped_host}")
    return {"status": "completed"}