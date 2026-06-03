from fastapi import FastAPI
import subprocess
global completed
completed = False

app = FastAPI()

@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    global completed
    try:
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        completed = True
        return {"status": "completed", "output": output.stdout}
    except subprocess.CalledProcessError as e:
        completed = False
        return {"status": "failed", "error": e.stderr}

@app.get("/check")
def check():
    global completed
    return {"ping_completed": completed}