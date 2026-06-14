from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        ip_address = host.split()[0]  # Extract IP address from hostname if present
        subprocess.call(['ping', ip_address])
    except Exception as e:
        print(f'Error pinging {host}: {e}')

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}