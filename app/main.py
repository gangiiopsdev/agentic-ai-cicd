from fastapi import FastAPI
import subprocess
def secure_ping(host: str):
    if not is_safe_host(host):
        raise ValueError("Unsafe host")
    subprocess.call(["ping", host])

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    return secure_ping(host)

def is_safe_host(host: str) -> bool:
    # Implement logic to validate the host
    allowed_hosts = ["127.0.0.1", "localhost"]
    return host in allowed_hosts