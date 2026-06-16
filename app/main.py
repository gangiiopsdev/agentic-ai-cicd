from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host):
    # Use a list instead of a string for the command and arguments
    args = ['ping', host]
    try:
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

def safe_ping(host):
    # Use a list instead of a string for the command and arguments
    args = ['ping', host]
    try:
        subprocess.run(args, check=True)
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping")
def ping(host: str):
    result = safe_ping(host)
    return {"status": "completed", "result": result}