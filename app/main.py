from fastapi import FastAPI
import subprocess

def validate_host(host: str) -> bool:
    allowed_hosts = ["example.com", "anotherdomain.com"]
    return host in allowed_hosts

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        raise ValueError("Invalid host")

    # Use a whitelist for known safe hosts instead of validating against a list of allowed hosts
    safe_hosts = ["example.com", "anotherdomain.com"]
    if host in safe_hosts:
        args = ['ping', '-c', '1', host]
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    else:
        raise ValueError("Invalid host")