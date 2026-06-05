from fastapi import FastAPI
import subprocess
from os.path import abspath

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation using a whitelist of allowed hosts
    allowed_hosts = ["127.0.0.1", "localhost"]
    if host in allowed_hosts:
        subprocess.call([abspath("ping"), host])
    else:
        return {"status": "unauthorized"}

    return {"status": "completed"}