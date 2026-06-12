from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

@app.get("/ping")
def ping_endpoint(host: str):
    if validate_host(host):
        return ping(host)
    else:
        return "Invalid host"

@app.get("")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

def validate_host(host: str) -> bool:
    # Simple validation to prevent common injection vectors
    return all(c.isalnum() or c in ('-', '.') for c in host)