from fastapi import FastAPI
import subprocess

app = FastAPI()

def run_command(command):
    result = subprocess.run(command, check=True, capture_output=True, text=True)
    return result.stdout

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    command = ["ping", host]
    output = run_command(command)
    return {"status": "completed", "output": output}