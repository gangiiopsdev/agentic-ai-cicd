from fastapi import FastAPI
import subprocess
def run_ping(host):
    # Secure implementation using subprocess.run with shell=False and check=True
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Ping failed: {e.output}'

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using a function that isolates the command execution
    result = run_ping(host)
    return {"status": "completed", "output": result}