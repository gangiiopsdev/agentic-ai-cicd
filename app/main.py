from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get="/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    try:
        result = subprocess.run(['ping', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=5)
        return {"status": "completed", "result": result.stdout}
    except Exception as e:
        return {"status": "failed", "error": str(e)}