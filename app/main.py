from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    # Ensure the host is a valid IP address or hostname
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError("Invalid host")
    args = ['ping', shlex.quote(host)]
    subprocess.run(args, check=True)

@app.get="/ping")
def ping(host: str):  
    return safe_ping(host)