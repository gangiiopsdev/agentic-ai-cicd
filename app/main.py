from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Sanitize input to prevent command injection
    if not host.isalnum() and '_' not in host:
        return {"status": "error", "message": "Invalid input"}
    args = ['ping', host]
    subprocess.run(args, check=True)
    return {"status": "completed"}