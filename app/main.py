from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation
    if subprocess.call(['ping', host]) == 0:
        return {"status": "completed"}
    else:
        return {"status": "failed"}