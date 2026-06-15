from fastapi import FastAPI
import subprocess
def execute_command(command):
    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True, shell=False)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Use a whitelist of allowed hosts or validate the input
    if host not in ["example.com", "another.example.com"]:
        raise ValueError("Invalid host")
    command = ["ping", host]
    result = execute_command(command)
    return {"status": "completed", "output": result}