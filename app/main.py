from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize user input
    if not host.isalnum() or len(host) > 15:
        return {"status": "error", "message": "Invalid input"}
    args = ['ping', host]
    subprocess.run(args)
    return {"status": "completed"}