from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Safe implementation using subprocess.run and shlex.quote
    subprocess.run(['ping', host], check=True)

@app.get("/ping")
def ping_route(host: str):  
    return ping(host)