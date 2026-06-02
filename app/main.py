from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    return host.isalnum() and ' ' not in host

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {"status": "invalid_input", "message": "Invalid host name"}
    args = ['ping', host]
    subprocess.call(['ping', host])  # Directly passing the list avoids shell=True
    return {"status": "completed"}