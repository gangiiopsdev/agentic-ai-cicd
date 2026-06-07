from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/"})
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        # Safe implementation
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {"status": "completed", "result": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}