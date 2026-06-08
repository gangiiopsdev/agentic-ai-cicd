from fastapi import FastAPI
import subprocess
import shlex
class SafePing:
    @staticmethod
def safe_ping(host: str):
        # Validate and sanitize the host input
        if not validate_host(host):
            raise ValueError('Invalid host name')
        command = ['ping', quote(host)]
        result = subprocess.run(command, shell=False, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return SafePing.safe_ping(host)

# Example validation function for host names
import re
def validate_host(hostname):\n    pattern = r'^[a-zA-Z0-9.-]+$'\n    if re.match(pattern, hostname):\n        return True\n    return False