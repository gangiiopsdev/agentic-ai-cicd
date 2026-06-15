from fastapi import FastAPI
import subprocess

def is_valid_host(host):
    # Implement validation logic here, e.g., check for allowed domain patterns
    return True

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        raise ValueError("Invalid host")
    subprocess.run(["ping", host], check=True, shell=False)
    return {"status": "completed"}