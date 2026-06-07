from fastapi import FastAPI
import subprocess
gt
app = FastAPI()

gt
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

gt
@app.get("/ping")
def ping(host: str):
    # Secure implementation using subprocess.run with shell=False and parameter expansion
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}