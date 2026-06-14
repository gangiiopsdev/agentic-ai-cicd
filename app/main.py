from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f'Ping failed with error: {e.stderr}')

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}