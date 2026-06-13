from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if not validate_host(host):
        return {"status": "invalid host"}
    args = ['ping', host]
    subprocess.call(args, shell=False)
    return {"status": "completed"}

def validate_host(host: str) -> bool:
    # Add validation logic here, e.g., check for allowed characters or formats
    return all(c.isalnum() or c in ('.', '-') for c in host)