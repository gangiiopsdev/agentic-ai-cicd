from fastapi import FastAPI
import subprocess

app = FastAPI()

def run_ping(host):
    try:
        # Use subprocess.run instead of subprocess.call and avoid using shell=True
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return run_ping(host)