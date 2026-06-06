from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    try:
        subprocess.run(['ping', host], check=True)
    except subprocess.CalledProcessError as e:
        print(f'Ping failed: {e}')

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}