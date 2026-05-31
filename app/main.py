from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Validate input to prevent command injection
    valid_hosts = ['example.com', 'localhost']
    if host in valid_hosts:
        args = ['ping', host]
        subprocess.run(args)

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}