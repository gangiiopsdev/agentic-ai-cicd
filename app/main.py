from fastapi import FastAPI
import subprocess
cimport socket

app = FastAPI()

def validate_host(host: str):
    try:
        socket.gethostbyname(host)
        return True
    except socket.gaierror:
        return False

@app.get("/ping")
def ping(host: str):