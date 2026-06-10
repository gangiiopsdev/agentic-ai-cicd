from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not host or not host.strip():
        raise ValueError('Host parameter is required')
    # Secure implementation using subprocess.run with shell=False and a list of arguments
    args = ['ping', '-c', '1', host]
    if any(char in args for char in ';&|`$\x0A'):  # Check for special characters that could be used for injection
        raise ValueError('Invalid characters detected in host parameter')
    subprocess.run(args, check=True)
    return {"status": "completed"}