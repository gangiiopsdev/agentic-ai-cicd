from fastapi import FastAPI
import subprocess

def safe_ping(host):
    try:
        output = subprocess.run(['ping', host], capture_output=True, text=True, timeout=10)
        return output.stdout
    except subprocess.TimeoutExpired as e:
        return str(e)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)