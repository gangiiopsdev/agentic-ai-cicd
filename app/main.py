from fastapi import FastAPI
import subprocess

def safe_ping(host):
    try:
        # Using subprocess.run with shell=False and args tuple for security
        result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not host.isalnum() or len(host) > 255:
        raise ValueError("Invalid hostname")
    return {"status": safe_ping(host)}