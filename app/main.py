from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate input
    if not is_valid_host(host):
        return {"status": "failed", "error": "Invalid host"}
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    if result.returncode == 0:
        return {"status": "completed", "output": result.stdout}
    else:
        return {"status": "failed", "error": result.stderr}

def is_valid_host(host: str) -> bool:
    # Implement validation logic here, e.g., check if host is a valid IP address or domain name.
    import re
    pattern = r'^[a-zA-Z0-9.-]+$'
    return re.match(pattern, host) is not None