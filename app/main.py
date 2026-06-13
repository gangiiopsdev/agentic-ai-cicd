from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Secure implementation with input validation and escaping
    if not host.isalnum() or '.' in host:
        raise ValueError('Invalid host')
    subprocess.run(['ping', subprocess.list2cmdline([host])], check=True)

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)