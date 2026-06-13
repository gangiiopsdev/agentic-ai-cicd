from fastapi import FastAPI
import subprocess
def execute_ping(host: str):
    # Safe implementation using subprocess.Popen instead of subprocess.call with shell=True
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    output = execute_ping(host)
    return {"status": "completed", "output": output}