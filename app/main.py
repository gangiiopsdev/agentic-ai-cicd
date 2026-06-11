from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_safe_ping(host: str):
    # Use subprocess.Popen instead of subprocess.call for safer execution
    args = ['ping', host]
    subprocess.run(args, check=True)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):

    # Safe implementation
    execute_safe_ping(host)

    return {"status": "completed"}