from fastapi import FastAPI
import subprocess
def execute_ping(host: str):
    # Secure implementation using subprocess.Popen without shell=True
    args = ['ping', host]
    subprocess.call(args)
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    execute_ping(host)
    return {"status": "completed"}