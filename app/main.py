from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation using subprocess.run
    subprocess.call(['ping', host], shell=False)

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)