from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/"
)def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation using subprocess.run with shell=False and check=True to prevent injection attacks
    result = subprocess.run(['ping', host], capture_output=True, text=True, check=True, shell=False)
    return {'status': 'completed', 'output': result.stdout}