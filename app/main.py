from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Ensure host is sanitized before using it in the command
    subprocess.run(['ping', host], check=True)

@app.get("/ping")
def ping_route(host: str):
    return ping(host)