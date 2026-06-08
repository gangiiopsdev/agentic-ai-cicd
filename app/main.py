from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def sanitize_host(host: str) -> str:
    if not re.match(r'^[a-zA-Z0-9]{1,64}$', host):
        raise ValueError("Invalid host")
    return host.strip()

@app.get="/ping")
def ping(host: str):\n    sanitized_host = sanitize_host(host)\n    args = ['ping', sanitized_host]\n    try:\n        result = subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)\n        return {"status": "completed", "output": result.stdout.decode()}\n    except subprocess.CalledProcessError as e:\n        return {"status": "error", "output": str(e)}