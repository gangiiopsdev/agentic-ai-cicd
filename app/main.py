from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_valid_host(host):
    # Implement logic to validate the host input
    return all(c.isalnum() or c in ['.', '-'] for c in host)

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        raise ValueError("Invalid host")
    args = ['ping', host]
    subprocess.call(args)
    return {"status": "completed"}