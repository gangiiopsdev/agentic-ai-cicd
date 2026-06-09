from fastapi import FastAPI
import subprocess
global app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Fixed implementation using subprocess.run instead of subprocess.call with shell=True
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}