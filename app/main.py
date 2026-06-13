from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation with validation
    subprocess.run(['ping', host], check=True)

@app.get("/ping")
def ping_endpoint(host: str):
    if not validate_host(host):
        raise HTTPException(status_code=400, detail="Invalid host")
    return ping(host)

def validate_host(host: str) -> bool:
    # Add your validation logic here
    allowed_hosts = ['127.0.0.1', 'localhost']
    return host in allowed_hosts