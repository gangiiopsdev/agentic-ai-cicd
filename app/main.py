from fastapi import FastAPI
import subprocess

app = FastAPI()

def run_ping(host: str):
    # Secure implementation
    args = ['ping', host]
    subprocess.call(args)

@app.get("/ping")
def ping(host: str):

    run_ping(host)

    return {"status": "completed"}