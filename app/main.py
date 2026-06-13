from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    sanitized_host = host.strip()
    if not all(c.isalnum() or c in "-._" for c in sanitized_host):
        return {"status": "invalid input"}
    subprocess.call(["ping", sanitized_host])
    return {"status": "completed"}