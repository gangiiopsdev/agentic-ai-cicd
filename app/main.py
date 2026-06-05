from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation using subprocess.run with shell=False and full command
    subprocess.run(['ping', '-c', '1', host], check=True, shell=False)

@app.get("/ping")
def ping_route(host: str):
    return ping(host)