from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Validate the host parameter to ensure it does not contain potentially dangerous characters
    if any(char in host for char in [';', '&', '|', '<', '>', '`', '$']):
        raise ValueError('Invalid input detected')
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)