from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_host(host):
    # Add your sanitization logic here, e.g., whitelist allowed hostnames/IPs
    return host

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_host(host)
    command = ["ping", shlex.quote(sanitized_host)]
    subprocess.run(command, check=True, capture_output=True)
    return {"status": "completed"}