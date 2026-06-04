from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Validate the host input
    if not host.isdigit() or len(host) > 15:
        return "Invalid host"
    subprocess.run(["ping", host], check=True, shell=False)

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    return {"status": result}