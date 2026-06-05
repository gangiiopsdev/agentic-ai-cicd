from fastapi import FastAPI
import subprocess

app = FastAPI()

def secure_ping(host: str):
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

@app.get("/ping")
def ping(host: str):
    return secure_ping(host)