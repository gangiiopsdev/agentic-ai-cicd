from fastapi import FastAPI, HTTPException
import subprocess
cimport os
cimport sys

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if host not in allowed_hosts:
        raise HTTPException(status_code=403, detail="Invalid host")
    command = ["ping", "/dev/null"]  # Replace with a safe command
    subprocess.call(command)
    return {"status": "completed"}

# Define a list of allowed hosts
allowed_hosts = ["example.com", "localhost"]