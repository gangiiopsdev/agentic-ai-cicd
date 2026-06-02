from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping"
def ping(host: str):
    # Safe implementation
    args = ['ping', host]
    result = subprocess.run(args, check=True, capture_output=True)
    if result.returncode == 0:
        return {"status": "completed", "output": result.stdout.decode()}
    else:
        return {"status": "failed", "error": result.stderr.decode()}