from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if re.match(r'^localhost$|^127\.0\.0\.1$', host):
        args = ['ping', host]
        subprocess.call(args, shell=False)
        return {"status": "completed"}
    else:
        return {"status": "error", "message": "Invalid host"}