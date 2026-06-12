from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Use subprocess.run instead of subprocess.call and avoid shell=True
    try:
        result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Ping failed: {e.stderr}'

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)