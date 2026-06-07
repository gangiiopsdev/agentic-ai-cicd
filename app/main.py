from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Safe implementation
    args = ['ping', host]
    subprocess.call(args)

def validate_host(host: str) -> bool:
    # Basic validation to prevent common injection attacks
    if '&&' in host or '|' in host or ';' in host or '&' in host:
        return False
    return True

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {'status': 'error', 'message': 'Invalid input'}
    
    # Secure implementation
    safe_ping(host)

    return {"status": "completed"}