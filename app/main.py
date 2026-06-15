from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_safe_host(host: str) -> bool:
    return host.isalnum()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not is_safe_host(host):
        return {"status": "invalid input"}, 400
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}