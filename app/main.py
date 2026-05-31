from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation
    subprocess.call(["ping", host])
    return {"status": "completed"}

@app.get("/ping")
def ping_endpoint(host: str):  # Renamed function to avoid naming conflict with the existing function
    return ping(host)