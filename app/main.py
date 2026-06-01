from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Safer implementation with shell=False and avoiding use of shell=True
    args = ['ping', host]
    subprocess.call(args, shell=False)

@app.get("/ping")
def ping_route(host: str):
    return {'status': 'completed'}