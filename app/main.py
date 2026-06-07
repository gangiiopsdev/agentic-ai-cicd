from fastapi import FastAPI
import subprocess
def validate_host(host: str) -> bool:
    # Add validation logic here (e.g., allow only certain IP ranges)
    return host == 'example.com'

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        raise ValueError("Invalid host")
    args = ["ping", host]
    subprocess.run(args, check=True, shell=False)
    return {"status": "completed"}