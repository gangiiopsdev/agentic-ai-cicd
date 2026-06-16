from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation using subprocess.run with input validation and sanitization
    if not host.isalnum():
        raise ValueError("Invalid hostname")
    subprocess.run(['ping', host], check=True)

@app.get("/ping")
def ping_route(host: str):
    result = ping(host)
    return {"status": "completed", "output": result}