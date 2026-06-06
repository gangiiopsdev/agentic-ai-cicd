from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(host: str) -> str:
    # Add your sanitization logic here, e.g., allow only certain IP addresses or hostnames
    return host

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    subprocess.run(['ping', sanitized_host], check=True)
    return {"status": "completed"}