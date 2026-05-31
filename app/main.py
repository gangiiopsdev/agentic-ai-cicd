from fastapi import FastAPI
import subprocess
def run_safe_ping(host: str):
    try:
        subprocess.call(['ping', host], timeout=5)
    except Exception as e:
        return {'error': str(e)}
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    return run_safe_ping(host)