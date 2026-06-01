from fastapi import FastAPI
import subprocess
def run_safe_ping(host: str):
    try:
        result = subprocess.run(['ping', host], timeout=5, capture_output=True, text=True, check=True)
        return {'result': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'error': e.stderr}
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    return run_safe_ping(host)