from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    try:
        subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except subprocess.CalledProcessError as e:
        print(f'Ping failed with error: {e.stderr.decode()}')

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}