from fastapi import FastAPI
import subprocess

class PingService:
    @staticmethod
def ping(host: str):
        # Safe implementation using subprocess.run with input validation
        args = ['ping', '-c', '1', host]
        subprocess.run(args, check=True)

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    if not is_valid_host(host):
        raise ValueError("Invalid host")
    PingService.ping(host)
    return {"status": "completed"}

def is_valid_host(host: str) -> bool:
    # Basic validation to ensure the host does not contain unexpected characters
    return all(char.isalnum() or char in ['.', '-'] for char in host)