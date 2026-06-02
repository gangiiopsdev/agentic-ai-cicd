from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Input validation and sanitization
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {"error": "Invalid input"}, 400
    args = ['ping', host]
    subprocess.run(args, check=True)
    return {"status": "completed"}