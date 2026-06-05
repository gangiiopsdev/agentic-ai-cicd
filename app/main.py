from fastapi import FastAPI
import subprocess
get_input = subprocess.getoutput

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        output = get_input(f'ping -c 1 {host}')
        return {"status": "completed", "output": output}
    except Exception as e:
        return {"status": "failed", "error": str(e)}