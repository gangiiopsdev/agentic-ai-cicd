from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        # Use a whitelist of allowed hosts or validate the input
        if host not in ['google.com', 'example.com']:  # Example validation
            return {"status": "error", "message": "Invalid host"}
        subprocess.call(['ping', host])
    except Exception as e:
        return {"status": "error", "message": str(e)}
    return {"status": "completed"}