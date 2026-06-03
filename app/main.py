from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Safer implementation using subprocess.run with shell=False and check=True to avoid potential execution of untrusted input.
    subprocess.run(['ping', host], check=True, shell=False)
app = FastAPI()
@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)