from fastapi import FastAPI
import subprocess

app = FastAPI()

def run_ping(host):
    try:
        # Using subprocess.run instead of subprocess.call
        result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return run_ping(host)