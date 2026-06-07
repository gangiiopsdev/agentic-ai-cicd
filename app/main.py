from fastapi import FastAPI
import subprocess
def escape_host(host):
    return ''.join(c for c in host if c.isalnum() or c.isdigit())

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    escaped_host = escape_host(host)
    # Use a safe way to execute the command without shell=True
    subprocess.run(["ping", escaped_host], check=True, shell=False)
    return {"status": "completed"}