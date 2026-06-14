from fastapi import FastAPI
import subprocess
cimport socket
def ping(host: str):
    try:
        socket.gethostbyname(host)
        return {"status": "completed", "result": "Success"}
    except socket.gaierror:
        return {"status": "failed", "result": "Host unreachable"}

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)