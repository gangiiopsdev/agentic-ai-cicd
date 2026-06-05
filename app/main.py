from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize host input
    if host.strip() == "":
        raise ValueError("Invalid host parameter")

    args = ['ping', host]
    subprocess.call(args)

    return {"status": "completed"}