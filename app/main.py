from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Secure implementation
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    if result.returncode != 0:
        return {"status": "failed", "error": result.stderr}
    else:
        return {"status": "completed", "output": result.stdout}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    if result.returncode != 0:
        return {"status": "failed", "error": result.stderr}
    else:
        return {"status": "completed", "output": result.stdout}