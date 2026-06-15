from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    # Validate host input to ensure it's a valid hostname or IP address
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError("Invalid host")

@app.get="/ping"
def ping(host: str):
    args = shlex.split(f"ping {host}")
    subprocess.call(args)
    return {"status": "completed"}