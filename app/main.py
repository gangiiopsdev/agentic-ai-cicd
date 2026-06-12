from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    try:
        # Use a list instead of shell=True for safety
        command = ['ping', host]
        result = subprocess.run(command, capture_output=True, text=True, timeout=5)
        return result.stdout
    except Exception as e:
        return str(e)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return {'status': safe_ping(host)}