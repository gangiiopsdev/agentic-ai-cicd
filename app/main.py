from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    # Safe implementation using subprocess.Popen with a list of arguments
    args = ['ping', host]
    subprocess.run(args, check=True)

def validate_host(host: str) -> bool:
    # Basic validation to prevent shell injection
    return all(char.isalnum() or char in '.-_' for char in host)

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {"status": "error", "message": "Invalid host name"}
    try:
        safe_ping(host)
        return {"status": "completed"}
    except Exception as e:
        return {"status": "error", "message": str(e)}