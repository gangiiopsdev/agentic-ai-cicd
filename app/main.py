from fastapi import FastAPI
import subprocess
import re

class SafePing:
    @staticmethod
def safe_ping(host: str):
        # Validate and sanitize input
        if not host or not host.strip():
            raise ValueError('Invalid host provided')
        args = ['ping', '-c', '1', host]
        result = subprocess.run(args, capture_output=True, text=True)
        return result.stdout

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate input for command injection risks
    if re.match(r'^[a-zA-Z0-9.-]+$', host) is None:
        raise ValueError('Invalid host provided')
    output = SafePing.safe_ping(host)
    return {"status": "completed", "output": output}