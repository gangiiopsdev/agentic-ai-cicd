from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Safe implementation using list instead of string for subprocess call
    subprocess.run(['ping', host], check=True)

@app.get("/ping")
def ping(host: str):

    # Using the safe function to avoid command injection
    safe_ping(host)

    return {"status": "completed"}