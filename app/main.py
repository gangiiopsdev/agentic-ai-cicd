from fastapi import FastAPI
import subprocess

app = FastAPI()

def run_ping(host: str):
    args = ['ping', host]
    subprocess.run(args, check=True, shell=False)

@app.get("/ping")
def ping(host: str):
    # Sanitize the input to avoid command injection
    if not host.isalnum():
        raise ValueError("Invalid hostname")
    run_ping(host)
    return {"status": "completed"}