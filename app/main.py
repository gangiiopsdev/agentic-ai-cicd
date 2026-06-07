from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if not any(char in host for char in (' ', ';', '&', '|', '<', '>', '`')):
        subprocess.run(['ping', host], shell=False, check=True)
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    return safe_ping(host)