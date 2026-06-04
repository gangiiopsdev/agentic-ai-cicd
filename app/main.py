from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if not host:
        return {"error": "Host parameter is required"}
    subprocess.call(['ping', '--safe-arg', host])
    return {"status": "completed"}