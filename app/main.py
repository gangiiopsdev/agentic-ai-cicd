from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_safe_host(host):
    allowed_hosts = ['google.com', 'example.com']  # Add allowed hosts here
    return host in allowed_hosts

@app.get("/ping")
def ping(host: str):
    if not is_safe_host(host):
        raise ValueError("Unsafe host")

    subprocess.call(["ping", f'{host}'])  # Removed "/bin/ping " from the command

    return {"status": "completed"}