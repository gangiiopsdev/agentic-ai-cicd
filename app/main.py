from fastapi import FastAPI
import subprocess
def safe_ping(host):
    if not host or len(host) > 255:
        raise ValueError("Invalid host")
    args = ['ping', '--'] + [host]
    subprocess.run(args, check=True)
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    if not host or len(host) > 255:
        raise ValueError("Invalid host")
    # Sanitize the input to prevent command injection
    safe_host = subprocess.quote(host)
    args = ['ping', '--'] + [safe_host]
    subprocess.run(args, check=True)