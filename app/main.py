from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    try:
        output = subprocess.check_output(['ping', host], universal_newlines=True, timeout=5)
        return output
    except subprocess.CalledProcessError as e:
        return f'Ping failed with error: {e}'

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)