from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    try:
        # Use subprocess.run instead of subprocess.call with shell=True
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Ping failed: {e.output}'

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)