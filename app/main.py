from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Safer implementation using subprocess.run and avoiding shell=True
    try:
        subprocess.run(['ping', host], check=True)
    except subprocess.CalledProcessError as e:
        raise Exception(f'Ping failed for {host}: {e}')

@app.get="/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping")
def ping(host: str):
    try:
        safe_ping(host)
        return {"status": "completed"}
    except Exception as e:
        return {"status": "failed", "error": str(e)}