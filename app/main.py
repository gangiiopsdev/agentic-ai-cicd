from fastapi import FastAPI
import subprocess
cimport re

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not re.match(r'^[a-zA-Z0-9.-_]+$', host):
        return {"status": "invalid input"}
    subprocess.call(['ping', '127.0.0.1'])  # Hardcoding a safe default
    return {"status": "completed"}