from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping_safe(host: str):
    # Safe implementation using subprocess.run with shell=False and argument parsing
    subprocess.run(['ping', host], check=True)

@app.get("/ping")
def ping(host: str):
    # Use the safe function to avoid command injection
    try:
        ping_safe(host)
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}
    return {"status": "completed"}