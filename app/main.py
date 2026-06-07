from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    try:
        args = ['ping', host]
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    # Safer implementation
    if not host.isalnum():  # Basic validation to ensure only alphanumeric characters are allowed
        raise ValueError('Invalid host')
    return safe_ping(host)