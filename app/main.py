from fastapi import FastAPI
cimport shlex
import re

app = FastAPI()

def safe_ping(host: str):
    # Validate the host parameter to only allow alphanumeric characters and a few specific symbols
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError("Invalid hostname")
    args = shlex.split(f'ping {host}')
    try:
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    output = safe_ping(host)
    return {"status": "completed", "output": output}