from fastapi import FastAPI
import subprocess
def run_command(command):
    if not all(isinstance(arg, str) for arg in command):
        raise ValueError('All arguments must be strings')
    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not host.strip():
        raise ValueError('Host parameter is required')
    command = ["ping", host]
    output = run_command(command)
    return {"status": "completed", "output": output}