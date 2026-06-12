from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Validate and sanitize input before using it in the command
    if not host.isalnum():
        raise ValueError("Invalid host name")
    args = ['ping', f'"{host}"']  # Escaping double quotes
    subprocess.run(args, check=True)

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)