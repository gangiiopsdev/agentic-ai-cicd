from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation
    if not host.strip().isalnum():
        return {"status": "invalid input"}
    subprocess.call(['ping', '-c', '1', host])
    return {"status": "completed"}

@app.get("/ping")
def ping_handler(host: str):
    return ping(host)