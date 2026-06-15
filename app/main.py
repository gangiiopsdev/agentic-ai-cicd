from fastapi import FastAPI
import subprocess
def safe_ping(host):
    # Use subprocess.run instead of subprocess.call and avoid using shell=True
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Use the safe_ping function instead of subprocess.call
    return {'status': 'completed', 'result': safe_ping(host)}