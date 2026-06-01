from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    args = ['ping', host]
    subprocess.run(args)

@app.get("/ping")
def ping(host: str):
    # Validate the input to ensure it's a valid hostname or IP address
    import re
    if re.match(r'^[a-zA-Z0-9.-]+$', host):
        safe_ping(host)
    else:
        raise ValueError('Invalid host')