from fastapi import FastAPI
import subprocess

app = FastAPI()

def _ping(host):
    args = ['ping', host]
    subprocess.run(args)

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    _ping(host)
    return {"status": "completed"}