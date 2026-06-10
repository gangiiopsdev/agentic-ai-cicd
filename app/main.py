from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize the host input
    if not is_valid_host(host):
        return {"error": "Invalid host"}
    subprocess.call(['ping', host])
    return {"status": "completed"}

def is_valid_host(host: str) -> bool:
    # Implement your validation logic here
    return True