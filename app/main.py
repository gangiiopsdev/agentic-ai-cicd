from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Safer implementation without using shell=True
    args = ['ping', host]
    subprocess.call(args)

@app.get("/ping")
def ping_route(host: str):
    return {'status': 'completed'}