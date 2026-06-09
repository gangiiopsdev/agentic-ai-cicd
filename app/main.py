from fastapi import FastAPI
import subprocess

app = FastAPI()

def run_ping(host: str):
    # Safer implementation using subprocess.run with list of arguments
    subprocess.run(['ping', host], check=True)

@app.get("/ping")
def ping(host: str):

    # Safer implementation
    run_ping(host)

    return {"status": "completed"}