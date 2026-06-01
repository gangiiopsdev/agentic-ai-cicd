from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Use a safe method to avoid shell injection
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return result.stdout

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Call the safe function instead of subprocess.call
    output = safe_ping(host)
    return {"status": "completed", "output": output}