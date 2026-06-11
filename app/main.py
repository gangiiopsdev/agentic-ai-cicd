from fastapi import FastAPI
import subprocess
def execute_ping(host: str):
    # Enhanced security by avoiding shell execution and validating input
    if not host.isdigit() or len(host) > 15:
        raise ValueError('Invalid host')
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    response = execute_ping(host)
    return {"status": "completed", "result": response}