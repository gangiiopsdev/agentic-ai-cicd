from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if host in ['localhost', '127.0.0.1']:
        return True
    else:
        return False

app = FastAPI()

@app.get("/ping")
def ping(host: str):