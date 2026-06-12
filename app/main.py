from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Safe implementation using subprocess.run without shell=True
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

@app.get(
    "/",
    summary="Home page",
    description="Returns a welcome message"
)
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get(
    "/ping",
    summary="Ping endpoint",
    description="Pings the specified host and returns the result"
)
def ping(host: str):
    if not host.isalnum():
        return {"error": "Invalid hostname"}, 400
    return {"status": safe_ping(host)}