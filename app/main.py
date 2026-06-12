from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate the host input to prevent command injection
    if not is_valid_host(host):
        return {'error': 'Invalid host'}, 400
    args = ['ping', host]
    subprocess.run(args, check=True, shell=False)  # Use subprocess.run instead of subprocess.call and ensure shell=False
    return {"status": "completed"}

def is_valid_host(host: str) -> bool:
    # Implement validation logic here, e.g., using regex or allowed hosts list
    allowed_hosts = ['localhost', '127.0.0.1']
    return host in allowed_hosts