from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation
    try:
        subprocess.run(['ping', host], check=True, capture_output=True, text=True)
    except subprocess.CalledProcessError as e:
        return {'error': e.stderr}

@app.get("/ping")
def ping_handler(host: str):
    return ping(host)