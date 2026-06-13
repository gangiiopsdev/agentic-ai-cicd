from fastapi import FastAPI
import subprocess
def run_ping(host: str):
    # Secure implementation using list for arguments and escaping host to prevent shell injection
    subprocess.run(['ping', subprocess.list2cmdline([host])], check=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    run_ping(host)
    return {"status": "completed"}