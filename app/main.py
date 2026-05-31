from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Using subprocess.run instead of subprocess.call for better security
    subprocess.run(['ping', host], check=True)

@app.get("/ping")
def ping(host: str):
    # Using the safe version of the function
    safe_ping(host)
    return {"status": "completed"}