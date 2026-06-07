from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host):
    try:
        # Validate the host input
        if not host.isalnum():
            raise ValueError("Invalid host")
        subprocess.call(shlex.split(f'ping {host}'))
        return {"status": "completed"}
    except Exception as e:
        return {"error": str(e)}

@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping"
def ping(host: str):
    return safe_ping(host)