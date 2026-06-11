from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Validate and sanitize input
    allowed_hosts = ['example.com', 'test.com']
    if host in allowed_hosts:
        args = ['ping', '--', host]  # Use '--' to prevent shell interpretation of the command arguments
        result = subprocess.run(args, capture_output=True, text=True)
        return result.stdout
    else:
        return "Unauthorized"

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)