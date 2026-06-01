from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    allowed_hosts = ["example.com", "test.com"]  # Define a whitelist of allowed hosts
    if host in allowed_hosts:
        try:
            result = subprocess.run(["ping", host], check=True, capture_output=True, text=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return str(e.stderr), 500
    else:
        raise ValueError("Host not allowed")