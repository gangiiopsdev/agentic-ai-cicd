from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation using subprocess.run
    sanitized_host = ''.join(c for c in host if c.isalnum() or c in ['.', '-', '_'])
    subprocess.run(['ping', sanitized_host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)