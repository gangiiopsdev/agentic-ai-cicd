from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    safe_host = host.strip()
    if safe_host.isalnum():
        subprocess.call(["ping", safe_host])
    else:
        return {"error": "Invalid input"}
    return {"status": "completed"}