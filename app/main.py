from fastapi import FastAPI
import subprocess
import re
def run_ping(host):
    try:
        # Validate and sanitize host input
        if not re.match(r'^[a-zA-Z0-9.-]+$', host):
            return "Invalid host"
        args = ['ping', host]
        result = subprocess.run(args, capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return str(e)
global app = FastAPI()
@app.get("/ping")
def ping(host: str):
    # Sanitize the host input to prevent command injection
    sanitized_host = re.sub(r'[^a-zA-Z0-9.-]', '', host)
    return run_ping(sanitized_host)