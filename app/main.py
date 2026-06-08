from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Use a safe way to call ping without shell=True
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    output = safe_ping(host)
    return {"status": "completed", "output": output}