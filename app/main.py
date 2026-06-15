from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        # Safe implementation using check_output to avoid shell=True
        subprocess.check_output(f'ping -c 1 {host}', shell=False, text=True)
        return {"status": "completed", "result": "success"}
    except Exception as e:
        return {"status": "failed", "result": str(e)}