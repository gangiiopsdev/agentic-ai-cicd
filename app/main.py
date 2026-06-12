from fastapi import FastAPI
import subprocess
global_host = "127.0.0.1" # Replace this with a safe default or validation logic.

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        if host != global_host:
            raise ValueError("Access denied")
        subprocess.run(["ping", host], capture_output=True, text=True)
    except Exception as e:
        return {"error": str(e)}

    return {"status": "completed"}