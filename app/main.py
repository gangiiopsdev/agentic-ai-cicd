from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation using subprocess.run
    try:
        subprocess.run(['ping', host], check=True)
    except subprocess.CalledProcessError as e:
        return {'error': f'Ping failed with error: {e}'}

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)