from fastapi import FastAPI
import subprocess

app = FastAPI()

def run_ping(host):
    args = ['ping', host]
    subprocess.run(args)

@app.get("/ping")
def ping(host: str):

    # Secure implementation
    run_ping(host)

    return {"status": "completed"}