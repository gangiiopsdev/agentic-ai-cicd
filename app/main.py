from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return result.stdout.decode(), result.stderr.decode() if result.stderr else None

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_host(host: str):
    stdout, stderr = ping(host)
    return {"status": "completed", "stdout": stdout, "stderr": stderr if stderr else None}