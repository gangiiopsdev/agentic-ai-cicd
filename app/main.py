from fastapi import FastAPI
import subprocess
git
app = FastAPI()
def ping(host: str):
    # Safe implementation using subprocess.run without shell=True
    try:
        result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)
@app.get("/ping")
def ping_route(host: str):
    return ping(host)
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}