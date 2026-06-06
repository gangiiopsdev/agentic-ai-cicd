from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Safe implementation using subprocess.run and escaping the argument
    subprocess.run(['ping', '-c', '1', host], check=True)

@app.get("/ping")
def ping_route(host: str):
    return ping(host)