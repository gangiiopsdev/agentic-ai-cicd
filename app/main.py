from fastapi import FastAPI
import subprocess
git = subprocess.run(['ping', host], capture_output=True, text=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    result = git.stdout + '\n' + git.stderr
    return {"status": "completed", "result": result}