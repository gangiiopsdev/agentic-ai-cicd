from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Safer implementation without shell=True
    subprocess.call(['ping', host])

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)