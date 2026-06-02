from fastapi import FastAPI
import subprocess
cimport subprocess32

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        # Safe implementation using subprocess32 which provides better control over the command execution
        result = subprocess32.call(['ping', host], timeout=5)
        return {"status": "completed", "result": result}
    except Exception as e:
        return {"error": str(e)}