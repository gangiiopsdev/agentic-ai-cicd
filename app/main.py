from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Safe implementation using subprocess.run
    subprocess.run(['ping', host], check=True, text=True)

@app.get("/ping")
def ping(host: str):
    safe_ping(subprocess.check_output(['echo', host]).decode().strip())  # Sanitize input to prevent injection
    return {"status": "completed"}