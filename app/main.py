from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize input
    if not host.strip() or '@' in host:
        return {"error": "Host parameter is empty, invalid, or contains special characters"}
    args = ['ping', host]
    subprocess.run(args, check=True)
    return {"status": "completed"}