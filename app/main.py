from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation using subprocess.run with shell=False and args tuple
    if validate_host(host):
        subprocess.run(['ping', host], shell=False)
        return {"status": "completed"}
    else:
        return {"error": "Invalid host"}, 400

def validate_host(host: str) -> bool:
    # Add validation logic here to ensure the host is safe to ping
    allowed_hosts = ['example.com', 'localhost']
    return host in allowed_hosts