from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Safer implementation
    subprocess.call(['ping', host])

@app.get("/ping")
def ping_endpoint(host: str):
    # Sanitize input to prevent command injection
    safe_host = ''.join(c for c in host if c.isalnum() or c in ('.', '-'))
    return ping(safe_host)