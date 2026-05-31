from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation using parameterized command
    if host in allowed_hosts:
        subprocess.call(["ping", host])
    else:
        raise ValueError("Host not allowed")

allowed_hosts = ["example.com", "test.com"]  # Define a whitelist of allowed hosts