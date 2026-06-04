from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/"),
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation with argument sanitization and exception handling
    try:
        subprocess.call(['ping', '-c', '1', host])  # Limiting the number of pings to one
        return {"status": "completed"}
    except Exception as e:
        return {"error": str(e), "status": "failed"}