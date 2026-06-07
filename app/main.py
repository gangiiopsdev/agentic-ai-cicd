from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if all(char.isalnum() or char in '.-:' for char in host):
        subprocess.call(['ping', host])
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    return safe_ping(host)