from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Secure implementation
    subprocess.call(['ping', host], shell=False)
app = FastAPI()
@app.get("/ping")
def ping_safe(host: str):
    return ping(host)