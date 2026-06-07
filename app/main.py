from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Secure implementation
    subprocess.call(['ping', host])
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    return ping(host)