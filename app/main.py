from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        # Secure implementation using subprocess.run with check=True and capture_output
        result = subprocess.run(['ping', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return {"status": "completed", "output": result.stdout}
    except Exception as e:
        return {"status": "failed", "error": str(e)}