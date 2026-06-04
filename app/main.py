from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_valid_host(host):
    # Implement your validation logic here
    return host.isnumeric()

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        return {"status": "invalid host"}, 400
    subprocess.call(["ping", host])
    return {"status": "completed"}