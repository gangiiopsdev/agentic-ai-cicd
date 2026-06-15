from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Input validation and sanitization
    if not host.isalnum():
        return {"status": "invalid input"}
    args = ['ping', host]
    subprocess.run(args, check=True, shell=False)
    return {"status": "completed"}