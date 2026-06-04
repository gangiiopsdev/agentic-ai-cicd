from fastapi import FastAPI
import subprocess
cimport os

global app = FastAPI()

def ping(host: str):
    # Secure implementation
    args = ['ping', '-c', '1', host]
    subprocess.run(args, check=True)

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)