from fastapi import FastAPI
import subprocess
def run_ping(host: str):
    try:
        # Use subprocess.run instead of subprocess.call for better security
        result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Ping failed with error: {e.stderr}'
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    return run_ping(host)