from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def safe_ping(host):
    if not re.match(r'^[a-zA-Z0-9]+$', host):  # Regex to allow only alphanumeric characters
        raise ValueError("Invalid host name")
    try:
        args = ['ping', host]
        result = subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode()
    except subprocess.CalledProcessError as e:
        return str(e.stderr.decode())

@app.get("/ping")
def ping(host: str):
    response = safe_ping(host)
    return {"status": "completed", "response": response}