from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation with input validation
    if validate_host(host):
        args = ['ping', host]
        result = subprocess.run(args, capture_output=True, text=True)
        return result.stdout
    else:
        raise ValueError('Invalid host')

def validate_host(host: str) -> bool:
    # Simple validation example, replace with actual logic
    return '.' in host

@app.get("/ping")
def ping_route(host: str):
    return ping(host)