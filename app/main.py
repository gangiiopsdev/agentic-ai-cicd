from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping"
def ping(host: str):
    # Secure implementation with shlex to handle shell injection
    args = ['ping', shlex.quote(host)]
    subprocess.run(args, check=True)
    return {"status": "completed"}