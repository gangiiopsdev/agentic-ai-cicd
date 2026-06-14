from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    # Add validation logic here
    allowed_hosts = ['example.com', 'localhost']
    if host in allowed_hosts:
        return True
    return False

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        raise Exception("Invalid host")
    # Secure implementation
    subprocess.run(["ping", host], check=True, shell=False)
    return {"status": "completed"}