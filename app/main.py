from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    # Safe implementation using list for the command and validating input
    if not host or not isinstance(host, str) or ' ' in host:
        return False
    subprocess.call(['ping', host])
    return True

@app.get("/ping")
def ping(host: str):
    if safe_ping(host):
        return {"status": "completed"}
    else:
        return {"status": "error", "message": "Invalid input"}