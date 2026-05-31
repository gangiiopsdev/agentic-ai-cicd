from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    try:
        subprocess.call(['ping', '-c', '1', host])
    except Exception as e:
        return {"error": str(e)}

    return {"status": "completed"}