from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation
    subprocess.call(['ping', host])

@app.get("/ping")
def ping_route(host: str):
    if not validate_host(host):
        return {'error': 'Invalid host'}
    return ping(host)

def validate_host(host: str) -> bool:
    # Basic validation, real-world use should be more comprehensive
    return '.' in host