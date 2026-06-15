from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation using subprocess.run
    subprocess.run(['ping', host], check=True)

@app.get("/ping")
def ping_handler(host: str):
    return ping(host)