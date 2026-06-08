from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if 'ping' in host:
        return {'status': 'not allowed'}
    command = ["ping", host]
    subprocess.call(command, shell=False)
    return {"status": "completed"}