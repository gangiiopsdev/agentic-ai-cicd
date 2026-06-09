from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Secure implementation
    subprocess.call(['ping', host])
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    return subprocess.run(['ping', host], capture_output=True, text=True)