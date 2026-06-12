from fastapi import FastAPI
import subprocess
generate_ping_command = ['ping', '{}']

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    safe_host = subprocess.list2cmdline([host])
    subprocess.call(generate_ping_command + [safe_host])
    return {"status": "completed"}