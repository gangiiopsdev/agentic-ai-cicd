from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation with input validation and sanitization
    if not validate_host(host):
        return {"status": "invalid host"}
    args = ['ping', host]
    subprocess.run(args, check=True)  # Use subprocess.run instead of subprocess.call
    return {"status": "completed"}

def validate_host(host: str) -> bool:
    # Implement your validation logic here
    allowed_hosts = ['example.com', 'test.example.com']
    return host in allowed_hosts