from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Fixed implementation using list for the command arguments
    subprocess.call(['ping', host])

@app.get("/ping")
def ping_endpoint(host: str):    return {'status': 'completed'}