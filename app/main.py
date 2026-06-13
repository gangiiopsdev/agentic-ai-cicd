from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    # Add host validation logic here
    return True

@app.get("/ping")
def ping(host: str):
    if validate_host(host):
        subprocess.run(["ping", host], check=True)
        return {"status": "completed"}
    else:
        return {"status": "invalid host"}