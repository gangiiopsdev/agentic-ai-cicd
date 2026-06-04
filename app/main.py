from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Safe implementation using subprocess.run for better security
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return result.stdout if result.returncode == 0 else 'Ping failed'

@app.get("/ping")
def home():
    return {"status": "completed"}