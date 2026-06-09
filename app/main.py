from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Validate the host parameter
    if not valid_host(host):
        raise ValueError("Invalid host")
    subprocess.run(['ping', '-c', '1'] + [host], check=True, shell=False)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        safe_ping(host)
    except ValueError as e:
        return {"error": str(e)}, 400
    return {"status": "completed"}

def valid_host(host: str) -> bool:
    # Implement validation logic here
    return all(c.isalnum() or c in '-._' for c in host)