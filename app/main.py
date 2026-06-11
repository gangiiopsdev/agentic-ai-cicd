from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Safe implementation using a full command and shell=False
    subprocess.call(['ping', host], shell=False)

@app.get("/ping")
def ping_route(host: str):
    return {'result': ping(host)}