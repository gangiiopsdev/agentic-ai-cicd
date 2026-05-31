from fastapi import FastAPI
import subprocess
globally_allowed_hosts = {"example.com", "localhost"}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if host in globally_allowed_hosts:
        # Using a safer method instead of shell=True
        subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    else:
        raise ValueError("Host not allowed")
    return {"status": "completed"}