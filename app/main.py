from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if host.isalnum():
        subprocess.call(["ping", host])
        return {"status": "completed"}
    else:
        return {"error": "Invalid input"}