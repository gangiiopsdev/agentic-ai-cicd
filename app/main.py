from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        # Using check_output to avoid shell=True and prevent injection attacks
        subprocess.check_output(f'ping -c 1 {host}', shell=False, stderr=subprocess.STDOUT)
        return {"status": "completed", "message": "Ping successful"}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e.output)}