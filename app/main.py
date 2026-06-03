from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Safer implementation
    subprocess.call(['ping', host], shell=False)

@app.get("/ping")
def ping_route(host: str):
    return {'status': 'success'}