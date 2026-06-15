from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_valid_host(host):
    # Simple validation logic (e.g., allowed domains)
    return host in ['example.com', 'localhost']

@app.get("/ping")
def ping(host: str):
    if not host:
        return "Host parameter is required"
    if not is_valid_host(host):
        return "Invalid host"
    try:
        result = subprocess.run(['ping', '--', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)