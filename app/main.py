from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def safe_ping(host: str) -> None:
    try:
        # Validate and sanitize the host input to only allow alphanumeric characters and hyphens
        if not re.match('^[a-zA-Z0-9-]+$', host):
            raise ValueError("Invalid hostname")
        # Use shlex to safely handle command arguments
        args = ['ping', shlex.quote(host)]
        subprocess.run(args, check=True)
    except Exception as e:
        print(f"Error: {e}")
        raise

@app.get('/ping')
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}