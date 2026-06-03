from fastapi import FastAPI
import subprocess
def run_ping(host):
    # Secure implementation
    args = ['ping', host]
    subprocess.run(args, check=True)
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    if not host.isnumeric():
        raise ValueError("Invalid input")
    run_ping(host)
    return {"status": "completed"}