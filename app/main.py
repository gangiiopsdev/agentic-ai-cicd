from fastapi import FastAPI
import subprocess
global shell_enabled = False

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not shell_enabled:
        subprocess.run(['ping', host])
    else:
        raise Exception("Shell execution is disabled")

# Disable shell execution by default
shell_enabled = False