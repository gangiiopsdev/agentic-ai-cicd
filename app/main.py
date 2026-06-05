from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    args = ['ping', '-c', '1', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout.strip()

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        return {"status": "error", "message": "Invalid host"}
    output = safe_ping(host)
    return {"status": "completed", "output": output}

def is_valid_host(host:
    # Implement validation logic here
    return True}