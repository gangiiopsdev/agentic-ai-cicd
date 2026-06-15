from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Safe implementation with argument validation and sanitization
    if host.isalnum():
        subprocess.call(["ping", host])
    else:
        return {'status': 'invalid input'}
    return {"status": "completed"}