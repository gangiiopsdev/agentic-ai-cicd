from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Safe implementation
    subprocess.run(['ping', host], capture_output=True, text=True)

@app.get("/ping")
def ping_endpoint(host: str):\n    return ping(host)