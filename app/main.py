from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    safe_host = subprocess.run(['echo', host], capture_output=True, text=True).stdout.strip()
    # Use a list to pass arguments safely instead of shell=True
    subprocess.call(['ping', safe_host])
    return {"status": "completed"}