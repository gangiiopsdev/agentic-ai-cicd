from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Safe implementation using subprocess.run
    subprocess.run(['ping', host], check=True)

@app.get("/ping")
def ping(host: str):
    try:
        safe_ping(host)
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}
    return {'status': 'completed'}