from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Using subprocess.run instead of subprocess.call and avoiding shell=True
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return result.stdout

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)