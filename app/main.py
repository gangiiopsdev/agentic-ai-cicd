from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    # Safe implementation using list of args and proper sanitization
    subprocess.call(['ping', subprocess.list2cmdline([host])])

@app.get("/ping")
def ping(host: str):
    # Using safe function with input validation
    if not all(c.isalnum() or c in ['.', '-'] for c in host):
        raise ValueError("Invalid hostname")
    safe_ping(host)
    return {"status": "completed"}