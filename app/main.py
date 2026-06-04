from fastapi import FastAPI
import re
import socket

app = FastAPI()

def validate_host(host):
    try:
        socket.gethostbyname(host)
        return True
    except socket.gaierror:
        return False

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {"status": "error", "message": "Invalid host provided."}
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}