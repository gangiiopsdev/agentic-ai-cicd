from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        # Use shell=False to prevent shell injection
        subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False)
    except subprocess.CalledProcessError as e:
        print(f'Ping failed: {e.stderr.decode()}')
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}