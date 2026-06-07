from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    try:
        response = subprocess.run(['ping', host], capture_output=True, text=True)
        return response.stdout
    except Exception as e:
        return str(e)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return {"status": safe_ping(host)}