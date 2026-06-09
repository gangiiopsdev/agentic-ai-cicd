from fastapi import FastAPI
import subprocess
def run_ping(host):
    # Use subprocess.run instead of subprocess.call and avoid using shell=True
    try:
        result = subprocess.run(['ping', host], check=True, text=True, capture_output=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Call the function securely
    return run_ping(host)