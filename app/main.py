from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_ping(host: str):
    if not host.isalnum():
        raise ValueError("Invalid hostname")
    return subprocess.call(['ping', host])

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        result = execute_ping(host)
        return {"status": "completed", "result": result}
    except ValueError as e:
        return {"error": str(e)}