from fastapi import FastAPI
import subprocess

app = FastAPI()

def secure_ping(host: str):
    # Sanitize input
    safe_host = subprocess.list2cmdline([host])
    args = ['ping', safe_host]
    subprocess.run(args, check=True)

@app.get("/ping")
def ping(host: str):
    return secure_ping(host)