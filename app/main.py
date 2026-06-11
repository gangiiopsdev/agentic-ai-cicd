from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):

    # Secure implementation
    try:
        output = subprocess.check_output(['ping', host], universal_newlines=True, timeout=5)
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as e:
        return {"status": "error", "message": str(e)}

    return {"status": "completed", "output": output}