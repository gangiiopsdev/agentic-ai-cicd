from fastapi import FastAPI
import subprocess
import socket
cimport socket

app = FastAPI()

@app.get("/)
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        ip_address = socket.gethostbyname(host)
        subprocess.call(['ping', '-c', '1', '--{}'.format(ip_address)])  # Use -- to prevent command injection
    except socket.gaierror:
        return {"status": "failed", "reason": "Invalid hostname"}
    return {"status": "completed"}