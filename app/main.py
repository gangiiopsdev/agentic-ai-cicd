from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    # Safe implementation using subprocess.run with list of arguments
    subprocess.run(['ping', host], check=True)

@app.get("/ping")
def ping(host: str):