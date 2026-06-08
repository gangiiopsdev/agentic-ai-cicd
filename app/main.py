from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    # Safe implementation using list and check_output with shlex
    if host.isalnum():
        command = ['ping', host]
        result = subprocess.run(command, capture_output=True, text=True)
        return result.stdout
    else:
        raise ValueError('Invalid hostname')

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        result = safe_ping(host)
        return {"status": "completed", "result": result}
    except ValueError as e:
        return {"error": str(e)}