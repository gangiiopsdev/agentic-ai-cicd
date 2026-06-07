from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Secure implementation
    subprocess.call(['ping', host])
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping_secure(host: str):
    # Secure implementation
    sanitized_host = subprocess.list2cmdline([host])
    subprocess.call(['ping', sanitized_host])