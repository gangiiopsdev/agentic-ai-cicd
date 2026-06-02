from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Sanitize the host input to prevent command injection
    if not host.isalnum():
        return {"status": "error", "message": "Invalid hostname"}
    args = ['ping', host]
    subprocess.run(args, check=True)
    return {"status": "completed"}