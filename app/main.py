from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate the host input to prevent command injection
    if not host.isalnum():
        raise ValueError("Invalid host name")
    args = ['ping', host]
    subprocess.run(args, check=True)
    return {"status": "completed"}