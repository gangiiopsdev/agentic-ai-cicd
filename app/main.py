from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Using subprocess.run instead of subprocess.call and avoiding shell=True
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        response = safe_ping(host)
        return {"status": "completed", "output": response}
    except Exception as e:
        return {"status": "error", "message": str(e)}