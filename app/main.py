from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Secure implementation using shlex to prevent shell injection
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

@app.get("/ping")
def ping_handler(host: str):
    return ping(shlex.quote(host))

@app.get("")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}