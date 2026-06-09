from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate input to prevent shell injection
    if not re.match(r'^[a-zA-Z0-9-.]+$', host):
        return {"error": "Invalid hostname"}, 400
    args = ['ping', host]
    subprocess.run(args, check=True)
    return {"status": "completed"}