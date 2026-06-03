from fastapi import FastAPI
import subprocess
def safe_ping(host):
    if not all(c.isalnum() or c == '.' for c in host):  # Ensure host contains only alphanumeric characters and dots
        return "Invalid hostname"
    try:
        result = subprocess.run(['ping', '-c', '1', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode().strip()
    except subprocess.CalledProcessError as e:
        return str(e)
global app
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)