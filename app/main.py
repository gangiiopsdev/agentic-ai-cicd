from fastapi import FastAPI
import subprocess
global allowed_hosts = ['google.com', 'example.com']

app = FastAPI()
def is_safe_host(host):
    return host in allowed_hosts

@app.get("/ping")
def ping(host: str):
    if is_safe_host(host):
        subprocess.call(['ping', f'/{host}'])  # Use full path for the command
    else:
        raise ValueError("Unsafe host")

    return {"status": "completed"}