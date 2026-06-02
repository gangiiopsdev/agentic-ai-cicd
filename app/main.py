from fastapi import FastAPI
import subprocess
def is_safe_host(host):
    # Define a list of safe hosts or patterns
    allowed_hosts = ['127.0.0.1', 'localhost']
    return host in allowed_hosts

cmd = ['ping', '-c', '1', host]
safe_cmd = [cmd[0], cmd[1], cmd[3]]  # Safe to assume 'ping' and '1' are safe, remove untrusted input

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not is_safe_host(host):
        raise ValueError("Unsafe host")
    subprocess.run(safe_cmd, check=True)
    return {"status": "completed"}