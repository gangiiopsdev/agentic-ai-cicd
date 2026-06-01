from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping_safe(host: str):
    try:
        # Use safe method to avoid shell injection
        subprocess.run(['ping', host], check=True, capture_output=True)
    except subprocess.CalledProcessError as e:
        return {'error': e.stderr.decode()}

@app.get("/ping")
def ping(host: str):
    result = ping_safe(host)
    return result