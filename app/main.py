from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate the host input to ensure it is safe
    if not host.isalnum():
        return {"error": "Invalid input"}
    
    # Secure implementation
    subprocess.call(["ping", host])