from fastapi import FastAPI
import subprocess
import shlex

def ping(host: str):
    # Secure implementation using shlex.quote to escape any special characters in the host input
    args = ['ping', shlex.quote(host)]
    result = subprocess.run(args, capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}

app = FastAPI()
@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get="/ping"
def ping(host: str):
    # Secure implementation using shlex.quote to escape any special characters in the host input
    args = ['ping', shlex.quote(host)]
    result = subprocess.run(args, capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}