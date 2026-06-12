from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if host.isnumeric() and '.' in host:
        # Use a safer method instead of subprocess.call
        response = subprocess.run(['ping', host], capture_output=True, text=True)
        return response.stdout
app = FastAPI()
@app.get("/ping")
def ping(host: str):    return safe_ping(host)