from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    # Sanitize input to prevent shell injection
    if not host.isalnum():
        raise ValueError("Invalid characters in host name")
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    output = safe_ping(host)
    return {'status': 'completed', 'output': output}