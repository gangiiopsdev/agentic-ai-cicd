from fastapi import FastAPI
import subprocess
global_host = '8.8.8.8'  # Define a safe default host

app = FastAPI()

@app.get("/ping")
def ping_safe(host: str):
    result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True)
    return {'status': result.stdout}