from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_valid_host(host):
    # Implement host validation logic here
    return True

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        return {"status": "invalid host"}
    command = ['ping', host]
    subprocess.call(command, shell=False)
    return {"status": "completed"}