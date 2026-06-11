from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def validate_host(host):
    if not host.isdigit():
        raise ValueError("Invalid host")

@app.get("/ping")
def ping(host: str):
    return {"message": "Pong"}