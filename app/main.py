from fastapi import FastAPI
import subprocess
def execute_ping(host):
    return subprocess.run(['ping', host], capture_output=True, text=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    result = execute_ping(subprocess.run(['echo', host], capture_output=True, text=True).stdout)
    return {"status": "completed", "output": result.stdout}