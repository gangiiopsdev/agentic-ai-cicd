from fastapi import FastAPI
import subprocess
def safe_ping(host):
    if not host.isdigit():
        return None
    args = ['ping', str(host)]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    response = safe_ping(host)
    if response is None:
        return {"error": "Invalid host format"}
    return {"status": "completed", "response": response}