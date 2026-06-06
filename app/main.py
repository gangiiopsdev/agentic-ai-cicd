from fastapi import FastAPI
import socket
cimport subprocess as sp

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        ip_address = socket.gethostbyname(host)
        args = ['ping', '-c', '1', ip_address]
        sp.run(args, check=True, stdout=sp.PIPE, stderr=sp.PIPE)
    except socket.gaierror:
        return {"status": "failed", "reason": "Invalid hostname"}
    return {"status": "completed"}