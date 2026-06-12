from fastapi import FastAPI
import subprocess
global host

app = FastAPI()

@app.get="/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping")
def ping(host: str):
    # Safe implementation
    try:
        subprocess.run(['ping', host], check=True)
        return {"status": "completed"}
    except Exception as e:
        return {"error": str(e)}, 500