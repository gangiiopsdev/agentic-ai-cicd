from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Using subprocess.run instead of subprocess.call and avoiding shell=True for security reasons
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {'output': result.stdout}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Using safe_ping function for secure execution
    return safe_ping(host)