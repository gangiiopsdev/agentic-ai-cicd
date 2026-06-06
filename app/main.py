from fastapi import FastAPI
import subprocess
def execute_ping(host: str):
    # Safe implementation using subprocess.run without shell=True
    try:
        result = subprocess.run(['ping', host], check=True, capture_output=True)
        return result.stdout.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return f'Error: {e}'

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    response = execute_ping(host)
    return {"status": "completed", "output": response}