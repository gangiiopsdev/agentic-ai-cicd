from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    host = subprocess.quote(host)
    try:
        result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Error pinging {host}: {e}'
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    return safe_ping(host)