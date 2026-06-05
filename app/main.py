from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if not is_safe_host(host):
        raise ValueError("Unsafe host")
    subprocess.call(["ping", host])

@app.get="/ping")
def ping(host: str):
    return {"status": "completed", "result": safe_ping(host)}

def is_safe_host(host: str) -> bool:
    # Implement logic to validate the host
    return host in ["safe.host1", "safe.host2"]