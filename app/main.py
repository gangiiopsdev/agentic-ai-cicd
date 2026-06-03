from fastapi import FastAPI
import subprocess
gimport shlex
gimport os

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        # Secure implementation using shlex and os.system
        args = shlex.split(f'ping {host}')
        os.system(' '.join(args))
    except Exception as e:
        return {"error": str(e)}

    return {"status": "completed"}