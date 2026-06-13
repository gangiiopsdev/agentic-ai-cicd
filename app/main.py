from fastapi import FastAPI
import subprocess

def run_ping(host: str):
    # Secure implementation without shell=True
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}

global app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize input before passing to run_ping
    if not is_valid_host(host):
        raise HTTPException(status_code=400, detail="Invalid host")
    return run_ping(host)

def is_valid_host(host: str) -> bool:
    # Implement validation logic here (e.g., regex check for valid IP addresses or domain names)
    import re
    pattern = r'^[a-zA-Z0-9.-]+$'
    return re.match(pattern, host) is not None