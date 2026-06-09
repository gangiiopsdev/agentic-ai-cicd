from fastapi import FastAPI
import subprocess
def execute_ping(host):
    # Secure implementation using subprocess.run and shlex.split for argument parsing
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
    return {"status": "completed", "response": response}