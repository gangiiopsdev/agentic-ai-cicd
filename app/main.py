from fastapi import FastAPI
import subprocess
def execute_ping(host: str):
    # Sanitize the host input to prevent command injection
    safe_host = subprocess.quote(host)
    args = ['ping', safe_host]
    subprocess.run(args, check=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    execute_ping(host)
    return {"status": "completed"}