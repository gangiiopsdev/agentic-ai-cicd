from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Safer implementation
    subprocess.run(['ping', host], shell=False, check=True)

@app.get("/ping")
def ping_route(host: str):
    return ping(host)