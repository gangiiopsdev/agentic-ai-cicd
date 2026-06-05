from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    try:
        args = ['ping'] + shlex.split(host)
        output = subprocess.run(args, capture_output=True, text=True, check=True)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return None

def is_valid_host(hostname: str):
    import socket
    try:
        socket.gethostbyname(hostname)
        return True
    except socket.gaierror:
        return False

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        return {"status": "failed", "error": "Invalid host"}
    output = safe_ping(host)
    if output:
        return {"status": "completed", "output": output}
    else:
        return {"status": "failed", "error": "Ping failed"}