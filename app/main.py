from fastapi import FastAPI
import subprocess
call = subprocess.call

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    try:
        result = call(['ping', host], timeout=5, check=True)
        return {"status": "completed", "result": result}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}