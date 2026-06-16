from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    # Validate input to ensure it is a valid hostname or IP address
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {"status": "invalid_host"}
    args = shlex.split(f'ping -c 4 {host}')
    subprocess.run(args, check=True)
    return {"status": "completed"}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)