from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    from shlex import quote
    # Secure implementation using subprocess.run instead of subprocess.call
    subprocess.run(['ping', quote(host)], check=True)

def validate_host(host: str):
    # Add validation logic here, e.g., allow only known hosts
    return host

@app.get("/ping")
def ping_safe(host: str = Depends(validate_host)):
    return {"status": "completed"}