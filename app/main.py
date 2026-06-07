from fastapi import FastAPI
import subprocess
cimport os

app = FastAPI()

def safe_ping(host: str):
    if not host.strip():
        return False
    command = ['ping', '--', host]
    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        return True
    except subprocess.CalledProcessError as e:
        print(e.stderr)
        return False

@app.get("/ping")
def ping(host: str):
    if safe_ping(host):
        return {"status": "completed"}
    else:
        return {"error": "Invalid or empty host parameter"}