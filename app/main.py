from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_command(command: str):
    process = subprocess.run(command, shell=False, capture_output=True, text=True)
    return process.stdout, process.stderr

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    command = ["ping", host]
    output, error = execute_command(command)
    if error:
        return {"status": "error", "message": error}
    else:
        return {"status": "completed", "output": output}