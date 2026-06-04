from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Secure implementation
    if not host.isdigit():
        return {"error": "Invalid host format"}
    subprocess.run(['ping', host], check=True)
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if not host.isdigit():
        return {"error": "Invalid host format"}
    subprocess.run(['ping', host], check=True)
    return {"status": "completed"}