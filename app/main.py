from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    if validate_host(host):
        subprocess.call(["ping", host])
        return {"status": "completed"}
    else:
        return {"error": "Invalid host"}, 400

def validate_host(host: str) -> bool:
    # Add validation logic here, e.g., check for allowed IP addresses or domains
    return all(char.isalnum() or char in ['.', '-'] for char in host)