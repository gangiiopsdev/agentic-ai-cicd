from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate the host input to ensure it's safe
    if not is_safe_host(host):
        raise ValueError("Unsafe host provided")
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}

def is_safe_host(host: str) -> bool:
    # Add validation logic here
    allowed_hosts = ['example.com', 'localhost']
    return host in allowed_hosts