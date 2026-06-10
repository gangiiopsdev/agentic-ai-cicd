from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def is_valid_host(host):
    return all(c.isalnum() or c in ['.', '-'] for c in host)

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        raise ValueError("Invalid host")
    args = ['ping', shlex.quote(host)]  # Use shlex.quote to escape special characters
    subprocess.run(args, check=True)  # Use subprocess.run for better error handling
    return {"status": "completed"}