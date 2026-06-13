from fastapi import FastAPI
import subprocess
def safe_ping(host):
    # Use subprocess safely without shell=True
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not host.isalnum():
        return {"error": "Invalid host input"}, 400
    output = safe_ping(host)
    return {"status": "completed", "output": output}