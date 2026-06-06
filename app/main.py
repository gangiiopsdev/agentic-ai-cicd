from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    # Safe implementation using list for arguments
    subprocess.run(['ping', host], check=True)

@app.get("/ping")
def ping(host: str):

    # Safe implementation using function
    safe_ping(host)

    return {"status": "completed"}